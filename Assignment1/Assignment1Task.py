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

        self.semaphore=threading.Semaphore(self.NUM_PRINTERS)
        self.binary=threading.Semaphore(1)

    def startSimulation(self):
        # Create Machine and Printer threads
        # Write code here
        for i in range(self.NUM_MACHINES):
            m=self.machineThread(i,self)
            self.mThreads.append(m)

            
        # Start all the threads
        # Write code here

        for i in range(self.NUM_PRINTERS):
            p=self.printerThread(i,self)
            self.pThreads.append(p)

        for m in self.mThreads:
            m.start()

        for p in self.pThreads:
            p.start()


        # Let the simulation run for some time
        time.sleep(self.SIMULATION_TIME)

        
        

        # Finish simulation
        self.sim_active = False

        # Wait until all printer threads finish by joining them
        # Write code here

        for p in self.pThreads:
            p.join()


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
                self.printDox(self.printerID)
                

        def printerSleep(self):
            sleepSeconds = random.randint(1, self.outer.MAX_PRINTER_SLEEP)
            time.sleep(sleepSeconds)

        def printDox(self, printerID):

            print(f"Printer ID: {printerID} : now available")

            self.outer.binary.acquire()
            # Print from the queue
            if self.outer.print_list.head is not None:

                self.outer.print_list.queuePrint(printerID)
                self.outer.semaphore.release()
            
            self.outer.binary.release()

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
                # Check if it is safe to send a request by acquiring semaphores
                self.isRequestSafe(self.machineID)
                # Both semaphores have been acquired, now send a print request
                self.printRequest(self.machineID)
                # Release the binary semaphore after inserting the print request
                self.postRequest(self.machineID)
              

        def machineSleep(self):
            sleepSeconds = random.randint(1, self.outer.MAX_MACHINE_SLEEP)
            time.sleep(sleepSeconds)

          # Write code here for Acquiring the Counting Semaphore
        def isRequestSafe(self, id):
            print(f"Machine {id} Checking availability")
            # Acquire counting semaphore (wait for an available printer)
            self.outer.semaphore.acquire()
            # Acquire binary semaphore for mutual exclusion of the print queue
            self.outer.binary.acquire()
            
            # Both semaphores acquired
            print(f"Machine {id} will proceed")
        
        def printRequest(self, id):
            print(f"Machine {id} Sent a print request")
            # Build a print document
            doc = printDoc(f"My name is machine {id}", id)
            # Insert it in the print queue
            self.outer.print_list.queueInsert(doc)

        # Write code here for postRequest, i.e., after inserting the print request
        def postRequest(self, id):
            print(f"Machine {id} Releasing binary semaphore")
            # Release the binary semaphore
            self.outer.binary.release()

        