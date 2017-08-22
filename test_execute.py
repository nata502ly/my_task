import pytest

from my_task.application import Application
from my_task.params import Data

@pytest.fixture
def app():
    fixture = Application()
    return fixture

def test_mine(app):
    app.find_element()
    app.login(Data(email = "tomsmith", password="SuperSecretPassword!"))
    app.screenshot()
    app.driver_close()