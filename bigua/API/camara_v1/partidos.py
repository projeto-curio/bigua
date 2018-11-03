import sys
import datetime
from pathlib import Path 
current_path = Path(__file__).absolute()
abs_path = str(current_path.parent.parent)
sys.path.append(abs_path)

from capture import Capture
from utils import *

def from_api_to_db_deputados(data_list, url):
    
    func = lambda datum: dict(
        id_partido=         datum['idPartido'],
        sigla_partido=      datum['siglaPartido'],
        nome_partido=       datum['nomePartido'],
        data_criacao=       to_date(datum['dataCriacao'], '%d/%m/%Y'),
        data_extincao=      to_date(datum['dataExtincao'], '%d/%m/%Y'),
        data_captura=       datetime.datetime.now(),
        url_captura=        url
        )

    return map(func, data_list)


def main():

    capture = Capture(schema='camara_v1')

    # capture data with this
    capture.capture_data(
        url='http://www.camara.leg.br/SitCamaraWS/Deputados.asmx/ObterPartidosCD')

    # get the list of dict for this table
    data_list = capture.data['partidos']['partido'] 

    # 
    data_list = capture.to_default_dict(data_list) 

    # make it rigth
    data_list = from_api_to_db_deputados(data_list, capture.url) 

    # insert it!
    capture.insert_data(data_list, table='partidos')

if __name__ == '__main__':
    main()
