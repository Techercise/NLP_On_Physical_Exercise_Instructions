def lexical_diversity(exercise):
    return len(set(exercise)) / len(exercise)


exs = open("/Users/matthewleinhauser/Documents/NLP Research Project/Exercises/exerciseList.txt", "r")
exerciseList = [line.rstrip('\n') for line in exs]

for indivEx in exerciseList:
    #  with open("/Users/matthewleinhauser/Documents/NLP Research Project/Exercises/BAD/" + indivEx + ".txt", "r") as bad:
    with open("/Users/matthewleinhauser/Documents/NLP Research Project/Exercises/GOOD/" + indivEx + ".txt", "r") as good:
        text = good.read()
        indivEx += ":"
        print(indivEx,  end='')
        print("\t", lexical_diversity(text))
