from maya import cmds

import logging


logging.basicConfig()
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)




def BuildUI():
    winName = 'Rename'
    winWidth = 400


    if cmds.window(winName, exists=True):
            cmds.deleteUI(winName)
    window = cmds.window(winName, w = winWidth, title = 'Renaming tool', menuBar = True)
    cmds.columnLayout()

#RENAME__________________________________________________________________________________

    cmds.frameLayout(l = 'Rename', w = winWidth, cll = True)

    tmpRowWidth = [winWidth*0.15, winWidth*0.84]
    cmds.rowLayout(nc = 2, cw2 = tmpRowWidth)

    cmds.text(l = 'Rename :', w = tmpRowWidth[0], align = 'center', h = 30)
    cmds.textField('rename', w = tmpRowWidth[1])

    cmds.setParent('..')

#__________

    tmpRowWidth = [winWidth*0.20, winWidth*0.30, winWidth*0.15, winWidth*0.33]
    cmds.rowLayout(nc = 4, cw4 = tmpRowWidth)

    cmds.text(l = 'Start number  :', align = 'center', w = tmpRowWidth[0], h = 20)
    cmds.textField('startNum', w = tmpRowWidth[1], tx = '1')
    cmds.text(l = 'Padding  :', align = 'center', w = tmpRowWidth[2], h = 20)
    cmds.textField('padding', w = tmpRowWidth[3], tx = '1')
    cmds.setParent('..')

#___________

    tmpRowWidth = winWidth
    cmds.rowLayout(nc = 1, cw1 = tmpRowWidth)

    cmds.button('rename', l = 'Rename', w = winWidth, align='center', h = 30, c='from WB_Utils.utils import rename;'
                                                                        'rename.do_rename()')

    cmds.setParent('..')

    cmds.showWindow()

def do_rename():

    newName = cmds.textField('rename', q=True, tx = True)
    startNum = int(cmds.textField('startNum', q=True, tx = True))
    padding = int(cmds.textField('padding', q=True, tx = True))


    print(newName)

    sel = cmds.ls(sl=True)


    if sel:

        for i in sel:
            cmds.rename(i, newName + '_' + str(startNum).rjust(padding,'0'))
            startNum = startNum + 1


    else:

        LOG.error('Nothing in selection.')

BuildUI()
