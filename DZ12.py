# my_list = [42, 43]
# my_dict = {
#    'foo': {
#       'a': 12,
#       'b': (1, 2, 3, 4, my_list)
#    },
#    'bar': {
#       'c': 12,
#       'd': {5, 6, 7, 8}
#    },
#    'moo': {
#       'e': 12,
#       'f': {'Lol': ['L', 'o', 'l']}
#    },
# }
# # 1
# print(my_dict['foo'])
# # 2
# print(my_dict['foo']['b'])
# # 3
# my_list.append(44)
# # 4
# print(my_dict['foo']['b'])
# # 5
# print(my_dict['bar']['d'])
# # 6
# my_dict['bar']['d'].add(9)
# # 7
# print(my_dict['bar']['d'])
# # 8
# my_dict['moo']['f']['Lol'].pop(1)
# print(my_dict['moo']['f']['Lol'])
# # 9
# my_dict['moo']['f'].update({'K': ['K', 'e', 'k']})
# print(my_dict['moo']['f'])
# # 10
# my_dict.clear()
# print(my_dict)