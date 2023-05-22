from maya import cmds

import logging
import re
import os


logging.basicConfig()
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)




def BuildUI():
    winName = 'VrayObjectSettings'
    winWidth = 400
    dev = 'William Bélanger'
    mail = 'william@unstandardstudio.com'
    version = 'V.1.0'

    if cmds.window(winName, exists=True):
            cmds.deleteUI(winName)
    window = cmds.window(winName, w = winWidth, title = 'Vray object settings', menuBar = True, rtf=True)
    cmds.columnLayout()
#Infos________

    cmds.menu(l = 'Info')

    cmds.menuItem(l = 'Developer', d = True, ld = True)
    cmds.menuItem(l = dev)
    cmds.menuItem(l = 'Join', d = True, ld = True)
    cmds.menuItem(l = mail)
    cmds.menuItem(l = 'Version', d = True, ld = True)
    cmds.menuItem(l = version)

#Subdivision__________________________________________________________________________________

    cmds.frameLayout(l = 'Subdivision', w = winWidth)

    tmpRowWidth = [winWidth*0.5, winWidth*0.5]
    cmds.rowLayout(nc = 2, cw2 = tmpRowWidth)

    cmds.button('addSubd', l = "Add Subdivision", w = tmpRowWidth[0], align='left', h = 30, c='vrayUtils.do_subdivideObject(state="add")')
    cmds.button('remSubd', l = 'Remove Subdivision', w = tmpRowWidth[1], align='right', h = 30, c='vrayUtils.do_subdivideObject(state="remove")')

    cmds.setParent('..')

#__________

    tmpRowWidth = winWidth
    cmds.rowLayout(nc = 1, cw1 = tmpRowWidth)

    cmds.button('selSubd', l = 'Select Objects with Subdivision', w = winWidth, align='center', h = 30, c='vrayUtils.do_selObjectSubd()')
    cmds.setParent('..')

#ObjectID__________________________________________________________________________________

    cmds.frameLayout(l = 'Object ID', w = winWidth)

    tmpRowWidth = winWidth
    cmds.rowLayout(nc = 1, cw1 = tmpRowWidth)

    cmds.intSliderGrp('ID', field=True, w = winWidth, h = 30, v = 0)
    cmds.setParent('..')

#__________

    tmpRowWidth = [winWidth*0.5, winWidth*0.5]
    cmds.rowLayout(nc = 2, cw2 = tmpRowWidth)

    cmds.button('addID', l = 'Add ID', w = tmpRowWidth[0], align='left', h = 30, c='vrayUtils.do_changeObjectID(state="add")')
    cmds.button('selID', l = 'Select Objects with ID', w = tmpRowWidth[1], align='right', h = 30, c='vrayUtils.do_selObjectID()')

    cmds.setParent('..')

#__________

    tmpRowWidth = winWidth
    cmds.rowLayout(nc = 1, cw1 = tmpRowWidth)

    cmds.button('removeID', l = 'Remove ID', w = winWidth, align='center', h = 30, c='vrayUtils.do_changeObjectID(state="remove")')
    cmds.setParent('..')

    cmds.showWindow()





def do_changeObjectID(state=""):

    objectID = cmds.intSliderGrp("ID", q=True, v = True)


    selMesh = cmds.ls(sl = True)
    selShape = cmds.listRelatives(s = True, f= True, type = "mesh")


    for i in selShape:
        if state == "add":

            cmds.vray("addAttributesFromGroup", i, "vray_objectID", 1)
            cmds.setAttr(i+".vrayObjectID", objectID)

        elif state == "remove":

            cmds.vray("addAttributesFromGroup", i, "vray_objectID", 0)

def do_selObjectID():

    objectID = cmds.intSliderGrp("ID", q=True, v = True)


    sel = cmds.select(all = True)
    selGood = cmds.ls( type="mesh" )
    cmds.select(cl = True)

    for i in selGood:
        objectAttr = cmds.listAttr(i)
        print(objectAttr)
        if "vrayObjectID" in objectAttr:
            currentID = cmds.getAttr(i+".vrayObjectID")
            if currentID == objectID:
                cmds.select(i, add = True)

def do_subdivideObject(state=""):

    selMesh = cmds.ls(sl = True)
    selShape = cmds.listRelatives(s = True, f= True, type = "mesh")

    for i in selShape:
        if state == "add":

            cmds.vray("addAttributesFromGroup", i, "vray_subdivision", 1)

        elif state == "remove":

            cmds.vray("addAttributesFromGroup", i, "vray_subdivision", 0)

def do_selObjectSubd():

    sel = cmds.select(all = True)
    selGood = cmds.ls( type="mesh" )
    cmds.select(cl = True)

    for i in selGood:
        objectAttr = cmds.listAttr(i)
        print(objectAttr)
        if "vraySeparator_vray_subdivision" in objectAttr:
            cmds.select(i, add = True)
