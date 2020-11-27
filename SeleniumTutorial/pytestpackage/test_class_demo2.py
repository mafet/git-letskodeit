import pytest
from class_to_test import SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetup", "setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = SomeClassToTest(self.value)

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

