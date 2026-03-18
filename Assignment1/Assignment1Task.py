import threading
import time
import random

from printDoc import printDoc
from printList import printList

class Assignment1:
    # Simulation Initialisation parameters
    NUM_MACHINES = 50        # Number of machines that issue print requests
    NUM_PRINTERS = 5         # Number of printers in the system
    SIMULATION_TIME = 30     # Total simulation time in seconds
    MAX_PRINTER_SLEEP = 3    # Maximum sleep time for printers
    MAX_MACHINE_SLEEP = 5    # Maximum sleep time for machines

    # Initialise simulation variables
    def __init__(self):
        self.sim_active = True
        self.print_list = printList()  # Create an empty list of print requests
        self.mThreads = []             # list for machine threads
        self.pThreads = []             # list for printer threads

    def startSimulation(self):
        # Create Machine and Printer threads
        # Write code here
            
        # Start all the threads
        # Write code here

        # Let the simulation run for some time
        time.sleep(self.SIMULATION_TIME)

        # Finish simulation
        self.sim_active = False

        # Wait until all printer threads finish by joining them
        # Write code here

    # Printer class
    class printerThread(threading.Thread):
        def __init__(self, printerID, outer):
            threading.Thread.__init__(self)
            self.printerID = printerID
            self.outer = outer  # Reference to the Assignment1 instance

        def run(self):
            while self.outer.sim_active:
                # Simulate printer taking some time to print the document
                self.printerSleep()
                # Grab the request at the head of the queue and print it
                # Write code here

        def printerSleep(self):
            sleepSeconds = random.randint(1, self.outer.MAX_PRINTER_SLEEP)
            time.sleep(sleepSeconds)

        def printDox(self, printerID):
            print(f"Printer ID: {printerID} : now available")
            # Print from the queue
            self.outer.print_list.queuePrint(printerID)

    # Machine class
    class machineThread(threading.Thread):
        def __init__(self, machineID, outer):
            threading.Thread.__init__(self)
            self.machineID = machineID
            self.outer = outer  # Reference to the Assignment1 instance

        def run(self):
            while self.outer.sim_active:
                # Machine sleeps for a random amount of time
                self.machineSleep()
                # Machine wakes up and sends a print request
                # Write code here

        def machineSleep(self):
            sleepSeconds = random.randint(1, self.outer.MAX_MACHINE_SLEEP)
            time.sleep(sleepSeconds)

        def printRequest(self, id):
            print(f"Machine {id} Sent a print request")
            # Build a print document
            doc = printDoc(f"My name is machine {id}", id)
            # Insert it in the print queue
            self.outer.print_list.queueInsert(doc)