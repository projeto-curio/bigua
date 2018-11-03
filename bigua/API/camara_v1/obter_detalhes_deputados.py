import sys
import datetime

from pathlib import Path 
current_path = Path(__file__).absolute()
abs_path = str(current_path.parent.parent)
sys.path.append(abs_path)

from capture import Capture
from utils import *


def from_api_to_db_deputados_detalhes(data_list, url):
    
    func = lambda datum: dict(
         num_legislatura=                datum['numLegislatura'],
         email=                          datum['email'],
         nome_profissao=                 datum['nomeProfissao'],
         data_nascimento=                to_date(datum['dataNascimento'], '%d/%m/%Y'),
         data_falecimento=               to_date(datum['dataFalecimento'],'%d/%m/%Y'),
         uf_representacao_atual=         datum['ufRepresentacaoAtual'],
         situacao_na_legislatura_atual=  datum['situacaoNaLegislaturaAtual'],
         ide_cadastro=                   datum['ideCadastro'],
         id_parlamentar_deprecated=      datum['idParlamentarDeprecated'],
         nome_civil=                     datum['nomeCivil'],
         sexo=                           datum['sexo'],
         partido_atual_id_partido=       datum['partidoAtual']['idPartido'],
         partido_atual_sigla=            datum['partidoAtual']['sigla'],
         partido_atual_nome=             datum['partidoAtual']['nome'],        
         gabinete_numero=                datum['gabinete']['numero'],
         ganinete_anexo=                 datum['gabinete']['anexo'],
         gabinete_telefone=              datum['gabinete']['telefone'],
         data_captura=                   datetime.datetime.now(),
         url_captura=                    url
    )
    
    return map(func, data_list)

def from_api_to_db_deputados_detalhes_comissoes(data_list, url, data_generic):
    
    func = lambda datum: dict(
        ide_cadastro=                    data_generic['ideCadastro'],
        nome_parlamentar_atual=          data_generic['nomeParlamentarAtual'],
        partido_atual_nome=              data_generic['partidoAtual']['nome'],   
        partido_atual_id_partido=        data_generic['partidoAtual']['idPartido'],
        uf_representacao_atual=          data_generic['ufRepresentacaoAtual'],
        id_orgao_legislativo_cd=         datum['idOrgaoLegislativoCD'],
        sigla_comissao=                  datum['siglaComissao'],
        nome_comissao=                   datum['nomeComissao'],
        condicao_membro=                 datum['condicaoMembro'],
        data_entrada=                    to_date(datum['dataEntrada'], '%d/%m/%Y'),                    
        data_saida=                      to_date(datum['dataSaida'], '%d/%m/%Y'),
        data_captura=                    datetime.datetime.now(),
        url_captura=                     url 
    )
    return map(func, data_list)


def from_api_to_db_deputados_detalhes_cargo_comissoes(data_list, url, data_generic):
    
    func = lambda datum: dict(
        ide_cadastro=                    data_generic['ideCadastro'],
        nome_parlamentar_atual=          data_generic['nomeParlamentarAtual'],
        partido_atual_nome=              data_generic['partidoAtual']['nome'],   
        partido_atual_id_partido=        data_generic['partidoAtual']['idPartido'],
        uf_representacao_atual=          data_generic['ufRepresentacaoAtual'],
        id_orgao_legislativo_cd=         datum['idOrgaoLegislativoCD'],
        sigla_comissao=                  datum['siglaComissao'],
        nome_comissao=                   datum['nomeComissao'],
        id_cargo=                        datum['idCargo'],
        nome_cargo=                      datum['nomeCargo'],
        data_entrada=                    to_date(datum['dataEntrada'], '%d/%m/%Y'),
        data_saida=                      to_date(datum['dataSaida'], '%d/%m/%Y'),
        data_captura=                    datetime.datetime.now(),
        url_captura=                     url 
    )
    
    return map(func, data_list)
        
    
def from_api_to_db_deputados_detalhes_periodo_exercicio(data_list, url, data_generic):
    
    func = lambda datum: dict(
        ide_cadastro=                     data_generic['ideCadastro'],
        nome_parlamentar_atual=           data_generic['nomeParlamentarAtual'],
        partido_atual_nome=               data_generic['partidoAtual']['nome'],   
        partido_atual_id_partido=         data_generic['partidoAtual']['idPartido'],
        uf_representacao_atual=           data_generic['ufRepresentacaoAtual'],
        sigla_uf_representacao=           datum['siglaUFRepresentacao'],
        situacao_exercicio=               datum['situacaoExercicio'],
        data_inicio=                      to_date(datum['dataInicio'], '%d/%m/%Y'),
        data_fim=                         to_date(datum['dataFim'], '%d/%m/%Y'),
        id_causa_fim_exercicio=           datum['idCausaFimExercicio'],
        descricao_causa_fim_exercicio=    datum['descricaoCausaFimExercicio'],
        id_cadastro_parlamentar_anterior= datum['idCadastroParlamentarAnterior'],
        data_captura=                     datetime.datetime.now(),
        url_captura=                      url 
    )
    
    return map(func, data_list)
        

def from_api_to_db_deputados_detalhes_filiacao_partidaria(data_list, url, data_generic):
    
    func = lambda datum: dict(
        ide_cadastro=                     data_generic['ideCadastro'],
        nome_parlamentar_atual=           data_generic['nomeParlamentarAtual'],
        partido_atual_nome=               data_generic['partidoAtual']['nome'],   
        partido_atual_id_partido=         data_generic['partidoAtual']['idPartido'],
        uf_representacao_atual=           data_generic['ufRepresentacaoAtual'],
        id_partido_anterior=              datum['idPartidoAnterior'],
        sigla_partido_anterior=           datum['siglaPartidoAnterior'],
        nome_partido_anterior=            datum['nomePartidoAnterior'],
        id_partido_posterior=             datum['idPartidoPosterior'],
        sigla_partido_posterior=          datum['siglaPartidoPosterior'],
        nome_partido_posterior=           datum['nomePartidoPosterior'],
        data_filiacao_partido_posterior=  to_date(datum['dataFiliacaoPartidoPosterior'],'%d/%m/%Y'),
        hora_filiacao_partido_posterior=  datum['horaFiliacaoPartidoPosterior'],

    )
    
    return map(func, data_list)
        
def from_api_to_db_deputados_detalhes_historico_lider(data_list, url, data_generic):
    
    func = lambda datum: dict(
        ide_cadastro=                     data_generic['ideCadastro'],
        nome_parlamentar_atual=           data_generic['nomeParlamentarAtual'],
        partido_atual_nome=               data_generic['partidoAtual']['nome'],   
        partido_atual_id_partido=         data_generic['partidoAtual']['idPartido'],
        uf_representacao_atual=           data_generic['ufRepresentacaoAtual'],
        id_historico_lider=               datum['idHistoricoLider'],
        id_cargo_lideranca=               datum['idCargoLideranca'],
        descricao_cargo_lideranca=        datum['descricaoCargoLideranca'],
        num_ordem_cargo=                  datum['numOrdemCargo'],
        data_designacao=                  to_date(datum['dataDesignacao'], '%d/%m/%Y'),
        data_termino=                     to_date(datum['dataTermino'], '%d/%m/%Y'),
        codigo_unidade_lideranca=         datum['codigoUnidadeLideranca'],
        sigla_unidade_lideranca=          datum['siglaUnidadeLideranca'],
        id_bloco_partido=                 datum['idBlocoPartido'],
        data_captura=                     datetime.datetime.now(),
        url_captura=                      url 
    )
    
    return map(func, data_list)


def urls_generator(capture, base_url):
    
    with capture.engine.connect() as conn:
        result = conn.execute("select distinct ide_cadastro from camara_v1.deputados")
    
    for row in result:
        yield base_url.format(row[0])

def main():

    capture = Capture(schema='camara_v1',)

    base_url = 'http://www.camara.leg.br/SitCamaraWS/Deputados.asmx/ObterDetalhesDeputado?ideCadastro={}&numLegislatura='

    for i, url in enumerate(urls_generator(capture, base_url)):
        print('----')
        print(url)
        
        # capture data with this
        capture.capture_data(url)
        
        data_generic = capture.data['Deputados']['Deputado']
            
        for data_legislatura in force_list(data_generic):
            
            # deputados detalhes
            print()
            print('deputados detalhes')
            data_list = data_legislatura
            data_list = capture.to_default_dict(data_list) 
            data_list = from_api_to_db_deputados_detalhes(data_list, url)
            capture.insert_data(data_list, table='detalhes_deputado')

            data_generic = capture.data['Deputados']['Deputado']

            # detalhes comissoes
            print()
            print('detalhes comissoes')
            if data_legislatura['comissoes'] is not None:
                data_list = data_legislatura['comissoes']['comissao']
                data_list = capture.to_default_dict(data_list) 
                data_list = from_api_to_db_deputados_detalhes_comissoes(data_list, url, data_legislatura)
                capture.insert_data(data_list, table='detalhes_deputado_comissoes')

            # cargo comissoes
            print()
            print('cargo comissoes')
            if data_legislatura['cargosComissoes'] is not None:
                data_list = data_legislatura['cargosComissoes']['cargoComissoes']
                data_list = capture.to_default_dict(data_list) 
                data_list = data_list = from_api_to_db_deputados_detalhes_comissoes(data_list, url, data_legislatura)
                capture.insert_data(data_list, table='detalhes_deputado_comissoes_cargos')

            # periodo exercicio
            print()
            print('periodo exercicio')
            if data_legislatura['periodosExercicio'] is not None:
                data_list = data_legislatura['periodosExercicio']['periodoExercicio']
                data_list = capture.to_default_dict(data_list) 
                data_list = from_api_to_db_deputados_detalhes_periodo_exercicio(data_list, url, data_legislatura)
                capture.insert_data(data_list, table='detalhes_deputado_periodos_exercicio')

            # filiacao partidaria
            print()
            print('filiacao partidaria')
            if data_legislatura['filiacoesPartidarias'] is not None:
                data_list = data_legislatura['filiacoesPartidarias']['filiacaoPartidaria']
                data_list = capture.to_default_dict(data_list) 
                data_list = from_api_to_db_deputados_detalhes_filiacao_partidaria(data_list, url, data_legislatura)
                capture.insert_data(data_list, table='detalhes_deputado_filiacoes_partidarias')


            # historico lider
            print()
            print('historico lider')
            if data_legislatura['historicoLider'] is not None:
                data_list = data_legislatura['historicoLider']['itemHistoricoLider']
                data_list = capture.to_default_dict(data_list) 
                data_list = from_api_to_db_deputados_detalhes_historico_lider(data_list, url, data_legislatura)
                capture.insert_data(data_list, table='detalhes_deputado_hitorico_lider')

if __name__ == '__main__':
    main()
