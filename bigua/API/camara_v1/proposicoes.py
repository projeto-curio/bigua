import sys
import datetime
from pathlib import Path 
current_path = Path(__file__).absolute()
abs_path = str(current_path.parent.parent)
sys.path.append(abs_path)

from capture import Capture
from utils import to_date, tryit


def from_api_to_db(data_list, url):
    
    func = lambda datum: dict(
        nome_proposicao=           datum['nomeProposicao'],
        id_proposicao=             datum['idProposicao'],
        id_proposicao_principal=   datum['idProposicaoPrincipal'],
        nome_proposicao_origem=    datum['nomeProposicaoOrigem'],
        tipo_proposicao=           datum['tipoProposicao'],
        tema=                      datum['tema'],
        ementa=                    datum['Ementa'],
        explicacao_ementa=         datum['ExplicacaoEmenta'],
        autor=                     datum['Autor'],
        ide_cadastro=              datum['ideCadastro'],
        uf_autor=                  datum['ufAutor'],
        partido_autor=             datum['partidoAutor'],
        data_apresentacao=         to_date(datum['DataApresentacao'], '%d/%m/%Y'),
        regime_tramitacao=         datum['RegimeTramitacao'],
        tipo_proposicao_sigla=     datum['@tipo'].strip(),
        numero_proposicao=         datum['@numero'],
        ano_proposicao=            datum['@ano'],
        ultimo_despacho_data=      to_date(datum['UltimoDespacho']['@Data'], '%d/%m/%Y'),
        ultimo_despacho=           tryit(datum['UltimoDespacho'], key='#text'), 
        apreciacao=                datum['Apreciacao'],
        indexacao=                 datum['Indexacao'],
        situacao=                  datum['Situacao'],
        link_inteiro_teor=         datum['LinkInteiroTeor'],
        data_captura=              datetime.datetime.now(),
        url_captura=               url
        )

    return map(func, data_list)


def urls_generator(capture, base_url):
    with capture.engine.connect() as conn:
        # Checa quais foram as últimas proposições tramitadas
        result = list(conn.execute("select id_proposicao \
                                     from camara_v1.proposicoes_tramitadas_periodo \
                                     where numero_captura = (select max(numero_captura) \
                                                            from camara_v1.proposicoes_tramitadas_periodo)"))

    return set(map(lambda x: base_url.format(x[0]), list(result)))

def main():

    capture = Capture(schema='camara_v1')

    # capture data with this
    base_url = 'http://www.camara.leg.br/SitCamaraWS/Proposicoes.asmx/ObterProposicaoPorID?IdProp={}'
    urls = urls_generator(capture, base_url)

    for url in urls:
        print(url)
        capture.capture_data(url)
    
        data_list = capture.data['proposicao']
        data_list = capture.to_default_dict(data_list) 
        data_list = from_api_to_db(data_list, url) 
        # capture.insert_data(data_list, table_name='proposicoes')
        capture.insert_data(data_list, table_name='proposicoes', if_exists='replace',
                            key='id_proposicao')

if __name__ == '__main__':
    main()
