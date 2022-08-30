# NOTES

## Useful MkDocs commands to get you started

* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print this help message.

## How to setup local development environment?

1. `python3 --version`
2. `python3 -m venv .venv`
3. `source .venv/bin/activate`
4. `pip install -r requirements.txt`
5. *Do smth useful*
6. `deactivate`

## Publish

1. `git clone git@github.com:halyph/halyph.github.io.git site` - clone target "publish" repo
2. `mkdocs build` - build
3. `git add .` and `git commit -m "Publish"`
4. `git push` - deploy/publish site 
