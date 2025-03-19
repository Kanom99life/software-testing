import pytest
from binarysearch import binary_search

def test_bin1(capsys):
    myArray = [1,2,3,4,5]
    target1 = 0    
    result = binary_search(myArray, target1)    
    captured = capsys.readouterr()
    assert "can't find" in captured.out1
    # assert "some ok text" in captured.out
    assert result == -1

def test_bin2():
    myArray = [1,2,3,4,5]
    target2 = 2
    assert binary_search(myArray, target2) == 1
