.PHONY: lint test

lint:
	black **/*.py && isort **/*.py && flake8 .

test:
	pytest
