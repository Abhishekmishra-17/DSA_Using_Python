s="aakknmlak"

# output = "m"
char_dict = dict()
for i in s:
    if i not in char_dict:
        char_dict[i]=1
    else:
        char_dict[i]+=1

for key, item in char_dict.items():
    if item ==1:
        print(key)
        break
