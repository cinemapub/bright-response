from mod_config import IniParser
import os.path

def printparam(section,key):
	""" strip enclosing double quotes """
	if(key.find("geo") > -1):
		print("%25s = %s" % (key,Config.getGeo(section,key)))
		return True
	val=Config.get(section,key)
	print("%25s = %s" % (key,val))
	return True

Config = IniParser()
cfile="../config/config.ini"
cexist=os.path.exists(cfile)
print ("%s exists: %r" % (os.path.realpath(cfile),cexist))
Config.read(cfile)
sections=Config.sections()
for section in sections:
    print("\n%17s SECTION : %s ===" % ("==========",section))
    keys=Config.options(section)
    for key in keys:
    	printparam(section,key)
        


