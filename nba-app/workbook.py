import pandas as pd 
import xlwings as xw 
import types 
from os import path
from xlwings.utils import rbg_to_int
from xlwings import constants
# from helpers import pygetwindow as gw

def get_workbook_hwnd(hwnd, self):
    # if win32gui.IsWindowVisible(hwnd):
    #     if 'NBA_Workbook' in win32gui.GetWindowText(hwnd):
    #         self.hwnd = hwnd.
    pass

class ExcelApp(xw.main.App):
    def __init__(self, app, book=None):
        self.app = app

        if book != None:
            super().__init__(visible=True)
            self.workbook = xw.Book(book)
            self.books[0].close()
        else:
            super().__init__(visible=False)
            self.workbook = self.books[0]
            
        self.workbook_window = gw.Window(self.hwnd)

        self.path_workbook_functions(self.workbook)

    def lock_user_interaction(self):
        attempt = 0
        while True:
            if attempt > 10:
                return
            try:
                self.screen_updating = False
                self.impl._xl.Interactive = False
                return
            except:
                attempt += 1
                continue
        
    def unlock_user_interaction(self):
        self.screen_updating = True
        self.impl._xl.Interactive = True
    
    def path_workbook_functions(self, book):
        
        def navigate(book, sheet_name):
            if sheet_name == 'Home':
                return
            try:
                book.sheets[sheet_name].activate()
            except Exception as e:
                print("Excel sheet navigation failure:", sheet_name, str(e))
                pass

        book.navigate = types.MethodType(navigate, book)

        def calcs_on(self):
            self.app.calculation = "automatic"
        books.calcs_on = types.MethodType(calcs_on, book)

        def calcs_off(self):
            self.app.calculation = "manual"
        books.calcs_off = types.MethodType(calcs_off, book)

        def set_foreground(self):
            activate_sheet = book.sheets.active 
            try:
                activate_sheet.activate()
            except:
                print('failed to activate sheet during workbook.set_foreground()')
        book.set_foreground = types.MethodType(set_foreground, book)