from datetime import datetime
import json
from time import sleep
from pandas import read_excel
from misc.templates import HEADERS
import requests
from progress.bar import ShadyBar
import csv
from win32ui import CreateFileDialog


def logError(error: str) -> None:
    timestamp = str(datetime.now())
    with open(f'log\{timestamp}.txt', 'w') as file:
        file.write(error)
        file.close()

def askFilePath(name: str) -> str:
    o = CreateFileDialog(1, '.xlsx', '', 0, '')
    o.DoModal()
    return str(o.GetPathName()).replace("\\", "\\\\")


def loadDataFromFile() -> dict:
    try:
        with open("settings.json", "r") as settings_file:
            data = json.load(settings_file)
            settings_file.close()
            return data
    except FileNotFoundError or json.JSONDecodeError:
        dumpDataToSettings()

def dumpDataToSettings(data: dict) -> None:
    with open("settings.json", "w") as settings_file:
            data = {
                "PN": data['PN'],
                "HOTLINE": data['HOTLINE'],
                "NADAVI": data['NADAVI'],
            }
            json.dump(data, settings_file)
            settings_file.close()

def checkHotline(path: dict) -> bool:
    try:
        data = read_excel(path['HOTLINE']).__array__(dtype=list)
        data = [list(item) for item in data if item[8] != "нет"]
        fail_data = list()
        bar = ShadyBar("Проверяем Hotline: ", max=len(data))
        for item in data:
            name = item[2]
            link = item[9]
            if not linkCheck(link=link):
                fail_data.append(
                    {'Имя': name, 'Ссылка': link}
                )
            bar.next()
        bar.finish()
        writeReport(name='hotline', data=fail_data)
        print('Готово')
        sleep(0.5)
        return True
    except FileNotFoundError:
        return False

def checkPn(path: str) -> bool:
    try:
        data = read_excel(path['PN']).__array__(dtype=list)
        data = [list(item) for item in data if item[6] == "+"]
        bar = ShadyBar("Проверяем PN: ", max=len(data))
        fail_data = list()
        for item in data:
            name = item[0]
            link = item[7]
            if not linkCheck(link):
                fail_data.append({"Имя": name, "Ссылка": link})
            bar.next()
        bar.finish()
        writeReport(name="pn", data=fail_data)
        print('Готово')
        sleep(0.5)
        return True
    except FileNotFoundError:
        return False


def checkNadavi(path: str) -> bool:
    try:    
        with open(path['NADAVI'], "r") as file:
            data = file.readlines()[1:]
            file.close()
        data = [item.split(";") for item in data]
        bar = ShadyBar("Проверяем Nadavi: ", max=len(data))
        fail_data = list()
        for item in data:
            name = item[2]
            link = item[9]
            if not linkCheck(link=link):
                fail_data.append({"Имя": name, "Ссылка": link})
            bar.next()
        bar.finish()
        writeReport(name="nadavi", data=fail_data)
        print('Готово')
        sleep(0.5)
        return True
    except FileNotFoundError:
        return False

def linkCheck(link: str) -> bool:
    try:
        if requests.get(link, headers=HEADERS).status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False

def writeReport(name: str, data: list) -> bool:
    with open(f"Отчеты\\{name}_report.csv", "w", encoding="UTF-8") as report:
        writer = csv.DictWriter(report, fieldnames=["Имя", "Ссылка"])
        writer.writeheader()
        for item in data:
            writer.writerow(item)
        report.close()
        