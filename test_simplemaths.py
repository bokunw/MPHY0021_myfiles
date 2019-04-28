import pytest
from .simplemaths import SimpleMaths as sm
from pytest import raises
import numpy as np

class TestSimpleMaths():
    def test_number_fails_on_floats(self):
        with raises(TypeError) as exception: 
            sm(1.2)
            
    def test_number_fails_on_str(self):
        with raises(TypeError) as exception: 
            sm("1")
            
    def test_number_fails_on_list(self):
        with raises(TypeError) as exception: 
            sm([1.2, 1])
            
    def test_sqaure(self):
        sm_obj = sm(2)
        
        assert sm_obj.square() == 4
        
    def test_factorial(self):
        sm_obj = sm(3)
        
        assert sm_obj.factorial() == 6
        
    def test_square_root(self):
        sm_obj = sm(0)
        
        assert sm_obj.square_root() == 0

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            