from benedict import benedict
d = benedict()

# установить значения по пути
d['profile.firstname'] = 'Fabio'
d['profile.lastname'] = 'Caccamo'
d 
# { 'profile':{ 'firstname':'Fabio', 'lastname':'Caccamo' } }
d['profile']
# { 'firstname':'Fabio', 'lastname':'Caccamo' }

# проверка существования пути к ключу
'profile.lastname' in d
# True
print(d)
# удаление значения по пути
del d['profile.lastname']
print(d)

#data = {
#    'awesome.com': 'https://awesome.com',
#    'skills': {
#        'programming': {
#            'Python': '5 stars',
#            'JavaScript': '4 stars',
#        }
#    }
#}
data = {
    'name': 'Josh',
    'occupation': 'Data scientist',
    'skills': {
        'programming': {
            'Python': '5 stars',
            'JavaScript': '4 stars',
            'Java': '3 stars'
        },
        'frameworks': ['Django', 'React', 'Spring']
    }
}

data=benedict(data)

print(data)


if 'skills.programming.Java' in data:
    print(data['skills.programming.Java'])
    # '3 stars'

    # или эквивалентно
    print(data['skills', 'programming', 'Java'])
    # '3 stars'

# путь к несуществующему ключу
print('skills.softskills.managing' in data)
# False

# можно также использовать `.get(...)`
print(data.get('skills.softskills.managing'))
# None

# можно добавлять пути
data['skills.softskills.managing'] = '5 stars'
print(data['skills', 'softskills', 'managing'])
# '5 stars'

# вывод словаря в читаемом виде
print(data.dump())