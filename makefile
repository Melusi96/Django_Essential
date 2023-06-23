install: venv
	python3 -m virtualenv venv; . venv/bin/activate; pip install -Ur requirements.txt

venv:
	test -d venv || python3 -m venv venv

clean:
	rm -rf venv