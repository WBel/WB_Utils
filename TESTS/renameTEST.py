from maya import cmds
import os

from importlib import reload


colorUI = []


from WB_Utils.shelves import shelf_baseUI
reload(shelf_baseUI)


class load(shelf_baseUI._ui):


    def build(self):

        
        self.addButton('test', label = 'testReussis', align = 'center', height = 30, command='', buttonName = 'test')
        cmds.formLayout(attachForm = [(buttonName, 'top', 100), (buttonName, 'left', 5)])
