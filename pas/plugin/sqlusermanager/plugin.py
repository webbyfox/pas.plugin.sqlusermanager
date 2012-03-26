"""Class: SqlusermanagerHelper
"""

from AccessControl.SecurityInfo import ClassSecurityInfo
from App.class_init import default__class_init__ as InitializeClass

from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin
from Products.PluggableAuthService.utils import classImplements

import interface
import plugins

## Imported Class By Riz
from Products.PluggableAuthService.interfaces.plugins import \
        IGroupsPlugin, IPropertiesPlugin

from OFS.Cache import Cacheable
from AccessControl.SecurityInfo import ClassSecurityInfo
from AccessControl.SecurityManagement import getSecurityManager
from zope.interface import Interface
from OFS.Folder import Folder

import logging

logger = logging.getLogger("pas.plugins.sqlusermanager")

class SqlusermanagerHelper(BasePlugin, Cacheable, Folder):
	"""Multi-plugin
	"""
	
	meta_type = 'SQL User Manager'
	security = ClassSecurityInfo()

	_properties = ( { 'id'    : 'title'
		, 'label' : 'Title'
		, 'type'  : 'string'
		, 'mode'  : 'w'
			}
		, {'id'   : 'group_sql'
		, 'label' : 'SQL Group ZSQL id'
		, 'type'  : 'string'
		, 'mode'  : 'w'
		}
		,{ 'id'    : 'group_column'
		, 'label' : 'Group Column Name'
		, 'type'  : 'string'
		, 'mode'  : 'w'
		}
		,{ 'id'    : 'property_sql'
		, 'label' : 'Property ZSQL id'
		, 'type'  : 'string'
		, 'mode'  : 'w'
		}
		
		)
	
	group_sql = 'simsGroupsForUser'
	group_column = 'web_role'
	property_sql = 'simsPropertiesForUser'
	
	def __init__( self, id,title=None):
		self._setId( id )
		self.title = title
		security = ClassSecurityInfo()

	security.declarePrivate('invalidateCacheForChangedUser')
	def invalidateCacheForChangedUser(self, user_id):
		pass        

	security.declarePublic('getGroupsForPrincipal' )
	
	def getGroupsForPrincipal(self, principal, request=None):
		"""Method use to get Groups from SQL Database. simsGroupsForUser is SQL placed in theme product
		   
		"""
		groups = []
		results = {}
		
		# checking user is sims based or not? if not return 
		try:
			user = principal.getId().encode('ascii')
			int(user)
		except ValueError:
			return groups
		
		if hasattr(self, self.group_sql):
			results = getattr(self, self.group_sql)(username=user)
		
		#import pdb; pdb.set_trace()
		if results:
			for row in results.dictionaries():
				group = row.get(self.group_column)
				#groups.append(group)
				groups.append(group.replace(' ','_'))
			
		return groups
		
	security.declarePublic('getPropertiesForUser' )
	def getPropertiesForUser(self, user, request=None):
		""" Method is used to get property of user. It can be futher extented to achieve different
		    property of user i.e. email etc"""
		properties = {}
		results ={}
		
		# checking user is sims based or not? if not return 
		try:
			user = user.getId().encode('ascii')
			int(user)
		except ValueError:
			return properties
		
		if hasattr(self, self.property_sql):
			results = getattr(self,self.property_sql)(username=user)
		
		if results:
			for row in results.dictionaries():
				properties['fullname'] = row.get('fullname')
		
		return properties


classImplements(SqlusermanagerHelper, interface.ISqlusermanagerHelper, IGroupsPlugin, IPropertiesPlugin)

InitializeClass( SqlusermanagerHelper )
