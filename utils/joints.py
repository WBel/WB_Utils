from maya import cmds

import logging
import re
import pymel.core as pm
import os

logging.basicConfig()
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)





def BuildUI():
    winName = 'MirrorJoints'
    winWidth = 400
    winHeight = 130
    dev = 'William Bélanger'
    mail = 'william@unstandardstudio.com'
    version = 'V.01'
    colorUI = []
    with open(os.path.join(os.path.dirname(__file__), "colors.dat"), 'r') as f:
        for i in f:

            x = float(i)


            colorUI.append(x)

        f.close()


    if cmds.window(winName, exists=True):
            cmds.deleteUI(winName)
    window = cmds.window(winName, w = winWidth, h = winHeight, title = 'Mirror joints', menuBar = True, rtf=True, s=False)
    cmds.columnLayout()

#Infos________

    cmds.menu(l = 'Info')

    cmds.menuItem(l = 'Developer', d = True, ld = True)
    cmds.menuItem(l = dev)
    cmds.menuItem(l = 'Join', d = True, ld = True)
    cmds.menuItem(l = mail)
    cmds.menuItem(l = 'Version', d = True, ld = True)
    cmds.menuItem(l = version)

#MIRROR_JOINTS_________________________

    tmpRowWidth = [winWidth*0.25, winWidth*0.75]
    cmds.rowLayout(nc = 2, cw2 = tmpRowWidth)

    cmds.text(l = 'Mirror axis : ', w = tmpRowWidth[0])
    cmds.radioButtonGrp('mAxis', numberOfRadioButtons = 3, sl = 2, labelArray3=['XY', 'YZ', 'XZ'], w = tmpRowWidth[1])

    cmds.setParent('..')

    tmpRowWidth = [winWidth*0.17, winWidth*0.83]
    cmds.rowLayout(nc = 2, cw2 = tmpRowWidth)

    cmds.text(l = 'Search for :', align = 'center', w = tmpRowWidth[0], h = 20)
    cmds.textField('jointS', w = tmpRowWidth[1])

    cmds.setParent('..')

#_________

    tmpRowWidth = [winWidth*0.20, winWidth*0.80]
    cmds.rowLayout(nc = 2, cw2 = tmpRowWidth)

    cmds.text(l = 'Replace with :', align = 'center', w = tmpRowWidth[0], h = 30)
    cmds.textField('jointR', w = tmpRowWidth[1])

    cmds.setParent('..')

    tmpRowWidth = [winWidth]
    cmds.rowLayout(nc = 1, cw1 = tmpRowWidth[0])

    cmds.button('mirrorJoint', l = 'Mirror joints', w = tmpRowWidth[0], h = 30, bgc=colorUI, c='mirrorJ()')

    cmds.setParent('..')

    cmds.separator(h = 10, w = winWidth)


    cmds.showWindow()





def do_mirrorJoints():

    mAxis = cmds.radioButtonGrp('mAxis', q=True, sl = True)
    oldName = cmds.textField('oldName', q=True, tx = True)
    newName = cmds.textField('newName', q=True, tx = True)

    sel = cmds.ls(sl=True)

    if cmds.nodeType(sel) == 'joint':

        if mAxis == 1:
            cmds.mirrorJoint(mxy = True, sr = (oldName, newName), mb = True)
        if mAxis == 2:
            cmds.mirrorJoint(myz = True, sr = (oldName, newName), mb = True)
        if mAxis == 3:
            cmds.mirrorJoint(mxz = True, sr = (oldName, newName), mb = True)

    else:
        LOG.error('No joints selected.')

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
        cmds.button('mirrorJoint', e = True, bgc=colorUI)
