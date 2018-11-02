CREATE SCHEMA camara_v1;

CREATE TABLE camara_v1.obter_deputados (
	ide_cadastro            INT,
    cod_orcamento           INT,
	condicao                TEXT,
    matricula               INT,
    id_parlamentar          INT,
	nome                    TEXT,
	nome_parlamentar        TEXT,
	url_foto                TEXT,
	sexo                    TEXT,
	uf                      TEXT,
	partido                 TEXT,
	gabinete                TEXT,
	anexo                   TEXT,
	fone                    TEXT,
	email                   TEXT,
    data_captura            TIMESTAMP,
    url_captura             TEXT
);

CREATE INDEX ide_cadastro_idx ON camara_v1.obter_deputados (ide_cadastro);


