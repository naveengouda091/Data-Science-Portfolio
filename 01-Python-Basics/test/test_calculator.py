import pytest
from calculator import sqr

#def main():
    #test_sqr()
'''
def test_sqr():
    if sqr(2)!=4:
        print("4 was not square of 2")
    if sqr(3)!=9:
        print("3 squared was not 9")
'''

'''
def test_sqr():
    for i in range (10):
        if sqr(i)!=i*i:
            print(f"{i} squared was not {i**2}")

'''
'''
def test_sqr():
    try:
        assert sqr(2) == 4
    except AssertionError:
        print("2 squeried was not 4")
    try:
        assert sqr(3) == 9
    except AssertionError:
        print("3 squeried was not 9")
    try:
        assert sqr(-2) == 4
    except AssertionError:
        print("-2 squeried was not 4")
    try:
        assert sqr(-3) == 9
    except AssertionError:
        print("-3 squeried was not 9")
    try:
        assert sqr(0) == 0
    except AssertionError:
        print("0 squeried was not 0")

'''
'''
def test_sqr():
    for i in range(-5,5):
        try:
            assert sqr(i) == i**2
        except AssertionError:
            print(f"{i} squaried was not {i**2}")
'''



def test_sqr():
    assert sqr(2) == 4
    assert sqr(3) == 9
    assert sqr(-2) == 4
    assert sqr(-3) == 9

def test_str():
    with pytest.raises(TypeError):
        sqr("cat")


#if __name__=="__main__":
    #main()
