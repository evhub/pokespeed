.PHONY: install
install: build
	pip install -Ue .

.PHONY: install-py2
install-py2: build
	python2 -m pip install -Ue .

.PHONY: force-install
force-install: force-build
	pip install -Ue .

.PHONY: force-install-py2
force-install-py2: force-build
	python2 -m pip install -Ue .

.PHONY: setup
setup:
	pip install -U setuptools wheel pip pytest coconut-develop[watch]

.PHONY: unclean-build
unclean-build:
	coconut pokespeed-source pokespeed --strict

.PHONY: build
build: clean unclean-build

.PHONY: force-build
force-build: clean
	coconut pokespeed-source pokespeed --force --strict

.PHONY: package
package:
	python3 setup.py sdist bdist_wheel

.PHONY: upload
upload: install package
	pip3 install -U --ignore-installed twine
	twine upload dist/*

.PHONY: test
test: install
	pytest --strict-markers --full-trace -s ./pokespeed/tests

.PHONY: force-test
force-test: force-install
	pytest --strict-markers --full-trace -s ./pokespeed/tests

.PHONY: force-test-py2
force-test-py2: force-install-py2
	python2 -m pytest --strict-markers --full-trace -s ./pokespeed/tests

.PHONY: clean
clean:
	rm -rf ./dist ./build
	-find . -name "*.pyc" -delete
	-C:/GnuWin32/bin/find.exe . -name "*.pyc" -delete
	-find . -name "__pycache__" -delete
	-C:/GnuWin32/bin/find.exe . -name "__pycache__" -delete

.PHONY: wipe
wipe: clean
	rm -rf ./pokespeed

.PHONY: watch
watch: install
	coconut pokespeed-source pokespeed --watch --strict
