import os
import collections


s = ''

for root, directories, filenames in os.walk('./'):
    for filename in filenames:
        s+=filename+' '

dict = collections.Counter(s.split())

print("Unique filenames:")
for key in dict:
    if dict.get(key) == 1:
        print(key)
