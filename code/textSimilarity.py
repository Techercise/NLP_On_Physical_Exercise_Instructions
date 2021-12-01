
def get_jaccard_sim(str1, str2):
    first = set(str1.split())
    second = set(str2.split())
    intersect = first.intersection(second)
    return float(len(intersect)) / (len(first) + len(second) - len(intersect))


text_similarity_array = []
exs = open("/Users/matthewleinhauser/Documents/NLP Research Project/Exercises/exerciseList.txt", "r")
exercise_list_single_line = [line.rstrip('\n') for line in exs]


def make_text_similarity_array(file_directory):
    ts_array = []
    for i in exercise_list_single_line:
        with open("/Users/matthewleinhauser/Documents/NLP Research Project/Exercises/" + file_directory +
                  "/" + i + ".txt", "r") as ex1:
            text1 = ex1.read()
        #  index_array = []
        avg_exercise_similarity = 0
        for j in exercise_list_single_line:
            with open("/Users/matthewleinhauser/Documents/NLP Research Project/Exercises/" + file_directory +
                      "/" + j + ".txt", "r") as ex2:
                text2 = ex2.read()
                similarity = get_jaccard_sim(text1, text2)
                if similarity != 1.0:
                    #  index_array.append(similarity)
                    avg_exercise_similarity += similarity
        #  ts_array.append(index_array)
        ts_array.append(avg_exercise_similarity / 29)
    return ts_array


good_exercise_similarity_array = list((make_text_similarity_array("GOOD")))
bad_exercise_similarity_array = list((make_text_similarity_array("BAD")))
good_similarity_total = 0
bad_similarity_total = 0
