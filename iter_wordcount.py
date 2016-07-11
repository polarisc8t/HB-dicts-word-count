myDict = {}
input_file = open("twain.txt")
for line in input_file:
    line = line.rstrip()
    words = line.split(" ")
    for word in words:
        myDict[word] = myDict.get(word, 0) + 1
for key, value in myDict.iteritems():
    print "%s %d" %(key, value)
input_file.close()

