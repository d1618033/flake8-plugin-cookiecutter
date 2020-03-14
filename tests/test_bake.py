def test_defaults(cookies):
    result = cookies.bake()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == "flake8-if-statements"
    assert result.project.isdir()
