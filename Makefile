#!/usr/bin/make -f

export PEX := $(PWD)/bin/pex

PEX := bin/pex
VIRTUALENV := python3 -m venv
PIP := venv/bin/pip
SCRIPT := justwatch

all: build

.PHONY: build
build: bin/pex bin/$(SCRIPT)

bin/pex:
	mkdir -p bin/
	$(eval TMPDIR := $(shell mktemp -d))
	python3 -m venv $(TMPDIR)
	$(TMPDIR)/bin/pip install pex requests wheel
	$(TMPDIR)/bin/pex requests pex -c pex -o $@
	rm -rf $(TMPDIR)

bin/$(SCRIPT): $(wildcard **/*.py)
	$(PEX) . -r requirements.txt --python=python3.6 -c $(SCRIPT) -o $@

.PHONY: requirements.txt
requirements.txt:
	@echo 'Installing into a clean virtualenv'
	$(eval TMPDIR := $(shell mktemp -d))
	$(VIRTUALENV) $(TMPDIR)
	$(TMPDIR)/bin/pip install --upgrade -e .
	@echo 'Writing out new requirements.txt based on setup.py'
	$(TMPDIR)/bin/pip freeze -r requirements.txt | grep -v '^-e' > requirements.txt
	@echo 'Wrote new requirements.txt'
	rm -rf $(TMPDIR)

.PHONY: venv
venv:
	$(VIRTUALENV) venv
	$(PIP) install -r requirements.txt
	$(PIP) install -e .

.PHONY: clean
clean:
	rm -rf bin/ venv/ *.egg-info
