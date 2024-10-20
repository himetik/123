lint:
	@flake8

install:
	@pip install -e .

uninstall:
	@pip uninstall canopy

reinstall:
	@pip uninstall canopy
	@pip install -e .

.PHONY: lint install reinstall