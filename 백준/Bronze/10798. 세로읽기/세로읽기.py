list_words = []
result = ''

for _ in range(5):
    list_words.append(list(map(str, input())))

len_max = max(len(list_words[i]) for i in range(5))

for i in range(len_max):
    for j in range(5):
        try:
            result += list_words[j][i]
        except:
            pass

print(result)