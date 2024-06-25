import pytest


class TestCase:

    # 使用assert断言
    def test_01(self):
        print("断言1")
        assert 1 == 1
        print('断言2')
        assert 2 == 1
        print("断言3")
        assert 3 == 3
        print('用例结束')

    # 使用pytest.assume()断言
    def test_02(self):
        print('断言1')
        pytest.assume(1 == 1)
        print('断言2')
        pytest.assume(2 == 1)
        print('断言3')
        pytest.assume(3 == 3)
        print('用例结束')


if __name__ == '__main__':
    pytest.main(['-vs'])