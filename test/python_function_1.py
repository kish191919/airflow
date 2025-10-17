def regist(name,sex, *args):
    print(type(args))
    country = args[0] if len(args) > 0 else None
    city = args[1] if len(args) > 1 else None
    print(f'name: {name}')
    print(f'sex: {sex}')
    if country is not None:
        print(f'country: {country}')
    if city is not None:
        print(f'city: {city}')

regist('danny', 'man')
regist('hyunjoo', 'girl', 'korea', 'seoul')

print('---------------------')


def some_func(**kwargs):
    print(type(kwargs))
    print(kwargs)
    name = kwargs.get('name') or ''
    country = kwargs.get('country') or ''
    print(f'name: {name}, country:{country}')

some_func(name='danny', country='korea')
some_func(name='hyunjoo', city='seoul')