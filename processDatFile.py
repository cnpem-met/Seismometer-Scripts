import os
import datetime
import numpy as np
from scipy.fftpack import fft

class ProcessDatFile:
    
    @staticmethod
    def getValue(data):
        option, value = tuple(data.replace(" ", "").split("="))
        return value
    
    @staticmethod
    def processDate(fileDate):
        fileDate = ProcessDatFile.getValue(fileDate)
        year, dayOfYear, hour, minutes, seconds, ms = tuple(fileDate.replace(".", ":").split(":"))
        dt = datetime.date(int(year), 1, 1) + datetime.timedelta(int(dayOfYear) - 1)
        print(int(ms)*100)
        return datetime.datetime(dt.year, dt.month, dt.day, int(hour), int(minutes), int(seconds), int(ms)*100)
    
    @staticmethod
    def convertCounts(counts, bitWeight):
        volts = counts * bitWeight
        # Transduction factor: 800 V/(m/s) 
        speed = volts / 800
        return speed

    # Record the actions in monitor.txt
    @staticmethod
    def recordData(datetime, seismicData, canal):
        path = ("/home/reftek/bin/archive/SeismicData/%s/%s/"+ canal + "/%s") % ProcessDatFile.howToRecord(datetime)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "a") as file:
            file.write(seismicData)
        file.close()
        
    @staticmethod
    def recordFourierData(datetime, seismicData, canal):
        path = ("/home/reftek/bin/archive/FourierData/%s/%s/"+ canal+ "/%s") % ProcessDatFile.howToRecord(datetime)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "a") as file:
            file.write(seismicData)
        file.close()
    
    @staticmethod
    def howToRecord(date):
        year = date.year
        dayOfYear = (date - datetime.datetime(year, 1, 1)).days + 1
        hour = date.hour
        return (year, dayOfYear, str(hour)+".txt")
    
    @staticmethod
    def processFile(data, canal):
        seismicData = ""
        aSeismicData = []
        data = data.replace("$", "").split("\n")
        sampleRate = float(ProcessDatFile.getValue(data[3]))
        initialDate = ProcessDatFile.processDate(data[4])
        date = ProcessDatFile.processDate(data[4])
        bitWeight = float(ProcessDatFile.getValue(data[6]))
        # Seismic Data
        for counts in data[10:(len(data)-1)]:
            value = ProcessDatFile.convertCounts(float(counts), bitWeight)
            aSeismicData.append(value)
            seismicData += str(datetime.datetime.timestamp(date)) + ": %.60f" % value + "\n"
            date = date + datetime.timedelta(milliseconds=(1000/sampleRate))
        ProcessDatFile.recordData(initialDate, seismicData, canal)