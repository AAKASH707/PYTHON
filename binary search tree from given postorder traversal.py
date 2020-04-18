# Python program to construct binary search tree from given postorder traversal

# importing sys module
import sys


# class for creating tree nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# initializing MIN and MAX
MIN = -sys.maxsize - 1
MAX = sys.maxsize


# recurrsive function for creating binary search tree from postorder
def constructBST(postorder, postIndex, key, min, max, size):
    # base case
    if postIndex[0] < 0:
        return None

    root = None

    # If current element of postorder is in range(min to max), then only it is part
    # of current subtree
    if key > min and key < max:

        # creating a new node and assigning it to root, decrementing postIndex[0] by 1
        root = Node(key)
        postIndex[0] -= 1

        if (postIndex[0] >= 0):
            # all the nodes in the range(key to max) will be in the right subtree,
            # and first such node will be the root of the right subtree.
            root.right = constructBST(postorder, postIndex,
                                      postorder[postIndex[0]],
                                      key, max, size)

            # all the nodes in the range(min to key) will be in the left subtree,
            # and first such node will be the root of the left subtree.
            root.left = constructBST(postorder, postIndex,
                                     postorder[postIndex[0]],
                                     min, key, size)

    return root


# function for printing the inorder traversal of the binary search tree
def printInorder(root):

    if (root == None):
        return
    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)


# Driver code
def main():
    # asking the user for postorder sequence
    postorder = list(map(int, input('Enter the postorder traversal: ').split()))
    size = len(postorder)

    # postIndex is used to keep track of index in postorder
    postIndex = [size - 1]

    # calling function constructBST
    root = constructBST(postorder, postIndex, postorder[postIndex[0]], MIN, MAX, size)

    print("The inorder traversal of the constructed binary search tree: ")

    # calling function printInorder
    printInorder(root)


if __name__ == "__main__":
    main()
