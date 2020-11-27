import pytest

@pytest.yield_fixture()
def setUp():
    print("Once before every method 2")
    yield
    print("Once after every method 2")

def test_demo2_methodA(setUp):
    print("Running method A 2")

def test_demo2_methodB(setUp):
    print("Running method B 2")


