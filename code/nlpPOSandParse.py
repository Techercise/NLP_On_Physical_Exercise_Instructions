# from nltk import word_tokenize
# from nltk.corpus import brown
# from nltk.tag import DefaultTagger, NgramTagger
#
# trainText = brown.tagged_sents(categories='news')
# sampleText = benchPress.split()
#
# tagger = DefaultTagger('NN')
# for n in range(1, 4):
#     tagger = NgramTagger(n, trainText, backoff=tagger)

from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'/Users/matthewleinhauser/Downloads/stanford-corenlp-full-2018-10-05')

sentence = open("/Users/matthewleinhauser/Documents/NLP Research Project/Exercises/GOOD/Bench Press.txt", "r").read()
print("Constituency Parsing: ", nlp.parse(sentence))

nlp.close()
