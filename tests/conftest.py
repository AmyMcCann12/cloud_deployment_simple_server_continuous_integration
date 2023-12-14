import pytest, sys, random, py, os
from app import app
from xprocess import ProcessStarter
from playwright.sync_api import (
    BrowserContext,
    Page,
)
from typing import Generator

@pytest.fixture
def web_client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def page(context: BrowserContext) -> Generator[Page, None, None]:
    page = context.new_page()
    yield page

@pytest.fixture
def test_web_address(xprocess):
    python_executable = sys.executable
    app_file = py.path.local(__file__).dirpath("../app.py")
    port = str(random.randint(4000, 4999))
    class Starter(ProcessStarter):
        env = {"PORT": port, "APP_ENV": "test", **os.environ}
        pattern = "Debugger PIN"
        args = [python_executable, app_file]

    xprocess.ensure("flask_test_server", Starter)

    yield f"localhost:{port}"

    xprocess.getinfo("flask_test_server").terminate()