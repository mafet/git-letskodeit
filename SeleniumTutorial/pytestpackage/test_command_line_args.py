import pytest

def test_methodA(oneTimeSetup, setUp):
    print("Running method A")

def test_methodB(setUp, oneTimeSetup):
    print("Running method B")