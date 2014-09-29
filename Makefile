.PHONY: docs wheel tox

TOX=$(shell (which tox))
WHEEL=$(shell (which wheel))

tox:
ifeq ($(strip $(TOX)),)
	pip install tox
endif

wheel:
ifeq ($(strip $(WHEEL)),)
	pip install wheel
endif

test: tox
	tox

publish: wheel
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel upload

docs-init:
	pip install -r docs/requirements.txt

docs:
	cd docs && make html

clean:
	rm -rf build dist *.egg-info __pycache__ .tox .coverage
	cd docs && make clean
