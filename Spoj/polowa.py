def spoj_polowa_Gosi():
    n = int(input())
    for i in range(n):
        word = input()
        half = word[0:int(len(word) / 2)]
        print(half)


def spoj_polowa_Rafala():
    print(*[word[:len(word) // 2] for word in [input() for i in range(int(input()))]], sep='\n')


def remove_spaces_manually(x):
    new_string = ""
    for c in x:
        if c != " ":
            new_string += c
    return new_string


def remove_spaces(x):
    without_spaces = x.replace(" ", "")
    return without_spaces


def remove_4_consequent_spaces(x):
    return x.replace(" " * 4, "")


def remove_consequent_letters(string, letter, n=2):
    """
    :param string: string to remove from
    :param letter: letter to remove from string, if not provided every consequetive letters are removed
    :param n: how many consequetive letters
    :return:
    """
    assert n > 0, f"N must be greater than zero {n} provided"
    result = ""
    tmp_result = ""
    for c in string:
        if len(tmp_result) == n:
            tmp_result = ""
        if c == letter:
            tmp_result += letter
        else:
            result += tmp_result
            tmp_result = ""
            result += c
    return result


def test_remove_consequent_letters():
    assert remove_consequent_letters("aabaaabbaaaa", 'a') == "babb"


def compare_solutions_length():
    gosia = """n = int(input())
    for i in range(n):
        word = input()
        half = word[0:int(len(word) / 2)]
        print(half)"""
    rafal = r"print(*[word[:len(word) // 2] for word in [input() for i in range(int(input()))]], sep='\n')"
    print("Dlugosc podstawowa")
    print("Rafal:", len(rafal), ", Gosia:", len(gosia))
    print("Bez zadnych spacji:")
    print("Rafal:", len(remove_spaces(rafal)), ", Gosia:", len(remove_spaces(gosia)))
    print("Bez tabow:")
    print("Rafal:", len(remove_4_consequent_spaces(rafal)), ", Gosia:", len(remove_4_consequent_spaces(gosia)))
