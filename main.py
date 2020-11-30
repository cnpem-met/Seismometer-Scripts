"""
    @author: Leonardo Rossi Leão / Rodrigo de Oliveira Neto
    @create: november, 30, 2020
    @title: main
"""

# Libraries
import time
from rawFileMonitor import RawFileMonitor

# Start the software
file = open("start.txt", "r");
start = bool(file.read())
file.close()

if start == True:
    # Instantiates a monitoring object
    fileMonitor = RawFileMonitor()
    fileMonitor.start() # Start the file monitoring
    while start == True:
        time.sleep(60)
        file = open("start.txt", "r");
        start = bool(int(file.read()))
        file.close()

fileMonitor.stop()
