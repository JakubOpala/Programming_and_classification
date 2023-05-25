import pytest
import functions as f

# Cesar tests ---------------------------------------------------------------

def test_cesar_normal():
    assert f.cesar('hn0', 2) == 'jp2'

def test_cesar_big_shift():
    assert f.cesar('hn0', 1026) == 'jp2'

def test_cesar_wrong_inp():
    with pytest.raises(AttributeError):
        f.cesar(3,12) 

def test_cesar_wrong_shift():
    with pytest.raises(TypeError):
        f.cesar('test', 2.5)

# sort_dict tests --------------------------------------------------------------------

def test_sort_dict():
    assert f.sort_dict(["Jane","Adam","Dave"],["Chicago", "Warsaw", "Boston"]) == {
    "Dave": "Boston",
    "Jane": "Chicago",
    "Adam": "Warsaw"
    }

def test_sort_dict_same_adress():
    assert f.sort_dict(["Jane","Adam","Dave"],["Warsaw", "Warsaw", "Boston"]) == {
    "Dave": "Boston",
    "Jane": "Warsaw",
    "Adam": "Warsaw"
    }

def test_sort_dict_length():
    with pytest.raises(ValueError):
        f.sort_dict(["Jane","Adam","Dave"],["Chicago", "Warsaw"])
        
def test_sort_dict_length():
    with pytest.raises(ValueError):
        f.sort_dict(["Jane","Dave","Dave"],["Chicago", "Warsaw", "Zagreb"])