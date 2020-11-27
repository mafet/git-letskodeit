import pytest

@pytest.mark.run(order=2)
def test_methodB(setUp, oneTimeSetup):
    print("Running method B")

@pytest.mark.run(order=3)
def test_methodC(setUp, oneTimeSetup):
    print("Running method C")

@pytest.mark.run(order=4)
def test_methodD(setUp, oneTimeSetup):
    print("Running method D")

@pytest.mark.run(order=5)
def test_methodF(setUp, oneTimeSetup):
    print("Running method F")

@pytest.mark.run(order=1)
def test_methodA(setUp, oneTimeSetup):
    print("Running method A")

@pytest.mark.run(order=6)
def test_methodE(setUp, oneTimeSetup):
    print("Running method E")
