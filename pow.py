import hashlib
import pickle

# Part 2 response: "challenge":"7b66b27a3bb4bb5e076344566f91","difficulty":3

difficulty = 3
difficultyString = ''.join(['0' for x in range(difficulty)])
print(difficultyString)

block = {'message': '7b66b27a3bb4bb5e076344566f91'}
nonce = 1
p = hashlib.sha256()

block['nonce'] = 1
while p.hexdigest()[:difficulty] != difficultyString:
    nonce += 1
    block['nonce'] = nonce
    p = hashlib.sha256()
    p.update(pickle.dumps(block))
    print(nonce, p.hexdigest())
# last iteration: 10236 0004fe8f2e49c093ada2a9cb97d5896578ad4792124f4811b24c27c57b8b0093

print(block)
#{'message': '7b66b27a3bb4bb5e076344566f91', 'nonce': 10236}
