usage = '''

API CLI Texas Chainsaw Managers

Usage:
    tcm.py banana
    tcm.py is_prime <input>
    tcm.py fibonacci <input>
    tcm.py kv-retrieve <input>
    tcm.py factorial <input>
    tcm.py md5 <input>

'''

from docopt import docopt

args = docopt(usage)

from docopt import docopt
import requests

if args['banana']:
    data = requests.get('http://localhost:5000/banana')
    print(data.text)
    data = data.json()
    print(data['is_banana'])

if args['is_prime']:
    data = requests.get('http://localhost:5000/is_prime'+'/'+args['<input>'])
    print(data.text)
    data = data.json()
    print(data['output'])

if args['md5']:
    data = requests.get('http://localhost:5001/md5'+'/'+args['<input>'])
    print(data.text)
    data = data.json()
    print(data['output'])

if args['fibonacci']:
    data = requests.get('http://localhost:5000/fibonacci'+'/'+args['<input>'])
    print(data.text)
    data = data.json()
    print(data['output'])

if args['factorial']:
    data = requests.get('http://localhost:5000/factorial'+'/'+args['<input>'])
    print(data.text)
    data = data.json()
    print(data['output'])

if args['kv-retrieve']:
    data = requests.get('http://localhost:5000/kv-retrieve'+'/'+args['<input>'])
    print(data.txt)
    data = data.json()
    print(data['output'])
