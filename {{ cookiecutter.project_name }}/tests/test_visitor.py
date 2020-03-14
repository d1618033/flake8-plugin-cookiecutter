from textwrap import dedent

from flake8_plugin_utils import assert_error, assert_not_error

from {{cookiecutter.project_slug}}.errors import {{cookiecutter.error_name}}Error
from {{cookiecutter.project_slug}}.visitor import {{cookiecutter.plugin_name}}Visitor


def test_error():
    code = dedent(
        """

        """
    )
    assert_error(
        {{cookiecutter.plugin_name}}Visitor, code, {{cookiecutter.error_name}}Error
    )



def test_no_error():
    code = dedent(
        """
        
        """
    )
    assert_not_error({{cookiecutter.plugin_name}}Visitor, code)
