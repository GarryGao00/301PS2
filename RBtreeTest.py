import RBtree as rbt
import numpy as np
import random

def checkChild(node):
    return (node.left.c == False and node.right.c == False)
        
def prop4helper(node):
    if node.key == "NIL":
        return True
    if node.c == True:
        rst = checkChild(node)
        if not rst:
            return False
        
    x = prop4helper(node.left)
    y = prop4helper(node.right)
    return (x and y)

def prop4(T):
    rst = prop4helper(T.root)
    if rst:
        print("Property 4 holds")
    else: 
        print("Property 4 does not hold")

    return

#insertion test block
#insertion test completed
insert = 0
if insert:
    print("insert test block start")
    T = rbt.RedBlackTree()
    numNode = 10
    nodes = {}

    for i in range(numNode):
        numRand = random.randrange(1, 100)
        nodes["Node"+str(i)] = rbt.RedBlackNode(numRand)
        T.insert(nodes["Node"+str(i)])
        print(i+1, " elements added, value =", numRand)

    rbt.print_tree1(T.root)

#delete test block
#delete test incomplete
#case needed: delete same node twice
#case needed: delete from empty tree
#case needed: delete non-existent node
delete = 0
if delete: 
    print("delete test block start:")
    testblock = [10, 80, 92, 42, 28, 26, 73, 45, 41, 97]
    T = rbt.RedBlackTree()
    numNode = 10
    nodes = {}

    for i in range(numNode):
        nodes["Node"+str(i)] = rbt.RedBlackNode(testblock[i])
        T.insert(nodes["Node"+str(i)])
        #print(i+1, " elements added, value =", testblock[i])

    rbt.print_tree1(T.root)

    # T.delete(nodes["Node0"])
    # rbt.print_tree1(T.root)
    # T.delete(nodes["Node3"])
    # rbt.print_tree1(T.root)
    # T.delete(nodes["Node3"])
    # rbt.print_tree1(T.root)

    for i in range(15):
        T.delete(T.root)
        rbt.print_tree1(T.root)
        print("")

    print("delete non-existent node")
    T.delete(nodes["Node3"])
    rbt.print_tree1(T.root)

    
    

#search test block
#search test completed

# search test block start:
# Tree init done
# True
# False
# True
# False
# False
# False

search = 0
if search:
    print("search test block start:")
    testblock = [10, 80, 92, 42, 28, 26, 73, 45, 41, 97]
    T = rbt.RedBlackTree()
    numNode = len(testblock)
    nodes = {}

    for i in range(numNode):
        nodes["Node"+str(i)] = rbt.RedBlackNode(testblock[i])
        T.insert(nodes["Node"+str(i)])
        #print(i+1, " elements added, value =", testblock[i])

    print("Tree init done")

    print(T.searchKey(10))
    print(T.searchKey(11))
    print(T.searchKey(45))
    print(T.searchKey(46))
    T.delete(nodes["Node7"])
    T.delete(nodes["Node0"])
    print(T.searchKey(10))
    print(T.searchKey(45))

#prop4 test block
#prop4 test incomplete

prop4test = 1
if prop4test:
    print("prop4 test block start:")
    testblock = [10, 80, 92, 42, 28, 26, 73, 45, 41, 97]
    T = rbt.RedBlackTree()
    numNode = len(testblock)
    nodes = {}

    for i in range(numNode):
        nodes["Node"+str(i)] = rbt.RedBlackNode(testblock[i])
        T.insert(nodes["Node"+str(i)])
        #print(i+1, " elements added, value =", testblock[i])

    print("Tree init done")
    prop4(T)
