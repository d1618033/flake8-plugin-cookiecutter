import subprocess
from textwrap import dedent


def test_actual_code(tmpdir):
    file = tmpdir / 'code.py'
    with file.open('w') as f:
        f.write(
            dedent(
                """

                """
            ).lstrip()
        )
    output = (
        subprocess.run(
            ['poetry', 'run', 'flake8', str(file)], stdout=subprocess.PIPE
        )
        .stdout.decode()
        .strip()
    )
    assert output == (
        f'{tmpdir}/code.py:3:1: '
        f'{{cookiecutter.error_prefix}}001 {{cookiecutter.error_message}}'
    )
