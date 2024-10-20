lint:
	@flake8

install:
	@pip install -e .

uninstall:
	@pip uninstall -y canopy

reinstall:
	@pip uninstall -y canopy
	@pip install -e .

.PHONY: lint install uninstall reinstall