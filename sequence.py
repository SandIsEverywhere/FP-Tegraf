class Tree:
    def __init__(self):
        self.nodes = {}
        self.next_id = 0
        self.root = None

    def add_node(self, value, parent_id=None):
        node_id = self.next_id
        self.next_id += 1
        
        self.nodes[node_id] = {"value": value, "children": []}

        if parent_id is None:
            if self.root is None:
                self.root = node_id
        else:
            self.nodes[parent_id]["children"].append(node_id)
        
        return node_id
    
    def print_tree(self):
        def dfs(node_id, depth=0):
            node = self.nodes[node_id]
            indent = "  " * depth
            print(f"{indent}{node['value']} (id {node_id})")
            for child_id in node["children"]:
                dfs(child_id, depth + 1)

        if self.root is not None:
            dfs(self.root)
        else:
            print("Tree is empty.")
    

def add_value(tree, parent, sequence, i):
    value = sequence[i]
    new_node = tree.add_node(value, parent)
    for j in range(i+1, len(sequence)):
        if sequence[j] > value:
            add_value(tree, new_node, sequence, j)

def make_tree(sequence):
    tree = Tree()
    root = tree.add_node("root")
    for i in range(len(sequence)):
        value = sequence[i]
        add_value(tree, root, sequence, i)

    return tree

sequence = [4, 1, 13, 7, 0, 2, 8, 11, 3]

tree = make_tree(sequence)

tree.print_tree()

# sequence = input("input sequence (seperated by commas)")class Tree:
    def __init__(self):
        self.nodes = {}
        self.next_id = 0
        self.root = None

    def add_node(self, value, parent_id=None):
        node_id = self.next_id
        self.next_id += 1
        
        self.nodes[node_id] = {"value": value, "children": []}

        if parent_id is None:
            if self.root is None:
                self.root = node_id
        else:
            self.nodes[parent_id]["children"].append(node_id)
        
        return node_id
    
    def print_tree(self):
        def dfs(node_id, depth=0):
            node = self.nodes[node_id]
            indent = "  " * depth
            print(f"{indent}{node['value']} (id {node_id})")
            for child_id in node["children"]:
                dfs(child_id, depth + 1)

        if self.root is not None:
            dfs(self.root)
        else:
            print("Tree is empty.")
    

def add_value(tree, parent, sequence, i):
    value = sequence[i]
    new_node = tree.add_node(value, parent)
    for j in range(i+1, len(sequence)):
        if sequence[j] > value:
            add_value(tree, new_node, sequence, j)

def make_tree(sequence):
    tree = Tree()
    root = tree.add_node("root")
    for i in range(len(sequence)):
        value = sequence[i]
        add_value(tree, root, sequence, i)

    return tree

sequence = [4, 1, 13, 7, 0, 2, 8, 11, 3]

tree = make_tree(sequence)

tree.print_tree()

# sequence = input("input sequence (seperated by commas)")
