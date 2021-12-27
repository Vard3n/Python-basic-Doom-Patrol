import pytest
import functions_for_testing as fp


def test_div():
    assert fp.div(30, 5) == 6
    assert fp.div(4200, 60) == 70
    assert fp.div(6, 2) == 3
