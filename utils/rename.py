from maya import cmds

import logging
import re
import pymel.core as pm
import os


logging.basicConfig()
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)




def BuildUI():
    winName = 'Rename'
    winWidth = 400
    dev = 'William Bélanger'
    mail = 'william@unstandardstudio.com'
    version = 'V.1.0'
    easterEgg = 'Andrew Cyr-Marcoux'

    if cmds.window(winName, exists=True):
            cmds.deleteUI(winName)
    window = cmds.window(winName, w = winWidth, title = 'Renaming tool', menuBar = True, rtf=True)
    cmds.columnLayout()
#Infos________

    cmds.menu(l = 'Info')

    cmds.menuItem(l = 'Developer', d = True, ld = True)
    cmds.menuItem(l = dev)
    cmds.menuItem(l = 'Join', d = True, ld = True)
    cmds.menuItem(l = mail)
    cmds.menuItem(l = 'Version', d = True, ld = True)
    cmds.menuItem(l = version)


#RENAME__________________________________________________________________________________

    cmds.frameLayout(l = 'Rename', w = winWidth)

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

    cmds.button('rename', l = 'Rename', w = winWidth, align='center', h = 30, c='rename.do_rename()')

    cmds.setParent('..')

#REPLACE____________________

    tmpRowWidth = [winWidth*0.15, winWidth*0.84]
    cmds.rowLayout(nc = 2, cw2 = tmpRowWidth)

    cmds.text(l = 'Replace :', align = 'center', w = tmpRowWidth[0], h = 20)
    cmds.textField('oldNameR', w = tmpRowWidth[1])

    cmds.setParent('..')

#_________

    tmpRowWidth = [winWidth*0.15, winWidth*0.84]
    cmds.rowLayout(nc = 2, cw2 = tmpRowWidth)

    cmds.text(l = 'With :', align = 'center', w = tmpRowWidth[0], h = 30)
    cmds.textField('newNameR', w = tmpRowWidth[1])

    cmds.setParent('..')

#__________

    tmpRowWidth = winWidth
    cmds.rowLayout(nc = 1, cw1 = tmpRowWidth)

    cmds.button('replace', l = 'Replace', w = winWidth, h = 30, c='rename.do_replace()')

    cmds.setParent('..')

    cmds.setParent('..')

    cmds.separator(h = 20, w = winWidth)


#PREFIX_____________________________________________________________________________________

    cmds.frameLayout(l = 'Prefix and suffix', w = winWidth)

    tmpRowWidth = [winWidth*0.5, winWidth*0.5]
    cmds.rowLayout(nc = 2, cw2 = tmpRowWidth)

    cmds.textField('prefix', w = tmpRowWidth[0])
    cmds.button('prefix', l = 'Prefix', align='center', w = tmpRowWidth[1], h = 30, c='rename.do_addPrefix()')

    cmds.setParent('..')

#SUFFIX____________

    tmpRowWidth = [winWidth*0.5, winWidth*0.5]
    cmds.rowLayout(nc = 2, cw2 = tmpRowWidth)

    cmds.textField('suffix', w = tmpRowWidth[0])
    cmds.button('suffix', l = 'Suffix', align='center', w = tmpRowWidth[1], h = 30, c='rename.do_addSuffix()')

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

            if newName == 'Vincent_Corriveau':
                newName = 'Face_De_Cul'


            cmds.rename(i, newName + str(startNum).rjust(padding,'0'))
            startNum = startNum + 1


    else:

        LOG.error('Nothing in selection.')


def do_replace():

    oldNameR = cmds.textField('oldNameR', q=True, tx=True)
    newNameR = cmds.textField('newNameR', q=True, tx=True)


    sel = pm.ls(sl=True)



    for i in sel:

        if oldNameR in i.nodeName():
            i.rename(i.nodeName().replace(oldNameR, newNameR))

        else:
            LOG.info('Selected object does not contain replacement name.')


def do_addPrefix():

    prefix = cmds.textField('prefix', q=True, tx=True)

    sel = pm.selected()

    for i in sel:

        if prefix:
            i.rename(prefix + i)

        else:
            LOG.error('No prefix added.')

def do_addSuffix():

    suffix = cmds.textField('suffix', q=True, tx=True)

    sel = pm.selected()

    for i in sel:

        if suffix:
            i.rename(i + suffix)

        else:
            LOG.error('No suffix added.')
