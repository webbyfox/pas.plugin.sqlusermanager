import install

install.register_sqlusermanager_plugin()

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    install.register_sqlusermanager_plugin_class(context)
