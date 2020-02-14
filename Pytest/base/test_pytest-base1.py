import pytest
def funa(X,Y):
    return X+Y


def test_funb():
    assert funa(1,3) == 3

if __name__ == '__main__':
    pytest.main()

