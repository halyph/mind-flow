.PHONY: help install clean serve readme tags

all: help

GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
CYAN   := $(shell tput -Txterm setaf 6)
RESET  := $(shell tput -Txterm sgr0)

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

install: ## Install dependencies and create venv
	@echo "Installing dependencies with uv..."
	@uv sync
	@echo
	@echo "✓ Dependencies installed in .venv/"
	@echo "Note: No need to manually activate venv - use 'uv run' or Makefile targets"

clean: ## Remove .venv directory
	@echo "Cleaning .venv..."
	@rm -rf .venv

## Development environment:

serve: ## Run mkdocs server
	uv run mkdocs serve --livereload

tags: ## Generate tags index
	uv run python scripts/generate-tags.py

readme: tags ## Generate blog index and tags
	uv run python scripts/generate-blog-index.py
