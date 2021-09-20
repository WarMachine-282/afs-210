# binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# function to convert sorted array to a
# balanced BST
# input : sorted array of integers
# output: root node of balanced BST
def array_to_bst(nums):
    if not nums:
        return None
    mid_val = len(nums)//2
    node = TreeNode(nums[mid_val])
    node.left = array_to_bst(nums[:mid_val])
    node.right = array_to_bst(nums[mid_val+1:])
    return node
# A utility function to print the preorder
# traversal of the BST
def preOrder(node): 
    if not node: 
        return      
    print(node.val)
    preOrder(node.left) 
    preOrder(node.right)   
# driver program to test above function
result = array_to_bst([1, 2, 3, 4, 5, 6, 7])
preOrder(result)