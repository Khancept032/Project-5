usage = '''

API CLI Texas Chainsaw Managers

Usage:
    tcm.py banana
    tcm.py is-prime <input>
    tcm.py md5 <input>
    tcm.py fibonacci <input>
    tcm.py factorial <input>
    tcm.py kv-record <input>
    tcm.py kv-retrieve <input>

'''

from docopt import docopt

args = docopt(usage)

from docopt import docopt
import requests

def human(com, arg, res):
    res = res.json()
    print('\n\tCLI command: \t' + com + ' ' + str(arg))
    print('\tAPI response: \t' + str(res['output']) + '\n')
    return

if args['banana']:
    data = requests.get('http://localhost:5000/banana')
    # print(data.text)      # for debugging
    human('banana', '', data)

if args['is-prime']:
    data = requests.get('http://localhost:5000/is_prime/' + args['<input>'])
    # print(data.text)      # for debugging
    human('is-prime', args['<input>'], data)

if args['md5']:
    data = requests.get('http://localhost:5000/md5/' + args['<input>'])
    # print(data.text)      # for debugging
    human('md5', args['<input>'], data)

if args['fibonacci']:
    data = requests.get('http://localhost:5000/fibonacci/' + args['<input>'])
    # print(data.text)      # for debugging
    human('fibonacci', args['<input>'], data)

if args['factorial']:
    data = requests.get('http://localhost:5000/factorial/' + args['<input>'])
    # print(data.text)      # for debugging
    human('factorial', args['<input>'], data)

if args['kv-record']:
    data = requests.get('http://localhost:5000/kv-record/' + args['<input>'])
    # print(data.text)      # for debugging
    human('kv-record', args['<input>'], data)

if args['kv-retrieve']:
    data = requests.get('http://localhost:5001/kv-retrieve/' + args['<input>'])
    # print(data.text)      # for debugging
    human('kv-retrieve', args['<input>'], data)
