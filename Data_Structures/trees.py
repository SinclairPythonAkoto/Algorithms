"""Trees

A binary tree is a hierarchical sata structure consisting of nodes connected by
edges, with a root noe at the top and leaf nodes at the bottom.

One common use of a binary tree is in computer file systems, where files and 
directories are organized in a hierarchical structure. Each directory can 
contain multiple subdirectories and files, forming a tree-like structure.

In the example below, we define a TreeNode class that represents a node in the 
binary tree, and a FileSystem class that represents the file system using a binary 
tree data structure. The add_file and add_directory methods are used to add files 
and directories to the binary tree, respectively, and the find_node method is used 
to locate a node in the binary tree based on its name.
"""
class TreeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class FileSystem:
    def __init__(self, root_name: str):
        self.root = TreeNode(root_name)

    def add_file(self, parent_name: str, file_name: str):
        parent_node = self.find_node(parent_name, self.root)
        if parent_node:
            if parent_node.left == None:
                parent_node.left = TreeNode(file_name)
            elif parent_node.right == None:
                parent_node.right = TreeNode(file_name)
            else:
                print("Cannot add file to parent node: ", parent_name)

    def add_directory(self, parent_name: str, dir_name: str):
        parent_node = self.find_node(parent_name, self.root)
        if parent_node:
            if parent_node.left == None:
                parent_node.left = TreeNode(dir_name)
            elif parent_node.right == None:
                parent_node.right = TreeNode(dir_name)
            else:
                print("Cannot add directory to parent node: ", parent_name)

    def find_node(self, name, node):
        if node == None:
            return None
        if node.name == name:
            return node
        left_node = self.find_node(name, node.left)
        if left_node:
            return left_node
        right_node = self.find_node(name, node.right)
        if right_node:
            return right_node
        return None

# create a file system with a directory called 'root'
system: FileSystem = FileSystem('root')

# add a directory called 'documents' to the root directory
system.add_directory('root', 'documents')

# add a file to the documents directory
system.add_file('documents', 'report.txt')

# add a directory called 'photos' to the documents directory
system.add_directory('documents', 'my_photos')

# add a file to the photos directory
system.add_file('my_photos', 'beach.jpg')

# find the photos directory and print its name
photos_directory = system.find_node('my_photos', system.root)
if photos_directory:
    print('Found directory:', photos_directory.name)

# find file and print file name
beach_pic = system.find_node('beach.jpg', system.root)
if beach_pic:
    print('Found file:', beach_pic.name)


# Output
# Found directory: my_photos
# Found file: beach.jpg