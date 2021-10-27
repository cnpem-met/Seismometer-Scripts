"""
    @author: Leonardo Rossi Leão / Rodrigo de Oliveira Neto
    @create: november, 24, 2020
    @title: Convert Data
"""

# Libraries
import os
from datetime import datetime
from processDatFile import ProcessDatFile as pdf    

class DatFileMonitor():
    
    def __init__(self):
        super(DatFileMonitor, self).__init__()
        self.path_in = "/home/reftek/Seismometer-Scripts/"
        
    def getDateTime(self):
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")
        
    def recordAction(self, text):
        monitor = open("monitor.txt", "a")
        monitor.write(text + "\n")
        monitor.close()    
        
    def searchFiles(self):
        arquivos = set(os.listdir(self.path_in))
        return arquivos
                
    def run(self):
        content = self.searchFiles()
        for filename in content:
            if ".atr" in filename:
                file = open(self.path_in + filename, "r")
                data = file.read()
                file.close()
                pdf.processFile(data, filename[-5])
                os.remove(self.path_in + filename)
                self.recordAction("[%s] Action: Channel %s | dat file treatment concluded" % (self.getDateTime(), filename[-5]))
        