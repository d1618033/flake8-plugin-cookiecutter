# flake8-plugin-cookiecutter

A cookiecutter template of a flake8 package with poetry, github actions and more.

## Usage

### Create project

```bash
$ cookiecutter https://github.com/d1618033/flake8-plugin-cookiecutter.git
checks [if-statements]: 
project_name [flake8-lint-if-statements]: 
description [Flake8 Linter for If Statements]: 
project_slug [flake8_lint_if_statements]: 
full_name [John Doe]: 
email [john.doe@gmail.com]: 
github_username [johndoe]: 
plugin_name [IfStatements]: 
error_name [IfStatements]: 
error_prefix [IFSTATEMENTS]: 
error_message [should be x]: 
```

### Run linters, autoformat, tests etc.

    make pretty lint test

### Bump new version

    make bump_major
    make bump_minor
    make bump_patch

 