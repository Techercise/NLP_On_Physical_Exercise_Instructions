import textacy
from textacy import TextStats

exercise_list = open("/Users/matthewleinhauser/Documents/NLP Research Project/Exercises/exerciseList.txt", "r")
exercise_list_single_line = [line.rstrip('\n') for line in exercise_list]


def text_to_doc(file_directory):
    doc_array = []
    for individualEx in exercise_list_single_line:
        with open("/Users/matthewleinhauser/Documents/NLP Research Project/Exercises/" + file_directory +
                  "/" + individualEx + ".txt", "r") as exercise:
            exerciseText = exercise.read()
            docx = textacy.Doc(textacy.preprocess_text(exerciseText, lowercase=True, no_punct=True))
            doc_array.append(docx)
    return doc_array


goodExerciseDocArray = list((text_to_doc("GOOD")))
#  badExerciseDocArray = list((text_to_doc("BAD")))

i = 0

while i < len(goodExerciseDocArray):
    ts1 = TextStats(goodExerciseDocArray[i])
    goodExerciseDocArray[i] = list((round(ts1.flesch_reading_ease),
                                    round(ts1.flesch_kincaid_grade_level),
                                    round(ts1.gunning_fog_index),
                                    round(ts1.automated_readability_index)))
    # ts2 = TextStats(badExerciseDocArray[i])
    # badExerciseDocArray[i] = list((round(ts2.flesch_reading_ease),
    #                                round(ts2.flesch_kincaid_grade_level),
    #                                round(ts2.gunning_fog_index),
    #                                round(ts2.automated_readability_index)))
    i += 1

if i == len(goodExerciseDocArray):
    i = 0


def create_spaces(number_spaces):
    count = 0
    spaces = ""
    while count < number_spaces:
        spaces += " "
        count += 1
    return spaces


print("Exercise\t\t\t\t |  Flesch-Kincaid Reading Ease  |  Flesch-Kincaid Grade Level  |  Gunning-Fog Score  |  "
      "Automated Readability Index  |\n")

for individualEx in exercise_list_single_line:
    character_dif = len(exercise_list_single_line[29]) - len(individualEx)
    print(individualEx, end='')
    print(create_spaces(character_dif), "|\t\t\t", goodExerciseDocArray[i][0], end='')
    character_dif = len(str(goodExerciseDocArray[6][0])) - len(str(goodExerciseDocArray[i][0]))
    print(create_spaces(character_dif), "\t\t\t\t |\t\t\t", goodExerciseDocArray[i][1], end='')
    print("\t\t\t\t\t|\t\t\t", goodExerciseDocArray[i][2], end='')
    print("\t\t  |\t\t\t", goodExerciseDocArray[i][3], "\t\t\t\t  |")
    i += 1
