import myfunctions as my
import numpy as np

def test_my_sum__int():    
    assert my.my_sum(1,2) == 3
    
def test_my_sum__nan():
    assert my.my_sum(np.NaN,1) == 1
    