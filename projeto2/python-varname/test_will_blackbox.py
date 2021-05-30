import pytest
from varname.core import VarnameRetrievingError, will
from varname.utils import MultiTargetAssignmentWarning


class TestWillBB:

#########################################################################
#########################################################################
################################DO#######################################
#########################################################################
#########################################################################

    def test_do_f0_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=0,raise_exc=False)
                return self


            def do(self):
                return 'I am doing!'

        awesome = AwesomeClass()
        ret = awesome.permit().do()
        assert awesome.will == None
        
    
    def test_do_f0_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=0,raise_exc=True)
                return self

            def do(self):
                return 'I am doing!'

        awesome = AwesomeClass()
        with pytest.raises(VarnameRetrievingError):
            ret = awesome.permit().do()



    def test_do_f1_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=1,raise_exc=False)    
                return self


            def do(self):
                return 'I am doing!'

        awesome = AwesomeClass()
        ret = awesome.permit().do()
        assert awesome.will == 'do'
        
    
    def test_do_f1_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=1,raise_exc=True)
                return self

            def do(self):
                return 'I am doing!'

        awesome = AwesomeClass()
        ret = awesome.permit().do()
        assert awesome.will == 'do'   

    def test_do_f2_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit():
                    self.will = will(frame=2,raise_exc=False)
                    return self
                return inner_permit()

            def do(self):
                return 'I am doing!'

        awesome = AwesomeClass()
        ret = awesome.permit().do()
        assert awesome.will == 'do'
        
    
    def test_do_f2_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit():
                    self.will = will(frame=2,raise_exc=True)
                    return self
                return inner_permit()

            def do(self):
                return 'I am doing!'

        awesome = AwesomeClass()
        ret = awesome.permit().do()
        assert awesome.will == 'do'

    
    def test_do_f5_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                self.will = will(frame=5,raise_exc=False)
                                return self
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def do(self):
                return 'I am doing!'

        awesome = AwesomeClass()
        ret = awesome.permit().do()
        assert awesome.will == 'do'
        
    
    def test_do_f5_true(self):
        
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                self.will = will(frame=5,raise_exc=True)
                                return self
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def do(self):
                return 'I am doing!'

        awesome = AwesomeClass()
        ret = awesome.permit().do()
        assert awesome.will == 'do'
    
    def test_do_f6_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    self.will = will(frame=6,raise_exc=False)
                                    return self
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def do(self):
                return 'I am doing!'

        awesome = AwesomeClass()
        ret = awesome.permit().do()
        assert awesome.will == 'do'

    def test_do_f6_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    self.will = will(frame=6,raise_exc=True)
                                    return self
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def do(self):
                return 'I am doing!'

        awesome = AwesomeClass()
        ret = awesome.permit().do()
        assert awesome.will == 'do'

    def test_do_f7_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    def inner_permit6():
                                        self.will = will(frame=7,raise_exc=False)
                                        return self
                                    return inner_permit6()
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def do(self):
                return 'I am doing!'

        awesome = AwesomeClass()
        ret = awesome.permit().do()
        assert awesome.will == 'do'

    def test_do_f7_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    def inner_permit6():
                                        self.will = will(frame=7,raise_exc=True)
                                        return self
                                    return inner_permit6()
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def do(self):
                return 'I am doing!'

        awesome = AwesomeClass()
        ret = awesome.permit().do()
        assert awesome.will == 'do'

#########################################################################
#########################################################################
###############################NODO######################################
#########################################################################
#########################################################################
        
    def test_NoDo_f0_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=0,raise_exc=False)
                return self


            def NoDo(self):
                return 'I am NoDoing!'

        awesome = AwesomeClass()
        ret = awesome.permit().NoDo()
        assert awesome.will == None
        
    
    def test_NoDo_f0_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=0,raise_exc=True)
                return self

            def NoDo(self):
                return 'I am NoDoing!'

        awesome = AwesomeClass()
        with pytest.raises(VarnameRetrievingError):
            ret = awesome.permit().NoDo()



    def test_NoDo_f1_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=1,raise_exc=False)
                return self


            def NoDo(self):
                return 'I am NoDoing!'

        awesome = AwesomeClass()
        ret = awesome.permit().NoDo()
        assert awesome.will == 'NoDo'
        
    
    def test_NoDo_f1_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=1,raise_exc=True)
                return self

            def NoDo(self):
                return 'I am NoDoing!'

        awesome = AwesomeClass()
        ret = awesome.permit().NoDo()
        assert awesome.will == 'NoDo'   

    def test_NoDo_f2_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit():
                    self.will = will(frame=2,raise_exc=False)
                    return self
                return inner_permit()

            def NoDo(self):
                return 'I am NoDoing!'

        awesome = AwesomeClass()
        ret = awesome.permit().NoDo()
        assert awesome.will == 'NoDo'
        
    
    def test_NoDo_f2_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit():
                    self.will = will(frame=2,raise_exc=True)
                    return self
                return inner_permit()

            def NoDo(self):
                return 'I am NoDoing!'

        awesome = AwesomeClass()
        ret = awesome.permit().NoDo()
        assert awesome.will == 'NoDo'

    
    def test_NoDo_f5_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                self.will = will(frame=5,raise_exc=False)
                                return self
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def NoDo(self):
                return 'I am NoDoing!'

        awesome = AwesomeClass()
        ret = awesome.permit().NoDo()
        assert awesome.will == 'NoDo'
        
    
    def test_NoDo_f5_true(self):
        
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                self.will = will(frame=5,raise_exc=True)
                                return self
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def NoDo(self):
                return 'I am NoDoing!'

        awesome = AwesomeClass()
        ret = awesome.permit().NoDo()
        assert awesome.will == 'NoDo'
    
    def test_NoDo_f6_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    self.will = will(frame=6,raise_exc=False)
                                    return self
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def NoDo(self):
                return 'I am NoDoing!'

        awesome = AwesomeClass()
        ret = awesome.permit().NoDo()
        assert awesome.will == 'NoDo'

    def test_NoDo_f6_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    self.will = will(frame=6,raise_exc=True)
                                    return self
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def NoDo(self):
                return 'I am NoDoing!'

        awesome = AwesomeClass()
        ret = awesome.permit().NoDo()
        assert awesome.will == 'NoDo'

    def test_NoDo_f7_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    def inner_permit6():
                                        self.will = will(frame=7,raise_exc=False)
                                        return self
                                    return inner_permit6()
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def NoDo(self):
                return 'I am NoDoing!'

        awesome = AwesomeClass()
        ret = awesome.permit().NoDo()
        assert awesome.will == 'NoDo'

    def test_NoDo_f7_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    def inner_permit6():
                                        self.will = will(frame=7,raise_exc=True)
                                        return self
                                    return inner_permit6()
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def NoDo(self):
                return 'I am NoDoing!'

        awesome = AwesomeClass()
        ret = awesome.permit().NoDo()
        assert awesome.will == 'NoDo'

#########################################################################
#########################################################################
##########################FuncWithNumber113214###########################
#########################################################################
#########################################################################
        
    def test_FuncWithNumber113214_f0_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=0,raise_exc=False)
                return self


            def FuncWithNumber113214(self):
                return 'I am FuncWithNumber113214ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().FuncWithNumber113214()
        assert awesome.will == None
        
    
    def test_FuncWithNumber113214_f0_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=0,raise_exc=True)
                return self

            def FuncWithNumber113214(self):
                return 'I am FuncWithNumber113214ing!'

        awesome = AwesomeClass()
        with pytest.raises(VarnameRetrievingError):
            ret = awesome.permit().FuncWithNumber113214()



    def test_FuncWithNumber113214_f1_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=1,raise_exc=False)
                return self


            def FuncWithNumber113214(self):
                return 'I am FuncWithNumber113214ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().FuncWithNumber113214()
        assert awesome.will == 'FuncWithNumber113214'
        
    
    def test_FuncWithNumber113214_f1_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=1,raise_exc=True)
                return self

            def FuncWithNumber113214(self):
                return 'I am FuncWithNumber113214ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().FuncWithNumber113214()
        assert awesome.will == 'FuncWithNumber113214'   

    def test_FuncWithNumber113214_f2_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit():
                    self.will = will(frame=2,raise_exc=False)
                    return self
                return inner_permit()

            def FuncWithNumber113214(self):
                return 'I am FuncWithNumber113214ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().FuncWithNumber113214()
        assert awesome.will == 'FuncWithNumber113214'
        
    
    def test_FuncWithNumber113214_f2_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit():
                    self.will = will(frame=2,raise_exc=True)
                    return self
                return inner_permit()

            def FuncWithNumber113214(self):
                return 'I am FuncWithNumber113214ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().FuncWithNumber113214()
        assert awesome.will == 'FuncWithNumber113214'

    
    def test_FuncWithNumber113214_f5_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                self.will = will(frame=5,raise_exc=False)
                                return self
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def FuncWithNumber113214(self):
                return 'I am FuncWithNumber113214ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().FuncWithNumber113214()
        assert awesome.will == 'FuncWithNumber113214'
        
    
    def test_FuncWithNumber113214_f5_true(self):
        
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                self.will = will(frame=5,raise_exc=True)
                                return self
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def FuncWithNumber113214(self):
                return 'I am FuncWithNumber113214ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().FuncWithNumber113214()
        assert awesome.will == 'FuncWithNumber113214'
    
    def test_FuncWithNumber113214_f6_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    self.will = will(frame=6,raise_exc=False)
                                    return self
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def FuncWithNumber113214(self):
                return 'I am FuncWithNumber113214ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().FuncWithNumber113214()
        assert awesome.will == 'FuncWithNumber113214'

    def test_FuncWithNumber113214_f6_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    self.will = will(frame=6,raise_exc=True)
                                    return self
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def FuncWithNumber113214(self):
                return 'I am FuncWithNumber113214ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().FuncWithNumber113214()
        assert awesome.will == 'FuncWithNumber113214'

    def test_FuncWithNumber113214_f7_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    def inner_permit6():
                                        self.will = will(frame=7,raise_exc=False)
                                        return self
                                    return inner_permit6()
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def FuncWithNumber113214(self):
                return 'I am FuncWithNumber113214ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().FuncWithNumber113214()
        assert awesome.will == 'FuncWithNumber113214'

    def test_FuncWithNumber113214_f7_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    def inner_permit6():
                                        self.will = will(frame=7,raise_exc=True)
                                        return self
                                    return inner_permit6()
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def FuncWithNumber113214(self):
                return 'I am FuncWithNumber113214ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().FuncWithNumber113214()
        assert awesome.will == 'FuncWithNumber113214'
#########################################################################
#########################################################################
##############################_4_Arg_Test##############################
#########################################################################
#########################################################################
      
    def test__4_Arg_Test_f0_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=0,raise_exc=False)
                return self


            def _4_Arg_Test(self):
                return 'I am _4_Arg_Testing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._4_Arg_Test()
        assert awesome.will == None
        
    
    def test__4_Arg_Test_f0_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=0,raise_exc=True)
                return self

            def _4_Arg_Test(self):
                return 'I am _4_Arg_Testing!'

        awesome = AwesomeClass()
        with pytest.raises(VarnameRetrievingError):
            ret = awesome.permit()._4_Arg_Test()


    

    def test__4_Arg_Test_f1_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=1,raise_exc=False)
                return self


            def _4_Arg_Test(self):
                return 'I am _4_Arg_Testing!'

        awesome = AwesomeClass()
        print("HEHEYEYEYYYE")
        ret = awesome.permit()._4_Arg_Test()
        print(awesome.will)
        assert awesome.will == "_4_Arg_Test"
         
    def test__4_Arg_Test_f1_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=1,raise_exc=True)
                return self

            def _4_Arg_Test(self):
                return 'I am _4_Arg_Testing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._4_Arg_Test()
        assert awesome.will == '_4_Arg_Test'   

    def test__4_Arg_Test_f2_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit():
                    self.will = will(frame=2,raise_exc=False)
                    return self
                return inner_permit()

            def _4_Arg_Test(self):
                return 'I am _4_Arg_Testing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._4_Arg_Test()
        assert awesome.will == '_4_Arg_Test'
        
    
    def test__4_Arg_Test_f2_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit():
                    self.will = will(frame=2,raise_exc=True)
                    return self
                return inner_permit()

            def _4_Arg_Test(self):
                return 'I am _4_Arg_Testing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._4_Arg_Test()
        assert awesome.will == '_4_Arg_Test'

    
    def test__4_Arg_Test_f5_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                self.will = will(frame=5,raise_exc=False)
                                return self
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def _4_Arg_Test(self):
                return 'I am _4_Arg_Testing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._4_Arg_Test()
        assert awesome.will == '_4_Arg_Test'
        
    
    def test__4_Arg_Test_f5_true(self):
        
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                self.will = will(frame=5,raise_exc=True)
                                return self
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def _4_Arg_Test(self):
                return 'I am _4_Arg_Testing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._4_Arg_Test()
        assert awesome.will == '_4_Arg_Test'
    
    def test__4_Arg_Test_f6_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    self.will = will(frame=6,raise_exc=False)
                                    return self
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def _4_Arg_Test(self):
                return 'I am _4_Arg_Testing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._4_Arg_Test()
        assert awesome.will == '_4_Arg_Test'

    def test__4_Arg_Test_f6_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    self.will = will(frame=6,raise_exc=True)
                                    return self
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def _4_Arg_Test(self):
                return 'I am _4_Arg_Testing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._4_Arg_Test()
        assert awesome.will == '_4_Arg_Test'

    def test__4_Arg_Test_f7_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    def inner_permit6():
                                        self.will = will(frame=7,raise_exc=False)
                                        return self
                                    return inner_permit6()
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def _4_Arg_Test(self):
                return 'I am _4_Arg_Testing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._4_Arg_Test()
        assert awesome.will == '_4_Arg_Test'

    def test__4_Arg_Test_f7_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    def inner_permit6():
                                        self.will = will(frame=7,raise_exc=True)
                                        return self
                                    return inner_permit6()
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def _4_Arg_Test(self):
                return 'I am _4_Arg_Testing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._4_Arg_Test()
        assert awesome.will == '_4_Arg_Test'

#########################################################################
#########################################################################
##################################_12_34_234#################################
#########################################################################
#########################################################################
      
    def test__12_34_234_f0_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=0,raise_exc=False)
                return self

            def _12_34_234(self):
                return 'I am _12_34_234ing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._12_34_234()
        assert awesome.will == None
        
    
    def test__12_34_234_f0_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=0,raise_exc=True)
                return self

            def _12_34_234(self):
                return 'I am _12_34_234ing!'

        awesome = AwesomeClass()
        with pytest.raises(VarnameRetrievingError):
            ret = awesome.permit()._12_34_234()


    

    def test__12_34_234_f1_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=1,raise_exc=False)
                return self


            def _12_34_234(self):
                return 'I am _12_34_234ing!'

        awesome = AwesomeClass()
        print("HEHEYEYEYYYE")
        ret = awesome.permit()._12_34_234()
        print(awesome.will)
        assert awesome.will == "_12_34_234"
         
    def test__12_34_234_f1_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=1,raise_exc=True)
                return self

            def _12_34_234(self):
                return 'I am _12_34_234ing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._12_34_234()
        assert awesome.will == '_12_34_234'   

    def test__12_34_234_f2_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit():
                    self.will = will(frame=2,raise_exc=False)
                    return self
                return inner_permit()

            def _12_34_234(self):
                return 'I am _12_34_234ing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._12_34_234()
        assert awesome.will == '_12_34_234'
        
    
    def test__12_34_234_f2_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit():
                    self.will = will(frame=2,raise_exc=True)
                    return self
                return inner_permit()

            def _12_34_234(self):
                return 'I am _12_34_234ing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._12_34_234()
        assert awesome.will == '_12_34_234'

    
    def test__12_34_234_f5_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                self.will = will(frame=5,raise_exc=False)
                                return self
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def _12_34_234(self):
                return 'I am _12_34_234ing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._12_34_234()
        assert awesome.will == '_12_34_234'
        
    
    def test__12_34_234_f5_true(self):
        
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                self.will = will(frame=5,raise_exc=True)
                                return self
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def _12_34_234(self):
                return 'I am _12_34_234ing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._12_34_234()
        assert awesome.will == '_12_34_234'
    
    def test__12_34_234_f6_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    self.will = will(frame=6,raise_exc=False)
                                    return self
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def _12_34_234(self):
                return 'I am _12_34_234ing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._12_34_234()
        assert awesome.will == '_12_34_234'

    def test__12_34_234_f6_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    self.will = will(frame=6,raise_exc=True)
                                    return self
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def _12_34_234(self):
                return 'I am _12_34_234ing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._12_34_234()
        assert awesome.will == '_12_34_234'

    def test__12_34_234_f7_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    def inner_permit6():
                                        self.will = will(frame=7,raise_exc=False)
                                        return self
                                    return inner_permit6()
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def _12_34_234(self):
                return 'I am _12_34_234ing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._12_34_234()
        assert awesome.will == '_12_34_234'

    def test__12_34_234_f7_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    def inner_permit6():
                                        self.will = will(frame=7,raise_exc=True)
                                        return self
                                    return inner_permit6()
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def _12_34_234(self):
                return 'I am _12_34_234ing!'

        awesome = AwesomeClass()
        ret = awesome.permit()._12_34_234()
        assert awesome.will == '_12_34_234'

#########################################################################
#########################################################################
##################################____#################################
#########################################################################
#########################################################################
      
    def test______f0_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=0,raise_exc=False)
                return self


            def ____(self):
                return 'I am ____ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().____()
        assert awesome.will == None
        
    
    def test______f0_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=0,raise_exc=True)
                return self

            def ____(self):
                return 'I am ____ing!'

        awesome = AwesomeClass()
        with pytest.raises(VarnameRetrievingError):
            ret = awesome.permit().____()


    

    def test______f1_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=1,raise_exc=False)
                return self


            def ____(self):
                return 'I am ____ing!'

        awesome = AwesomeClass()
        print("HEHEYEYEYYYE")
        ret = awesome.permit().____()
        print(awesome.will)
        assert awesome.will == "____"
         
    def test______f1_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                self.will = will(frame=1,raise_exc=True)
                return self

            def ____(self):
                return 'I am ____ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().____()
        assert awesome.will == '____'   

    def test______f2_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit():
                    self.will = will(frame=2,raise_exc=False)
                    return self
                return inner_permit()

            def ____(self):
                return 'I am ____ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().____()
        assert awesome.will == '____'
        
    
    def test______f2_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit():
                    self.will = will(frame=2,raise_exc=True)
                    return self
                return inner_permit()

            def ____(self):
                return 'I am ____ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().____()
        assert awesome.will == '____'

    
    def test______f5_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                self.will = will(frame=5,raise_exc=False)
                                return self
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def ____(self):
                return 'I am ____ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().____()
        assert awesome.will == '____'
        
    
    def test______f5_true(self):
        
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                self.will = will(frame=5,raise_exc=True)
                                return self
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def ____(self):
                return 'I am ____ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().____()
        assert awesome.will == '____'
    
    def test______f6_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    self.will = will(frame=6,raise_exc=False)
                                    return self
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def ____(self):
                return 'I am ____ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().____()
        assert awesome.will == '____'

    def test______f6_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    self.will = will(frame=6,raise_exc=True)
                                    return self
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def ____(self):
                return 'I am ____ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().____()
        assert awesome.will == '____'

    def test______f7_false(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    def inner_permit6():
                                        self.will = will(frame=7,raise_exc=False)
                                        return self
                                    return inner_permit6()
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def ____(self):
                return 'I am ____ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().____()
        assert awesome.will == '____'

    def test______f7_true(self):
        
        class AwesomeClass:
            def __init__(self):
                self.will = None

            def permit(self):
                def inner_permit1():
                    def inner_permit2():
                        def inner_permit3():
                            def inner_permit4():
                                def inner_permit5():
                                    def inner_permit6():
                                        self.will = will(frame=7,raise_exc=True)
                                        return self
                                    return inner_permit6()
                                return inner_permit5()
                            return inner_permit4()
                        return inner_permit3()
                    return inner_permit2()
                return inner_permit1()

            def ____(self):
                return 'I am ____ing!'

        awesome = AwesomeClass()
        ret = awesome.permit().____()
        assert awesome.will == '____'
  
if __name__ == "__main__":
    #test____4_Arg_Test_f1_false()
    pytest.main()
