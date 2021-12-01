exs = open("/Users/matthewleinhauser/Documents/NLP Research Project/Exercises/exerciseList.txt", "r")
exercise_list_single_line = [line.rstrip('\n') for line in exs]
lexicalDiversityDifferenceArray = []


def lexical_diversity(exercise):
    return len(set(exercise)) / len(exercise)


def make_lexical_diversity_array(file_directory):
    lexical_diversity_array = []
    for individEx in exercise_list_single_line:
        with open("/Users/matthewleinhauser/Documents/NLP Research Project/Exercises/" + file_directory +
                  "/" + individEx + ".txt", "r") as ex:
            text = ex.read()
            lexical_diversity_array.append(lexical_diversity(text))
    return lexical_diversity_array


goodExerciseLexicalDiversity = list((make_lexical_diversity_array("GOOD")))
badExerciseLexicalDiversity = list((make_lexical_diversity_array("BAD")))

i = 0
while i < len(badExerciseLexicalDiversity) and i < len(goodExerciseLexicalDiversity):
    lexicalDiversityDifferenceArray.append((goodExerciseLexicalDiversity[i] - badExerciseLexicalDiversity[i]))
    i += 1

if i == len(badExerciseLexicalDiversity) and i == len(goodExerciseLexicalDiversity):
    i = 0

for indivEx in exercise_list_single_line:
    indivEx += ":"
    print(indivEx, end="")
    print("\t", lexicalDiversityDifferenceArray[i])
    i += 1
