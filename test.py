from urllib.request import Request, urlopen
from urllib.parse import urlencode
import pickle
import hashlib
import requests
import json

# defining the api-endpoint


respuesta = '326a1f23f47491de0856a1ca3acf'
respuestaCifrada = hashlib.sha256(respuesta.encode('utf-8'))
a = respuestaCifrada.digest()
print(a)
url = "https://candidates.mifiel.com/api/v1/users/0be97999-d8e8-4ae5-89d4-bc57366308d0/challenge/digest"
url1 = "https://candidates.mifiel.com/api/v1/users/"

data = {
    'result': a}

data1 = {
    'name': 'Alan Alvarez',
    'email': 'alandanielalvarez0000@gmail.com'
}

headers = {'Content-type': 'application/json'}
r = requests.post(url1, data=json.dumps(data1), headers=headers)
print(r.text)


################# PARTE 1 ########################
#  curl -X 'POST' \
#   'https://candidates.mifiel.com/api/v1/users' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "name": "Alan Alvarez",
#   "email": "alandanielalvarez0000@gmail.com"
# }'
#
# JSON response from POST https://candidates.mifiel.com/api/v1/users
# {"success": true, "id": "0be97999-d8e8-4ae5-89d4-bc57366308d0", "message": "Hello Alan Alvarez, nice to swee you!", "next_challenge": {"name": "digest", "challenge": "326a1f23f47491de0856a1ca3acf", "solved": false}}%
#
# user.id from response 1
# 0be97999-d8e8-4ae5-89d4-bc57366308d0
#################################################


################# PARTE 2 #######################
# next_challenge.challenge parameter from POST request
# "challenge": "326a1f23f47491de0856a1ca3acf"


# print(respuestaCifrada.digest())
# console output: b'(\x8d\xe3\x15\xd1\x95\xfe\xe8R\x00\x05\xc0B\xb7~=7\xc5a\xe6-d\xacu\x13*\x91\x7f\xa5\x81\x9c\xa9'

# print(respuestaCifrada.hexdigest())
# console output: 288de315d195fee8520005c042b77e3d37c561e62d64ac75132a917fa5819ca9

# curl - X 'POST' \
#     'https://candidates.mifiel.com/api/v1/users/0be97999-d8e8-4ae5-89d4-bc57366308d0/challenge/digest' \
#     - H 'accept: application/json' \
#      - H 'Content-Type: application/json' \
#     - d '{
#         "result": "b'(\x8d\xe3\x15\xd1\x95\xfe\xe8R\x00\x05\xc0B\xb7~=7\xc5a\xe6-d\xacu\x13*\x91\x7f\xa5\x81\x9c\xa9'"
#     }'

#################################################


################# PARTE 3 #######################

# block = {
#     'transactions': [
#         {
#             'from': 'A',
#             'to': 'B',
#             'amount': 10
#         },
#         {
#             'from': 'B',
#             'to': 'C',
#             'amount': 10
#         },
#         {
#             'from': 'C',
#             'to': 'D',
#             'amount': 10,
#             'message': 'thanks for the help'
#         },
#     ]
# }

# m = hashlib.sha3_256()
# m.update(pickle.dumps(block))
# m.digest()
# m.hexdigest()
# print(m.hexdigest())

# topBlock = {
#     'transactions': [
#         {
#             'from': 'A',
#             'to': 'B',
#             'amount': 10
#         },
#         {
#             'from': 'B',
#             'to': 'C',
#             'amount': 10
#         },
#         {
#             'from': 'C',
#             'to': 'D',
#             'amount': 10,
#             'message': 'thanks for the help'
#         },
#     ],
#     'lastBlock': m.hexdigest(),
#     'nonce': 0  # makes a hash starts with 0
# }

# n = hashlib.sha3_256()
# n.update(pickle.dumps(topBlock))
# n.digest()
# n.hexdigest()
# print(n.hexdigest())

# # Proof of work
# difficulty = 3
# difficultyString = ''.join(['0' for x in range(difficulty)])
# print(difficultyString)
# p = hashlib.sha3_256()
# nonce = 1
# topBlock['nonce'] = 1
# while p.hexdigest()[:difficulty] != difficultyString:
#     nonce += 1
#     topBlock['nonce'] = nonce
#     p = hashlib.sha3_256()
#     p.update(pickle.dumps(topBlock))
#     print(nonce, p.hexdigest())

# print(topBlock)
