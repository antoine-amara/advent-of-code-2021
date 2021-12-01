.SILENT:

default: help

refreshcache:	## quick and dirty command to add write permission to poetry to write the ~/.cache folder
	sudo chown -R vscode ~/.cache
.PHONY: refreshcache

dependencies: refreshcache	## install python packages
	poetry install
.PHONY: dependencies

attach-git-hooks: refreshcache	## attach git hooks to make some checks on the code for each commits
	poetry run pre-commit install
.PHONY: attach-git-hooks

lint: refreshcache	## run flake8 linter
	poetry run flake8 advent_of_code_2021
.PHONY: lint

format: refreshcache	## run black formater
	poetry run black advent_of_code_2021

run: refreshcache	## run python script which resolve one day problem. the name should be day-{N}.py. For example to run problem day 23rd: "make run day=23"
	echo "#### Launching solution for day ${day} ####\n"
	poetry run ipython advent_of_code_2021/day-${day}.py
	echo "\n###########################################\n"
.PHONY: run

run-debug: refreshcache	## run python script which resolve one day problem in debug mode. it stop the execution until vscode debugger is connected to the process on port 4242.
	poetry run python -m debugpy --listen localhost:4242 --wait-for-client advent_of_code_2021/day-${day}.py
.PHONY: run-debug

help:	## show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
