'''
Created on Apr 25, 2019

@author: truong.pham
'''

from pywinauto import Application, Desktop
import pywinauto
import time
if __name__ == '__main__':
    
    #app = Application(backend="uia").start('C:\\Program Files\\Centrify\\Centrify Agent for Windows\\NetworkManager.exe')
    #app = Application(backend="uia").start('notepad.exe')
    #time.sleep(5)
    #list = Desktop(backend="win32").windows()
    #print(str(list))
#     for win in list:
#         try:
#             print(win)
#         except :
#             print("")
#     #dlg = Desktop(backend="uia").window(title='Untitled - Notepad')
#     dlg = Desktop().window(title='Centrify Network Manager')
#     #dlg.type_keys('2*3=')
#     print(dlg.print_ctrl_ids())
   # app = Application(backend="uia").windows()
    #print(app)
    all = pywinauto.findwindows.find_elements(title='Centrify Network Manager')
    for win in all:
        for e in win.children():
            print (e.children())

    #mswpr = app.window(title="Centrify Network Manager")
    #mswpr.print_control_identifiers()
    #dlg.minimize()
    #Desktop(backend="uia").window(title='Calculator', visible_only=False).restore()