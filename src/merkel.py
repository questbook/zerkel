import pickle
import base64

from web3 import Web3

class MerkelTree :
    _items = []
    _merkelItems = []
    _depth = 1
    _merkelRoot = None
    def __init__(self, items, depth):
        self._depth = depth
        self._items = sorted(map( lambda item: self.normalizeItem(item), items))
        self.constructMerkle()
    
    def normalizeItem(self, item):
        return base64.b64encode(pickle.dumps(item)).hex()

    def hash(self, string):
        return Web3.sha3(text=string).hex()

    def constructMerkle(self):
        null = self.normalizeItem(None)
        merkelItems = sorted(map(lambda item: self.hash(item), self._items + [null]*(2**self._depth - len(self._items))))
        print(merkelItems)
        self._tree = [merkelItems]
        for height in range(self._depth):
            nodes = []
            print("===")
            for i in range(int(len(merkelItems)/2)):
                print(i)
                node = (merkelItems[2*i], merkelItems[2*i+1])
                print(node)
                nodes.append(self.hash(self.normalizeItem(node)))
            merkelItems = nodes
            self._tree.append(nodes)
        self._merkelRoot = merkelItems[0]
    
    def getRoot(self):
        return self._merkelRoot
    
    def getMerkleProof(self, item):
        merkelItem = self.hash(self.normalizeItem(item))
        proof = []
        
        for i in range(self._depth):
            nodes = self._tree[i]
            index = nodes.index(merkelItem)
            node = None
            if index%2 == 0:
                node = (nodes[index], nodes[index+1])
            else:
                node = (nodes[index - 1], nodes[index])
            merkelItem = self.hash(self.normalizeItem(node))
            proof.append(node)
        return proof
