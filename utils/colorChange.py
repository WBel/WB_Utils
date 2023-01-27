from maya import cmds

import pymel.core as pm
import logging


def BuildUI():
    winName = 'colorOverride'
    winWidth = 400
    winHeight = 130
    dev = 'William Bélanger'
    mail = 'william@unstandardstudio.com'
    version = 'V.1.0'

    if cmds.window(winName, exists=True):
            cmds.deleteUI(winName)
    window = cmds.window(winName, w = winWidth, h = winHeight, title = 'Override Colors', menuBar = True, rtf=True, s=False)
    cmds.columnLayout()

#Infos________

    cmds.menu(l = 'Info')

    cmds.menuItem(l = 'Developer', d = True, ld = True)
    cmds.menuItem(l = dev)
    cmds.menuItem(l = 'Join', d = True, ld = True)
    cmds.menuItem(l = mail)
    cmds.menuItem(l = 'Version', d = True, ld = True)
    cmds.menuItem(l = version)


#COLOR_CHANGE_______________________________________________________________________________

    cmds.frameLayout(l = 'Color change', w = winWidth)

    tmpRowWidth = [winWidth*0.33, winWidth*0.33, winWidth*0.33]
    cmds.rowLayout(nc = 3, cw3 = tmpRowWidth)

    cmds.text(label='item selection', align = 'center', w = tmpRowWidth[0])
    cmds.checkBox('out', label='Outliner', align = 'center', w = tmpRowWidth[1], value = False)
    cmds.checkBox('view', label='Viewport', align = 'center', w = tmpRowWidth[2], value = True)

    cmds.setParent('..')

#________________________

    tmpRowWidth = [winWidth*0.3, winWidth*0.7]
    cmds.rowLayout(nc = 2, cw2 = tmpRowWidth)

    cmds.text(l = 'Color Selection', w = tmpRowWidth[0])
    cmds.colorSliderGrp('cSlide', w = tmpRowWidth[1])

    cmds.setParent('..')

#________________________

    tmpRowWidth = winWidth
    cmds.rowLayout(nc = 1, cw1 = tmpRowWidth)

    cmds.button('colorChange', l = 'Change color', w = winWidth, h = 30, c='colorChange.doColorChange()')
    cmds.showWindow( window )

    cmds.setParent('..')

    cmds.setParent('..')

    cmds.separator(h = 20, w = winWidth)




def doColorChange():

    outBox = cmds.checkBox('out', q=True,value = True)
    viewBox = cmds.checkBox('view', q=True, value = True)
    color = cmds.colorSliderGrp('cSlide', q=True, rgbValue=True)

    sel = cmds.ls(sl=True)

    if sel:


        for i in sel:

            if viewBox and not outBox:

                shape = cmds.listRelatives(i, s = True)
                cmds.setAttr(shape[0] + '.overrideEnabled', 1)
                cmds.setAttr(shape[0] + '.overrideRGBColors', 1)
                cmds.setAttr(shape[0] + '.overrideColorRGB', color[0], color[1], color[2])

            elif outBox and not viewBox:

                cmds.setAttr(i + '.useOutlinerColor', 1)
                cmds.setAttr(i + '.outlinerColor', color[0], color[1], color[2])

            elif outBox and viewBox:

                shape = cmds.listRelatives(i, s = True)
                cmds.setAttr(shape[0] + '.overrideEnabled', 1)
                cmds.setAttr(shape[0] + '.overrideRGBColors', 1)
                cmds.setAttr(shape[0] + '.overrideColorRGB', color[0], color[1], color[2])

                cmds.setAttr(i + '.useOutlinerColor', 1)
                cmds.setAttr(i + '.outlinerColor', color[0], color[1], color[2])


            else:
                LOG.error('Nothing selected in item selection.')
    else:

        LOG.error('Nothing selected.')
