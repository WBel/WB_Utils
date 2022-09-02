from maya import cmds

import logging


logging.basicConfig()
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)


def BuildUI():
    winName = 'mirrorControls'
    winWidth = 400
    winHeight = 130
    dev = 'William Bélanger'
    mail = 'william@unstandardstudio.com'
    version = 'V.01'

    if cmds.window(winName, exists=True):
            cmds.deleteUI(winName)
    window = cmds.window(winName, w = winWidth, h = winHeight, title = 'Mirror controls', menuBar = True, rtf=True, s=False)
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
    cmds.textField('oldName', w = tmpRowWidth[1])

    cmds.setParent('..')

#_________

    tmpRowWidth = [winWidth*0.20, winWidth*0.80]
    cmds.rowLayout(nc = 2, cw2 = tmpRowWidth)

    cmds.text(l = 'Replace with :', align = 'center', w = tmpRowWidth[0], h = 30)
    cmds.textField('newName', w = tmpRowWidth[1])

    cmds.setParent('..')

    tmpRowWidth = [winWidth]
    cmds.rowLayout(nc = 1, cw1 = tmpRowWidth[0])

    cmds.button('mirrorControls', l = 'Mirror controls', w = tmpRowWidth[0], h = 30, c='controls.do_mirrorControls()')

    cmds.setParent('..')

    cmds.separator(h = 10, w = winWidth)


    cmds.showWindow()





def do_mirrorControls():

    mAxis = cmds.radioButtonGrp('mAxis', q=True, sl = True)
    if mAxis == 1:
        mAxis = 'Z'
    if mAxis == 2:
        mAxis = 'X'
    if mAxis == 3:
        mAxis = 'Y'
    oldName = cmds.textField('oldName', q=True, tx = True)
    newName = cmds.textField('newName', q=True, tx = True)

    sel = cmds.ls(sl=True, fl=True)

    if sel:
        for i in sel:
            dup = cmds.duplicate(sel, rc=False, name = i.replace(oldName, newName))
            cmds.select(clear=True)
            invGrp = cmds.group(em = True, w=True)
            cmds.parent(i, invGrp)
            cmds.setAttr('{}.scale{}'.format(invGrp, mAxis), -1)
            cmds.parent(i, w=True)
            cmds.delete(invGrp)

    else:
        LOG.error('Nothing selected.')
