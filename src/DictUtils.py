# Утилиты для словарей


def check_equals_dict_key_value(d1: dict[str, int], d2: dict[str, int]) -> bool:
    if len(d1) != len(d2):
        return False
    for k in d1.keys():
        if k not in d2:
            return False
        if d1[k] != d2[k]:
            return False
    return True
