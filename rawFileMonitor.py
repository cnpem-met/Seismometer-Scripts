"""
    @author: Leonardo Rossi Leão / Rodrigo de Oliveira Neto
    @create: november, 24, 2020
    @title: File monitor
"""

# Libraries
import os
import time
import threading
from datetime import datetime
from datFileMonitor import DatFileMonitor

# Restricoes para identificacao de um novo arquivo
# 1. xxxxxxx_00000000: Arquivo em processamento

class RawFileMonitor(threading.Thread):
    
    def __init__(self):
        super(RawFileMonitor, self).__init__()
        self.kill = threading.Event()
        self.path_in = "/home/reftek/bin/archive"
        self.path_cvt = self.path_in + "/pas2asc"
        self.datFileMonitor = DatFileMonitor()
        
    def getDateTime(self):
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")
        
    def recordAction(self, text):
        monitor = open("monitor.txt", "a")
        monitor.write(text + "\n")
        monitor.close()        
        
    def searchFiles(self):
        today = datetime.now()
        year = today.year
        dayOfYear = (today - datetime(year, 1, 1)).days + 1
        path = "%s/%d%d/B67D/1/" % (self.path_in, year, dayOfYear)
        arquivos = set(os.listdir(path))
        return (path, arquivos)
    
    def conversao(self, path, newFiles):
        for file in newFiles:
            path_in = path + file
            if "_00000000" not in path_in:
                os.system(self.path_cvt + " -Ln " + path_in)
                os.remove(path_in)
                self.recordAction("[%s] Action: raw file converted to dat" % self.getDateTime())
                self.datFileMonitor.run()
        
    def run(self):
        self.recordAction("[%s] Action: start raw file monitor" % self.getDateTime())
        path, content = self.searchFiles()
        while not self.kill.is_set():
            path, newContent = self.searchFiles()
            newFiles = newContent.difference(content)
            # Caso identificado um novo arquivo na pasta, realiza a conversao
            if newFiles:
                self.recordAction("[%s] Action: new raw file founded" % self.getDateTime())
                self.conversao(path, newFiles)
            content = newContent
            time.sleep(0.5)