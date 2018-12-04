import sys
import datetime
from pathlib import Path 
current_path = Path(__file__).absolute()
abs_path = str(current_path.parent.parent)
sys.path.append(abs_path)

from capture import Capture
from utils import to_date, tryit


def from_api_to_db(data_list, url, id_proposicao):
    
    func = lambda datum: dict(
        id_proposicao=          id_proposicao,
        data_hora=              to_date(datum['dataHora'], '%Y-%m-%dT%H:%M'),
        sequencia=              datum['sequencia'],
        sigla_orgao=            datum['siglaOrgao'],
        uri_orgao=              datum['uriOrgao'],
        regime=                 datum['regime'],
        descricao_tramitacao=   datum['descricaoTramitacao'],
        id_tipo_tramitacao=     datum['idTipoTramitacao'],
        descricao_situacao=     datum['descricaoSitucao'],
        id_situacao=            datum['idSituacao'],
        despacho=               datum['despacho'],
        url=                    datum['url'],
        data_captura=           datetime.datetime.now(),
        url_captura=            url
        )

    return map(func, data_list)


def urls_generator(capture, base_url):
    
    with capture.engine.connect() as conn:
        # Checa quais foram as últimas proposições tramitadas
        result = list(conn.execute("SELECT DISTINCT id_proposicao FROM camara_v1.proposicoes"))

    return set(map(lambda x: (base_url.format(x[0]), x[0]), list(result)))

def main():

    capture = Capture(schema='camara_v2')

    # capture data with this
    base_url = 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/{}/tramitacoes'
    urls = urls_generator(capture, base_url)

    for url, id_proposicao in urls:
        print(url)
        capture.capture_data(url, content_type='json')
    
        data_list = capture.data['dados']
        data_list = capture.to_default_dict(data_list) 
        data_list = from_api_to_db(data_list, url, id_proposicao) 
        capture.insert_data(data_list, table_name='tramitacao')

if __name__ == '__main__':
    main()
