class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None
        self.max = self.root
        
    def insert(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
        else:
            ptr = self.root
            while(True):
                if val<ptr.val:
                    if ptr.left:
                        ptr = ptr.left
                    else:
                        ptr.left = node
                        break
                elif val>ptr.val:
                    if ptr.right:
                        ptr = ptr.right
                    else:
                        ptr.right = node
                        break
                else:
                    break
    def BFS(self):
        ptr = self.root
        q = []
        ans = []
        q.append(ptr)
        while q:
            print(q)
            node = q.pop(0)
            ans.append(node.val)
            if node.left:q.append(node.left)
            if node.right: q.append(node.right)
        print(ans)
    
    def inorder(self):
        ptr = self.root
        s = []
        ans = []
        while True:
            if ptr:
                s.append(ptr)
                ptr = ptr.left
            elif s:
                ptr = s.pop()
                ans.append(ptr.val)
                ptr = ptr.right
            else: break
        print(ans)
        return ans
        

tree = Tree()

a = [8,6,9,5,7,10]

for i in a:
    tree.insert(i)

tree.BFS()

tree.inorder()