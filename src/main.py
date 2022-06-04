from merkel import MerkelTree

m = MerkelTree([1,2,3], 5)
print(m.getRoot())
print(m.hash(m.normalizeItem(m.getMerkleProof(4) [-1])))