# d = {}
# d['Давид'] = 'dell'
# d['Сергей'] = 'asus'
# d.update({'Юлия': 'asus', 'Светлана': 'hp'})
# print(d['Светлана'])
# # del d['Светлана']
# d.pop('Светлана')
# print(d)
# print(d.keys())
# print(d.items())
# print(d.values())
# for k in d.keys():
#     print(k)
# attendance = {
#     'Kuptsevich': {
#         '01.04': 'ok',
#         '04.04': 'ok'
#     },
#     'Vidnikevich': {
#         '01.04': 'ok',
#         '04.04': 'ok'
#     }
# }
# print(attendance.keys())
# print(attendance['Vidnikevich'])
# print(attendance['Vidnikevich']['01.04'])

my_list = [42, 43]
my_dict = {
   'foo': {
      'a': 12,
      'b': (1, 2, 3, 4, my_list)
   },
   'bar': {
      'c': 12,
      'd': {5, 6, 7, 8}
   },
   'moo': {
      'e': 12,
      'f': {'Lol': ['L', 'o', 'l']}
   },
}
print(my_dict['foo'])
print(my_dict['foo']['b'])
my_list.append(44)
print(my_dict['foo']['b'])
print(my_dict['bar']['d'])