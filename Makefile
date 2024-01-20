.PHONY: run
run: install
	pokespeed

.PHONY: force-run
force-run: force-install
	pokespeed

.PHONY: install
install: build
	pip install -Ue .

.PHONY: force-install
force-install: force-build
	pip install -Ue .

.PHONY: setup
setup:
	pip install -U setuptools wheel pip pytest coconut-develop[watch]

.PHONY: unclean-build
unclean-build:
	coconut pokespeed-source pokespeed --strict --target 3

.PHONY: build
build: clean unclean-build

.PHONY: force-build
force-build: clean
	coconut pokespeed-source pokespeed --force --strict --target 3

.PHONY: package
package:
	python setup.py sdist bdist_wheel

.PHONY: upload
upload: install package
	pip3 install -U --ignore-installed twine
	twine upload dist/*

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
	coconut pokespeed-source pokespeed --watch --strict --target 3
