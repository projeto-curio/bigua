import sys
import datetime

from pathlib import Path 
current_path = Path(__file__).absolute()
abs_path = str(current_path.parent.parent)
sys.path.append(abs_path)

from capture import Capture
from utils import force_list, to_date


def from_api_to_db_votacao_orientacao(data_list, url, data_proposicao, data_votacao, id_proposicao, numero_captura):
    func = lambda datum: dict(
        id_proposicao=                    id_proposicao,
        tipo_proposicao_sigla=            data_proposicao['Sigla'], 
        numero_proposicao=                data_proposicao['Numero'],
        ano_proposicao=                   data_proposicao['Ano'],
        resumo_votacao=                   data_votacao['@Resumo'],
        data_votacao=                     to_date(data_votacao['@Data'], '%d/%m/%Y'),
        hora_votacao=                     to_date(data_votacao['@Hora'], '%H:%M'),
        objeto_votacao=                   data_votacao['@ObjVotacao'],
        cod_sessao=                       data_votacao['@codSessao'],
        sigla_partido=                    datum['@Sigla'],
        orientacao_partido=               datum['@orientacao'].strip(),
        data_captura=                     datetime.datetime.now(),
        url_captura=                      url,
        numero_captura=                   numero_captura
    )
    
    return map(func, data_list)


def from_api_to_db_votacao_deputado(data_list, url, data_proposicao, data_votacao, id_proposicao):
    func = lambda datum: dict(
        id_proposicao=                    id_proposicao,
        tipo_proposicao_sigla=            data_proposicao['Sigla'], 
        numero_proposicao=                data_proposicao['Numero'],
        ano_proposicao=                   data_proposicao['Ano'],
        resumo_votacao=                   data_votacao['@Resumo'],
        data_votacao=                     to_date(data_votacao['@Data'], '%d/%m/%Y'),
        hora_votacao=                     to_date(data_votacao['@Hora'], '%H:%M'),
        objeto_votacao=                   data_votacao['@ObjVotacao'],
        cod_sessao=                       data_votacao['@codSessao'],
        nome=                             datum['@Nome'],
        ide_cadastro=                     datum['@ideCadastro'],
        sigla_partido=                    datum['@Partido'],
        uf=                               datum['@UF'],
        voto=                             datum['@Voto'],
        data_captura=                     datetime.datetime.now(),
        url_captura=                      url 
    )
    
    return map(func, data_list)


def urls_generator(capture, base_url):
    
    with capture.engine.connect() as conn:
        result = conn.execute("""
        SELECT DISTINCT ano_proposicao, numero_proposicao, tipo_proposicao_sigla, id_proposicao
        FROM camara_v1.proposicoes 
        WHERE id_proposicao IN (
            SELECT id_proposicao
            FROM camara_v1.proposicoes_votadas_plenario
            WHERE numero_captura = (SELECT CASE 
                                                WHEN MAX(numero_captura) IS NULL THEN 1
                                                ELSE MAX(numero_captura)
                                            END
                                    FROM camara_v1.votacao_proposicao_orientacao))""")

        numero_captura = int(list(conn.execute("""SELECT CASE 
                                                WHEN MAX(numero_captura) IS NULL THEN 0
                                                ELSE MAX(numero_captura)
                                            END
                                    FROM camara_v1.votacao_proposicao_orientacao"""))[0][0]) + 1
    
    urls_and_ids = list(map(lambda row: (base_url.format(ano=row[0], numero=row[1], tipo=row[2]), row[3],), list(result)))

    return urls_and_ids, numero_captura

def main():

    capture = Capture(schema='camara_v1',)

    base_url = 'http://www.camara.leg.br/SitCamaraWS/Proposicoes.asmx/ObterVotacaoProposicao?tipo={tipo}&numero={numero}&ano={ano}'

    url_and_ids, numero_captura = urls_generator(capture, base_url)

    print(url_and_ids, numero_captura)

    for url, id_proposicao in url_and_ids:
        print('----')
        print(url)
        url = 'http://www.camara.leg.br/SitCamaraWS/Proposicoes.asmx/ObterVotacaoProposicao?tipo=PL&numero=1992&ano=2007'
        
        # capture data with this
        capture.capture_data(url)
        
        data_proposicao = capture.data['proposicao']

        data_generic = data_proposicao['Votacoes']['Votacao']
            
        for data_votacao in force_list(data_generic):
            
            # orientacao
            print()
            print('orientacao')
            data_list = data_votacao['orientacaoBancada']['bancada']
            data_list = capture.to_default_dict(data_list) 
            data_list = from_api_to_db_votacao_orientacao(
                                data_list, url, data_proposicao, data_votacao,
                                id_proposicao, numero_captura)
            capture.insert_data(data_list, table_name='votacao_proposicao_orientacao')

            # deputados
            print()
            print('deputados')
            data_list = data_votacao['votos']['Deputado']
            data_list = capture.to_default_dict(data_list) 
            data_list = from_api_to_db_votacao_deputado(
                                data_list, url, data_proposicao, data_votacao,
                                 id_proposicao)
            capture.insert_data(data_list, table_name='votacao_proposicao')


if __name__ == '__main__':
    main()
