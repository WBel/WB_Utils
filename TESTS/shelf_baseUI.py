"""
Credit to vshotarov
https://bindpose.com/scripting-custom-shelf-in-maya-python/
"""

from maya import cmds
import os


def _null(*args):
    pass

class _ui():



    def __init__(self, name="customName", title='', winWidthHeight=(0,0), s=True):

        self.name = name
        self.width = winWidthHeight[0]
        self.color = colorUI = []
        with open(os.path.join(os.path.dirname(__file__), "colors.dat"), 'r') as f:
            for i in f:

                x = float(i)


                colorUI.append(x)

            f.close()


        self._deleteUI()

        self.window = cmds.window(self.name, title = title, wh = winWidthHeight, s = s)
        cmds.formLayout(nd=100)

        cmds.showWindow(self.window)
        self.build()


    def _deleteUI(self):
        if cmds.window(self.name, exists=True):
            cmds.deleteUI(self.name)


    def build(self):
        """This method should be overwritten in derived classes to actually build the shelf
        elements. Otherwise, nothing is added to the shelf."""
        pass


    def addButton(self, name, label, align, height, command, buttonName):
        buttonName = cmds.button(name, l = label, align = align, bgc = self.color, w = self.width, h = height, command = command)
