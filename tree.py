from typing import Optional, Any

class TreeNode:
    def __init__(self,value: Any):
        self.value =value
        self.left:Optional['TreeNode']=None
        self.right:Optional['TreeNode']=None

    def __repr__ (self) -> str:
        return f"Node({self.value})"

if __name__== "__main__":
    root=TreeNode(10)
    root.left = TreeNode(5)
    root.right=TreeNode(15)

    print(f"Root:{root.value}")
    print(f"left child:{root.left.value}")
    print(f"right child:{root.right.value}")