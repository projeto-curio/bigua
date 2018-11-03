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

def main():

    capture = Capture(
            schema='camara_v1',)

    # capture data with this
    capture.capture_data(
        url='http://www.camara.leg.br/SitCamaraWS/Deputados.asmx/ObterDeputados')

    # get the list of dict for this table
    data_list = capture.data['deputados']['deputado'] 

    # 
    data_list = capture.to_default_dict(data_list) 

    # make it rigth
    data_list = from_api_to_db_deputados(data_list, capture.url) 

    # insert it!
    capture.insert_data(data_list, table='deputados')

if __name__ == '__main__':
    main()
