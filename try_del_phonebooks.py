my_dic = {"Benjie": "040302020", "Allison":"020202002"}
# Is important here to cast because ".keys()" method returns a dict_keys object.
key_list = list(my_dic.keys())

# Iterate on the list:
print(my_dic)
num = input('Delete name: ')
for num in my_dic.keys():
    if num == my_dic[num]:
        del my_dic[num]
    


print(my_dic)
