.PHONY: setup dev clean

setup:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

dev:
	./venv/bin/flask --app src/app.py --debug run

clean:
	rm -rf venv
