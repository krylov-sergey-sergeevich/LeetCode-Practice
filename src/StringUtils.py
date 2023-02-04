# Утилиты для строк


def str_to_dict_count(s: str) -> dict[str, int]:
    """
    Подсчет символов в строке и возвращение соотношения <символ, число>.

    :param s: строка
    :return: словарь
    """
    d = dict()
    for el in s:
        if el not in d:
            d[el] = 1
        else:
            d[el] = d[el] + 1
    return d
