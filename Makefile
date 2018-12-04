NAME = projeto_curio/bigua
TAG = latest
SHELL = /bin/bash

APP_NAME=bigua

USER_NAME=kratos
USER_HOME=/home/$(USER_NAME)
APP=/app
SOURCE_PATH=bigua/
VOLUME_PATH=-v $(PWD)/$(SOURCE_PATH)/:/app/ \
			-v $(APP_NAME)-venv:/home/kratos/.pyenv/versions

# Prepare the environment
# ==============================
prepare:
	# Build Docker image
	make build
	# Create volume for venv and fix permissions
	docker volume create $(APP_NAME)-venv || true
	docker run --rm -it \
		$(VOLUME_PATH) \
		--entrypoint="" \
		$(NAME):$(TAG) chown 1000.1000 /home/kratos/.pyenv/versions
	make services

# Docker builds
# ==============================
build: basics
	docker build -t $(NAME):$(TAG) --rm .

# Tools
# ==============================
basics:
	@mkdir -p ./$(SOURCE_PATH)

services:
	@# Create network
	@echo -e "\e[32mCreating network...\e[0m"
	@docker network create $(APP_NAME) >/dev/null 2>/dev/null || true

repair:
	@echo -e "\e[32mReparing...\e[0m"
	docker rm -f db $(docker container ls -af name=$(APP_NAME)) 2>/dev/null || true
	make basics

# Interactive commands
# ==============================
shell: basics
	@docker run --rm -it \
		$(VOLUME_PATH) \
		$(ENVS) \
		--entrypoint="" \
		--user=$(USER_NAME) \
		--network $(APP_NAME) \
		--name $(APP_NAME)-shell-$$RANDOM \
		--workdir /app \
		$(NAME):$(TAG) $(SHELL)

shell-root: basics
	@echo -e "\e[91mMaking you a god...\e[0m"
	@docker run --rm -it \
		$(VOLUME_PATH) \
		$(ENVS) \
		--entrypoint="" \
		--name $(APP_NAME)-shellroot-$$RANDOM \
		--workdir /app \
		--network $(APP_NAME) \
		$(NAME):$(TAG) $(SHELL)

# Captures
# ==============================
camara_v1-historico: camara_v1-proposicoes_historico camara_v1-detalhes_deputados_historico

camara_v1-proposicoes_historico:
	
	@docker run --rm \
		$(VOLUME_PATH) \
		--entrypoint="" \
		--user=$(USER_NAME) \
		--network $(APP_NAME) \
		--name $(APP_NAME)-shell-$$RANDOM \
		--workdir /app/API/camara_v1/ \
		$(NAME):$(TAG) \
		sh -c '. /home/kratos/.pyenv/versions/venv/bin/activate; python proposicoes_historico.py'

camara_v1-detalhes_deputados_historico:
	
	@docker run --rm \
		$(VOLUME_PATH) \
		--entrypoint="" \
		--user=$(USER_NAME) \
		--network $(APP_NAME) \
		--name $(APP_NAME)-shell-$$RANDOM \
		--workdir /app/API/camara_v1/ \
		$(NAME):$(TAG) \
		sh -c '. /home/kratos/.pyenv/versions/venv/bin/activate; python detalhes_deputados_historico.py'

camara_v1-proposicoes_votadas_plenario_historico:
	
	@docker run --rm \
		$(VOLUME_PATH) \
		--entrypoint="" \
		--user=$(USER_NAME) \
		--network $(APP_NAME) \
		--name $(APP_NAME)-shell-$$RANDOM \
		--workdir /app/API/camara_v1/ \
		$(NAME):$(TAG) \
		sh -c '. /home/kratos/.pyenv/versions/venv/bin/activate; python proposicoes_votadas_plenario_historico.py'

camara_v1-votacao_historico:
	
	@docker run --rm \
		$(VOLUME_PATH) \
		--entrypoint="" \
		--user=$(USER_NAME) \
		--network $(APP_NAME) \
		--name $(APP_NAME)-shell-$$RANDOM \
		--workdir /app/API/camara_v1/ \
		$(NAME):$(TAG) \
		sh -c '. /home/kratos/.pyenv/versions/venv/bin/activate; python votacao_historico.py'

camara_v1-tramitacao_historico:
	
	@docker run --rm \
		$(VOLUME_PATH) \
		--entrypoint="" \
		--user=$(USER_NAME) \
		--network $(APP_NAME) \
		--name $(APP_NAME)-shell-$$RANDOM \
		--workdir /app/API/camara_v2/ \
		$(NAME):$(TAG) \
		sh -c '. /home/kratos/.pyenv/versions/venv/bin/activate; python tramitacao_historico.py'

camara_v1-deputados:
	
	@docker run --rm \
		$(VOLUME_PATH) \
		--entrypoint="" \
		--user=$(USER_NAME) \
		--network $(APP_NAME) \
		--name $(APP_NAME)-shell-$$RANDOM \
		--workdir /app/API/camara_v1/ \
		$(NAME):$(TAG) \
		sh -c '. /home/kratos/.pyenv/versions/venv/bin/activate; python deputados.py'

camara_v1-detalhes_deputados:
	
	@docker run --rm \
		$(VOLUME_PATH) \
		--entrypoint="" \
		--user=$(USER_NAME) \
		--network $(APP_NAME) \
		--name $(APP_NAME)-shell-$$RANDOM \
		--workdir /app/API/camara_v1/ \
		$(NAME):$(TAG) \
		sh -c '. /home/kratos/.pyenv/versions/venv/bin/activate; python detalhes_deputados.py'

camara_v1-partidos:
	
	@docker run --rm \
		$(VOLUME_PATH) \
		--entrypoint="" \
		--user=$(USER_NAME) \
		--network $(APP_NAME) \
		--name $(APP_NAME)-shell-$$RANDOM \
		--workdir /app/API/camara_v1/ \
		$(NAME):$(TAG) \
		sh -c '. /home/kratos/.pyenv/versions/venv/bin/activate; python partidos.py'

camara_v1-proposicoes_tramitadas:
	
	@docker run --rm \
		$(VOLUME_PATH) \
		--entrypoint="" \
		--user=$(USER_NAME) \
		--network $(APP_NAME) \
		--name $(APP_NAME)-shell-$$RANDOM \
		--workdir /app/API/camara_v1/ \
		$(NAME):$(TAG) \
		sh -c '. /home/kratos/.pyenv/versions/venv/bin/activate; python proposicoes_tramitadas.py'

camara_v1-proposicoes_votadas_plenario:
	
	@docker run --rm \
		$(VOLUME_PATH) \
		--entrypoint="" \
		--user=$(USER_NAME) \
		--network $(APP_NAME) \
		--name $(APP_NAME)-shell-$$RANDOM \
		--workdir /app/API/camara_v1/ \
		$(NAME):$(TAG) \
		sh -c '. /home/kratos/.pyenv/versions/venv/bin/activate; python proposicoes_votadas_plenario.py'

camara_v1-proposicoes:
	
	@docker run --rm \
		$(VOLUME_PATH) \
		--entrypoint="" \
		--user=$(USER_NAME) \
		--network $(APP_NAME) \
		--name $(APP_NAME)-shell-$$RANDOM \
		--workdir /app/API/camara_v1/ \
		$(NAME):$(TAG) \
		sh -c '. /home/kratos/.pyenv/versions/venv/bin/activate; python proposicoes.py'

camara_v1-votacao:
	
	@docker run --rm \
		$(VOLUME_PATH) \
		--entrypoint="" \
		--user=$(USER_NAME) \
		--network $(APP_NAME) \
		--name $(APP_NAME)-shell-$$RANDOM \
		--workdir /app/API/camara_v1/ \
		$(NAME):$(TAG) \
		sh -c '. /home/kratos/.pyenv/versions/venv/bin/activate; python votacao.py'
