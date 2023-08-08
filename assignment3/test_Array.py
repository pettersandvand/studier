from array2 import Array

shape = (2,)
a = Array(shape, 1, 2)
b = Array(shape, 3, 4)
c = Array(shape, 3, 4)
d = Array(shape, 1, 2)


def test_String():
    assert (str(a)) == "[1, 2]"


def test_Add():
    assert (a + b) == Array(shape, 4, 6)
    assert (a + 4) == Array(shape, 5, 6)


def test_Sub():
    assert (b - a) == Array(shape, 2, 2)
    assert (a - 1) == Array(shape, 0, 1)


def test_Mul():
    assert (a * b) == Array(shape, 3, 8)
    assert (a * 4) == Array(shape, 4, 8)


def test_eq():
    assert (a == b) == False
    assert (a == b) == False


def test_is_equal():
    assert (a.is_equal(5)) == Array(shape, False, False)
    assert (a.is_equal(1)) == Array(shape, True, False)
    assert (a.is_equal(1.0)) == Array(shape, True, False)
    assert (a.is_equal(b)) == Array(shape, False, False)
    assert (a.is_equal(d)) == Array(shape, True, True)


def test_min_element():
    assert b.min_element() == 3
    assert a.min_element() == 1


# 2d array tests
s_2d = (2, 2)
s2_2d = (1, 1)
a2 = Array(s_2d, 1, 2, 3, 4)
b2 = Array(s_2d, 5, 6, 7, 8)
c2 = Array(s_2d, 1, 2, 3, 4)
d2 = Array(s2_2d, 1, 3)


def test_2d_array():
    assert a2.array[1][0] == 3


def test_String_2d():
    assert (str(a2)) == "[[1, 2], [3, 4]]"


def test_Add_2d():
    assert (a2 + b2) == Array(s_2d, 6, 8, 10, 12)
    assert (a2 + 4) == Array(s_2d, 5, 6, 7, 8)
def test_Sub_2d():
    assert (b2 - a2) == Array(s_2d, 4, 4, 4, 4)
    assert (b2 - 4) == Array(s_2d, 1, 2, 3, 4)
def test_Mul_2d():
    assert (a2 * b2) == Array(s_2d, 5, 12, 21, 32)
    assert (a2 * 4) == Array(s_2d, 4, 8, 12, 16)

def test_eq_2d():
    assert (a2 == b2) == False
    assert (a2 == c2) == True
    assert (a2 == d2) == False

def test_min_element_2d():
    assert b2.min_element() == 5
    assert a2.min_element() == 1


def test_is_equal_2d():
    assert (a2.is_equal(5)) == Array(s_2d, False, False, False, False)
    assert (a2.is_equal(1)) == Array(s_2d, True, False, False, False)
    assert (a2.is_equal(1.0)) == Array(s_2d, True, False, False, False)
    assert (a2.is_equal(b2)) == Array(s_2d, False, False, False, False)
    assert (a2.is_equal(c2)) == Array(s_2d, True, True, True, True)


