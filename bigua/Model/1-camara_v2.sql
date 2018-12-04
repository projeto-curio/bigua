CREATE SCHEMA camara_v2;

CREATE TABLE camara_v2.tramitacao (
    id_proposicao          INT,
    data_hora              TIMESTAMP,
    sequencia              INT,
    sigla_orgao            TEXT,
    uri_orgao              TEXT,
    regime                 TEXT,
    descricao_tramitacao   TEXT,
    id_tipo_tramitacao     TEXT,
    descricao_situacao     TEXT,
    id_situacao            INT,
    despacho               TEXT,
    url                    TEXT,
	data_captura           TIMESTAMP,
	url_captura            TEXT 
)

CREATE INDEX id_proposicao_idx_tramitacao ON camara_v2.tramitacao (id_proposicao);
CREATE INDEX data_hora_idx_tramitacao ON camara_v2.tramitacao (data_hora);



"dataHora": "2007-06-05T17:48",
      "sequencia": 1,
      "siglaOrgao": "PLEN",
      "uriOrgao": "https://dadosabertos.camara.leg.br/api/v2/orgaos/180",
      "regime": "Ordinária (Art. 151, III, RICD)",
      "descricaoTramitacao": "Apresentação de Proposição",
      "idTipoTramitacao": "100",
      "descricaoSituacao": null,
      "idSituacao": null,
      "despacho": "Apresentação do Projeto de Lei pela Deputada Sueli Vidigal (PDT-ES).",
      "url": "http://www.camara.gov.br/proposicoesWeb/prop_mostrarintegra?codteor=467037"


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