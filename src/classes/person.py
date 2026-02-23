from datetime import datetime

from typing import Literal

class Person:
    def __init__(
        self, 
        first_name: str,
        last_name: str ,
        birdthday: datetime,
        has_hair: bool,
        gender: Literal['male', 'female', 'other'],
        hair_color: str = None,
    ):
        self._first_name = first_name
        self._last_name = last_name
        self._birdthday = birdthday
        self._has_hair = has_hair
        self._hair_color = hair_color
        self._gender = gender

        if self._has_hair and self._hair_color == None:
            raise ValueError(f'{self._first_name} has hair, you must set the color...!!!')

    def get_age(
        self
    ) -> int:
        today = datetime.now()
        birthday = self._birdthday
        age: int = today.year - birthday.year

        if today.month < birthday.month:
            return age - 1
        elif today.month > birthday.month:
            if today.day >= birthday.day:
                return age
            elif today.day < birthday.day:
                return age - 1
        elif today.month == birthday.month:
            if today.day < birthday.day:
                return age - 1
        
        return age

    @property
    def first_name(self) -> str:
        return self._first_name
    
    @property
    def last_name(self) -> str:
        return self._last_name
    
    @property
    def birdthday(self) -> datetime:
        return self._birdthday
    
    @property
    def birdthday_str(self) -> str:
        return self._birdthday.strftime('%Y-%m-%d')
    
    @property
    def hair(self) -> str:
        if self._has_hair:
            return self._hair_color
        return 'No hair'

    @property
    def gender(self) -> str:
        return self._gender