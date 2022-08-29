from maya import cmds
import os

from importlib import reload


colorUI = []


from WB_Utils.shelves import shelf_baseUI
reload(shelf_baseUI)


class load(shelf_baseUI._ui):


    def build(self):


        cmds.rowLayout(nc = 1, cw1 = 200)

        self.addButton('test', label = 'testReussis', align = 'center', height = 30, command='')



def do_colorUI():

    newColor = cmds.colorSliderGrp('newColor', q=True, rgbValue = True)

    with open(os.path.join(os.path.dirname(__file__), "colors.dat"), 'w') as f:

        for i in newColor:
            f.write(str(i) + '\n')
        f.close()
    colorUI = []
    with open(os.path.join(os.path.dirname(__file__), "colors.dat"), 'r') as f:
        for i in f:

            x = float(i)


            colorUI.append(x)

        f.close()

        cmds.button('test', e = True, bgc=colorUI)
