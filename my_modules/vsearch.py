def search4vowels(word: str) -> set:  # Аннотация это стандарт документирования
    """Выводит гласные, найденные во введенном слове."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search4letters(phrase: str, letter: str = 'aeiou') -> set:
    return set(letter).intersection(set(phrase))


if __name__ == '__main__':
    print(123)
    print('Hello World')
