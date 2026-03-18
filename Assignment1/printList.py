class printList:

    class Node:
        # Constructor
        def __init__(self, doc):
            self.document = doc
            self.next = None

    def __init__(self):
        self.head = None # Head of list

    # Insert a print request in the queue
    def queueInsert(self, doc):
        new_node = printList.Node(doc)
        # if the queue is empty, start a queue
        if self.head is None:
            self.head = new_node
            print(f"Inserted a request in the queue from {new_node.document.getSender()}")
            print("Number of requests in the queue 1")
        else:
            # Maintain a queue of 5 print requests.
            # If more than 5 requests are sent add the latest one in the queue but remove
            # the head of the list

            # Traverse the list
            last = self.head
            count = 1
            while last.next is not None:
                last = last.next
                count += 1

            # Insert the new_node at the last node
            last.next = new_node
            count += 1
            print(f"Inserted a request in the queue from {new_node.document.getSender()}")
            # If there are more than 5 nodes in the queue, move the head one node down
            if count > 5:
                self.head = self.head.next
                print("!!!!!!Attention: Overwrite!!!!!!")
                count -= 1
            print(f"Number of requests in the queue {count}")
        return self

    # Method to print the head of the list
    def queuePrint(self, printerID):
        # Only print if there is a node in the list
        if self.head is not None:
            currNode = self.head
            print(":::::")
            print(f"Printer {printerID} Printing the request from Machine ID: {currNode.document.getSender()} {currNode.document.getStr()}")
            print(":::::")
            # Once printed, remove the node from the queue
            self.head = self.head.next

    # Print the contents of the entire list ---for debugging ---
    # Doesn't remove any nodes from the list
    def queuePrintAll(self):
        currNode = self.head

        print("LinkedList:", end=" ")

        # Traverse through the LinkedList
        while currNode is not None:
            # Print the data at current node
            print(currNode.document.getStr(), end=" ")

            # Go to next node
            currNode = currNode.next
        print()