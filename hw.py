input_text = """
One day a rabbit was boasting about,how fast he could run. 
He was laughing at the turtle for being so slow. Much to the 
rabbit’s surprise, the turtle challenged him to a race. The rabbit 
thought this was a good joke and accepted the challenge. The fox 
was to be the umpire of the race. As the race began, the rabbit 
raced way ahead of the turtle, just like everyone thought.
The rabbit got to the halfway point and could not see the turtle 
anywhere. He was hot and tired and decided to stop and take a short 
nap. Even if the turtle passed him, he would be able to race to the
finish line ahead of him. All this time the turtle kept walking step 
by step by step. He never quit no matter how hot or tired he got. 
He just kept going. 
However, the rabbit slept longer than he had thought and woke up. 
He could not see the turtle anywhere! He went at full speed to 
the finish line but found the turtle there waiting for him.
""".lower()
input_text2 = """
Paragraphs are the building blocks of papers. 
Many students define paragraphs in terms of length:
The next movement in paragraph development is an explanation of 
each example and its relevance to the topic sentence and rationale
 that were stated at the beginning of the paragraph. 
 was to be the umpire of the race. As the race began, the rabbit 
raced way ahead of the turtle, just like everyone thought.
The rabbit got to the halfway point and could not see the turtle 
anywhere. He was hot and tired and decided to stop and take a short 
nap. Even if the turtle passed him, he would be able to race to the
finish line ahead of him. All this time the turtle kept walking step 
by step by step. He never quit no matter how hot or tired he got. 
He just kept going. 
However, the rabbit slept longer than he had thought and woke up. 
He could not see the turtle anywhere! He went at full speed to 
the finish line but found the turtle there waiting for him.
 This explanation shows readers why you chose to use this/or these particular 
 examples as evidence to support the major claim, or focus, in your paragraph.
Continue the pattern of giving examples and explaining them until all points/examples 
that the writer deems necessary have been made and explained. NONE of your examples 
should be left unexplained. You might be able to explain the relationship between the
 example and the topic sentence in the same sentence which introduced the example. 
 More often, however, you will need to explain that relationship in a separate sentence.
 Look at these explanations for the two examples in the slave spirituals paragraph:
""".lower()
"""
TODO:
1. unify case, i.e., ==> lower   done
2. remove irrelevant words, the, a, is, was, 
3. remove propositions
"""


def filter(input_txt):
    irrelevant_words = {".", "," , "\n", " the ", " a ", " and "," is "," him "," of ", " was ", " he ", " at ", " to ", " for ", " can "," how "," could "}
    for iw in irrelevant_words:
        input_txt = input_txt.replace(iw, " ")
    return input_txt


def hist(input_txt, word_histogram):
    mx=0
    wod = " "
    for word in word_histogram:
        if word_histogram[word] > mx:
            mx = word_histogram[word]
            wod = word

    return wod


def dic(word_list):
    word_histogram = {}
    for word in word_list:
        if word not in word_histogram.keys():
            word_histogram[word] = 1
        else:
            word_histogram[word] = word_histogram[word]+1
    word_histogram.pop("")
    return word_histogram


input_text = filter(input_text)
word_list = input_text.split(" ")
word_histogram = dic(word_list)
wod_list = []
for i in range(6):
    wod_list = wod_list + [hist(word_histogram,word_histogram)]
    word_histogram.pop(hist(word_histogram,word_histogram))

word_histogram.clear()

input_text2 = filter(input_text2)
word_list2 = input_text2.split(" ")
word_histogram2 = dic(word_list2)

wod_list2 = []

for i in range(6):
    wod_list2 = wod_list2+[hist(word_histogram2,word_histogram2)]
    word_histogram2.pop(hist(word_histogram2,word_histogram2))

print(wod_list)

print(wod_list2)
counter = 0

for i in range(6):
    for j in range(6):
        if wod_list[j] == wod_list2[i]:
            counter = counter + 1

if counter > 2:
    print("both paragraph are related")
else:
    print("both paragraph are not related")
