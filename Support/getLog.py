import os

from datetime import *

class Log:

    def __init__(self, filename, path):
        date_now = datetime.now().strftime("%Y%m%d")
        self.filename = path + '\\' + date_now + '_Scale' + filename + '.log'
        try:
            os.makedirs(path)
        except:
            pass

    def Info(self, text):
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f = open(self.filename, "a")
        # with open(self.filename, 'r') as contents:
        #     save = contents.read()
        # with open(self.filename, 'w') as contents:
        #     contents.write(date_now + ': INFO -     ' +str(text) + '\n')
        # with open(self.filename, 'a') as contents:
        #     contents.write(save)
        f.write(date_now + ': INFO -     ' +str(text) + '\n')
        f.close()

    # def Info(self, text):
    #     date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     f = open(self.filename, "a")
    #     with open(self.filename, 'r') as contents:
    #         save = contents.read()
    #     with open(self.filename, 'w') as contents:
    #         contents.write(date_now + ': INFO -     ' +str(text) + '\n')
    #     with open(self.filename, 'a') as contents:
    #         contents.write(save)
    #     f.close()

    def Error(self, text):
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f = open(self.filename, "a")
        # with open(self.filename, 'r') as contents:
        #     save = contents.read()
        # with open(self.filename, 'w') as contents:
        #     contents.write(date_now + ': ERROR -     ' +str(text) + '\n')
        # with open(self.filename, 'a') as contents:
        #     contents.write(save)
        f.write(date_now + ': ERROR -     ' +str(text) + '\n')
        f.close()

    def Start(self, text):
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f = open(self.filename, "a")
        f.write(date_now + ': START - ' + str(text) + '\n')
        f.close()

    def End(self, text):
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f = open(self.filename, "a")
        # with open(self.filename, 'r') as contents:
        #     save = contents.read()
        # with open(self.filename, 'w') as contents:
        #     contents.write(date_now + ': START - ' +str(text) + '\n\n')
        # with open(self.filename, 'a') as contents:
        #     contents.write(save)
        f.write(date_now + ': END - ' + str(text) + '\n\n')
        f.close()

    def Text_Tab(self, text):
        f = open(self.filename, "a")

        f.write('\t\t\t\t\t\t' +str(text) + '\n')

        f.close()

    def Empy_Line(self):
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f = open(self.filename, "a")
        # with open(self.filename, 'r') as contents:
        #     save = contents.read()
        # with open(self.filename, 'w') as contents:
        #     contents.write('\n')
        # with open(self.filename, 'a') as contents:
        #     contents.write(save)
        f.write('\n')
        f.close()
