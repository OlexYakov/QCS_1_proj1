import pytest
from .core import VarnameRetrievingError, varname


class TestVarName:
    def test_path_1(self):
        with pytest.raises(VarnameRetrievingError):
            varname(frame=2)

    def test_path_2(self):
        assert varname(frame=2, raise_exc=False) is None
