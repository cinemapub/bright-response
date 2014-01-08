import ConfigParser
import os

class IniParser(ConfigParser.SafeConfigParser):
    def __init__(self):
        ConfigParser.SafeConfigParser.__init__(self)
        #substitution pattern in the config file: ${section.parameter}
        self.subs_pattern = "\$\{[^\$\{\}]*\}"
        #local cache for the configuration parameters
        self.config_params_cache = {}
        #mechanism to detect circular dependancies
        self.dependancy_list = []         

    def read(self,file):
        if not os.path.exists(file):
            raise OSError(file + ' does not exist')
        return ConfigParser.SafeConfigParser.read(self,file)
 
    def get(self,section,option):
        """ strip enclosing double quotes """
 
        value = ConfigParser.SafeConfigParser.get(self,section,option)
        value=value.strip('"')
        return value

    def getGeo(self,section,option):
        """ strip enclosing double quotes, parse coordinates """
        value=ConfigParser.SafeConfigParser.get(self,section,option)
        value=value.strip('"')
        coord=value.split(",",2)
        # print(coord)
        ll={}
        ll["long"]=coord.pop()
        ll["lat"]=coord.pop()
        return ll

    def getList(self,section,option,sep=";"):
        """ strip enclosing double quotes, parse list """
        value=ConfigParser.SafeConfigParser.get(self,section,option)
        value=value.strip('"')
        vallist=value.split(sep)
        return vallist

    def isInRange(self,section,option,testval):
        """ strip enclosing double quotes, parse range """
        """ us to test if 15 is in range defined as e.g. "1-10,12,16-19" """
        value=ConfigParser.SafeConfigParser.get(self,section,option)
        value=value.strip('"')
        elems=value.split(",")
        inrange=False
        if elems:
            for elem in elems:
                if(elem.find("-")):
                    # it's a range
                    limits=elem.split("-",2)
                    notlower=limits.pop()
                    nothigher=limits.pop()
                    if(testval >= notlower and testval <= nothigher)
                        inrange=True
                else
                    # it's just 1 number
                    if(elem == testval):
                        inrange=True
        return inrange
