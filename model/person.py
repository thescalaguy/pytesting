import datetime

import peewee

from model import db


class Person(peewee.Model):

    MAX_AGE = 120

    class Meta:
        database = db

    id = peewee.BigAutoField(primary_key=True, null=False)
    name = peewee.CharField(null=False, max_length=120)
    dob = peewee.DateField(null=False)

    @property
    def age(self) -> int:
        return (datetime.date.today()).year - self.dob.year
