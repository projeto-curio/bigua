CREATE SCHEMA camara_v1;

CREATE TABLE camara_v1.deputados (
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

CREATE INDEX ide_cadastro_idx_deputados ON camara_v1.deputados (ide_cadastro);


CREATE TABLE camara_v1.detalhes_deputado (
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
	data_captura            	TIMESTAMP,
	url_captura             	TEXT
);

CREATE INDEX ide_cadastro_idx_detalhes_deputado ON camara_v1.detalhes_deputado (ide_cadastro);


CREATE TABLE camara_v1.detalhes_deputado_comissoes (
	ide_cadastro			INT,
	nome_parlamentar_atual		TEXT,
	partido_atual_id_partido	TEXT,
	uf_representacao_atual		TEXT,
	id_orgao_legislativo_cd		INT,
	sigla_comissao			TEXT,
	nome_comissao			TEXT,
	condicao_membro			TEXT,
	data_entrada			DATE,
	data_saida			DATE,
	data_captura            	TIMESTAMP,
	url_captura             	TEXT
);

CREATE INDEX id_orgao_legislativo_cd_detalhes_deputado_comissoes ON camara_v1.detalhes_deputado_comissoes (id_orgao_legislativo_cd);
CREATE INDEX ide_cadastro_detalhes_deputado_comissoes ON camara_v1.detalhes_deputado_comissoes (ide_cadastro);


CREATE TABLE camara_v1.detalhes_deputado_comissoes_cargos (
	ide_cadastro			INT,
	nome_parlamentar_atual		TEXT,
	partido_atual_id_partido	TEXT,
	uf_representacao_atual		TEXT,
	id_orgao_legislativo_cd		INT,
	sigla_comissao			TEXT,
	nome_comissao			TEXT,
	id_cargo			INT,
	nome_cargo			TEXT,
	data_entrada			DATE,
	data_saida			DATE,
	data_captura            	TIMESTAMP,
	url_captura             	TEXT
);

CREATE INDEX id_orgao_legislativo_cd_detalhes_deputado_comissoes_cargos ON camara_v1.detalhes_deputado_comissoes_cargos (id_orgao_legislativo_cd);
CREATE INDEX ide_cadastro_detalhes_deputado_comissoes_cargos ON camara_v1.detalhes_deputado_comissoes_cargos (ide_cadastro);



CREATE TABLE camara_v1.detalhes_deputado_periodos_exercicio (	
	ide_cadastro				INT,
	nome_parlamentar_atual			TEXT,
	partido_atual_id_partido		TEXT,
	situacao_exercicio			TEXT,
	sigla_uf_representacao			TEXT,
	data_inicio				DATE,
	data_fim				DATE,
	id_causa_fim_exercicio			INT,
	descricao_causa_fim_exercicio		TEXT,
	id_cadastro_parlamentar_anterior	INT,	
	data_captura            		TIMESTAMP,
	url_captura             		TEXT
);

CREATE INDEX ide_cadastro_detalhes_deputado_periodos_exercicio ON camara_v1.detalhes_deputado_periodos_exercicio (ide_cadastro);


CREATE TABLE camara_v1.detalhes_deputado_filiacoes_partidarias (	
	ide_cadastro			INT,
	nome_parlamentar_atual		TEXT,
	partido_atual_id_partido	TEXT,
	uf_representacao_atual		TEXT,
	id_partido_anterior		TEXT,
	sigla_partido_anterior		TEXT,
	nome_partido_anterior		TEXT,
	id_partido_posterior		TEXT,
	sigla_partido_posterior		TEXT,
	nome_partido_posterior		TEXT,
	data_filiacao_partido_posterior	DATE,
	hora_filiacao_partido_posterior	TEXT,	
	data_captura            	TIMESTAMP,
	url_captura             	TEXT
);

CREATE INDEX ide_cadastro_detalhes_deputado_filiacoes_partidarias ON camara_v1.detalhes_deputado_filiacoes_partidarias (ide_cadastro);


CREATE TABLE camara_v1.detalhes_deputado_hitorico_lider (	
	ide_cadastro			INT,
	nome_parlamentar_atual		TEXT,
	partido_atual_id_partido	TEXT,
	uf_representacao_atual		TEXT,
	id_historico_lider		INT,
	id_cargo_lideranca		TEXT,
	descricao_cargo_lideranca	TEXT,
	num_ordem_cargo			INT,
	data_designacao			DATE,
	data_termino			DATE,
	codigo_unidade_lideranca	TEXT,
	sigla_unidade_lideranca		TEXT,
	id_bloco_partido		TEXT,	
	data_captura            	TIMESTAMP,
	url_captura             	TEXT
);

CREATE INDEX ide_cadastro_detalhes_deputado_hitorico_lider ON camara_v1.detalhes_deputado_hitorico_lider (ide_cadastro);


CREATE TABLE camara_v1.partidos (
  id_partido        TEXT,
  sigla_partido     TEXT,
  nome_partido      TEXT,
  data_criacao      DATE,
  data_extincao     DATE,
	data_captura      TIMESTAMP,
	url_captura       TEXT
);

CREATE INDEX id_partido_partidos ON camara_v1.partidos (id_partido);

CREATE TABLE camara_v1.proposicoes_tramitadas_periodo(
	cod_proposicao    INT,
	tipo_proposicao   TEXT,
	numero            INT,
	ano               INT,
	data_tramitacao   TIMESTAMP,
	data_alteracao    TIMESTAMP,
	data_captura      TIMESTAMP,
	url_captura       TEXT,
	numero_captura    INT
);

CREATE INDEX cod_proposicao_proposicoes_tramitadas ON camara_v1.proposicoes_tramitadas_periodo (cod_proposicao);
CREATE INDEX data_tramitacao_proposicoes_tramitadas ON camara_v1.proposicoes_tramitadas_periodo (data_tramitacao);
CREATE INDEX data_captura_proposicoes_tramitadas ON camara_v1.proposicoes_tramitadas_periodo (data_captura);
CREATE INDEX numero_captura_proposicoes_tramitadas ON camara_v1.proposicoes_tramitadas_periodo (numero_captura);