venv:
	python3 -m venv venv

setup:
	python -m ensurepip --upgrade
	python -m pip install --upgrade setuptools
	pip install --upgrade pip
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt