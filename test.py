from urllib.request import Request, urlopen
from urllib.parse import urlencode
import pickle
import hashlib
import requests
import json


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


# respuesta = '326a1f23f47491de0856a1ca3acf'
# respuestaCifrada = hashlib.sha256(respuesta.encode('utf-8'))
# a = respuestaCifrada.digest()
# print(a)


################# PARTE 2 #######################
# next_challenge.challenge parameter from POST request
# "challenge": "326a1f23f47491de0856a1ca3acf"

# print(respuestaCifrada.hexdigest())
# console output: 288de315d195fee8520005c042b77e3d37c561e62d64ac75132a917fa5819ca9

# curl - X 'POST' \
#     'https://candidates.mifiel.com/api/v1/users/0be97999-d8e8-4ae5-89d4-bc57366308d0/challenge/digest' \
#     - H 'Content-Type: application/json' \
#     - d '{
#         "result": "288de315d195fee8520005c042b77e3d37c561e62d64ac75132a917fa5819ca9"
#     }'

#################################################
