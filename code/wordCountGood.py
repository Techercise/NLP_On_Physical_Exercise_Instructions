exerciseList = open("/Users/matthewleinhauser/Documents/NLP Research Project/Exercises/exerciseList.txt", "r")
exerciseListSingleLine = [line.rstrip('\n') for line in exerciseList]

for indivEx in exerciseListSingleLine:
    with open("/Users/matthewleinhauser/Documents/NLP Research Project/Exercises/GOOD/" + indivEx + ".txt", "r") as goodEx:
        text = goodEx.read()
        words = text.split()
        wordTotal = len(words)
        indivEx += ":"
        # print(indivEx,  end='')
        print("\t", wordTotal)