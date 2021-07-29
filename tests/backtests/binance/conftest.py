import pytest

from tests.backtests.helpers import Backtest
from tests.conftest import REPO_ROOT


@pytest.fixture(scope="session")
def check_exchange_data_presence():
    binance_exchange_data_dir = REPO_ROOT / "user_data" / "data" / "binance"
    if not binance_exchange_data_dir.is_dir():
        pytest.fail(
            "There's no exchange data. Make sure the repository submodule is init/update. "
            "Check the repository README.md for more information."
        )
    if not list(binance_exchange_data_dir.rglob("*.json.gz")):
        pytest.fail(
            "There's no exchange data. Make sure the repository submodule is init/update. "
            "Check the repository README.md for more information."
        )


@pytest.fixture
def backtest(request, check_exchange_data_presence):
    return Backtest(request, "binance")
