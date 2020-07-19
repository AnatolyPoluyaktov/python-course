import os
import tempfile
import json
import argparse
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")

args = parser.parse_args()
if args.key and args.val:
    if os.path.isfile(storage_path):
        with open(storage_path) as f:
            if os.stat(storage_path) == 0:
                data = {}
                data[args.key] = []
                data[args.key].append(args.val)
                with open(storage_path, "w+") as f:
                    json.dump(data, f)
            else:
                data = json.load(f)
                if args.key in data:
                    data[args.key].append(args.val)
                    with open(storage_path, "w+") as f:
                        json.dump(data, f)
                else:
                    data[args.key] = []
                    data[args.key].append(args.val)
                    with open(storage_path, "w+") as f:
                        json.dump(data, f)
    else:
        with open(storage_path, "w") as f:
            data = {}
            data[args.key] = []
            data[args.key].append(args.val)
            json.dump(data,f)



elif args.key and not args.val:
    if os.path.isfile(storage_path):
        with open(storage_path) as f:
            if os.stat(storage_path) == 0:
                print("None")
            else:
                data = json.load(f)
                if args.key in data:
                   print(*data[args.key],sep=", ")
                else:
                    print("None")
    else:
        print("None")



#storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
#with open(storage_path, 'w') as f:
      #f.write("s")
