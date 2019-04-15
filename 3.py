import collections

tested_string = input("Type a string to check: \n")

print("\nCount result:")
results = collections.Counter(tested_string)

for key in results.copy():
    if results.get(key) == 1 or key in {' '}:
        del results[key]

for entry in results.most_common():
    print("count of "+entry[0]+" = " + str(entry[1]))
