.PHONY: setup test clean

setup:
	python3 -m venv venv &&\
	. venv/bin/activate &&\
	pip install --upgrade pip setuptools &&\
	pip install -r requirements.txt -r requirements-dev.txt -r requirements-docs.txt &&\
	python -m pip install -e .

test:
	python3 -m coverage run --source trimmer -m pytest -vv --tb=short -ra --color=yes $(test)
	python3 -m coverage report --show-missing --skip-empty --skip-covered

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf ./*.egg-info

build:
	python setup.py sdist bdist_wheel

release-pypi: clean build
	python -m twine upload -u __token__ dist/*

mkdocs-local:
	mkdocs serve

mkdocs-push:
	mkdocs gh-deploy --force --clean --verbose
