setup:
	python3 -m venv venv
	. venv/bin/activate
	python -m ensurepip --upgrade
	python -m pip install --upgrade setuptools
	pip install --upgrade pip
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt