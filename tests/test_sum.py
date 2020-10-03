from pytest import raises

from testando_gh_actions.important_stuff import sum


def test_sum_1_and_1():
    assert sum(1,1) == 2

def test_sum_2_and_2_correct():
    assert sum(2,2) == 4

def test_sum_9_and_9():
    with raises(NotImplementedError):
        sum(9,9)

def test_sum_8_and_8():
    assert sum(4,4) == 8
