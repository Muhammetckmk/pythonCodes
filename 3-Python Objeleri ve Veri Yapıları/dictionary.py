#key - value

#41 => kocaeli 34 => istanbul

#sehirler = ['kocaeli','istanbul']
#plakalar = [41, 34]

#print(plakalar[sehirler.index('istanbul')])

#print(plakalar['kocaeli']) # => 41
#print(plakalar['istanbul']) #=> 34

plakalar = { 'samsun' : 55, 'Kahramanmaraş': 46 }

print(plakalar['samsun'])
print(plakalar['Kahramanmaraş'])

plakalar['Gaziantep'] = 6
plakalar['Niğde'] = 51

print(plakalar)

users = {
    'muhammetCakmak': {
        'age': 36,        
        'roles': ['user'],
        'email': 'mhmmt@gmail.com',
        'address': 'Samsun',
        'phone': '1231321'
    },
    'nimetCakmak': {
        'age': 31,
        'roles': ['admin','user'],
        'email': 'mckmk@gmail.com',
        'address': 'gaziantep',
        'phone': '1231321'
    }
}

print(users['nimetCakmak'])



