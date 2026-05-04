def calculate_gacha_probability(pull_num):
    if pull_num <= 0:
        raise ValueError()
    n = pull_num % 90
    if n == 0:
        n = 90
    if n <= 73:
        return 0.006
    elif n <= 89:
        return 0.006 + (n - 73) * 0.06
    else:
        return 1.0
