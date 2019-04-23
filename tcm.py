# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# usage = """Usage:
#         test.py -h
#         test.py md5 <input>
#         test.py factorial <input>
# """
#
# from docopt import docopt
# import requests
#
# args = docopt(usage)
#
# if args['md5']==True:
#     r = requests.get("http://localhost:5000/md5/"+ args["<input>"])
#     data = r.json()
#     print(data['output'])
# if args['factorial']==True:
#     r = requests.get("http://localhost:5000/factorial/"+ args["<input>"])
#     data = r.json()
#     print(data['output'])

usage = '''

API CLI Texas Chainsaw Managers

Usage:
    tcm.py banana
    tcm.py is_prime <input>

'''

from docopt import docopt

args = docopt(usage)

from docopt import docopt
import requests

if args['banana']:
    data = requests.get('http://localhost:5001/banana')
    print(data.text)
    data = data.json()
    print(data['is_banana'])

if args['is_prime']:
    data = requests.get('http://localhost:5001/is_prime'+'/'+args['<input>'])
    print(data.text)
    data = data.json()
    print(data['output'])
