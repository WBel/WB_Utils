from maya import cmds
import os

from importlib import reload


colorUI = []


from WB_Utils.shelves import ui_base
reload(ui_base)


class load(ui_base._ui):


    def build(self):


        self.addButton('test', label = 'testReussis', align = 'center', height = 30, command='', buttonName = 'test')
        cmds.formLayout(attachForm = [(buttonName, 'top', 100), (buttonName, 'left', 5)])
