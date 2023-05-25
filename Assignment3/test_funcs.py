import pytest
import funcs as f

# sim_bitstrings tests ---------------------------------------------------------------

def test_sim_bitsrings_normal():
    assert f.sim_bitstrings('111', 2) == {'100', '001', '010'}

def test_sim_bitsrings_same():
    assert f.sim_bitstrings('111', 0) == {'111'}

def test_sim_bitsrings_notbitstring():
    with pytest.raises(AttributeError):
        f.sim_bitstrings('53', 2) 

def test_sim_bitsrings_notintdistance():
    with pytest.raises(TypeError):
        f.sim_bitstrings('1001', 2.5)

def test_sim_bitsrings_wrongdist():
    with pytest.raises(ValueError):
        f.sim_bitstrings('1001', -2)        

# set_jaccard tests --------------------------------------------------------------------

def test_set_jaccard():
    assert f.set_jaccard(set1 = {1,2,3,4,5}, set2 = {2,3,4,5,6,7}) == 4/7

def test_set_jaccard_zerolength():
    with pytest.raises(AttributeError):
        f.set_jaccard({}, {1,2,3})

def test_set_jaccard_zero():
    assert f.set_jaccard(set(), {1,2,3}) == 0


# bag_jaccard tests --------------------------------------------------------------------

def test_bag_jaccard():
    assert f.bag_jaccard(x = "Uno dos tres", y = "tres dos los") == 1/2

def test_bag_jaccard_zerolength():
    assert f.bag_jaccard("", "bag of words") == 0

# shingles tests --------------------------------------------------------------------

def test_shingles():
    assert f.shingles("rabarbar", 2) == {"ra", "ab", "ba", "rb", "ar"}

def test_shingles_kbig():
    with pytest.raises(ValueError):
        f.shingles("karamba", 10)

def test_shingles_kminus():
    with pytest.raises(ValueError):
        f.shingles("karamba", -2)

# diameter tests ---------------------------------------------------------------------

def test_diameter():
    assert f.diameter({'1011', '1001', '0011', '0000', '1111'}, f.hamming) == 4

def test_diameter_wronginput():
    with pytest.raises(ValueError):
        f.diameter({'1011', '1001', '001110', '00000', '1111'}, f.hamming)



