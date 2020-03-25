import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

#print(storage_path)
parser = argparse.ArgumentParser()
parser.add_argument("--key", dest='key')
parser.add_argument('--val', dest='val')
args = parser.parse_args()


if args.key is not None and args.val is not None:
    if os.path.exists(storage_path):
        f = open(storage_path, 'r')
        json_string = f.read()
        d = json.loads(json_string)
        if args.key not in d:
            d[args.key] = args.val
        elif type(d[args.key]) == list:
            d[args.key].append(args.val)
        else:
            d[args.key] = [d[args.key], args.val]

        with open(storage_path, 'w') as f:
            f.write(json.dumps(d))
        #print(d, 'все прошло хорошо')
    else:
        f = open(storage_path, 'w+')
        d={}
        if args.key not in d:
            d[args.key] = args.val
        elif type(d[args.key]) == list:
            d[args.key].append(args.val)
        else:
            d[args.key] = [d[args.key], args.val]

        with open(storage_path, 'w') as f:
            f.write(json.dumps(d))


if args.key is not None and args.val is None:
    if os.path.exists(storage_path):
        with open(storage_path, 'r') as f:
            json_string = f.read()
            dict_string = json.loads(json_string)
            if args.key in dict_string:

                if type(dict_string[args.key]) == list:
                    print(', '.join(dict_string[args.key]))
                else:
                    print(dict_string[args.key])

#print('я отработала')

