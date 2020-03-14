from flake8_plugin_utils import Plugin

from .visitor import {{cookiecutter.plugin_name}}Visitor


class {{cookiecutter.plugin_name}}Plugin(Plugin):
    name = '{{cookiecutter.plugin_name}}'
    version = '0.0.0'
    visitors = [{{cookiecutter.plugin_name}}Visitor]
