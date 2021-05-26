from types import FunctionType
from typing import Tuple
import pytest
from varname.core import VarnameRetrievingError, varname
from varname.utils import ImproperUseError, MultiTargetAssignmentWarning


class TestVarName:

    @pytest.mark.skip(reason="No input to varname will cause the needed exception to occur")
    def test_unable_error(self):
        ''' 
        1. [1,2,3,5]

        To fail, an exception must occur within the ignore.get_frame method.
        Could not find a way to cause an exeption there.
        '''
        with pytest.raises(VarnameRetrievingError, match="Unable to"):
            varname(frame=2)

    @pytest.mark.skip(reason="No input to varname will cause the needed exception to occur")
    def test_unable_error_no_raise(self):
        ''' 
        2. [1,2,3,6]

        To fail, an exception must occur within the ignore.get_frame method.
        This is effectivelly the same test as above, but instead of raising an exception the 
        function returns None
        Could not find a way to cause an exeption there.
        '''
        assert varname(frame=2, raise_exc=False) is None

    def test_parent_failed_error(self):
        '''
        3. [1,2,4,7,8,10]
        '''
        # Its suposed to be used within another function (or use frame = 0 karg)
        with pytest.raises(VarnameRetrievingError, match="Failed to"):
            name = varname(frame=3)

    def test_parent_failed_error_no_raise(self):
        '''
        4. [1,2,4,7,8,11]
        '''
        # Its suposed to be used within another function (or use frame = 0 karg)
        assert varname(frame=3, raise_exc=False) is None

    def test_annotated_multivars(self):
        '''
        5. [1,2,4,7,9,12,16,17,18,19,20]
        '''
        def foo():
            return varname(multi_vars=True)

        name: tuple = foo()

        assert isinstance(name, tuple) and name[0] == "name"

    def test_annotated(self):
        '''
        6. [1,2,4,7,9,12,16,17,18,19,21,23]
        '''
        def foo():
            return varname()

        name: str = foo()

        assert isinstance(name, str) and name == "name"

    def test_improper_use(self):
        '''
        7. [1,2,4,7,9,13,15,16,17,19,21,22]
        '''
        def foo():
            return varname()

        with pytest.raises(ImproperUseError, match="Expect a single variable"):
            name, name2 = foo()

    def test_normal(self):
        '''
        8. [1,2,4,7,9,13,15,16,17,18,19,21,23]
        '''
        def foo():
            return varname()

        name = foo()

        assert name == "name"

    def test_multiple_assignment(self):
        '''
        9. 1,2,4,7,9,13,14,15,16,17,18,19,21,23
        '''
        def foo():
            return varname()

        with pytest.warns(MultiTargetAssignmentWarning, match="Multiple targets in assignment"):
            target1 = target2 = foo()
            assert target1 == "target1" and target2 == "target1"  # not bug, feature


if __name__ == "__main__":
    pytest.main()
