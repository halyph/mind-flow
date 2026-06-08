.PHONY: help install clean serve readme tags rss build lint lint-fix

all: help

GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
CYAN   := $(shell tput -Txterm setaf 6)
RESET  := $(shell tput -Txterm sgr0)

BLOG_MD_FILES := "docs/blog/**/*.md"
BLOG_2026_MD_FILES := "docs/blog/2026/*.md"

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

clean: ## Remove .venv and site directories
	@echo "Cleaning .venv and site directories..."
	@rm -rf .venv site

## Development environment:

serve: ## Run mkdocs server
	uv run mkdocs serve --livereload

build: ## Build site with CI config
	uv run mkdocs build -f mkdocs.ci.yml

tags: ## Generate tags index
	uv run python scripts/generate-tags.py

readme: tags ## Generate blog index and tags
	uv run python scripts/generate-blog-index.py

rss: build ## Generate RSS and Atom feeds (requires built site)
	uv run python scripts/generate-rss.py

## Linting:

lint: ## Lint markdown files in docs/blog
	npx markdownlint-cli2 $(BLOG_MD_FILES)

lint-fix: ## Auto-fix markdown issues in docs/blog
	npx markdownlint-cli2 --fix $(BLOG_MD_FILES)

lint-2026: ## Lint only 2026 blog posts
	npx markdownlint-cli2 $(BLOG_2026_MD_FILES)

lint-fix-2026: ## Auto-fix markdown issues in 2026 blog posts only
	npx markdownlint-cli2 --fix $(BLOG_2026_MD_FILES)
