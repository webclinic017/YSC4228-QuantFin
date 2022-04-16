import sys
import pytest
from backtest_strategy import execute
from tests.test_utils import generate_random_str

def test_bad_string_aum():
    for _ in range(50):
        with pytest.raises(SystemExit):
            # Bad AUM Param since it has characters
            bad_aum = generate_random_str()
            argv_head = [sys.argv[0]]
            new_args = [
                "tickers", "MSFT AAPL NVDA GOOG",
                "b", "20210315",
                "e", "20211023"
                "initial_aum", bad_aum,
                "strategy_type", "R",
                "days", "20",
                "top_pct", "75"
            ]
            sys.argv = argv_head + new_args
            execute()

def test_bad_top_pct():
    for _ in range(50):
        with pytest.raises(SystemExit):
            # Bad AUM Param since it has characters
            bad_top_pct = generate_random_str()
            argv_head = [sys.argv[0]]
            new_args = [
                "tickers", "MSFT AAPL NVDA GOOG",
                "b", "20210315",
                "e", "20211023"
                "initial_aum", "10000",
                "strategy_type", "R",
                "days", "20",
                "top_pct", bad_top_pct
            ]
            sys.argv = argv_head + new_args
            execute()