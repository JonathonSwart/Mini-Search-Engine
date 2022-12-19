import os
import WebPageIndex

# Returns a list of all documents in a path
def readFiles(path):
    files = os.listdir(path)
    indexes = []

    for file in files:
        webpage = WebPageIndex.WebPageIndex("data/"+file)
        indexes.append(webpage)
    
    return indexes

# Main function
def main():
    webpages = readFiles("data")

    filename = "queries (1).txt"
    inFile = open(filename, "r")
    # Get all the queries and store them in an array
    lines = inFile.readlines()
    queries = []
    for line in lines:
        line = line.replace("\n", "")
        queries.append(line)

    # Iterate through all the queries and print relevant matches
    i = 0
    queue = WebPageIndex.WebpagePriorityQueue(queries[i], webpages)
    while i < len(queries):
        print ()
        matches = eval(input("Enter amount of matches you would like returned: "))
        print ("All relevant matches:")
        if matches <= 9:
            counter = 0
            # Print all relevant matches
            for x in range(0, 9):
                # Check if priority isn't 0 so that no irrelevent
                # matches are printed and that counter isn't equal to 
                # matches so that the printed amount stays to the specified
                # amount 
                if queue.peek().priority != 0 and counter != matches:
                    print (queue.poll().data.path.replace("data/", ""))
                    counter += 1
        
        else:
            # Print all relevant matches
            for x in range(0, 9):
                # Check if priority isn't 0 so that no irrelevent
                # matches are printed
                if queue.peek().priority != 0:
                    print(queue.poll().data.path.replace("data/", ""))

        i += 1
        if i < len(queries):
            queue.reheap(queries[i])

    
    inFile.close()
    

if __name__ == '__main__':
    main()
