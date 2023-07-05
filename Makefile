run:
	poetry run python cafe/

.PHONY: clean
clean:
	@find ./ -name '__pycache__' -exec rm -rf {} \;