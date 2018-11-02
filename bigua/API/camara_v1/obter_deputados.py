from API.capture import Capture

def from_api_to_db_obter_deputados(data, url):
    
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
        url='http://www.camara.leg.br/SitCamaraWS/Deputados.asmx/ObterDeputados',
        schema='camara_v1',
        table='obter_dgit eputados',)
    
    capture.prepare_data()

    # Faça coisas aqui embaixo
    data_list = capture.data['deputados']['deputado'] 

    # Also this
    data_list = capture.to_default_dict(data_list)  # Isso está pronto
    data_list = from_api_to_db_obter_deputados(data, capture.url) 

    capture.insert_data(data_list) # Insert Data

if __name__ == '__main__':
    main()
