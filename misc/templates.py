from tabnanny import check


MAIN_MENU = "\n".join(
    ["1. Проверка прайсов", "2. Настройки", "3. Выход", "\n", "Выберите пункт: "]
)

CHECK_MENU = "\n".join(
    [
        "1. Проверить все прайсы",
        "2. Проверка Hotline",
        "3. Проверка PN",
        "4. Проверка Nadavi",
        "0. Назад",
        "\n",
        "Выберите пункт: ",
    ]
)

SETTINGS_MENU = "\n".join(
    [
        "1. Проверить путь к прайсу в настройках",
        "2. Изменить путь к прайсу в настройках",
        "3. ",
        "0. Назад",
        "\n",
        "Выберите пункт: ",
    ]
)

PATH_EDIT_MENU = "\n".join(
    [
        "1. Изменить путь Hotline",
        "2. Изменить PN",
        "3. Изменить Nadavi",
        "0. Назад",
        "\n",
        "Выберите пункт: ",
    ]
)

WRONG_INPUT = "\n".join(
    ["-------------------------", "Неверный ввод", "-------------------------"]
)

WRONG_FILE = "\n".join(
    [
        "-------------------------",
        "Отсутствует файл для проверки",
        "-------------------------",
    ]
)

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.50",
}

SYMBOLS = {True: "\u2611", False: "\u2612"}
