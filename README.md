# flake8-plugin-cookiecutter

A cookiecutter template of a flake8 package with poetry, github actions and more.

## Usage

### Create project

```bash
$ cookiecutter https://github.com/d1618033/flake8-plugin-cookiecutter.git
project_name []: flake8_lint_something
full_name []: John Doe
email []: john_doe@gmail.com
github_username []: john_doe
plugin_name: lint_something
error_name: My
error_prefix: ME
error_message: x should be y
```

### Run linters, autoformat, tests etc.

    make pretty lint test

### Bump new version

    make bump_major
    make bump_minor
    make bump_patch

 