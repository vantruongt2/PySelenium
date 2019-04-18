import pytest


def pytest_addoption(parser):
    parser.addoption("--remote-host", action="store", help="Remote server for execution. http://127.0.0.1:4444/wd/hub", metavar="")


@pytest.fixture(scope="session", autouse=True)
def get_remote_host(request):
    remote_host = request.config.getoption("--remote-host", None)
    if remote_host:
        pytest.remote_host = remote_host    
    return remote_host
