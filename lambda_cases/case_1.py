def lamb_case_1():
    list_of_names = ['Ala', 'Jola', 'Marzena', 'Jan', 'Marek']
    print('Case_1A')
    a_list = sorted(list_of_names, key=lambda name: len(name))
    print(list_of_names)
    print(a_list)
    print('\nCase_1B')
    b_list = sorted(list_of_names, key=lambda name: len(name), reverse=True)
    print(b_list)
    print('\nCase_1C')
    c_list = sorted(list_of_names)
    print(c_list)
