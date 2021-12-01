#  Difference equation: (Good exercise) - (Bad exercise) = difference in word count
wordCountDifferenceArray = []
exercise_list = open("/Users/matthewleinhauser/Documents/NLP Research Project/Exercises/exerciseList.txt", "r")
exercise_list_single_line = [line.rstrip('\n') for line in exercise_list]


def make_word_count_array(file_directory):
    word_count_array = []
    for individualEx in exercise_list_single_line:
        with open("/Users/matthewleinhauser/Documents/NLP Research Project/Exercises/" + file_directory + "/"
                  + individualEx + ".txt", "r") as badEx:
            text = badEx.read()
            words = text.split()
            word_count_array.append(len(words))
    return word_count_array


goodExerciseWordCount = list((make_word_count_array("GOOD")))
badExerciseWordCount = list((make_word_count_array("BAD")))

i = 0

while i < len(badExerciseWordCount) and i < len(goodExerciseWordCount):
    wordCountDifferenceArray.append((goodExerciseWordCount[i] - badExerciseWordCount[i]))
    i += 1

if i == len(badExerciseWordCount) & i == len(goodExerciseWordCount):
    i = 0

for indivEx in exercise_list_single_line:
    indivEx += ":"
    print(indivEx, end="")
    print("\t", wordCountDifferenceArray[i])
    i += 1
