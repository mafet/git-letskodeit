import pytest

@pytest.yield_fixture()
def setUp():
    print("Running method level setup")
    yield
    print("Running method level tearDown")

@pytest.yield_fixture(scope="class")
def oneTimeSetup(request, browser):
    print("Running one time setup")
    if browser == 'firefox':
        value = 10
        print("Running test in Firefox")
    else:
        value = 20
        print("Running test in Chrome")

    if request.cls is not None:
        request.cls.value = value
    yield value
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--ostype", help="Type of Operating System")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--ostype")