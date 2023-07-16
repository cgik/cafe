run:
	poetry run python cafe/

.PHONY: show
show:
	poetry env info

.PHONY: install
install:
	poetry install

.PHONY: clean
clean:
	@find ./ -name '__pycache__' -exec rm -rf {} \;

.PHONY: test
test:
	poetry run pytest -v --cov-config .coveragerc --cov=cafe tests/