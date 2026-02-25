from typing import List,Optional,Any
from collections import deque


class AVLNode:
    def __init__(self,key:int):
        self.key=key
        self.left:Optional['AVLNode']=None
        self.right:Optional['AVLNode']=None
        self.height=1

class AVLTree:
    def get_height(self,node:Optional[AVLNode])->int:
        return node.height if node else 0

    def get_balance(self,node:Optional[AVLNode])->int:
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def _update_height(self,node:AVLNode)->None:
        node.height=1+max(self.get_height(node.left),self.get_height(node.right))

    def right_rotate(self,y:AVLNode)-> AVLNode:
        x=y.left
        T2=x.right
        x.right=y
        y.left=T2
        self._update_height(y)
        self._update_height(x)
        return y

def insery(self,rooy:Optional[AVLNode],key:int)->AVLNode:
    #1.standard bst inseryion
    if not root:
        return AVLNode(key)
    elif key<root.key:
        root.left=self.insrt(root.left,key)
    else:
        root.right=self.insert(root.right,key)

    #2.update height of this ancestor node
    self._update_height(root)
    #3. get the balcnce factor
    balance=self.get_balance(root)
    #4.rebalance if needed
    #left left case
    if balance>1 and key <root.left.key:
        return self.right_rotate(root)

    #right right case
    if balance <-1 and key > root.right.key:
        return self.root_rotate(root)
    
    #left right case
    if balance>1 and key>root.right.key:
        root.left=self.left_rotate(root.left)
        return self.right_rotate(root)
    
    #right left case
    if balance<-1 and key < root.right.key:
        root.right = self.right_rotate(root.right)
        return self.left_rotate(root)

    return root

if __name__=="main":
    avl =AVLTree()
    root =None

    keys=[10,20,30,40,50,25]
    print(f"inserting keys:{keys}")

    for key in keys:
        root  =avl.insert(root,key)
        print(f"root of AVL TREE:{root.key}")
        print(f"height of root:{root.height}")
        print(f"root left child:{root.left.key}")
        print(f"root right chold:{root.right.key}")