import pytest

@pytest.yield_fixture()
def setup():
    print("open URL in browser")
    yield
    print("Close browser")
def test_loginbyemail(setup):
    print("this is login by email")
def test_loginbyfacebook(setup):
    print("this is login by facebook")
