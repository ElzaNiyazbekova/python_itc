# a = {1, 2, 3, 4, 5}
# a.add('6')
# print(a)
# a.pop()
# print(a)

# dates_of_birth = {3, 10, 11, 7, 31, 21, 1, 10, 3, 5, 6,  6}
# dates_of_birth.discard(7)
# print(dates_of_birth)

# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 3, 6, 7, 9}
# print(set1.intersection(set2))
# print(set1.difference(set2))

# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu.update({'besh_barmak': 130})
# menu['lagman']=135
# print(menu)
# menu.pop('borsh')
# print(menu)

# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu.update({
#     'drinks':['Coca-cola', 'Sprite', 'Fanta'] })
# print(menu)

# s = {'pop', 'add', 'update', 'intersection', 'remove', 'difference',
# 'intersection_update', 'clear', 'discard', 'difference_update' }
# d = {'clear', 'get', 'keys', 'values', 'items', 'update', }
# print(d.intersection(s))

# my_friends = {
#     "Joomart": "+77555246810",
#     "Adinai": "+77555013579",
#     "Ermek": "+77777013579",
#     "Atai": "+77777246810",
#     "Alymbek": "+77555501234",
# }
# his_friends = {
    # "Lyazat": "+77551123456",
    # "Salavat": "+77552234567",
    # "Daniyar": "+77553345678",
    # "Bolot": "+77554456789",
    # "Alymbek": "+77555501234",
    # "Dastan": "+77556678912",
    # "Maksat": "+77557789012",
    # "Adinai": "+77555013579",

# my_friends.update({"Lyazat": "+77551123456",
#     "Salavat": "+77552234567",
#     "Daniyar": "+77553345678",
#     "Bolot": "+77554456789",
#     "Alymbek": "+77555501234",
#     "Dastan": "+77556678912",
#     "Maksat": "+77557789012",
#     "Adinai": "+77555013579"})
# print(my_friends)

# his_friends = {'Lyazat',
#     'Salavat',
#     'Daniyar',
#     'Bolot',
#     'Alymbek',
#     'Dastan',
#     'Maksat',
#     'Adinai'}


# my_friends = {"Joomart",
#     "Adinai",
#     "Ermek",
#     'Bolot',
#     'Alymbek',
#     'Dastan',
#     "Atai",
#     "Alymbek"}
# print(my_friends.intersection(his_friends))

# users = {}
# i = input('login')
# p = int(input('password'))
# users[i]=p
# print(users)   
       


# a = set()
# print(type(a))
# методы добавления
# a.add(2)
# a.update([1, 2, 4])

# методы удаления
# a.remove('asd')
# a.clear()
# a.discard('')
# print(a)

# методы сравнения
# a = {2, 'quart', 31, 43, 'asd', 2}
# b = {21, 'quart', 3, 4, 'asd', 2}
# print(b.difference(a))
# a.intersection_update(b)
# print(a.intersection(b))
# a.difference_update(b)

# a = {}
# методы добавления
# a.update({1: 23})
# a['hello'] = 'world'

# users = {
#     '0023846728':{
#     'user1': 'Asan',
#     'age': 13,
#     'phone':784683
#     }
#     }
# print(users.values())
# print(users.keys)
# from pprint import pprint 
# pprint(users)
# users = [('kiri', '12345')]
# print(users.get('02030407776'))
# login = input('vvedi login: ')
# password = input('vedi password: ')
# password_confirm = input('vedi password eshe raz: ')
# if not login.isdigit() and not login.isalpha():
#     if password == password_confirm:
#     users.append((login, password))
# for key, value in users.items():
#     print(key)







