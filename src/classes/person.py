from datetime import datetime, date

from typing import Literal

class Person_Gender:
    male: str
    female: str
    other: str

    def __init__(
        self,
        male: str = 'male',
        female: str = 'female',
        other: str = 'other',
    ):
        self.male = male
        self.female = female
        self.other = other
    
    @property
    def __repr__(
        self
    ) -> str:
        return (
            f'Person_Gender=(male={self.male}, '
            f'female={self.female}, '
            f'other={self.other})'
        )

class Person:
    # _gender: Person_Gender()
    
    def __init__(
        self, 
        first_name: str,
        last_name: str ,
        birthday: datetime,
        has_hair: bool,
        # gender: Literal['male', 'female', 'other'],
        gender: Literal[Person_Gender().male, Person_Gender().female, Person_Gender().other],
        hair_color: str = None,
    ):
        self._first_name = first_name
        self._last_name = last_name
        self._birthday = birthday
        self._has_hair = has_hair
        self._hair_color = hair_color
        self._gender = gender

        if self._has_hair and self._hair_color == None:
            raise ValueError(f'{self._first_name} has hair, you must set the color...!!!')
    
    #region old code
    # def get_age(
    #     self
    # ) -> int:
    #     # today = datetime.now()
    #     today = date.today()
    #     birthday = self._birthday
    #     age: int = today.year - birthday.year

    #     #region old code
    #     # if today.month < birthday.month:
    #     #     return age - 1
    #     # elif today.month > birthday.month:
    #     #     if today.day >= birthday.day:
    #     #         return age
    #     #     elif today.day < birthday.day:
    #     #         return age - 1
    #     # elif today.month == birthday.month:
    #     #     if today.day < birthday.day:
    #     #         return age - 1
        
    #     # return age
    #     #endregion old code
    #     is_before_birthday = (today.month, today.year) < (birthday.month, birthday.year)
    #     return age - is_before_birthday
    #endregion old code

    @property
    def first_name(self) -> str:
        return self._first_name
    
    @property
    def last_name(self) -> str:
        return self._last_name
    
    @property
    def birthday(self) -> datetime:
        return self._birthday
    
    @property
    def birthday_str(self) -> str:
        return self._birthday.strftime('%Y-%m-%d')
    
    @property
    def age(self) -> int:
        today: today = date.today()
        age: int = today.year - self._birthday.year

        is_before_birthday: bool = (today.month, today.day) < (self._birthday.month, self._birthday.day)
        return age - is_before_birthday

    @property
    def hair(self) -> str:
        if self._has_hair:
            return self._hair_color
        return 'No hair'

    @property
    def gender(self) -> str:
        return self._gender

    @property
    def full_name(self) -> str:
        if (self._first_name and self._last_name):
            return f'{self._first_name} {self._last_name}'
        elif (self._first_name):
            return self._first_name
        elif (self._last_name):
            return self._last_name
        else:
            return 'No name'
