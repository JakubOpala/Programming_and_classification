import pytest
import functions as f


    
def cosine_test_2d():
    assert f.cosine([0,1],[1,0]) == 0

def cosine_test_3d():
    assert f.cosine([1,2,3],[-4,-5,-6]) == pytest.approx(-0.9746318461970762)

def cosine_test_diff_dim():
    with pytest.raises(ValueError):
        f.cosine([1,2,3],[4,5]) 


def divisible_in_range_test_normal():
    assert f.divisible_in_range(2,10,2) == [4,6,8]

def divisible_in_range_test_type_error():
    with pytest.raises(TypeError):
        f.divisible_in_range(1.2,3.4,5.1)

def divisible_in_range_test_set_error():
    with pytest.raises(ValueError):
        f.divisible_in_range(7,6,2)



def common_elements_test_normal():
    assert f.common_elements(["a",1,2.5,5,5,5,3,"a",3,6],[5,3,"a"]) == ["a",5,3]

def common_elements_test_empty_set():
    assert f.common_elements([5,3,"a"],0) == []

def common_elements_test_non_array():
    with pytest.raises(TypeError):
        f.common_elements(3,[5,3,"a"])

    
def exclude_test_let_not_in_string():
    assert f.exclude("kamehame","s")

def exclude_test_normal():
    assert f.exclude("jxaxnxpxaxwxexlxdxrxuxgxi","x")


def exclude_test_normal():
    assert f.letters_and_digits("jp2") == [2,1]


def subsets_test_same_chars():
    assert f.subsets(["a","a",1]) == [["a","a"],["a",1]]


def subsets_test_normal():
    assert f.mode("kamehame123") == ["a","m","e"]

def subsets_test_empty():
    assert f.mode("") == []



def dec_to_bin_test_normal():
    assert f.dec_to_bin(31) == "01b11111"

def dec_to_bin_test_not_number():
    with pytest.raises(TypeError):
        f.dec_to_bin("nie-liczba")
        

def non_negative_test_normal():
    assert f.non_negative([1,2,-2.5,4.3,-2]) == [1,2,4.3]

def non_negative_test_not_numbers():
    with pytest.raises(TypeError):
        f.non_negative(["a",1])


def no_longer_than_test_normal():
        assert f.no_longer_than(["zibidibi", "2morrow", "hey", "s", "nice", "kamehameha"],3) == ["hey","s"]

def no_longer_than_test_wrong_input():
    with pytest.raises(TypeError):
        f.no_longer_than(["zibidibi", "2morrow", "hey", "s", "nice", "kamehameha"],"ab")

def no_longer_than_test_wrong_input():
    with pytest.raises(ValueError):
        f.no_longer_than(["zibidibi", "2morrow", "hey", "s", "nice", "kamehameha"],-2)        
        


def max_string_test_normal():
    assert f.max_string(["zibidibi", "2morrow", "hey", "s", "nice", "kamehameha"]) == ["kamehameha"]

def max_string_test_wrong_input():
    with pytest.raises(TypeError):
        f.max_string([1,2,5])



def alternate_test_normal():
    assert f.alternate(["a1","a2","a3"], ["b1","b2","b3"]) == ["a1","b1","a2","b2","a3","b3"]

def alternate_test_different_length():
    with pytest.raises(ValueError):
        f.alternate(["a1","a2"],["b1","b2","b3"])

def separate_and_sort_test_normal():
    assert f.separate_and_sort(["fas",5,2,"fbs","a",1,9,3]) == ["a","f","s",1,2,3,5,9]






    
    
