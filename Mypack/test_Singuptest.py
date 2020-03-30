import pytest

@pytest.yield_fixture()
def setup():
    print("open URL in browser")
    yield
    print("close browser")
def test_signupbyemail(setup):
    print("this is signup by email")
def test_sigupbyfacebook(setup):
    print("this is signup by facebook")

