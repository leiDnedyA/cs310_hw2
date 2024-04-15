
def _get_digit(n, i):
    return (n//(10**i)) % 10

def sort_chars(chars: list[str]) -> list[str]:
    # since there are 26 possible letters, only 2 digits to loop through
    for i in [0, 1]:
        def key(c):
            n = _get_digit(ord(c) - ord('a'), i)
            return _get_digit(n, i)
        chars.sort(key=key)

if __name__ == "__main__":
    strings = ['d', 'a', 'c', 'b', 'f', 'e']
    sort_chars(strings)
    print(strings)
