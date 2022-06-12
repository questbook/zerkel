import hashlib

from zokrates_pycrypto.eddsa import PrivateKey, PublicKey
from zokrates_pycrypto.field import FQ
from web3 import Web3


def zokrates_sha3(hex):
    hash = Web3.sha3(hexstr=hex)
    ints = []
    for i in range(4):
        ints.append(int.from_bytes(hash[i*8:i*8+8], "little"))
    return ints

if __name__ == "__main__":

    raw_msg = "@madhavanmalolan"
    msg = hashlib.sha512(raw_msg.encode("utf-8")).digest()

    # sk = PrivateKey.from_rand()
    # Seeded for debug purpose
    key = FQ(1997011358982923168928344992199991480689546837621580239342656433234255379025)
    sk = PrivateKey(key)
    sig = sk.sign(msg)

    pk = PublicKey.from_private(sk)
    args = [pk.p.x.n, pk.p.y.n]
    args = " ".join(map(str, args))

    M0 = msg.hex()[:64]
    M1 = msg.hex()[64:]
    b0 = [str(int(M0[i:i+8], 16)) for i in range(0,len(M0), 8)]
    b1 = [str(int(M1[i:i+8], 16)) for i in range(0,len(M1), 8)]
    args = args + " " + " ".join(b0 + b1)

    hash_am = zokrates_sha3(M0[:32]+M1[:32])
    args += " "+ " ".join(map(lambda x: str(x), hash_am))+" "+ " ".join(map(lambda x: str(x), hash_am))
    #args += " "+ " ".join(map(lambda x: str(x), zokrates_sha3(hex(4)[2:])))+" "+ " ".join(map(lambda x: str(x), zokrates_sha3(hex(0)[2:])))
    print(args)    

    