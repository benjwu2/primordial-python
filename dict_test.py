dict1 = {'a':[7,1],'b':[8,4],'c':3}
print(dict1)
print(dict1.keys())
print(dict1.values())

# prints the key with the corresponding value of 2
print(dict1['a'])

if 'b' in dict1.keys():
    print("The value of key \'b\' is {}".format(dict1['b'][0]))
