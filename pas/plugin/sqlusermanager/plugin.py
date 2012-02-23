"""Class: SqlusermanagerHelper
"""

from AccessControl.SecurityInfo import ClassSecurityInfo
from App.class_init import default__class_init__ as InitializeClass

from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin
from Products.PluggableAuthService.utils import classImplements

import interface
import plugins

class SqlusermanagerHelper( # -*- implemented plugins -*-
                               ):
    """Multi-plugin

    """

    meta_type = 'sqlusermanager Helper'
    security = ClassSecurityInfo()

    def __init__( self, id, title=None ):
        self._setId( id )
        self.title = title



classImplements(SqlusermanagerHelper, interface.ISqlusermanagerHelper)

InitializeClass( SqlusermanagerHelper )
