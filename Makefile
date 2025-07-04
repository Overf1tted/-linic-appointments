.PHONY: lint test

lint:
	black . && isort . && flake8 .

test:
	pytest
