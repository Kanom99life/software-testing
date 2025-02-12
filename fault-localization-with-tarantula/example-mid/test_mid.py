import pytest
import mid

def test_mid1():
    assert mid.mid(3, 3, 5) == 3

def test_mid2():
    assert mid.mid(1, 2, 3) == 2
    
def test_mid3():
    assert mid.mid(3, 2, 1) == 2
    
def test_mid4():
    assert mid.mid(5, 5, 5) == 5
    
def test_mid5():
    assert mid.mid(5, 3, 4) == 4
    
def test_mid6():
    assert mid.mid(2, 1, 3) == 2