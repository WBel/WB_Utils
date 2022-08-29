"""
Credit to vshotarov
https://bindpose.com/scripting-custom-shelf-in-maya-python/
"""

from maya import cmds

def _null(*args):
    pass

class _ui():



    def __init__(self, name="customName", title='', winWidthHeight=(0,0), s=True):

        self.name = name
        self.width = winWidthHeight[0]

        self._deleteUI()

        self.window = cmds.window(self.name, title = title, wh = winWidthHeight, s = s)
        cmds.columnLayout(p=self.window)

        cmds.showWindow(self.window)
        self.build()


    def _deleteUI(self):
        if cmds.window(self.name, exists=True):
            cmds.deleteUI(self.name)


    def build(self):
        """This method should be overwritten in derived classes to actually build the shelf
        elements. Otherwise, nothing is added to the shelf."""
        pass

    def addButton(self, name, label, align, bgc, height, command):
        cmds.button(name, l = label, align = align, bgc = bgc, w = self.width, h = height, command = command)
        cmds.setParent('..')
