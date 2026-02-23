from datetime import datetime

from src.classes.person import Person

if __name__ == '__main__':
    #region variables
    input_option: str = 'y'
    program_end: bool = False
    is_first_person: bool = True
    #endregion variables

    print('begin process')
    print('')
    
    persons: list[Person] = []

    #region old code
    # carlos: Person = Person(
    #     first_name='Carlos',
    #     last_name='Hernadez',
    #     birthday=datetime(1982, 8, 12),
    #     has_hair=False,
    #     gender='male'
    # )
    # persons.append(carlos)

    # nikole: Person = Person(
    #     first_name='Nikole',
    #     last_name='Shert',
    #     birthday=datetime(2015, 11, 6),
    #     has_hair=True,
    #     gender='female',
    #     hair_color='brown',
    # )
    # persons.append(nikole)
    #endregion old code

    while not program_end:
        if not is_first_person:
            print('')
            print('Do you want to create a new person?')
            print('y = yes')
            print('n = no')
            # print('Please select an option (y / n), and press enter.')
            print('Please select an option, and press enter.')
            input_option = input()

        if input_option.lower() != 'y' and input_option.lower() != 'yes':
            program_end = True
        else:
            first_name: str = input('Please enter the first name: ')
            last_name: str = input('Please enter the last name: ')
            # birthday: datetime = datetime.strptime(input('Please enter the birthday (YYYY-MM-DD)'), '%Y-%m-%d')
            birthday: datetime = datetime.strptime(input('Please enter the birthday (YYY-MM-DD): '), '%Y-%m-%d')
            has_hair: bool = input('Please enter the has hair (y = yes, n = no): ')
            if has_hair.lower() == 'y' or has_hair.lower() == 'yes':
                has_hair = True
                hair_color: str = input('Please enter the hair color: ')
            else:
                has_hair = False
                hair_color: str = None
            gender: str = input('Please enter the gender (male, female, other): ')
            while gender.lower() != 'male' and gender.lower() != 'female' and gender.lower() != 'other':
                gender: str = input('Please enter the gender (male, female, other): ')
            
            person: Person = Person(
                first_name=first_name,
                last_name=last_name,
                birthday=birthday,
                has_hair=has_hair,
                gender=gender,
                hair_color=hair_color,
            )
            persons.append(person)
            is_first_person = False

    for person in persons:
        # print('----------------------')
        print('-' * 22)
        # print(f'first name: {person.first_name}')
        # print(f'last name: {person.last_name}')
        print(f'full name: {person.full_name}')
        print(f'gender: {person.gender}')
        # print(f'age: {person.get_age()}')
        print(f'age: {person.age}')
        print(f'birthday: {person.birthday}')
        print(f'birthday str: {person.birthday_str}')
        print(f'hair: {person.hair}')
        # print('----------------------')
        print('')

    print('end process')