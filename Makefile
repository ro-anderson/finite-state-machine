.PHONY: clean help cleanGit, chat, api, app

SHELL=/bin/bash

## Remove Python cache files
clean:
	find . -name "__pycache__" -type d -exec rm -r {} \+

## Run Monarch chat through terminal
chat:
	poetry run python monarch_multi_agent/app/main.py

## Run Monarch api locally through terminal
api:
	poetry run python serving/api.py

## Run Monarch streamlit app locally through terminal
app:
	poetry run python monarch_multi_agent/app/streamlit_app.py

## Delete all local branches except main and develop
cleanGit:
	@git fetch --all
	@for branch in $$(git branch | grep -v "main" | grep -v "develop" | sed 's/^\*//'); do \
		git branch -D $$branch; \
	done

## Display help information
help:
	@echo "Available commands:"
	@echo "  make clean         - Remove Python cache files"
	@echo "  make chat          - Run Monarch chat through terminal"
	@echo "  make api           - Run Monarch api locally through terminal"
	@echo "  make app           - Run Monarch streamlit app locally through terminal"
	@echo "  make help          - Display this help information"
	@echo "  make cleanGit      - Delete all local branches except main and develop"
# Default target
.DEFAULT_GOAL := help
