word_list = ['hello','world','my','name','is','Anna']
char = 'o'

output = []
for i in range(0, len(word_list)):
    test_word = word_list[i]
    for l in range(0, len(test_word)):
        if (test_word[l] == char):
            output.append(test_word)
            break
print output