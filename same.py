def calc_frequency(l):
    freqs = {}
    for num in l:
        freqs[num] = freqs.get(num, 0) + 1
    return freqs


def comp(a, b):
    if a is None or b is None:
        # early exit on null arrays
        return False
    b_freqs = calc_frequency(b)
    for num in a:
        square = num ** 2
        if square not in b_freqs:
            # early exit if the square of some value in a simply isn't in b
            return False
        b_freqs[square] -= 1
    for freq in b_freqs.values():
        if freq != 0:
            # could be < 0 if a has more occurrences, or > 0 if b has more occurrences
            return False
    return True


if __name__ == "__main__":
    print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]))
    print(comp([121, 144, 19, 161, 19, 144, 19, 11], [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]))
    print(comp([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361]))
    print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 36100, 25921, 361, 20736, 361]))
    print(comp([], []))
    print(comp([1, 2, 3], None))