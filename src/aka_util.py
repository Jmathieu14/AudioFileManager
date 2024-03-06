from src.models.aka import Aka


def handle_akas_list(akas: list) -> list[Aka]:
    if (akas is not None and akas.__len__() == 0) or (akas.__len__() > 0 and all(isinstance(i, Aka) for i in akas)):
        return akas
    elif all(isinstance(i, str) for i in akas):
        return string_list_to_akas(akas)
    else:
        return dict_list_to_akas(akas)


def string_list_to_akas(my_list: list[str]) -> list[Aka]:
    aka_list = []
    if my_list is not None and my_list.__len__() > 0 and all(isinstance(i, str) for i in my_list):
        for item in my_list:
            aka_list.append(Aka(item))
    else:
        raise ValueError
    return aka_list


def dict_list_to_akas(my_list: list[dict]) -> list[Aka]:
    aka_list = []
    if my_list is not None and my_list.__len__() > 0 and all(isinstance(i, dict) for i in my_list):
        for item in my_list:
            aka_list.append(Aka(item['name']))
    else:
        raise ValueError
    return aka_list


def akas_to_dict(akas: list[Aka]) -> dict[list, str]:
    akas_dict = []
    for aka in akas:
        akas_dict.append(aka.to_dict())
    return akas_dict


def akas_to_str(akas: list[Aka]) -> str:
    akas_str = "["
    for aka in akas:
        akas_str += "'{}', ".format(aka.name)
    akas_str = akas_str.removesuffix(", ")
    return akas_str + "]"


def sortAkasByName(element):
    return element.name


def akas_are_equal(akasOne: list[Aka], akasTwo: list[Aka]) -> bool:
    if akasOne.__len__() != akasTwo.__len__():
        return False
    akasOne.sort(key=sortAkasByName)
    akasTwo.sort(key=sortAkasByName)
    for i in range(0, akasOne.__len__()):
        if not akasOne[i].__eq__(akasTwo[i]):
            return False
    return True
