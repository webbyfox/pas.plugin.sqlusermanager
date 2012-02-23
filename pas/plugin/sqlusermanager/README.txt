Tests for pas.plugin.sqlusermanager

test setup
----------

    >>> from Testing.ZopeTestCase import user_password
    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()

Plugin setup
------------

    >>> acl_users_url = "%s/acl_users" % self.portal.absolute_url()
    >>> browser.addHeader('Authorization', 'Basic %s:%s' % ('portal_owner', user_password))
    >>> browser.open("%s/manage_main" % acl_users_url)
    >>> browser.url
    'http://nohost/plone/acl_users/manage_main'
    >>> form = browser.getForm(index=0)
    >>> select = form.getControl(name=':action')

pas.plugin.sqlusermanager should be in the list of installable plugins:

    >>> 'Sqlusermanager Helper' in select.displayOptions
    True

and we can select it:

    >>> select.getControl('Sqlusermanager Helper').click()
    >>> select.displayValue
    ['Sqlusermanager Helper']
    >>> select.value
    ['manage_addProduct/pas.plugin.sqlusermanager/manage_add_sqlusermanager_helper_form']

we add 'Sqlusermanager Helper' to acl_users:

    >>> from pas.plugin.sqlusermanager.plugin import SqlusermanagerHelper
    >>> myhelper = SqlusermanagerHelper('myplugin', 'Sqlusermanager Helper')
    >>> self.portal.acl_users['myplugin'] = myhelper

and so on. Continue your tests here

    >>> 'ALL OK'
    'ALL OK'

