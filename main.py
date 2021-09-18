import re

from nltk.probability import FreqDist
import matplotlib.pyplot as plt


RE_FILTER_FOR_HIST = r'[^а-я]'
RE_FILTER_FOR_TEXT = r'[^а-я.,;:!?"\' ]'


def text_hist_preprocess(text: str) -> str:
    """
    Предобрабатывает строку для построения гистограммы частотного анализа.

    :param text: Строка со знаками препинания, пробелами и т.д.
    :return: Чистая строка.
    """
    text = text.replace(" ", " ")
    text = text.replace("\n", " ")
    text = text.lower()
    text = text.replace("ё", "e")

    return re.sub(RE_FILTER_FOR_HIST, "", text)


def plot_freq_hist(text: str, hist_title: str, image_filename: str = None) -> None:
    """
    Строит гистограмму частотного анализа для данной строки.

    :param text: Строка для частотного анализа.
    :param hist_title: Имя для гистограммы.
    :param image_filename: Имя файла для картинки с гистограммой.
                           Если не определено - гистограмма просто отобразится без сохранения.
    :return: None.
    """
    freq_dict = dict(FreqDist(text))

    chars = list()
    counts = list()
    for char, count in sorted(freq_dict.items(), key=lambda item: item[1], reverse=True):
        chars.append(char)
        counts.append(count)
    index = [i for i in range(len(chars))]

    plt.figure(figsize=(12, 8))
    plt.bar(index, counts)
    plt.xticks(index, chars)
    plt.title(hist_title)

    if image_filename:
        plt.savefig(image_filename)
    else:
        plt.show()


def replace_chars(text: str, char_map: dict) -> str:
    """
    Дешифрует строку по словарю (меняет ключи на значения словаря).

    :param text: Строка до дешифровки.
    :param char_map: Словарь, использующийся при дешифровки.
    :return: Строка после дешифровки.
    """
    switched_indexes = list()
    for key, value in char_map.items():
        if value:
            new_text = str()
            for index, char in enumerate(text):
                if key == char and index not in switched_indexes:
                    new_text += value
                else:
                    new_text += char

            for index, pair_of_chars in enumerate(zip(text, new_text)):
                if pair_of_chars[0] != pair_of_chars[1]:
                    switched_indexes.append(index)

            text = new_text

    return text


if __name__ == '__main__':
    # # Пример построения гистограммы для Л.Н.Толстого "Война и мир".
    # with open("big_data.txt", 'r', encoding="utf-8") as file:
    #     text = text_hist_preprocess(file.read())
    #
    #     title = 'Частотный анализ романа Л.Н.Толстого "Война и мир"'
    #     plot_freq_hist(text, title, "big_data_freq.png")

    test_text = """1. Г ЙМЦУГКРЬ ЫДФЫБ ФЦ УГЙЬ ЗЫЮЫЙ ПТЮ — ЛЫМХ ЙОАМТЛ ОТФЫЙЬ. РЫЗДЦ О
СЫЮФГИ ЙЬЮГ ЫФЦ ЗЫЮЫЙЬЮЦ, РЦМЦЙМУЫЧЦ ПТЮЦ ФЦ УГЙЬ.
2. ПТЮ ЫДЬФ ЙМЦУЬЯЫР ЬЩ ЮЬОЫУФЫ, ЙЦЪТБ РУЫКЭЯФТБ О ЪЬУЭ, ПЭЙЙСЫУФЫ;
ФЫ РЦРЫБ-МЫ ВЭФЫР УЦЩ ЭЗЫ СЫДЙМЭУЭЗ Ь ЙЫНУЦЮ ЙМЦУЬЯРЦ ЬЩ
ЮЬОЫУФЫ."""

    test_text_hist = text_hist_preprocess(test_text)
    title = 'Вариант №1.'
    plot_freq_hist(test_text_hist, title, "variant_1.png")

    char_map = {'А': "Я",
                'Б': "Й",
                'В': "Щ",
                'Г': "У",
                'Д': None,
                'Е': None,
                'Ж': None,
                'З': "Г",
                'И': "Ю",
                'Й': "С",
                'К': "Ш",
                'Л': "Х",
                'М': "Т",
                'Н': "Ж",
                'О': "В",
                'П': "Б",
                'Р': "К",
                'С': "П",
                'Т': "Ы",
                'У': "Р",
                'Ф': "Н",
                'Х': "Ь",
                'Ц': "А",
                'Ч': "Ф",
                'Ш': None,
                'Щ': "З",
                'Ъ': "М",
                'Ы': "О",
                'Ь': "И",
                'Э': "Е",
                'Ю': "Л",
                'Я': "Ч"}

    new_text = replace_chars(test_text, char_map)
    print(test_text + "\n\n")
    print(new_text)



