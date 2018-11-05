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