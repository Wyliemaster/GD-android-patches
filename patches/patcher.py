import json
import os

with open(f"{os.getcwd()}\\patches.json", 'r') as f:
    patch_data = json.load(f)

with open('../libcocos2dcpp.so', 'rb') as file:
    libcocos2dcpp = bytearray(file.read())

for keys in patch_data:
    print(f"Name: {keys}")
    data = patch_data[keys]
    patch = data['patch'].split()

    for i in range(len(patch)):
        print(f"patch {i+1}: {patch[i]}")
        print(f"offset: {int(data['offset'], 16)}")
        libcocos2dcpp[int(data['offset'], 16) + i] = int(patch[i], 16)

with open('../patched_libcocos2dcpp.so', 'wb') as bin:
    bin.write(libcocos2dcpp)
