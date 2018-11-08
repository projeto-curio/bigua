import sys
import datetime
from pathlib import Path 
current_path = Path(__file__).absolute()
abs_path = str(current_path.parent.parent)
sys.path.append(abs_path)

from capture import Capture
from utils import to_date

def from_api_to_db(data_list, url, numero_captura):
    
    func = lambda datum: dict(
        id_proposicao=           datum['codProposicao'],
        nome_proposicao=         datum['nomeProposicao'],
        data_votacao=            to_date(datum['dataVotacao'], '%d/%m/%Y'),
        data_captura=            datetime.datetime.now(),
        url_captura=             url,
        numero_captura=          numero_captura
        )

    return map(func, data_list)




def urls_generator(capture, base_url):

    with capture.engine.connect() as conn:
        result = list(conn.execute("select MAX(numero_captura) \
                                     from camara_v1.proposicoes_votadas_plenario"))

    if result[0][0] is None:
        numero_captura = 1
    else:
        numero_captura = int(result[0][0]) + 1

    year = range(1988, 2018)

    return map(lambda y: base_url.format(y), year), numero_captura

def main():

    capture = Capture(schema='camara_v1')

    # capture data with this
    base_url = 'http://www.camara.leg.br/SitCamaraWS/Proposicoes.asmx/ListarProposicoesVotadasEmPlenario?ano={}&tipo='
    urls, numero_captura = urls_generator(capture, base_url)

    for url in urls:
        print(url, numero_captura)
        
        try:
            capture.capture_data(url)

            # get the list of dict for this table
            data_list = capture.data['proposicoes']['proposicao']
            data_list = capture.to_default_dict(data_list) 
            data_list = from_api_to_db(data_list, url, numero_captura) 
            capture.insert_data(data_list, table_name='proposicoes_votadas_plenario', 
                                if_exists='pass', key='id_proposicao')

        except Exception as e:
            print(e)
            continue

if __name__ == '__main__':
    main()
