from maya import cmds

import logging
import re

logging.basicConfig()
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)




def add_transform():

    sel = cmds.ls(sl=True)

    add_transforms = ['_off', '_grp']
    sel_transforms = sel


    for tfms in sel_transforms:
        if cmds.nodeType(tfms) == 'transform':
            LOG.info('Selected object is a transform')
            created_tfms = list()
            for i in range(0, len(add_transforms)):
            
                add_tfms = cmds.duplicate(tfms, po=True, name=tfms.replace('_ctl', add_transforms[i]).replace('_ctrl', add_transforms[i]))
                created_tfms.append(add_tfms)
                if i:
                    cmds.parent(created_tfms[i-1], created_tfms[i])
            cmds.parent(tfms, created_tfms[i-1])

        else:
            LOG.error('Selected object is not a transform.')
