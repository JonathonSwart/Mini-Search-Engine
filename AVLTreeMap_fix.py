
class AVLnode:

    def __init__(self, key = None, value=None):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.height = None

class AVLtree:

    def __init__(self):
        self.root = None

    def get(self, data):
        
        a = self.search(data, self.root)

        if a != None:

            return a.value
        
        return None

    def search(self, data, cur_node):
        if cur_node== None:
            return False

        elif data == cur_node.key:
            return cur_node
        
        if data < cur_node.key:
            return self.search(data, cur_node.left)
        else:
            return self.search(data, cur_node.right)
    
    def put(self, data, value = None):
        #print("Add-"+str(data)+'-'+str(value))
        data = AVLnode(data, value)
        y = None
        x = self.root

        while x != None:
            y = x
            if data.key < x.key:
                x = x.left
            else: 
                x = x.right
        
        data.parent = y 

        if y == None:
            self.root = data
        
        elif data.key < y.key:
            y.left = data
        else:
            y.right = data
        
        self.setHeight(data, data.key) 

    def setHeight(self, node,newInsert = None):
        newInsert = newInsert
        node.height = self._setHeight(node)

        if newInsert != None:
            self.unbalanceDetector(node, newInsert)

        if node.parent != None:
            self.setHeight(node.parent, newInsert)

    def _setHeight(self, node):
        
        if node == None:
            return 0
        left = self._setHeight(node.left)
        right = self._setHeight(node.right)
        return max(left, right) + 1

    def __setHeight(self, node):

        if node != None:
            node.height = self._setHeight(node)
            self.__setHeight(node.left)
            self.__setHeight(node.right)

    def unbalanceDetector(self, node, newInsert):

        root = node
        if root.left != None:
            leftH = root.left.height

        else:
            leftH = 0

        if root.right != None:
            rightH = root.right.height
        else:
            rightH = 0

        bHeight = leftH - rightH

        if bHeight < -1 or bHeight > 1:
            #print("the node %s is unblanced" %(node.key))
            #print("the new insert value %s" %(newInsert))
            self.directionDetector(node, bHeight, newInsert)

    
    def directionDetector(self, node, bfctor, newInsert):

        if bfctor > 1 and newInsert < node.left.key:
            #print("LL case")
            self.leftRoation(node)
          
        elif bfctor < -1 and newInsert > node.right.key:
            #print("RR case")
            self.rightRoation(node)
            
        elif bfctor > 1 and newInsert > node.left.key:
            #print("LR case")
            self.rightRoation(node.left)
            self.leftRoation(node)
            
        elif bfctor < -1 and newInsert < node.right.key:
            #print("RL case")
            self.leftRoation(node.right)
            self.rightRoation(node)
           
    
    def leftRoation(self, node):

        root = node
        pivot = node.left           #find the pivot in left side
     
        root.left = pivot.right     #move the right child of pivot to root
        #FIX2: add parent reset
        if pivot.right !=None:
            pivot.right.parent = root 
        pivot.right = root          #then pivot has right child root

        #reset their parent
        pivot.parent = root.parent  
        root.parent = pivot
        
        #if the pivot has parent
        if pivot.parent != None:

            #depends if pivot is in his parent left or right
            #according to the postion, insert pivot as child to his parent
            #FIX1: need to check if pivot.parent.left exists or not
            if pivot.parent.left !=None:
                if pivot.parent.left.key == root.key:
                    pivot.parent.left = pivot
                else:
                    pivot.parent.right = pivot
            else:
                pivot.parent.right = pivot
            
            #reset the height for parent above
            self.setHeight(pivot.parent)
        else:
            self.root = pivot

        #reset the height for pivot
        self.__setHeight(pivot)

    def rightRoation(self, node):

        root = node
        pivot = node.right

        root.right = pivot.left
        #FIX2: add parent reset
        if pivot.left !=None:
            pivot.left.parent = root 
        pivot.left = root

        pivot.parent = root.parent
        root.parent = pivot

        if pivot.parent != None:
            #FIXED: need to check if pivot.parent.left exists or not
            if pivot.parent.left !=None:
                if pivot.parent.left.key == root.key:
                    pivot.parent.left = pivot
                else:
                    pivot.parent.right = pivot
            else:
                pivot.parent.right = pivot

            self.setHeight(pivot.parent)
        else:
            self.root = pivot
        self.__setHeight(pivot)


    # Printing the tree
    def printTree(self):
        print("new tree:")
        self.__printTree(self.root)

    def __printTree(self, node, level=0):
        if node is None:
            return
        if node.value != None:
            self.__printTree(node.left, level + 1)
            print(' ' * 4 * level + '->', str(node.key)+","+str(node.value)+","+str(node.height))
            self.__printTree(node.right, level + 1)


# if __name__ == "__main__":
# #15-bob, 20-anna, 24-tom, 10-david, 13-david, 7-ben, 30-karen, 36-erin, 25-david.
#     T = AVLtree("lorem", 1)
#     T.printTree()
#     T.put("ipsum", 2)
#     T.printTree()
#     T.put("dolor", 3)
#     T.printTree()
#     T.put("sit", 4)
#     T.printTree()
#     T.put("amet", 5)
#     T.printTree()
#     T.put("consectetur", 6)
#     T.printTree()
#     T.put("adipiscing", 7)
#     T.printTree()
#     T.put("elit", 8)
#     T.printTree()
#     T.put("sed", 9)
#     T.printTree()
#     T.put("do", 10)
#     T.printTree()
#     T.put("eiusmod", 11)
#     T.printTree()
#     T.put("tempor", 12)
#     T.printTree()
#     T.put("incididunt", 13)
#     T.printTree()
#     T.put("ut", 14)
#     T.printTree()
#     T.put("labore", 15)
#     T.printTree()
#     T.put("et", 16)
#     T.printTree()
#     T.put("dolore", 17)
#     T.printTree()
#     T.put("magna", 18)
#     T.printTree()
#     T.put("aliqua", 19)
#     T.printTree()
#     T.put("enim", 20)
#     T.printTree()
#     T.put("ad", 21)
#     T.printTree()
#     T.put("minim", 22)
#     T.printTree()
#     T.put("veniam", 23)
#     T.printTree()
#     T.put("quis", 24)
#     T.printTree()
#     T.put("nostrud", 25)
#     T.printTree()
#     T.put("exercitation", 26)
#     T.printTree()
#     T.put("ullamco", 27)
#     T.printTree()
#     T.put("laboris", 28)
#     T.printTree()
#     T.put("nisi", 29)
#     T.printTree()
#     T.put("aliquip", 30)
#     T.printTree()
#     T.put("ex", 31)
#     T.printTree()
#     T.put("ea", 32)
#     T.printTree()
#     T.put("commodo", 33)
#     T.printTree()
#     T.put("consequat", 34)
#     T.printTree()
#     T.put("duis", 35)
#     T.printTree()
#     T.put("aute", 36)
#     T.printTree()
#     T.put("irure", 37)
#     T.printTree()
#     T.put("in", 38)
#     T.printTree()
#     T.put("reprehenderit", 39)
#     T.printTree()
#     T.put("voluptate", 40)
#     T.printTree()
#     T.put("velit", 41)
#     T.printTree()
#     T.put("esse", 42)
#     T.printTree()
#     T.put("cillum", 43)
#     T.printTree()
#     T.put("eu", 44)
#     T.printTree()
#     T.put("fugiat", 45)
#     T.printTree()
#     T.put("nulla", 46)
#     T.printTree()
#     T.put("pariatur", 47)
#     T.printTree()
#     T.put("excepteur", 48)
#     T.printTree()
#     T.put("sint", 49)
#     T.printTree()
#     T.put("occaecat", 50)
#     T.printTree()
#     T.put("cupidatat", 51)
#     T.printTree()
#     T.put("non", 52)
#     T.put("proident", 53)
#     T.put("sunt", 54)
#     T.put("culpa", 55)
#     T.put("qui", 56)
#     T.put("officia", 57)
#     T.put("deserunt", 58)
#     T.put("mollit", 59)
#     T.put("anim", 60)
#     T.put("id", 61)
#     T.put("est", 62)
#     T.put("laborum", 63)
#     T.printTree()
