class BinomialTree():
    def __init__(self, value):
        # define an empty binomial tree
        self.value = value
        self.order = 0
        self.parent = None
        self.child = []

    def travesel(self):
        for i in self.child:
            print self.value, '->', i.value
            i.travesel()

    def merge_Bi_Tree(self,Bi_Tree):     # to merge_Bi_Tree two binomial tree
        if self.order != Bi_Tree.order or self.value > Bi_Tree.value:
            return None
        self.child.append(Bi_Tree)
        self.order = self.order + 1

class BinomialHeap():
    def __init__(self):
        # define an empty binomial heap
        self.parent = self
        self.trees = []
        self.elements = 0
        self.maximum = 10000
        self.min = self.maximum               # set a min
        self.min_tree_order = -1

    def merge(self, Bi_Heap):           # to merge two Bi_heaps
        for i in Bi_Heap.trees:
            if i is not None:
                self.__add_tree(i)

    def insert(self, value):            # to insert the value as an order 0 binomial tree
        Bi_Tree = BinomialTree(value)
        self.__add_tree(Bi_Tree)

    def get_min(self):                  # simply use the init to get the min
        return self.min

    def delete_min(self):               # delete and rebalance the heap
        rm_var = self.trees[self.min_tree_order]
        self.trees[rm_var.order] = None
        self.elements = self.elements - 2**rm_var.order
        # to rebalance
        for i in rm_var.child:
            self.__add_tree(i)
        self.min = self.maximum
        for tree in self.trees:
            if tree is not None and tree.value <= self.min:
                    self.min = tree.value
                    self.min_tree_order = tree.order

    def __add_tree(self,Bi_Tree):    # To insert a tree into the original heap and do rebalance
        self.elements = self.elements + 2**Bi_Tree.order
        if 2**len(self.trees) - 1 < self.elements:
            self.trees.append(None)
        while self.trees[Bi_Tree.order] is not None:
            if Bi_Tree.value > self.trees[Bi_Tree.order].value:
                Bi_Tree, self.trees[Bi_Tree.order] = self.trees[Bi_Tree.order], Bi_Tree     # swap
            i = Bi_Tree.order
            Bi_Tree.merge_Bi_Tree(self.trees[Bi_Tree.order])    # call the merge_Bi_Tree binomial tree
            self.trees[i] = None                        # free it
        self.trees[Bi_Tree.order] = Bi_Tree
        if Bi_Tree.value <= self.min:
            self.min = Bi_Tree.value
            self.min_tree_order = Bi_Tree.order

    def decrease_key(self, old_key, new_key):
        # check if the old_key is valid
        keys = []
        for key in self.trees:
            keys.append(key.value)
            for i in key.child:
                keys.append(i.value)
        if old_key not in keys:
            return None
        # change the key
        key_arr = []
        while self.min != old_key:
            key_arr.append(self.min)
            self.delete_min()
        self.delete_min()
        self.insert(new_key)
        for i in key_arr [::-1]:
            self.insert(i)


    def __len__(self):
        return self.elements
