import ConfigParser

print "START"
Config = ConfigParser.ConfigParser()
Config.read("../config/config.ini")
sections=Config.sections()
for section in sections:
    print("\n%17s SECTION : %s ===" % ("==========",section))
    keys=Config.options(section)
    for key in keys:
        val=Config.get(section,key)
        print("%25s = %s" % (key,val.strip('"')))
        
