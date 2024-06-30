class Node:
    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

class BinaryTree:
    def __init__(self):
        self.root = None
        return 


    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, curr, value):
        if value < curr.value:
            if curr.left is None:
                curr.left = Node(value)
            else:
                self.insert_recursive(curr.left, value)


        elif value > curr.value:
            if curr.right is None:
                curr.right = Node(value)
            else:
                self.insert_recursive(curr.right, value)


    def search(self, value):
        curr = self.root
        while curr is not None:
            if curr.value == value:
                return True
            elif curr.value > value:
                curr = curr.left
            else:  # curr.value < value
                curr = curr.right
        return False


    def delete(self, value):
        if not self.search(value):
            return
        
        # Helper function to find the minimum value in a subtree
        def find_min(node):
            current = node
            while current.left is not None:
                current = current.left
            return current
        
        # Helper function to perform the deletion
        def delete_node(root, key):
            if root is None:
                return root
            
            # If the key to be deleted is smaller than the root's key, then it lies in the left subtree
            if key < root.value:
                root.left = delete_node(root.left, key)
            # If the key to be deleted is greater than the root's key, then it lies in the right subtree
            elif key > root.value:
                root.right = delete_node(root.right, key)
            # If key is the same as root's key, then this is the node to be deleted
            else:
                # Node with only one child or no child
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                
                # Node with two children: Get the inorder successor (smallest in the right subtree)
                temp = find_min(root.right)
                
                # Copy the inorder successor's content to this node
                root.value = temp.value
                
                # Delete the inorder successor
                root.right = delete_node(root.right, temp.value)
            
            return root
        
        # Update root with the modified tree after deletion
        self.root = delete_node(self.root, value)



    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
    
    def inorder(self):
        result = []
        self.inorder_traversal(self.root, result)
        return result


    def preorder_traversal(self, node, result):
        if node:
            result.append(node.value)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
    
    def preorder(self):
        result = []
        self.preorder_traversal(self.root, result)
        return result


    def postorder_traversal(self, node, result):
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)
    
    def postorder(self):
        result = []
        self.postorder_traversal(self.root, result)
        return result
    
tree = BinaryTree()
tree.insert(10)
tree.insert(15)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(20)
print(tree.search(15))
print(tree.search(20))
print(tree.search(6))
print(tree.inorder())
print(tree.postorder())
print(tree.preorder())