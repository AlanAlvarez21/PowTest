import hashlib
import pickle

block = {'message': 'Hello, world!'}

n = hashlib.sha256()
n.update(pickle.dumps(block))
n.hexdigest()
print(n.hexdigest())

difficulty = 3
difficultyString = ''.join(['0' for x in range(difficulty)])
print(difficultyString)

nonce = 1
p = hashlib.sha256()

block['nonce'] = 1
while p.hexdigest()[:difficulty] != difficultyString:
    nonce += 1
    block['nonce'] = nonce
    p = hashlib.sha256()
    p.update(pickle.dumps(block))
    print(nonce, p.hexdigest())

print(block)
