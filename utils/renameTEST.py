from maya import cmds

from importlib import reload





from WB_Utils.shelves import shelf_baseUI
reload(shelf_baseUI)


class load(shelf_baseUI._ui):


    def build(self):


        cmds.rowLayout(nc = 1, cw1 = 200)

        self.addButton('test', label = 'testReussis', align = 'center', bgc=(1,1,1), height = 30, command='')
