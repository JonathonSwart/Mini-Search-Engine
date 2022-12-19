import AVLTreeMap_fix

# Creates an AVL tree holding each word in an AVL tree
class WebPageIndex:
    # Initialze WebPageIndex
    def __init__(self, file):        
        self.path = file

        self.WebPage = AVLTreeMap_fix.AVLtree()
        # Open document in "read" state
        inFile = open(file, "r")
        text = inFile.read().lower()
        # Cleaning the string
        text = text.replace(",", "")
        text = text.replace(".", "")
        text = text.replace("(", " ")
        text = text.replace(")", " ")
        text = text.replace("?", "")
        text = text.replace("/", " ")
        text = text.replace(":", "")
        text = text.replace(";", "")
        # Putting the words and positions in the AVL Tree
        text = text.split()
        appended_words = []
        for word in text:
            arr = []
            # Check if word is in appened_words so that there are no
            # duplicates in teh AVL tree
            if word not in appended_words:
                for i in range(0, len(text)):
                    if word == text[i]:
                        arr.append(i)
                self.WebPage.put(word, arr)
            appended_words.append(word)
        inFile.close()

    # Returns the count of a specified word
    def getCount(self, word):
        root = self.WebPage.root
        data = self.WebPage.search(word, root)
        if data != False:
            return len(data.value)
        else:
            return 0

# Node class to insert into WebPagePriorityQueue
class PriorityQueueNode:
    # Initialize node 
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data

# Maxheap priority queue class
class WebpagePriorityQueue:
    # Initialize maxheap priority queue
    def __init__(self, query, webpages):
        self.queue = []
        self.query = query
        self.webpages = webpages
        
        # Create and organize the maxheap priority queue
        query = query.split()
        for webpage in self.webpages:
            priority = 0
            # Find priority for each webpage and create a node
            for word in query:
                priority += webpage.getCount(word)

            node = PriorityQueueNode(priority, webpage)
            self.queue.append(node)
            # Get child and parent indexes
            child = len(self.queue) - 1
            parent = int((child - 1)/2)
            # Check if child node has greater priority than parent node
            while self.queue[child].priority > self.queue[parent].priority:
                # Swap child and parent nodes
                child_node = self.queue[child]
                self.queue[child] = self.queue[parent]
                self.queue[parent] = child_node
            
                child = parent
                parent = int((child-1)/2)

    # Returns the highest priority node
    def peek(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[0]

    # Returns and removes the highest priority node
    def poll(self):
        # Check the length of the queue to determine which steps to take 
        if len(self.queue) == 0:
            return None

        elif len(self.queue) == 1 or len(self.queue) == 2:
            rtn = self.queue[0]
            self.queue.remove(self.queue[0])
            return rtn

        else:
            # Remove the highest priority node and set the smallest
            #priority node to the top(first) position
            rtn = self.queue[0]
            x = self.queue[-1]
            self.queue.remove(self.queue[-1])
            self.queue[0] = x

            # Get the indexes of the parent, left child, and right child
            i = 0
            parent = self.queue[i]
            child1 = self.queue[i*2 + 1]
            child2 = self.queue[i*2 + 2]

            # Iterate through the maxheap and fixes all the positions
            while parent.priority < child1.priority or parent.priority < child2.priority:
                # Swaps the greater priority child node with the parent node
                if child1.priority > child2.priority:
                    greater_child = child1
                    self.queue[i*2 + 1] = parent

                else:
                    greater_child = child2
                    self.queue[i*2 + 2] = parent               

                self.queue[i] = greater_child

                i = self.queue.index(parent)
                # Special cases so that the index doesn't go out of
                #range
                if (i*2 + 2) < len(self.queue):
                    child1 = self.queue[i*2 + 1]
                    child2 = self.queue[i*2 + 2]
                elif (i*2 + 1) < len(self.queue):
                    child1 = self.queue[i*2 + 1]
                    child2 = PriorityQueueNode(0, "")
                else:

                    break

            return rtn

    # Reorganize the maxheap for a new query
    def reheap(self, query):
        self.queue = []
        self.query = query

        # Create and organize the maxheap priority queue
        query = query.split()
        for webpage in self.webpages:
            priority = 0
            # Find priority for each webpage and create a node
            for word in query:
                priority += webpage.getCount(word)

            node = PriorityQueueNode(priority, webpage)
            self.queue.append(node)
            
            # Get child and parent indexes
            child = len(self.queue) - 1
            parent = int((child - 1)/2)
            #Check if child node has greater priority than parent node
            while self.queue[child].priority > self.queue[parent].priority:
                #Swap child and parent nodes
                child_node = self.queue[child]
                self.queue[child] = self.queue[parent]
                self.queue[parent] = child_node
            
                child = parent
                parent = int((child-1)/2)





