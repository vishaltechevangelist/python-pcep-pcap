def create_person(*args, **kwargs):
    argument_count = len(args)
    if argument_count == 1:
        return_dict = {'name': args[0], 'age': None, 'address': None}
    elif argument_count == 2:
        return_dict = {'name': args[0], 'age': args[1], 'address': None}
    elif argument_count == 3:
        return_dict = {'name': args[0], 'age': args[1], 'address': args[2]}
    else:
        raise IndexError('IndexError')

    if len(kwargs) != 0 and kwargs['phone_number']:
        return_dict['phone_number'] = kwargs['phone_number']

    return return_dict

print(create_person('Vishal', 40, 'Ghaziabad', phone_number='9871680102'))
print(create_person('Vishal', 40))
print(create_person('Vishal', phone_number='9871680102'))
print(create_person())