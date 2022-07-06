# tests/test_fruitBasket.py
import pytest
import filecmp

from typer.testing import CliRunner
from fruitBasket import __app_name__, __version__, cli, fruitBasket

runner = CliRunner()

def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout
	
def test_unhappyPath(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "notReal.csv")
    with pytest.raises(FileNotFoundError):
	    fruitBasket.ActiveBasket.process()
	
def test_badColumns(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "badheader.csv")
    with pytest.raises(ValueError):
	    fruitBasket.ActiveBasket.process()

def test_happyPath(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "fruitBasket.csv")
    fruitBasket.ActiveBasket.process()
    try:
        result = open('output.txt', 'r').read() == open('tests/outputSample.txt').read()
        assert(result)
    except Exception as ex:
        assert(False)