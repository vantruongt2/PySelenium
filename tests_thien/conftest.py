from tests_thien.utilities import constant
import pytest
import os


def pytest_addoption(parser):
    parser.addoption("--remote-host", action="store", help="Remote server for execution. http://127.0.0.1:4444/wd/hub", metavar="")
    parser.addoption("--driver", action="store", help="Configure the driver that you want to execute the tests. It should be: chrome, firefox", metavar="")
    parser.addoption("--url", action="store",default=constant.DA_URL , help="target machine url")


def pytest_configure(config):
    os.environ["url"] = config.getoption("url") 


@pytest.fixture(scope="session", autouse=True)
def remote_host(request):
    remote_host = request.config.getoption("--remote-host", None)
    pytest.remote_host = remote_host
    return remote_host


@pytest.fixture(scope="session", autouse=True)
def browser_name(request):
    browser_name = request.config.getoption("--driver", "chrome", True)
    pytest.browser_name = browser_name    
    return browser_name
