#Github project
sentence = input("Enter a sentence: ")
sentence_2 = sentence.lower().strip().replace(" ", "")
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for ele in sentence_2:
    if ele in punc:
        sentence_2 = sentence_2.replace(ele, "")

print(sentence_2)