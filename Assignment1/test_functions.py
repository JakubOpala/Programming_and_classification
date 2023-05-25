import pytest
import functions as f
import numpy as np

# cosine tests ---------------------------------------------------------
    
def test_cosine_2d():
    assert f.cosine([0,1],[1,0]) == 0

def test_cosine_3d():
    assert f.cosine([1,2,3],[-4,-5,-6]) == pytest.approx(-0.9746318461970762)

def test_cosine_diff_dim():
    with pytest.raises(ValueError):
        f.cosine([1,2,3],[4,5]) 

def test_cosine_type_error():
    with pytest.raises(ValueError):
        f.cosine(["a","b"],["c","d"])

def test_cosine_zero_error():
    with pytest.raises(ValueError):
        f.cosine([0,0],[1,0])

        

# divisible_in_range tests ---------------------------------------------------------

def test_divisible_in_range_normal():
    assert f.divisible_in_range(2,10,2) == [4, 6, 8]

def test_divisible_in_range_type_error():
    with pytest.raises(TypeError):
        f.divisible_in_range(1.2,3.4,2.1)

def test_divisible_in_range_set_error():
    with pytest.raises(ValueError):
        f.divisible_in_range(7,6,2)

def test_divisible_in_range_divisor_error():
    with pytest.raises(ValueError):
        f.divisible_in_range(3,6,7)

def test_divisible_in_range_zero_div():
    with pytest.raises(ZeroDivisionError):
        f.divisible_in_range(2,5,0)

# common_elements tests ---------------------------------------------------------

def test_common_elements_normal():
    assert np.array_equal(f.common_elements(np.array(["a",1,2.5,5,5,5,3,"a",3,6]),np.array([5,3,"a"])),["a",5,3])

def test_common_elements_empty_set():
    assert np.array_equal(f.common_elements([5,3,"a"],[]), [])

def test_common_elements_non_array():
    with pytest.raises(TypeError):
        f.common_elements(3,[5,3,"a"])

# exclude tests ---------------------------------------------------------
    
def test_exclude_let_not_in_string():
    assert f.exclude("s","kamehame") == "kamehame"

def test_exclude_normal():
    assert f.exclude("x","jxaxnxpxaxwxexlxdxrxuxgxi") == "janpaweldrugi"

def test_exclude_wrong_type():
        assert f.exclude(2,"str2ing22") == "string"

# letters and digits tests ---------------------------------------------------------

def test_letters_and_digits_normal():
    assert f.letters_and_digits("jp2") == [2,1]

def test_letters_and_digits_wrong_type():
    with pytest.raises(TypeError):
        f.letters_and_digits(228)

# subsets tests ---------------------------------------------------------

def test_subsets_same_chars():
    assert f.subsets(["a","a",1]) == [(), (1,), ('a',), (1, 'a')]

def test_subsets_not_list():
    with pytest.raises(TypeError):
        f.subsets(3)

# mode tests ---------------------------------------------------------

def test_mode_normal():
    assert f.mode("kamehame123") == ["a","m","e"]

def test_mode_empty():
    assert f.mode("") == []

def test_mode_type_error():
    with pytest.raises(TypeError):
        f.mode(22)


# dec_to_bin tests ---------------------------------------------------------

def test_dec_to_bin_normal():
    assert f.dec_to_bin(31) == "0b11111"

def test_dec_to_bin_not_number():
    with pytest.raises(TypeError):
        f.dec_to_bin("nie-liczba")

# non-negative tests --------------------------------------------------------- 

def test_non_negative_normal():
    assert f.non_negative([1,2,-2.5,4.3,-2]) == [1,2,4.3]

def test_non_negative_not_numbers():
    with pytest.raises(TypeError):
        f.non_negative(["a",1])

# no_longer_than tests ---------------------------------------------------------

def test_no_longer_than_normal():
        assert f.no_longer_than(3,["zibidibi", "2morrow", "hey", "s", "nice", "kamehameha"]) == ["hey","s"]

def test_no_longer_than_wrong_type_input():
    with pytest.raises(TypeError):
        f.no_longer_than("ab",["zibidibi", "2morrow", "hey", "s", "nice", "kamehameha"])

def test_no_longer_than_minus_input():
    with pytest.raises(ValueError):
        f.no_longer_than(-2,["zibidibi", "2morrow", "hey", "s", "nice", "kamehameha"])        
        
# max_string tests ---------------------------------------------------------

def test_max_string_normal():
    assert f.max_string(["zibidibi", "2morrow", "hey", "s", "nice", "kamehameha"]) == ["kamehameha"]

def test_max_string_wrong_input():
    with pytest.raises(TypeError):
        f.max_string([1,2,5])

# alternate tests ---------------------------------------------------------

def test_alternate_normal():
    assert f.alternate(["a1","a2","a3"], ["b1","b2","b3"]) == ["a1","b1","a2","b2","a3","b3"]

def test_alternate_different_length():
    with pytest.raises(ValueError):
        f.alternate(["a1","a2"],["b1","b2","b3"])

# separate_and_sort tests ---------------------------------------------------------

def test_separate_and_sort_normal():
    assert np.array_equal(f.separate_and_sort(np.array(["fas",5,2,"fbs","a",1,9,3])), np.array(["a","fas","fbs",1,2,3,5,9]))

def test_separate_and_sort_type_error():
    with pytest.raises(TypeError):
        f.separate_and_sort(123)






    
    
