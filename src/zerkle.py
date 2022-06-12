from merkel import MerkelTree
# A zerlke tree is a zk ready merkle tree
# Every leaf of this tree is of the form (address, ...data)
class ZerkleTree:
    def __init__(self, items):
        self._items = items
        self._merkleTree = MerkelTree(items)

    def getAddressFromSignature(signature):
        return signature # todo
    
    def getItems(self):
        return self._items

    def getZkProof(self, signature, item) :
        # prove "I own the private key to one of the leaves on this zerkle tree"
        # without revealing the public key or item :)
        address = self._getAddressFromSignature(signature)
        merkleProof = self._merkleTree((address, item))
        return []
    