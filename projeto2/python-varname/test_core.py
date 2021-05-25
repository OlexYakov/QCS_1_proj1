from types import FunctionType
from typing import Tuple
import pytest
from varname.core import VarnameRetrievingError, varname
from varname.utils import MultiTargetAssignmentWarning


class TestVarName:

    @pytest.mark.skip(reason="No input to varname will cause the needed exception to occur")
    def test_path_1(self):
        ''' 
        To fail, an exception must occur within the ignore.get_frame method.
        Could not find a way to cause an exeption there.
        '''
        with pytest.raises(VarnameRetrievingError, match="Unable to"):
            varname(frame=2)

    @pytest.mark.skip(reason="No input to varname will cause the needed exception to occur")
    def test_path_2(self):
        ''' 
        To fail, an exception must occur within the ignore.get_frame method.
        This is effectivelly the same test as above, but instead of raising an exception the 
        function returns None
        Could not find a way to cause an exeption there.
        '''
        assert varname(frame=2, raise_exc=False) is None

    def test_path_3(self):
        # Its suposed to be used within another function (or use frame = 0 karg)
        with pytest.raises(VarnameRetrievingError, match="Failed to"):
            name = varname(frame=3)

    def test_path_4(self):
        # Its suposed to be used within another function (or use frame = 0 karg)
        assert varname(frame=3, raise_exc=False) is None

    def test_path_5(self):
        '''
        Annotated assignment, with multi_vars.
        TODO: more tests with multi vars
        '''
        def foo():
            return varname(multi_vars=True)

        im_annotated: Tuple = foo()

        im_annotated = im_annotated[0]
        assert im_annotated == "im_annotated"

    def test_path_6(self):
        # 1,2,4,7,9,13,14,15,16,17,18,19,21,23
        def foo():
            return varname()

        with pytest.warns(MultiTargetAssignmentWarning, match="Multiple targets in assignment"):
            target1 = target2 = foo()
            assert target1 == "target1" and target2 == "target1"  # not bug, feature

    def test_path_10(self):
        def foo():
            return varname()

        a = foo()
        assert a == "a"


if __name__ == "__main__":
    pytest.main()
