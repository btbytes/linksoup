.venv:
	python -m venv .venv

deps: .venv
	.venv/bin/python install --upgrade pip
	.venv/bin/python install -r requirements.txt

run:
	uvicorn app.main:app --reload
