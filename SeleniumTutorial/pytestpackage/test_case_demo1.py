import pytest

@pytest.fixture()
def setUp():
    print("Once before every method 1")

def test_demo1_methodA(setUp):
    print("Running method A 1")

def test_demo1_methodB(setUp):
    print("Running method B 1")


