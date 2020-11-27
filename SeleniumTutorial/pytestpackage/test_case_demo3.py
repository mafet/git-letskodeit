import pytest

@pytest.yield_fixture()
def setUp():
    print("Once before every method 3")
    yield
    print("Once after every method 3")

def test_demo3_methodA(setUp):
    print("Running method A 3")

def test_demo3_methodB(setUp):
    print("Running method B 3")


