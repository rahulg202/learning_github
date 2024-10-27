from src.math_operations import add,sub,division

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(-1,-1)==-2

def test_sub():
    assert sub(5,3)==2
    assert sub(3,3)==0
    assert sub(3,9)==-6
    assert sub(-1,-1)==0

def test_divison():
    assert division(8,4)==2
    assert division(4,2)==2

