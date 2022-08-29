from maya import cmds

import logging
import os

logging.basicConfig()
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)

colorUI = []
with open(os.path.join(os.path.dirname(__file__), "colors.dat"), 'r') as f:
    for i in f:

        x = float(i)


        colorUI.append(x)

    f.close()

def buildColorUI():

    winName = 'colorUI'
    winWidth = 400
    winHeight = 60
    dev = 'William Bélanger'
    mail = 'william@unstandardstudio.com'
    version = 'V.01'


    if cmds.window(winName, exists=True):
            cmds.deleteUI(winName)
    window = cmds.window(winName, w = winWidth, h = winHeight, title = 'UI Color', menuBar = True, rtf=True, s=False)
    cmds.columnLayout()
#Infos________

    cmds.menu(l = 'Info')

    cmds.menuItem(l = 'Developer', d = True, ld = True)
    cmds.menuItem(l = dev)
    cmds.menuItem(l = 'Join', d = True, ld = True)
    cmds.menuItem(l = mail)
    cmds.menuItem(l = 'Version', d = True, ld = True)
    cmds.menuItem(l = version)

#________________________

    tmpRowWidth = [winWidth*0.3, winWidth*0.7]
    cmds.rowLayout(nc = 2, cw2 = tmpRowWidth)

    cmds.text(l = 'Color Selection', w = tmpRowWidth[0])
    cmds.colorSliderGrp('newColor', w = tmpRowWidth[1])

    cmds.setParent('..')

#________________________

    tmpRowWidth = winWidth
    cmds.rowLayout(nc = 1, cw1 = tmpRowWidth)

    cmds.button('colorChange', l = 'Change color', w = winWidth, h = 30, bgc=colorUI, c='generalTools.do_colorUI()')
    cmds.showWindow( window )

    cmds.setParent('..')

    cmds.setParent('..')



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
        cmds.button('colorChange', e = True, bgc=colorUI)
        from WB_Utils.utils import rename
        rename.do_colorUI()
        from WB_Utils.utils import joints
        joints.do_colorUI()
