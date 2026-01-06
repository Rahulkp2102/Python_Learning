#Reverse words in a sentence without using split()

sentence = input("Enter a sentence: ")

words_list = []
word = ''
for char in sentence:
    if char != " ":
        word += char
    else:
        words_list.append(word)
        word = ''
words_list.append(word)  
print(words_list)

reversed_sentence = ''
for word in words_list[::-1]:
    reversed_sentence += word + ' '
print(reversed_sentence)


# user_input = input('enter the word:')
# for i,j in enumerate(user_input):
#     #print(i,j)
#     i = 0
#     while i <= len(user_input):
#         if user_input[i] == j:
#            print(i)
#            i += 1
#         else:
#             i += 1
     
