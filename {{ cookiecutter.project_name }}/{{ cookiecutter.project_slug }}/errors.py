from flake8_plugin_utils import Error


class {{cookiecutter.error_name}}Error(Error):
    code = '{{cookiecutter.error_prefix}}001'
    message = '{{cookiecutter.error_message}}'
