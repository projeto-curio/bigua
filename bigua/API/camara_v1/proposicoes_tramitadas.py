import sys
import datetime
from pathlib import Path 
current_path = Path(__file__).absolute()
abs_path = str(current_path.parent.parent)
sys.path.append(abs_path)

from capture import Capture
from utils import *

def force_datetime(string):

    if len(string) <= 10:
        string = string + ' 00:00:00'
    
    return to_date(string, '%d/%m/%Y %H:%M:%S')

def from_api_to_db(data_list, url, numero_captura):
    
    func = lambda datum: dict(
        cod_proposicao=          datum['codProposicao'],
        tipo_proposicao=         datum['tipoProposicao'],
        numero=                  datum['numero'],
        ano=                     datum['ano'],
        data_tramitacao=         force_datetime(datum['dataTramitacao']),
        data_alteracao=          to_date(datum['dataAlteracao'], '%d/%m/%Y %H:%M:%S'),
        data_captura=            datetime.datetime.now(),
        url_captura=             url,
        numero_captura=          numero_captura
        )

    return map(func, data_list)


def urls_generator(capture, base_url):
    with capture.engine.connect() as conn:
        result = list(conn.execute("select MAX(data_captura), numero_captura \
                                     from camara_v1.proposicoes_tramitadas_periodo \
                                     group by numero_captura"))
    print(result)
    if not len(result):
        dtInicio = datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(days=6), '%d/%m/%Y')
        dtFim = datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y')
        numero_captura = 1
    else:
        dtInicio = datetime.datetime.strftime(result[0][0], '%d/%m/%Y')
        dtFim = datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y')
        numero_captura = int(result[0][1]) + 1

    return base_url.format(dtInicio=dtInicio, dtFim=dtFim), numero_captura

def main():

    capture = Capture(schema='camara_v1')

    # capture data with this
    base_url = 'http://www.camara.leg.br/SitCamaraWS/Proposicoes.asmx/ListarProposicoesTramitadasNoPeriodo?dtInicio={dtInicio}&dtFim={dtFim}'
    url, numero_captura = urls_generator(capture, base_url)
    print(url, numero_captura)
    try:
        capture.capture_data(url)
    except TypeError:
        print('Not Enough Data')
        return

    # get the list of dict for this table
    data_list = capture.data['proposicoes']['proposicao']

    # 
    data_list = capture.to_default_dict(data_list) 

    # make it rigth
    data_list = from_api_to_db(data_list, url, numero_captura) 

    # insert it!
    capture.insert_data(data_list, table='proposicoes_tramitadas_periodo')

if __name__ == '__main__':
    main()
