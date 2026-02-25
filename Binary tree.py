from typing import List,Optional,Any
from collections import deque


class BSTNode:
    def __init__(self,key:int):
        self.key=key
        self.left:Optional['BSTNode']=None
        self.right:Optional['BSTNode']=None


class BIinarySearchTree:
    def __init__(self):
        self.root:Optional[BSTNode]=None
        
    def insert(self, key:int)->None:
        self.root=self._insert_recursive(self.root,key)

    def _insert_recursive(self,node:Optional[BSTNode], key: int)->BSTNode:
        if not node:
            return BSTNode(key)
            
        if key<node.key:
            node.left =self._insert_recursive(node.left,key)
        elif key>node.key:
            node.right=self._insert_recursive(node.right,key)

        return node
    def search(self,key:int)->bool:
        return self._search_recursive(self.root,key)
        
    def _search_recursive(self,node:Optional[BSTNode],key: int)->bool:
        if not node:
            return False
        if key==node.key:
            return True
        return self._search_recursive(node.left,key) if key<node.key else self._search_recursive(node.right,key)
        
    def delete(self,key:int)->None:
        self.root=self._delete_recursive(self.root,key)
        
    def _delete_recursive(self,node:Optional[BSTNode],key:int)->Optional[BSTNode]:
        if not node:
            return None
        if key<node.key:
            node.left=self._delete_recursive(node.left,key)
        elif key>node.key:
            node.right=self._delete_recursive(node.right,key)
        else:
                #node found:Handle removal case
                # case a: Node withh only one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
                #case B:Node with two children
                #find inorder successor (smallest in the right subtree)
            temp=self._min_value_node(node.right)
                #copy the sucessor content to this node
            node.key=temp.key
                #delete the inorder sucessor
            node.right=self._delete_recursive(node.right,temp.key)
        return node
    def _min_value_node(self,node:BSTNode)->BSTNode:
        current=node
        while current.left:
            current =current.left
        return current


if __name__=="__main__":
    bst=BIinarySearchTree()
    elements =[50,30,20,40,70,60,80]
    print(f"Inserting elements:{elements}")
    for x in elements:
        bst.insert(x)
    print(f"Searching for 40:{bst.search(40)}")#expected:True
    print(f"Searching for 90:{bst.search(90)}")#expected false

    print("deleteing 20(leaf node)---")
    bst.delete(20)
    print(f"searching for 20:{bst.search(20)}")#expected false

    print("Deleting 30(node witg two childdren....)")
    bst.delete(30)
    print(f"Searching for 30:{bst.search(30)}")#expected false
    

