ci: format test
extra: lint typecheck
all: ci extra

format:
	black --quiet --check .
	isort --quiet --check .
test:
	pytest --doctest-modules -q
lint:
	ruff .
typecheck:
	mypy . --check-untyped-defs

.PHONY: ci extra all format test lint typecheck