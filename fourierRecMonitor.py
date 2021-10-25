"""
    @author: Leonardo Rossi Leão / Rodrigo de Oliveira Neto
    @create: november, 24, 2020
    @title: Recquisition Monitor
"""

# Libraries
import os
import time
import json
import requests
import threading
import numpy as np
from datetime import datetime
from scipy.fftpack import fft

# Restricoes para identificacao de um novo arquivo
# 1. xxxxxxx_00000000: Arquivo em processamento

class FourierRecMonitor(threading.Thread):
    
    def __init__(self):
        super(FourierRecMonitor, self).__init__()
        self.kill = threading.Event()
        self.path_in = "/home/reftek/bin/archive/FourierRec/request.txt"
        
    def getDateTime(self):
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")
        
    def recordAction(self, text):
        monitor = open("monitor.txt", "a")
        monitor.write(text + "\n")
        monitor.close()        
        
    def recordFourierData(self, iniTime, endTime, seismicData, canal):
        path = ("/home/reftek/bin/archive/FourierRec/%s;%s;%s" % (canal, iniTime, endTime))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        print("FOI")
        with open(path+".txt", "a") as file:
            file.write(seismicData)
        os.rename("%s.txt" % path, "%s-complete.txt" % path)
        file.close()
        
    def fourierTransform(self, iniTime, endTime, seismicData, sampleRate, canal):
        fourierData = str(sampleRate) + "\n"
        nsamp = len(seismicData)
        nyquist = int(np.ceil(nsamp/2))
        mags = abs(fft(seismicData))
        for i in range(1, nyquist):
            fourierData += "%.10f\n" % mags[i]
        self.recordFourierData(iniTime, endTime, fourierData, canal)
        
    def run(self):
        self.recordAction("[%s] Action: start recquisition monitor" % self.getDateTime())
        while not self.kill.is_set():
            if os.path.getsize(self.path_in) != 0:
                file = open(self.path_in, "r")
                data = file.read().split(";")
                file.close()
                file = open(self.path_in, "w")
                file.close()
                for i in range(int(len(data)/3)):
                    r = requests.get('http://localhost:3001/SeismicData/%s/%s/%s' % (data[0], data[1], data[2]))
                    y = json.loads(r.text)
                    self.fourierTransform(data[1], data[2], y["magnitude"], 100, data[0])
                time.sleep(0.5)
            
if __name__ == "__main__":
    fftMonitor = FourierRecMonitor()
    fftMonitor.start()