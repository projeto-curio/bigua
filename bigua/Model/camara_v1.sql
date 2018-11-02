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

CREATE INDEX ide_cadastro_idx_obter_deputados ON camara_v1.obter_deputados (ide_cadastro);


CREATE TABLE camara_v1.obter_detalhes_deputado (
	ide_cadastro			INT,
	id_parlamentar_deprecated	INT,
	num_legislatura			INT,
	nome_parlamentar_atual		TEXT,
	nome_civil			TEXT,
	partido_atual_id_partido	TEXT,
	partido_atual_sigla		TEXT,
	partido_atual_nome		TEXT,
	uf_representacao_atual		TEXT,
	sexo				TEXT,
	email				TEXT,
	data_nascimento			DATE,
	data_falecimento		DATE,
	nome_profissao			TEXT,
	gabinete_numero			INT,
	ganinete_anexo			INT,
	gabinete_telefone		TEXT,
	situacao_na_legislatura_atual	TEXT,
	data_captura            TIMESTAMP,
	url_captura             TEXT
);

CREATE INDEX ide_cadastro_idx_obter_detalhes_deputados ON camara_v1.obter_detalhes_deputados (ide_cadastro);

