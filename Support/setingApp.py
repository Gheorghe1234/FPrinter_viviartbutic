import ConfigParser
import os

import cyrtranslit


class Seting:
    def __init__(self,filename ,path):
        self.setingFile = path
        if path == '':
            self.dir_seting = filename+'Setting'
        else:
            self.dir_seting = self.setingFile + '\\' + filename + 'Setting'

        self.setingLocation = self.dir_seting
        self.setingFile = '\\'+ filename +'.ini'
        try:
            os.makedirs(self.setingLocation)
        except:
            pass
        self.Config = ConfigParser.ConfigParser()
        self.Config.read(self.dir_seting + self.setingFile)
        self.text_seting = ''
        # self.db_pass = self.ConfigSectionMap("COMPortSeting")['comport']

    def createFilesetig(self):
        fileRead = os.access(self.setingLocation + self.setingFile, os.R_OK)
        if fileRead == False:
            f = open(self.setingLocation + self.setingFile, "w+")
            f.write(str(self.text_seting))
            f.close()
            print("Verificati fisierul cu setari '" + self.setingLocation + self.setingFile +"' apoi reporniti aplicatia")
            res = 1
        else:
            res = 0

        return res

    def ConfigSectionMap(self, section):
        dict1 = {}
        options = self.Config.options(section)
        for option in options:
            try:
                dict1[option] = self.Config.get(section, option)
                if dict1[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1

    def LANGRusToCyrilik(self, TextRUS):
        TextCyrylik = str(TextRUS).decode('cp1251')
        TextCyrylik = unicode(TextCyrylik).encode('utf-8')
        print(cyrtranslit.to_latin(TextCyrylik, 'ru'))

        return TextCyrylik