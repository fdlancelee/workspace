import pytest

def funa(X):
    return X+1


def test_funa():
    assert funa(2) == 4

#test_funa()

#执行该目录下所有
if __name__ == '__main__':
    #执行该目录下所有
    #pytest.main()
    #执行指定测试文件
    #pytest.main(["-s","test_pytest-base.py"])
    #执行指定目录下测试文件
    pytest.main(["-s", "D:/Python/workspace/Pytest/"])  # 指定测试目录
'''
funa(2)
print(funa(2))
'''