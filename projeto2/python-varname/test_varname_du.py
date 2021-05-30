from types import FunctionType
from typing import Tuple
import pytest
from varname.core import VarnameRetrievingError, varname
from varname.utils import ImproperUseError, MultiTargetAssignmentWarning


class TestVarname:

    def test_ann_assign_multivars(self):
        '''
        path descovered for multivars 3. 1-2-3-7-8-12-13-15-14-17
        covers:
            multivars 3
            node 1,4,8,11
            target 1
            names 6
        '''

        def foo():
            return varname(multi_vars=True)

        name: tuple = foo()

        assert isinstance(name, tuple) and name[0] == "name"

    def test_ann_assign(self):
        '''
        path descovered for multivars 4. 1-2-3-7-8-12-13-15-14-16-18
        covers:
            multivars 4
            names 7
        '''

        def foo():
            return varname()

        name: tuple = foo()

        assert name == "name"

    def test_tuple(self):
        '''
        path descovered for multivars 5. 1-2-3-7-9-10-12-13-14-17
        covers:
            multivars 5
            raise_exc 1
            node 5,6,9
            target 2
            names 1
        '''

        def foo():
            return varname(multi_vars=True)

        name, name2 = foo()
        assert name == "name" and name2 == "name2"

    def test_tuple_multivars(self):
        '''
        path descovered for multivars 6. 1-2-3-7-9-10-12-13-14-16-18
        covers:
            multivars 6
            names 4
        '''

        def foo():
            return varname()

        with pytest.raises(ImproperUseError):
            name, name2 = foo()
            # assert name == "name" and name2 == "name2"

    def test_multivars(self):
        '''
        path descovered for multivars 7. 1-2-3-7-9-10-12-13-15-14-17
        covers:
            multivars 7
            names 2
        '''

        def foo():
            return varname(multi_vars=True)

        name = foo()

        assert isinstance(name, Tuple) and name[0] == "name"

    def test_normal(self):
        '''
        path descovered for multivars 8. 1-2-3-7-9-10-12-13-15-14-16-18
        covers:
            multivars 8
        '''

        def foo():
            return varname()

        name = foo()

        assert name == "name"

    def test_multiple_asgn_tup_multivars(self):
        '''
        path descovered for multivars 9. 1-2-3-7-9-11-10-12-13-14-17
        covers:
            multivars 9
            node 7,10
            names 3
        '''

        def foo():
            return varname(multi_vars=True)

        with pytest.warns(MultiTargetAssignmentWarning):
            name, name2 = name3, name4 = foo()
            assert name == name3 == "name" and name2 == name4 == "name2"

    def test_multiple_asgn_tup(self):
        '''
        path descovered for multivars 10. 1-2-3-7-9-11-10-12-13-14-16-19
        covers:
            multivars 10
            names 5
        '''

        def foo():
            return varname()

        with pytest.warns(MultiTargetAssignmentWarning), pytest.raises(ImproperUseError):
            name, name2 = name3, name4 = foo()
            assert name == name3 == "name" and name2 == name4 == "name2"

    def test_multivars_warn(self):
        '''
        path descovered for multivars 11. 1-2-3-7-9-11-10-12-13-15-14-17
        covers:
            multivars 11
        '''

        def foo():
            return varname(multi_vars=True)

        with pytest.warns(MultiTargetAssignmentWarning):
            name = name2 = foo()

            assert isinstance(name, Tuple) and name[0] == "name"

    def test_normal_warn(self):
        '''
        path descovered for multivars 12. 1-2-3-7-9-11-10-12-13-15-14-16
        covers:
            multivars 12
        '''

        def foo():
            return varname()

        with pytest.warns(MultiTargetAssignmentWarning):
            name = name2 = foo()

            assert name == "name"


if __name__ == "__main__":
    pytest.main()
