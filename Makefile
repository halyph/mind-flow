.PHONY: publish



publish:
	mkdocs build
	cd site
	git add .
	git commit -m "Publish"
	git push
	cd ..