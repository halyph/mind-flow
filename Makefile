.PHONY: help venv install clean serve readme tags

all: help

GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
CYAN   := $(shell tput -Txterm setaf 6)
RESET  := $(shell tput -Txterm sgr0)

VENV = .venv
ACTIVATE = $(VENV)/bin/activate
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip3

## Help:

help: ## Show this help
	@echo ''
	@echo 'Usage:'
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} { \
		if (/^[a-zA-Z_-]+:.*?##.*$$/) {printf "    ${YELLOW}%-20s${GREEN}%s${RESET}\n", $$1, $$2} \
		else if (/^## .*$$/) {printf "  ${CYAN}%s${RESET}\n", substr($$1,4)} \
		}' $(MAKEFILE_LIST)

## Local Setup:

venv: ## Init virtual environment
	@echo "Creating python virtual environment in '.venv' folder..."
	@python3 -m venv .venv

# !!! this does NOT work. Requires additional Makefile magic
# activate: ## Activate local virtual environment
# 	@eval $(echo ". .venv/bin/activate")

install: venv ## Install dependecies
	@echo "Installing python packages..."
	@$(PIP) install -r requirements.txt
	@echo
	@echo Run the following command to activate virtual environment:
	@echo . .venv/bin/activate

clean: ## Cleaning previous python virtual environment
	@echo "Cleaning previous python virtual environment '.venv'..."
	@rm -rf .venv

## Development environment:

serve: ## Run mkdocs server
	mkdocs serve --livereload

tags: ## Generate tags index
	python3 scripts/generate-tags.py

readme: tags ## Generate blog index and tags
	python3 scripts/generate-blog-index.py
