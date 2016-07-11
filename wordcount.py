myDict = {}
input_file = open("test.txt")
for line in input_file:
    line = line.rstrip()
    words = line.split(" ")
    for word in words:
        myDict[word] = myDict.get(word, 0) + 1
for key, value in myDict.items():
    print "%s %d" %(key, value)

