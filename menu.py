import os
import sys
from time import sleep

from pyfiglet import Figlet

from misc.functions import *
from misc.templates import *


class Menu:
    def __init__(self) -> None:
        self.__label = Figlet(font='slant').renderText('PRICE CHECKER')
        self.main_menu = {
            1: self._checkMenu,
            2: self._settingsMenu,
            3: self.__exit
        }
        self.check_menu = {
            0: self._mainMenu,
            1: checkHotline,
            2: checkPn,
            3: checkNadavi
        }
        self.settings_menu = {
            0: self._mainMenu,
            1: self._checkFilePath,
            2: self._editPathMenu
        }
        self.edit_path_menu = {
            0: self._settingsMenu
        }
        self.data = loadDataFromFile()
        self._mainMenu()   

    def __clear(self) -> None:
        os.system('cls')
        print(self.__label)
    
    def __exit(self) -> None:
        self.__clear()
        print('Закрываемся...')
        sleep(1)
        sys.exit()

    def _mainMenu(self, **kwargs) -> None:
        self.__clear()
        try:
            user_input = int(input(MAIN_MENU))
        except TypeError and ValueError:
            self.__clear()
            print(WRONG_INPUT)
            sleep(1)
            self._mainMenu()
        try:
            self.main_menu[user_input]()
        except KeyError:
            self.__clear()
            print(WRONG_INPUT)
            sleep(1)
            self._mainMenu()
    
    def _checkMenu(self) -> None:
        self.__clear()
        try:
            user_input = int(input(CHECK_MENU))
        except TypeError and ValueError:
            self.__clear()
            print(WRONG_INPUT)
            sleep(1)
            self._checkMenu()
        try:
            if user_input:
                self.__clear()
                if self.check_menu[user_input](self.data):
                    self._checkMenu()
            else:
                self._mainMenu()
        except KeyError:
            self.__clear()
            print(WRONG_INPUT)
            sleep(1)
            self._checkMenu()

    def _settingsMenu(self) -> None:
        self.__clear()
        try:
            user_input = int(input(SETTINGS_MENU))
        except TypeError and ValueError:
            self.__clear()
            print(WRONG_INPUT)
            sleep(1)
            self._settingsMenu()
        try:
            if user_input:
                self.settings_menu[user_input]()
            else:
                self._mainMenu()
        except KeyError:
            self.__clear()
            print(WRONG_INPUT)
            sleep(1)
            self._mainMenu()

    def _editPathMenu(self) -> None:
        self.__clear()
        try:
            user_input = int(input(PATH_EDIT_MENU))
        except TypeError and ValueError:
            self.__clear()
            print(WRONG_INPUT)
            sleep(1)
            self._editPathMenu()
        if user_input == 1:
            self.data.update(
                {
                    'HOTLINE':askFilePath('HOTLINE')
                }
            )
        elif user_input == 2:
            self.data.update(
                {
                    'PN': askFilePath('PN')
                }
            )
        elif user_input == 3:
            self.data.update(
                {
                    'NADAVI': askFilePath('NADAVI')
                }
            )
        elif not user_input:
            self._settingsMenu()
        dumpDataToSettings(self.data)
        self._settingsMenu()

    def _checkFilePath(self) -> None:
        self.__clear()
        for path in self.data.keys():
            try:
                with open(self.data[path], 'r') as file:
                    file.close()
                    print(
                        path, SYMBOLS[True], sep=' -- '
                    )
            except FileNotFoundError:
                print(path, SYMBOLS[False], sep=' -- ')
            sleep(0.5)
        user_confirm = input('Нажмите Enter что-бы продолжить...')
        self._settingsMenu()


if __name__ == '__main__':
    if os.path.exists('logs'):
        pass
    else:
        os.mkdir('logs')
    if os.path.exists('Отчеты'):
        pass
    else:
        os.mkdir('Отчеты')
    try:
        app = Menu()
    except Exception as error:
        logError(error=error)
        print('Произошла ошибка')
        sleep(0.5)
        app = Menu()


