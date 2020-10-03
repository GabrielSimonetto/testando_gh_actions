from pytest import raises

from testando_gh_actions.important_stuff import sum


def test_sum_1_and_1():
    assert sum(1,1) == 2

def test_sum_2_and_2():
    assert sum(2,2) == 4

def test_sum_3_and_3():
    assert sum(3,3) == 6

def test_sum_9_and_9():
    with raises(NotImplementedError):
        sum(9,9)
