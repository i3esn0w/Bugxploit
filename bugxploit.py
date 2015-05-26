#coding:utf-8
import os
import warnings
warnings.filterwarnings(action="ignore", message=".*was already imported", category=UserWarning)
warnings.filterwarnings(action="ignore", category=DeprecationWarning)
from optparse import OptionParser
from lib.load import *
import sys
reload(sys)
sys.setdefaultencoding("utf8")



if __name__=='__main__':

    usage="usage:%s -h www.test.com -p test"%(__file__)
    parser=OptionParser()
    parser.add_option("-t","--target",dest="target_url",default="www.testfire.com",
                      help="the target url you test"
                     )
    parser.add_option("-u","--plugin_used",dest="plugin_used",default="test",
                      help="the plugin used"
                      )
    parser.add_option("-v","--version",dest="version",default=False,action="store_false")
    
    parser.add_option("-d","--directory",dest="directory",default="")
    parser.add_option("-p","--port",dest="port")
    (options, args) = parser.parse_args()
    if options.version==True:
        print VERSION
        exit(1)
    if options.target_url=="www.testfire.com":
        print usage
    if not options.target_url=="www.testfire.com":
        try:
            load=load()
            plugin=load.get_plugin(options.directory,options.plugin_used)
            plugin.executeFun(options.target_url,options.port)
        except:
            pass
 
        
  
