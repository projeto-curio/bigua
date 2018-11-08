import sys
import datetime
from pathlib import Path 
current_path = Path(__file__).absolute()
abs_path = str(current_path.parent.parent)
sys.path.append(abs_path)
from capture import Capture

def from_api_to_db_deputados(data_list, url):
    
    func = lambda datum: dict(
        ide_cadastro=datum['ideCadastro'],
        cod_orcamento=datum['codOrcamento'],
        condicao=datum['condicao'],
        matricula=datum['matricula'],
        id_parlamentar=datum['idParlamentar'],
        nome=datum['nome'],
        nome_parlamentar=datum['nomeParlamentar'],
        url_foto=datum['urlFoto'],
        sexo=datum['sexo'],
        uf=datum['uf'],
        partido=datum['partido'],
        gabinete=datum['gabinete'],
        anexo=datum['anexo'],
        fone=datum['fone'],
        email=datum['email'],
        data_captura=datetime.datetime.now(),
        url_captura=url
        )
    
    return map(func, data_list)

def clean_table(capture):
    
    with capture.engine.connect() as conn:
        result = list(conn.execute( """DELETE
                                        FROM
                                            camara_v1.deputados a
                                                USING camara_v1.deputados b
                                        WHERE
                                            a.data_captura < b.data_captura
                                            AND a.ide_cadastro = b.ide_cadastro;"""))

def main():

    capture = Capture(
            schema='camara_v1',)

    capture.capture_data(
        url='http://www.camara.leg.br/SitCamaraWS/Deputados.asmx/ObterDeputados')
    data_list = capture.data['deputados']['deputado'] 
    data_list = capture.to_default_dict(data_list) 
    data_list = from_api_to_db_deputados(data_list, capture.url) 
    capture.insert_data(data_list, table_name='deputados')
    clean_table(capture)


if __name__ == '__main__':
    main()
