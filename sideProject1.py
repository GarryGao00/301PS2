import RBtree as rbt
import numpy as np
import random
import matplotlib.pyplot as plt
import copy
import time

numSong = 1000
numOneDay = 50
numSample = 3000
maxDay = 15*numSong//numOneDay

#create the whole tree
tic = time.perf_counter()
nodes = {}
T = rbt.RedBlackTree()
for i in range(numSong):
    nodes["Node"+str(i)] = rbt.RedBlackNode(i)
    T.insert(nodes["Node"+str(i)])

OriginalT = copy.deepcopy(T)
print("Initial tree completed")
toc = time.perf_counter()
print(f"Init in {toc - tic:0.4f} seconds")

#remove the songs from minimum days
for _ in range(numSong//numOneDay):
    randList = random.sample(range(numSong), numOneDay)
    for i in randList:
        T.deleteKey(i)

#count days
numDay = 0
#print("boolean: ", T.root.key != "NIL")
while T.root.key != "NIL":
    randList = random.sample(range(numSong), numOneDay)
    for i in randList:
        T.deleteKey(i)
    numDay += 1
    if numDay > 50:
        break

print("Test 1: numDay = ", numDay, "\n")


#start sample
T = copy.deepcopy(OriginalT)
result = np.zeros(maxDay+2)
for i in range(numSample):
    T = copy.deepcopy(OriginalT)
    numDay = 0
    while T.root.key != "NIL":
        randList = random.sample(range(numSong), numOneDay)
        for i in randList:
            T.deleteKey(i)
        numDay += 1
        if numDay > maxDay:
            break
    
    #print("numDay = ", numDay)
    result[numDay] += 1

print("Test2: result = ", result, "numSample:", numSample, "num in result:", sum(result))
plt.plot(range(maxDay+2), result)
plt.show()
print("Graph ploted")
