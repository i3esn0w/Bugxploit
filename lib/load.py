from pluginManager import * 
VERSION=0.1
class load():
    def __init__(self):
        pass

    def get_plugin(self,directory,plugin):
        try:
            plugin_manager = DirectoryPluginManager(directory)
            plugin_manager.loadPlugins()
            plugins = plugin_manager.getPlugins(plugin) 
            return plugins[0]
        except:
            pass
        
    
    
    
    
    