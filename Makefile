.PHONY: publish

publish:
	mkdocs build
	git -C site add --all
	git -C site commit -m "Publish"
	git -C site push --force