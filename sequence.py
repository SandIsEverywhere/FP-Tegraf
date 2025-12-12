class Tree:
    def __init__(self):
        self.nodes = {}
        self.next_id = 0

    def add_node(self, value, parent_id=None):
        node_id = self.next_id
        self.next_id += 1
        
        self.nodes[node_id] = {"value": value, "children": []}

        if parent_id is not None:
            self.nodes[parent_id]["children"].append(node_id)
        
        return node_id
    

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

