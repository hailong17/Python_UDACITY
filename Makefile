#* Variables
SHELL := /usr/bin/env bash
PYTHON := python
PYTHONPATH := `pwd`

#* Installation
.PHONY: install
install:
	pip install -r requirements.txt

#* Application
.PHONY: app
app:
	python app.py

#* Create meme
.PHONY: meme
meme:
	python meme.py


