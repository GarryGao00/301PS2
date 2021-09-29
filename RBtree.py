import math
import numpy as np

#tree block
class RedBlackNode:
    def __init__(self, val, p=None, left=None, right=None, c=False):
        # key should only contain integers
        self.key = val
        # p is parent
        self.p = p
        # left child
        self.left = left
        # right child 
        self.right = right
        # c = T is red, c = F is black
        self.c = c
        
class RedBlackTree:
    def __init__(self):
        self.nil = RedBlackNode("NIL")
        # root
        self.root = self.nil
    
    def leftRotate(self, x):
        y=x.right
        x.right=y.left
        if y.left != self.nil:
            y.left.p = x
        
        y.p=x.p
        if x.p == self.nil:
            self.root = y
        elif x==x.p.left:
            x.p.left=y
        else:
            x.p.right=y
            
        y.left=x
        x.p=y
        #print("leftR, root now is: ", self.root.key)
        return
    
    def rightRotate(self, y):
        x=y.left
        y.left=x.right
        if x.right != self.nil:
            x.right.p = y
        
        x.p=y.p
        if y.p == self.nil:
            self.root = x
        elif y==y.p.right:
            y.p.right=x
        else:
            y.p.left=x
            
        x.right=y
        y.p=x
        #print("rightR, root now is: ", self.root.key)
        return
    
    def insert(self, z):
        y=self.nil
        x=self.root
        while x != self.nil:
            y=x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
                
        z.p = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
            
        z.left = self.nil
        z.right = self.nil
        z.c = True
            
        self.insertFixup(z)
        return
    
    def insertFixup(self, z):
        while z != self.root and z.p.c:
            if z.p == z.p.p.left:
                #uncle
                y=z.p.p.right
                if y.c:
                    z.p.c = False
                    y.c = False
                    z.p.p.c = True
                    z=z.p.p
                else:
                    if z==z.p.right:
                        z=z.p
                        self.leftRotate(z)
                    z.p.c = False
                    z.p.p.c = True
                    self.rightRotate(z.p.p)
            else:
                #uncle
                y=z.p.p.left
                if y.c:
                    z.p.c = False
                    y.c = False
                    z.p.p.c = True
                    z=z.p.p
                else:
                    if z==z.p.left:
                        z=z.p
                        self.rightRotate(z)
                    z.p.c = False
                    z.p.p.c = True
                    self.leftRotate(z.p.p)
            
        self.root.c = False
        #print("insertF, root now is: ", self.root.key)
        return
    
    def transplant(self, u, v):
        if u.p == self.nil:
            self.root = v
        elif u==u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        
        v.p = u.p 
        return
                
        
    def treeMinimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x
    
    def delete(self, z):
        y = z
        yoc = y.c
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x=z.left
            self.transplant(z, z.left)
        else: 
            y=self.treeMinimum(z.right)
            yoc = y.c
            x = y.right
            if y.p==z:
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.c = z.c
        if not yoc:
            print("x type", type(x), "x.c", x.c)
            self.deleteFixup(x)
            print("delete&fixup done")
            
        return
    
    def deleteFixup(self, x):
        print("inside deletefixup", type(x))
        
        while (x != self.root) and (not x.c):
            if x == x.p.left:
                print("1st branch")
                w = x.p.right
                if w.c:
                    w.c = False
                    x.p.c = True
                    self.leftRotate(x.p)
                    w = x.p.right
                if not w.left.c and not w.right.c:
                    w.c = True
                    x = x.p
                else:
                    if not w.right.c:
                        w.left.c = False
                        w.c = True
                        self.rightRotate(w)
                        w = x.p.right
                    
                    w.c = x.p.c
                    x.p.c = False
                    w.right.c = False
                    self.leftRotate(x.p)
                    x = self.root
            else:
                print("2nd branch")
                w = x.p.left
                if w.c:
                    w.c = False
                    x.p.c = True
                    self.rightRotate(x.p)
                    w = x.p.left
                if not w.right.c and not w.left.c:
                    w.c = True
                    x = x.p
                else:
                    if not w.left.c:
                        w.right.c = False
                        w.c = True
                        self.leftRotate(w)
                        w = x.p.left
                    
                    w.c = x.p.c
                    x.p.c = False
                    w.left.c = False
                    self.rightRotate(x.p)
                    x = self.root

        x.c = False
        return

def print_tree1(node, level=0):
    if node.key != "NIL":
        print_tree1(node.left, level + 1)
        print('-' * 4 * level + '> ' +
                     str(node.key) + ' ' + ('r' if node.c else 'b'))
        print_tree1(node.right, level + 1)
        
    return