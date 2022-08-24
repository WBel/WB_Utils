q"""
Script made by William Belanger.

Email:  will_belanger@hotmail.com

V 1.0.6
"""





import maya.cmds as mc
from pymel.core import general as pm
import os
import pickle

def BuiltUI():
    winName = 'RiggingTools'
    winWidth = 400
    version = 'V 1.0.6'
    mail = 'will_belanger@hotmail.com'
    dev = 'William Belanger'
    dateC = '02/26/2020'
    
    home = os.getenv('APPDATA')
    
    finalPath = home.replace(os.sep, '/')
    
    
            

    
    
    if mc.window(winName, exists=True):
        mc.deleteUI(winName)
    window = mc.window(winName, w = winWidth, title = 'Rigging tools', menuBar = True)
    mc.columnLayout()
    
    
    
#MENUS______________________________
    

    try:
        with open(finalPath + "/color.dat",'rb') as fp:
            data=pickle.load(fp)
    except:
        createFold()
    finally:
        print('yeah!')
    
        
   
    mc.menu(l = 'Colors')
    
    mc.menuItem('red', l = 'Red',  c = 'redChange()')
    mc.menuItem('orange', l = 'Orange',  c = 'orangeChange()')
    mc.menuItem('yellow', l = 'Yellow',  c = 'yellowChange()')
    mc.menuItem('green', l = 'Green',  c = 'greenChange()')
    mc.menuItem('blue', l = 'Blue',  c = 'blueChange()')
    mc.menuItem('purple', l = 'Purple',  c = 'purpleChange()')
    mc.menuItem('grey', l = 'Grey',  c = 'greyChange()')
    
    
#Infos________

    mc.menu(l = 'Infos')
    
    mc.menuItem(l = 'Developer', d = True, ld = True)
    mc.menuItem(l = dev)
    mc.menuItem(l = 'Join', d = True, ld = True)
    mc.menuItem(l = mail)
    mc.menuItem(l = 'Version', d = True, ld = True)
    mc.menuItem(l = version)
    mc.menuItem(l = 'Last Update', d = True, ld = True)
    mc.menuItem(l = dateC)
    
    
    mc.columnLayout()
    
    
#COLOR_CHANGE_______________________________________________________________________________

    mc.frameLayout(l = 'Color change', w = winWidth, cll = True, cl = True)
    
    tmpRowWidth = [winWidth*0.33, winWidth*0.33, winWidth*0.33]
    mc.rowLayout(nc = 3, cw3 = tmpRowWidth)
    
    mc.text(label='item selection', align = 'center', w = tmpRowWidth[0])
    mc.checkBox('out', label='Outliner', align = 'center', w = tmpRowWidth[1], value = True)
    mc.checkBox('view', label='Viewport', align = 'center', w = tmpRowWidth[2], value = True)
    
    mc.setParent('..')
    
#________________________

    tmpRowWidth = [winWidth*0.3, winWidth*0.7]
    mc.rowLayout(nc = 2, cw2 = tmpRowWidth)
    
    mc.text(l = 'Color Selection', w = tmpRowWidth[0])
    mc.colorSliderGrp('cSlide', w = tmpRowWidth[1])
    
    mc.setParent('..')
    
#________________________
    
    tmpRowWidth = winWidth
    mc.rowLayout(nc = 1, cw1 = tmpRowWidth)
    
    mc.button('colorChange', l = 'Change color', w = winWidth, h = 30, c='colorChange()')
    mc.showWindow( window )
    
    mc.setParent('..')
    
    mc.setParent('..')
    
    mc.separator(h = 20, w = winWidth)
    
#RENAME__________________________________________________________________________________
    
    mc.frameLayout(l = 'Rename', w = winWidth, cll = True)
    
    tmpRowWidth = [winWidth*0.15, winWidth*0.84]
    mc.rowLayout(nc = 2, cw2 = tmpRowWidth)
    
    mc.text(l = 'Rename :', w = tmpRowWidth[0], align = 'center', h = 30)
    mc.textField('rename', w = tmpRowWidth[1])
    
    mc.setParent('..')
    
#__________
    
    tmpRowWidth = [winWidth*0.20, winWidth*0.30, winWidth*0.15, winWidth*0.33]
    mc.rowLayout(nc = 4, cw4 = tmpRowWidth)
    
    mc.text(l = 'Start number  :', align = 'center', w = tmpRowWidth[0], h = 20)
    mc.textField('number', w = tmpRowWidth[1], tx = '1')
    mc.text(l = 'Padding  :', align = 'center', w = tmpRowWidth[2], h = 20)
    mc.textField('padding', w = tmpRowWidth[3], tx = '1')
    
    mc.setParent('..')
    
#___________
    
    tmpRowWidth = winWidth
    mc.rowLayout(nc = 1, cw1 = tmpRowWidth)
    
    mc.button('rename', l = 'Rename', w = winWidth, align='center', h = 30, c='renameBut()')
     
    mc.setParent('..')
    
#REPLACE____________________

    tmpRowWidth = [winWidth*0.15, winWidth*0.84]
    mc.rowLayout(nc = 2, cw2 = tmpRowWidth)
    
    mc.text(l = 'Replace :', align = 'center', w = tmpRowWidth[0], h = 20)
    mc.textField('oldName', w = tmpRowWidth[1])
    
    mc.setParent('..')
    
#_________
    
    tmpRowWidth = [winWidth*0.15, winWidth*0.84]
    mc.rowLayout(nc = 2, cw2 = tmpRowWidth)
    
    mc.text(l = 'With :', align = 'center', w = tmpRowWidth[0], h = 30)
    mc.textField('newName', w = tmpRowWidth[1])
    
    mc.setParent('..')
    
#__________
    
    tmpRowWidth = winWidth
    mc.rowLayout(nc = 1, cw1 = tmpRowWidth)
    
    mc.button('replace', l = 'Replace', w = winWidth, h = 30, c='repButt()')
    
    mc.setParent('..')
    
    mc.setParent('..')
    
    mc.separator(h = 20, w = winWidth)
    
    
#RPEFIX_____________________________________________________________________________________

    mc.frameLayout(l = 'Prefix and suffix', w = winWidth, cll = True)

    tmpRowWidth = [winWidth*0.5, winWidth*0.5]
    mc.rowLayout(nc = 2, cw2 = tmpRowWidth)
    
    mc.textField('prefix', w = tmpRowWidth[0])
    mc.button('prefix', l = 'Prefix', align='center', w = tmpRowWidth[1], h = 30, c='prefButton()')
    
    mc.setParent('..')
    
#SUFFIX____________

    tmpRowWidth = [winWidth*0.5, winWidth*0.5]
    mc.rowLayout(nc = 2, cw2 = tmpRowWidth)
    
    mc.textField('suffix', w = tmpRowWidth[0])
    mc.button('suffix', l = 'Suffix', align='center', w = tmpRowWidth[1], h = 30, c='suffButton()')
    
    mc.setParent('..')
    
    
    
    mc.separator(h = 10, w = winWidth)
    

    
#GRPPREFIX______________________________________________________________________________________

    mc.frameLayout(l = 'Create group with prefix', cll = True, w = winWidth, cl = True)

    tmpRowWidth = [winWidth*0.15, winWidth*0.85]
    mc.rowLayout(nc = 2, cw2 = tmpRowWidth)
    
    mc.text(l = 'Prefix :', w = tmpRowWidth[0], align = 'center', h = 30)
    mc.textField('grpPrefix', w = tmpRowWidth[1])
    
    mc.setParent('..')
    
    tmpRowWidth = winWidth
    mc.rowLayout(nc = 1, cw1 = tmpRowWidth)
    
    mc.button('groupPrefix', l = 'Create group', align = 'center', w = winWidth, h = 30, c='grpPre()')
    
    mc.setParent('..')
    
    mc.setParent('..')
    
    mc.setParent('..')
    
    mc.separator(h = 20, w = winWidth)
    
#HIERARCHY___________________________________________________________________________________

    tmpRowWidth = winWidth
    mc.rowLayout(nc = 1, cw1 = tmpRowWidth)
    
    mc.button('hierarchy', l = 'Select hierarchy', align = 'center', w = winWidth, h = 30, c='selectHi()')
    
    mc.setParent('..')
    
    mc.separator(h = 20, w = winWidth)

#MIRROR_CTRL___________________________________________________________________________________

    mc.frameLayout(l = 'Mirror controllers', cll = True, w = winWidth, cl = True)
    
    tmpRowWidth = [winWidth*0.25, winWidth*0.75]
    mc.rowLayout(nc = 2, cw2 = tmpRowWidth)
    
    mc.text(l = 'Mirror axis : ', w = tmpRowWidth[0])
    mc.radioButtonGrp('mirrorC', numberOfRadioButtons = 3, sl = 2, labelArray3=['XY', 'YZ', 'XZ'], w = tmpRowWidth[1])
    
    mc.setParent('..')
    
    tmpRowWidth = [winWidth*0.15, winWidth*0.84]
    mc.rowLayout(nc = 2, cw2 = tmpRowWidth)
    
    mc.text(l = 'Replace :', align = 'center', w = tmpRowWidth[0], h = 20)
    mc.textField('ctrlS', w = tmpRowWidth[1])
    
    mc.setParent('..')
    
    tmpRowWidth = [winWidth*0.15, winWidth*0.84]
    mc.rowLayout(nc = 2, cw2 = tmpRowWidth)
    
    mc.text(l = 'With :', align = 'center', w = tmpRowWidth[0], h = 30)
    mc.textField('ctrlR', w = tmpRowWidth[1])
    
    mc.setParent('..')
    
    tmpRowWidth = [winWidth]
    mc.rowLayout(nc = 1, cw1 = tmpRowWidth[0])
    
    mc.button('mirrorCtrl', l = 'Mirror controllers', c='mirrorCtrl()', w = tmpRowWidth[0], h = 30)
    
    mc.setParent('..')
    
    mc.setParent('..')

    mc.separator(h = 20, w = winWidth)

#SHOW_HIDE_AXIS________________________________________________________________________________

    mc.frameLayout(l = 'Joints', w = winWidth, cll = True)
    
    tmpRowWidth = [winWidth*0.5, winWidth*0.5]
    mc.rowLayout(nc = 2, cw2 = tmpRowWidth)
    
    mc.button('showAxis', l = 'Show axis', align = 'center', w = tmpRowWidth[0], h = 30, c='mc.toggle(la = True, st = True)')
    mc.button('hideAxis', l = 'Hide axis', align = 'center', w = tmpRowWidth[1], h = 30, c='mc.toggle(la = True, st = False)')
    
    mc.setParent('..')
    
    mc.separator(h = 10, w = winWidth)


#MirrorJoint____________________________________________________________________________________

    tmpRowWidth = [winWidth*0.25, winWidth*0.75]
    mc.rowLayout(nc = 2, cw2 = tmpRowWidth)
    
    mc.text(l = 'Mirror axis : ', w = tmpRowWidth[0])
    mc.radioButtonGrp('mirrorJ', numberOfRadioButtons = 3, sl = 2, labelArray3=['XY', 'YZ', 'XZ'], w = tmpRowWidth[1])
    
    mc.setParent('..')
    
    tmpRowWidth = [winWidth*0.15, winWidth*0.84]
    mc.rowLayout(nc = 2, cw2 = tmpRowWidth)
    
    mc.text(l = 'Replace :', align = 'center', w = tmpRowWidth[0], h = 20)
    mc.textField('jointS', w = tmpRowWidth[1])
    
    mc.setParent('..')
    
#_________
    
    tmpRowWidth = [winWidth*0.15, winWidth*0.84]
    mc.rowLayout(nc = 2, cw2 = tmpRowWidth)
    
    mc.text(l = 'With :', align = 'center', w = tmpRowWidth[0], h = 30)
    mc.textField('jointR', w = tmpRowWidth[1])
    
    mc.setParent('..')
    
    tmpRowWidth = [winWidth]
    mc.rowLayout(nc = 1, cw1 = tmpRowWidth[0])
    
    mc.button('mirrorJoint', l = 'Mirror joints', c='mirrorJ()', w = tmpRowWidth[0], h = 30)
    
    mc.setParent('..')
    
    mc.separator(h = 10, w = winWidth)

#OrientJoints_____________________________________________________________________________________
    '''
    mc.frameLayout(l = 'Joint orientation', cll = False, w = winWidth)

    tmpRowWidth = [winWidth*0.25, winWidth*0.75]
    mc.rowLayout(nc = 2, cw2 = tmpRowWidth)
    
    mc.text(l = 'Aim axis : ', w = tmpRowWidth[0], align = 'center')
    mc.radioButtonGrp('aimAxis', numberOfRadioButtons = 3, sl = 1, labelArray3=['X', 'Y', 'Z'], cw3 = (90,90,90))
    
    mc.setParent('..')
    
    tmpRowWidth = [winWidth*0.25, winWidth*0.75]
    mc.rowLayout(nc = 2, cw2 = tmpRowWidth)
    
    mc.text(l = 'Up axis : ', w = tmpRowWidth[0], align = 'center')
    mc.radioButtonGrp('upAxis', numberOfRadioButtons = 3, sl = 2, labelArray3=['X', 'Y', 'Z'], cw3 = (90,90,90))
    
    mc.setParent('..')
    
    tmpRowWidth = [winWidth*0.25, winWidth*0.23, winWidth*0.23, winWidth*0.23]
    mc.rowLayout(nc = 4, cw4 = tmpRowWidth)
    
    mc.text(l = 'World up axis : ', w = tmpRowWidth[0], align = 'center')
    mc.textField('wUpAxisX', w = tmpRowWidth[1], tx = '0.00')
    mc.textField('wUpAxisY', w = tmpRowWidth[1], tx = '0.00')
    mc.textField('wUpAxisZ', w = tmpRowWidth[1], tx = '1.00')
    
    mc.setParent('..')
    
    
    tmpRowWidth = [winWidth]
    mc.rowLayout(nc = 1, cw1 = tmpRowWidth[0])
    
    mc.button('oJoint', l = 'Orient joints', w = tmpRowWidth[0], c='orientJ()', h = 30)

    mc.setParent('..')
    
    mc.setParent('..')
    '''  
    mc.setParent('..')

   
#UIcolorReading__________________________________
   
   
    with open(finalPath + "/color.dat",'rb') as fp:
        data=pickle.load(fp)
        if data == 'red':
            redChange()
        if data == 'orange':
            orangeChange()
        if data == 'yellow':
            yellowChange()
        if data == 'green':
            greenChange()
        if data == 'blue':
            blueChange()
        if data == 'purple':
            purpleChange()
        if data == 'grey':
            greyChange()

    
#COLOR_FUNCTION______________________________________________________________________________
    
    
    
def colorChange():
    #Va chercher les informations de item selection et color selection
    color = mc.colorSliderGrp('cSlide', q = True, rgbValue = True)
    oBox = mc.checkBox('out', q = True, value = True)
    oView = mc.checkBox('view', q = True, value = True)
    
    #Prend la selection en variable
    select = mc.ls(selection = True)
    
    
    if oView == True:
        for object in select:
            mc.setAttr(object + '.overrideEnabled', 1)
            mc.setAttr(object + '.overrideRGBColors', 1)
            mc.setAttr(object + '.overrideColorRGB', color[0], color[1], color[2])
            #Si Outliner est coché, change les couleurs dans le outliner
            if oBox == True:
                for object in select:
                    mc.setAttr(object + '.useOutlinerColor', 1)
                    mc.setAttr(object + '.outlinerColor', color[0], color[1], color[2])
            #Si viewport est coché, change les couleurs dans le viewport
            else:
                continue
    elif oBox == True:
        for object in select:
                    mc.setAttr(object + '.useOutlinerColor', 1)
                    mc.setAttr(object + '.outlinerColor', color[0], color[1], color[2])
                    #Si outliner n'est pas coché, mais que viewport est coché, change les couleurs dans le viewport
    else:
        print('Error! Nothing was checked.')

#_________________________________________________________________________________________

#renameFunc_______


def renameBut():
    textR = mc.textField('rename', q=True, tx = True)
    num = mc.textField('number', q = True, tx = True)
    pad = mc.textField('padding', q = True, tx = True)
    
    select = mc.ls(selection = True)
    i = int(num)
    p = int(pad)
    
    for object in select:
        
        if textR == '':
            return
        else:  
            mc.rename(object, textR + str(i))
            i += p
        
#prefixFunc_______

def prefButton():
    textP = mc.textField('prefix', q=True, tx = True)
    
    
    for object in pm.selected():
        if textP == '':
            print('No text')
            return
        else:
            object.rename(textP + object)
        
#suffixFunc________
        
def suffButton():
    textS = mc.textField('suffix', q=True, tx = True)
    
    
    for object in pm.selected():
        if textS == '':
            print('No text')
        else:
            object.rename(object + textS)
        
#replaceFunc_________ 
       
def repButt():
    oldN = mc.textField('oldName', q=True, tx = True)
    newN = mc.textField('newName', q=True, tx = True)
    
    if oldN != '':
        if newN != '':
            for item in pm.selected():
                item.rename(item.name().replace(oldN, newN))
        else:
            print('No text')
    else:
        print('No text') 
   
#selectHi___________

def selectHi():
    mc.select(hi = True)
    
    
#grpPre________________________________

def grpPre():
    prefix = mc.textField('grpPrefix', q = True, tx = True)
    
    select = mc.ls(selection = True)
    
    for object in pm.selected():
        mc.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        if prefix == '':
            print('Error! No Prefix')
        else:
            mc.group(n = prefix + object)
            
            
#MIRROR_JOINTS_________________________

def mirrorJ():
    
    axis = mc.radioButtonGrp('mirrorJ', q=True, sl = True)
    search = mc.textField('jointS', q=True, tx = True)
    replace = mc.textField('jointR', q=True, tx = True)
    
    if axis == 1:
        mc.mirrorJoint(mxy = True, sr = (search, replace), mb = True)
    if axis == 2:
        mc.mirrorJoint(myz = True, sr = (search, replace), mb = True)
    if axis == 3:
        mc.mirrorJoint(mxz = True, sr = (search, replace), mb = True)
    
    
#MIRROR_CTRL________________________________

def mirrorCtrl():
    
    ctrl = mc.ls(selection = True)
    axis = mc.radioButtonGrp('mirrorC', q = True, sl = True)
    search = mc.textField('ctrlS', q = True, tx = True)
    replace = mc.textField('ctrlR', q = True, tx = True)
    
    mc.group(em = True, n = 'GrpNull1')
    mc.parent(ctrl, 'GrpNull1')
    mc.select('GrpNull1')
    mc.duplicate(rc = False)
    
    if search == '':
        if replace == '':
        
            mc.select('GrpNull2', hi = True)
            mc.select('GrpNull2', d = True)
        
            for object in pm.selected():
                object.rename(object + '_NEW')
        else:
            Print('Error')
    else:
        mc.select('GrpNull2', hi = True)
        mc.select('GrpNull2', d = True)
        
        for object in pm.selected():
            object.rename(object.name().replace(search, replace))
    
    mc.select('GrpNull2')
    if  axis == 1:
        mc.scale(1,1-1)
    elif axis == 2:
        mc.scale (-1,1,1)
    elif axis == 3:
        mc.scale(1,-1,1)
    mc.select('GrpNull1')    
    oldO = mc.listRelatives(c = True)    
    mc.select('GrpNull2')
    dupO = mc.listRelatives(c = True)
    
    mc.parent(dupO, w = True)
    mc.parent(oldO, w = True)
    
    mc.delete('GrpNull1')
    mc.delete('GrpNull2')
    
    
    
#buttonChange_______________________________________________________________

redC = (1,0.4,0.5)
orangeC = (1,0.5,0.1)
yellowC = (1,0.9,0.3)
greenC = (0.3,0.8,0.5)
blueC = (0.2,0.6,0.8)
purpleC = (0.6,0.4,0.8)
greyC = (0.7,0.7,0.7)

home = os.getenv('APPDATA')
    
finalPath = home.replace(os.sep, '/')


def createFold():
    with open(finalPath + "/color.dat",'wb') as fp:
        pickle.dump('dumm', fp)

    

def redChange():
    mc.button('colorChange', e = True, bgc = redC)
    mc.button('rename', e = True, bgc = redC)
    mc.button('prefix', e = True, bgc = redC)
    mc.button('suffix', e = True, bgc = redC)
    mc.button('replace', e = True, bgc = redC)
    mc.button('hierarchy', e = True, bgc = redC)
    mc.button('showAxis', e = True, bgc = redC)
    mc.button('hideAxis', e = True, bgc = redC)
    mc.button('groupPrefix', e = True, bgc = redC)
    mc.button('mirrorJoint', e = True, bgc = redC)
    #mc.button('oJoint', e = True, bgc = redC)
    mc.button('mirrorCtrl', e = True, bgc = redC)
    
    with open(finalPath + "/color.dat",'wb') as fp:
        pickle.dump('red', fp)
    
def orangeChange():
    mc.button('colorChange', e = True, bgc = orangeC)
    mc.button('rename', e = True, bgc = orangeC)
    mc.button('prefix', e = True, bgc = orangeC)
    mc.button('suffix', e = True, bgc = orangeC)
    mc.button('replace', e = True, bgc = orangeC)
    mc.button('hierarchy', e = True, bgc = orangeC)
    mc.button('showAxis', e = True, bgc = orangeC)
    mc.button('hideAxis', e = True, bgc = orangeC)
    mc.button('groupPrefix', e = True, bgc = orangeC)
    mc.button('mirrorJoint', e = True, bgc = orangeC)
    #mc.button('oJoint', e = True, bgc = orangeC)
    mc.button('mirrorCtrl', e = True, bgc = orangeC)
    
    with open(finalPath + "/color.dat",'wb') as fp:
        pickle.dump('orange', fp)
     
def yellowChange():
    mc.button('colorChange', e = True, bgc = yellowC)  
    mc.button('rename', e = True, bgc = yellowC)  
    mc.button('prefix', e = True, bgc = yellowC)  
    mc.button('suffix', e = True, bgc = yellowC) 
    mc.button('replace', e = True, bgc = yellowC) 
    mc.button('hierarchy', e = True, bgc = yellowC) 
    mc.button('showAxis', e = True, bgc = yellowC) 
    mc.button('hideAxis', e = True, bgc = yellowC) 
    mc.button('groupPrefix', e = True, bgc = yellowC)
    mc.button('mirrorJoint', e = True, bgc = yellowC)
    #mc.button('oJoint', e = True, bgc = yellowC)
    mc.button('mirrorCtrl', e = True, bgc = yellowC)
    
    with open(finalPath + "/color.dat",'wb') as fp:
        pickle.dump('yellow', fp)
def greenChange():
    
    mc.button('colorChange', e = True, bgc = greenC)
    mc.button('rename', e = True, bgc = greenC)
    mc.button('prefix', e = True, bgc = greenC)
    mc.button('suffix', e = True, bgc = greenC)
    mc.button('replace', e = True, bgc = greenC)
    mc.button('hierarchy', e = True, bgc = greenC)
    mc.button('showAxis', e = True, bgc = greenC)
    mc.button('hideAxis', e = True, bgc = greenC)
    mc.button('groupPrefix', e = True, bgc = greenC)
    mc.button('mirrorJoint', e = True, bgc = greenC)
    #mc.button('oJoint', e = True, bgc = greenC)
    mc.button('mirrorCtrl', e = True, bgc = greenC)
    
    with open(finalPath + "/color.dat",'wb') as fp:
        pickle.dump('green', fp)
    
def blueChange():
    mc.button('colorChange', e = True, bgc = blueC)
    mc.button('rename', e = True, bgc = blueC)
    mc.button('prefix', e = True, bgc = blueC)
    mc.button('suffix', e = True, bgc = blueC)
    mc.button('replace', e = True, bgc = blueC)
    mc.button('hierarchy', e = True, bgc = blueC)
    mc.button('showAxis', e = True, bgc = blueC)
    mc.button('hideAxis', e = True, bgc = blueC)
    mc.button('groupPrefix', e = True, bgc = blueC)
    mc.button('mirrorJoint', e = True, bgc = blueC)
    #mc.button('oJoint', e = True, bgc = blueC)
    mc.button('mirrorCtrl', e = True, bgc = blueC)
    
    with open(finalPath + "/color.dat",'wb') as fp:
        pickle.dump('blue', fp)
    
def purpleChange():
    mc.button('colorChange', e = True, bgc = purpleC)
    mc.button('rename', e = True, bgc = purpleC)
    mc.button('prefix', e = True, bgc = purpleC)
    mc.button('suffix', e = True, bgc = purpleC)
    mc.button('replace', e = True, bgc = purpleC)
    mc.button('hierarchy', e = True, bgc = purpleC)
    mc.button('showAxis', e = True, bgc = purpleC)
    mc.button('hideAxis', e = True, bgc = purpleC)
    mc.button('groupPrefix', e = True, bgc = purpleC)
    mc.button('mirrorJoint', e = True, bgc = purpleC)
    #mc.button('oJoint', e = True, bgc = purpleC)
    mc.button('mirrorCtrl', e = True, bgc = purpleC)
    
    with open(finalPath + "/color.dat",'wb') as fp:
        pickle.dump('purple', fp)
    
def greyChange():
    mc.button('colorChange', e = True, bgc = greyC)
    mc.button('rename', e = True, bgc = greyC)
    mc.button('prefix', e = True, bgc = greyC)
    mc.button('suffix', e = True, bgc = greyC)
    mc.button('replace', e = True, bgc = greyC)
    mc.button('hierarchy', e = True, bgc = greyC)
    mc.button('showAxis', e = True, bgc = greyC)
    mc.button('hideAxis', e = True, bgc = greyC)
    mc.button('groupPrefix', e = True, bgc = greyC)
    mc.button('mirrorJoint', e = True, bgc = greyC)
    #mc.button('oJoint', e = True, bgc = greyC)
    mc.button('mirrorCtrl', e = True, bgc = greyC)
    
    with open(finalPath + "/color.dat",'wb') as fp:
        pickle.dump('grey', fp)
        
    
#MAIL____________________________



    
BuiltUI()


