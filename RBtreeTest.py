import RBtree as rbt
import numpy as np
import random

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
#delete test completed
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

    T.delete(nodes["Node0"])
    print("one node removed, value =", nodes["Node0"].key)
    rbt.print_tree1(T.root)
    T.delete(nodes["Node3"])
    print("one node removed, value =", nodes["Node3"].key)
    rbt.print_tree1(T.root)
    T.delete(nodes["Node1"])
    print("one node removed, value =", nodes["Node1"].key)
    rbt.print_tree1(T.root)

#search test block
#search test completed
search = 1
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
