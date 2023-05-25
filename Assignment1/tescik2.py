import pytest
import functions as f

class test_cosine():
    
    def test_2d(self):
        assert f.cosine([0,1],[1,0]) == 0

    def test_3d(self):
        assert f.cosine([1,2,3],[-4,-5,-6]) == pytest.approx(-0.9746318461970762)

    def test_diff_dim(self):
        with pytest.raises(ValueError):
            f.cosine([1,2,3],[4,5]) 



class test_divisible_in_range():

    def test_normal(self):
        assert f.divisible_in_range(2,10,2) == [4,6,8]

    def test_type_error(self):
        with pytest.raises(TypeError):
            f.divisible_in_range(1.2,3.4,5.1)

    def test_set_error(self):
        with pytest.raises(ValueError):
            f.divisible_in_range(7,6,2)

class test_common_elements():

    def test_normal(self):
        assert f.common_elements(["a",1,2.5,5,5,5,3,"a",3,6],[5,3,"a"]) == ["a",5,3]

    def test_empty_set(self):
        assert f.common_elements([5,3,"a"],0) == []

    def test_non_array(self):
        with pytest.raises(TypeError):
            f.common_elements(3,[5,3,"a"])

class test_exclude():
    
    def test_let_not_in_string(self):
        assert f.exclude("kamehame","s")

    def test_normal(self):
        assert f.exclude("jxaxnxpxaxwxexlxdxrxuxgxi","x")

class test_letters_and_digits():

    def test_normal(self):
        assert f.letters_and_digits("jp2") == [2,1]

    

class test_subsets():

    def test_same_chars(self):
        assert f.subsets(["a","a",1]) == [["a","a"],["a",1]]

class test_mode():

    def test_normal(self):
        assert f.mode("kamehame123") == ["a","m","e"]

    def test_empty(self):
        assert f.mode("") == []

class test_dec_to_bin():

    def test_normal(self):
        assert f.dec_to_bin(31) == "01b11111"

    def test_not_number(self):
        with pytest.raises(TypeError):
            f.dec_to_bin("nie-liczba")
        
class test_non_negative():

    def test_normal(self):
        assert f.non_negative([1,2,-2.5,4.3,-2]) == [1,2,4.3]

    def test_not_numbers(self):
        with pytest.raises(TypeError):
            f.non_negative(["a",1])

class test_no_longer_than():

    def test_normal(self):
        assert f.no_longer_than(["zibidibi", "2morrow", "hey", "s", "nice", "kamehameha"],3) == ["hey","s"]

    def test_wrong_input():
        with pytest.raises(TypeError):
            f.no_longer_than(["zibidibi", "2morrow", "hey", "s", "nice", "kamehameha"],"ab")

    def test_wrong_input():
        with pytest.raises(ValueError):
            f.no_longer_than(["zibidibi", "2morrow", "hey", "s", "nice", "kamehameha"],-2)        
        
class test_max_string():

    def test_normal(self):
        assert f.max_string(["zibidibi", "2morrow", "hey", "s", "nice", "kamehameha"]) == ["kamehameha"]

    def test_wrong_input(self):
        with pytest.raises(TypeError):
            f.max_string([1,2,5])

class test_alternate():

    def test_normal(self):
        assert f.alternate(["a1","a2","a3"], ["b1","b2","b3"]) == ["a1","b1","a2","b2","a3","b3"]

    def test_different_length(self):
        with pytest.raises(ValueError):
            f.alternate(["a1","a2"],["b1","b2","b3"])
    
class test_separate_and_sort():

    def test_normal(self):
        assert f.separate_and_sort(["fas",5,2,"fbs","a",1,9,3]) == ["a","f","s",1,2,3,5,9]

'''
test1 = test_cosine()
test2 = test_common_elements()
test3 = test_alternate()
test4 = test_dec_to_bin()
test5 = test_divisible_in_range()
test6 = test_exclude()
test7 = test_letters_and_digits()
test8 = test_max_string()
test9 = test_non_negative()
test10 = test_exclude()
test11 = test_no_longer_than()
'''






    
    
