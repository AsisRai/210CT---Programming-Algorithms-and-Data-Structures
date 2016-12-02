"""Implement the TREE_SORT algorithm in a language of your choice, based on the template provided on
Moodle, but make sure that the INORDER function is implemented iteratively, rather than recursively.

"""


#make sure that the INORDER function is implemented iteratively, rather than recursively.

import sys

class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
 
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
 
 
def INORDER(tree):
    stack = [tree]
    node = tree

    while len(stack)>0:#if the length of the stack is more than 0
        if node !=None:#If tree isnt empty
            while node.left:
                stack.append(node.left)#aappend the root node to the stack
                node=node.left#pointer goes to the left value
        popped_node=stack.pop()#pop the most recent value from stack
        if popped_node:
            print('Nodes INORDER: ',popped_node.value)#pop the most recent value from stack and print it
            node=popped_node.right#pointer goes to the right value
            stack.append(node)#aappend the root node to the stack

    
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,89)
  tree_insert(t,100)
  tree_insert(t,1)
  tree_insert(t,26)
  tree_insert(t,62)
  tree_insert(t,9)
  INORDER(t)

sys.exit()
