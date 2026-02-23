from datetime import datetime

from src.classes.person import Person

if __name__ == '__main__':
    print('begin process')
    print('')
    program_end: bool = False
    
    persons: list[Person] = []

    #region old code
    # carlos: Person = Person(
    #     first_name='Carlos',
    #     last_name='Hernadez',
    #     birdthday=datetime(1982, 8, 12),
    #     has_hair=False,
    #     gender='male'
    # )
    # persons.append(carlos)

    # nikole: Person = Person(
    #     first_name='Nikole',
    #     last_name='Shert',
    #     birdthday=datetime(2015, 11, 6),
    #     has_hair=True,
    #     gender='female',
    #     hair_color='brown',
    # )
    # persons.append(nikole)
    #endregion old code

    while not program_end:
        print('Do you want to create a new person?')
        print('y = yes')
        print('n = no')
        print('Please select an option (y / n), and press enter.')
        input_option: str = input()

        if input_option.lower() != 'y':
            program_end = True
        else:
            first_name: str = input('Please enter the first name: ')
            last_name: str = input('Please enter the last name: ')
            birdthday: datetime = datetime.strptime(input('Please enter the birdthday (YYYY-MM-DD)'), '%Y-%m-%d')
            has_hair: bool = input('Please enter the has hair (y = yes, n = no): ')
            gender: str = input('Please enter the gender (male, female, other): ')
            if has_hair.lower() == 'y':
                has_hair = True
                hair_color: str = input('Please enter the hair color: ')
            else:
                has_hair = False
                hair_color: str = None
            person: Person = Person(
                first_name=first_name,
                last_name=last_name,
                birdthday=birdthday,
                has_hair=has_hair,
                gender=gender,
                hair_color=hair_color,
            )
            persons.append(person)
    for person in persons:
        print('----------------------')
        print(f'first name: {person.first_name}')
        print(f'last name: {person.last_name}')
        print(f'gender: {person.gender}')
        print(f'age: {person.get_age()}')
        print(f'birdthday: {person.birdthday}')
        print(f'birdthday str: {person.birdthday_str}')
        print(f'hair: {person.hair}')
        # print('----------------------')
        print('')

    print('end process')