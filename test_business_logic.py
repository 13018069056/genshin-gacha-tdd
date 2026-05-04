from business_logic import calculate_gacha_probability

def test1():
    assert calculate_gacha_probability(1) == 0.006
def test2():
    assert calculate_gacha_probability(74) == 0.066
def test3():
    assert calculate_gacha_probability(90) == 1.0
