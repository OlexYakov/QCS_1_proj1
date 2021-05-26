import pytest
from varname.core import VarnameRetrievingError, will
from varname.utils import MultiTargetAssignmentWarning


class TestWill:

    @pytest.mark.skip(reason="No input to varname will cause the needed exception to occur")
    def test_path_1(self):
        '''
        To fail, an exception must occur within the ignore.get_frame method.
        Could not find a way to cause an exeption there.
        '''
        with pytest.raises(VarnameRetrievingError, match="Unable to"):
            will(frame=2)

    @pytest.mark.skip(reason="No input to varname will cause the needed exception to occur")
    def test_path_2(self):
        '''
        To fail, an exception must occur within the ignore.get_frame method.
        This is effectivelly the same test as above, but instead of raising an exception the
        function returns None
        Could not find a way to cause an exeption there.
        '''
        assert will(frame=2, raise_exc=False) is None

    def test_path_3(self):
        # Its suposed to be used within another function (or use frame = 0 karg)
        with pytest.raises(VarnameRetrievingError, match="Function `will`"):
            will(frame=3)

    def test_path_4(self):
        # Its suposed to be used within another function (or use frame = 0 karg)
        assert will(frame=3, raise_exc=False) is None

    def test_path_5(self):
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will()
                if self.will == 'do':
                    # let self handle do
                    return self
                raise AttributeError(
                    'Should do something with AwesomeClass object'
                )

            def do(self):
                if self.will != 'do':
                    raise AttributeError("You don't have permission to do")
                return 'I am doing!'

        awesome = AwesomeClass()
        ret = awesome.permit().do()
        assert ret == 'I am doing!'
        assert awesome.will == 'do'


if __name__ == "__main__":
    pytest.main()
