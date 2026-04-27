"""Timeslot Service"""

from peewee import (
    AutoField,
    BooleanField,
    ForeignKeyField,
    IntegerField,
    Model,
    SqliteDatabase,
    TimeField,
)

DB = SqliteDatabase("timeslot.db")


class BaseModel(Model):
    class Meta:
        database = DB


class DayOfWeek(BaseModel):
    """Справочник дней недели (внутренний)"""

    id = AutoField()
    day_number = IntegerField(unique=True, null=False)

    class Meta:
        db_table = "day_of_week"


class Schedule(BaseModel):
    """
    Расписание звонков для группы и подгруппы.
    external_group_id - Group Service
    external_subgroup_id - Subgroup Service
    day_of_week - день недели
    """

    id = AutoField()
    external_group_id = IntegerField(null=False)  # заглушка Group Service
    external_subgroup_id = IntegerField(
        null=False
    )  # заглушка Subgroup Service, 0 = группа в целом
    day_of_week = ForeignKeyField(DayOfWeek, backref="schedules", null=False)

    class Meta:
        indexes = (
            (("external_group_id", "external_subgroup_id", "day_of_week"), True),
        )


class Timeslot(BaseModel):
    """
    Временной слот – пара или перемена. Порядок задаётся order_number.
    """

    id = AutoField()
    schedule = ForeignKeyField(
        Schedule, backref="timeslots", on_delete="CASCADE", null=False
    )
    order_number = IntegerField(null=False)
    is_lesson = BooleanField(null=False)  # True = пара, False = перемена
    start_time = TimeField(null=False)
    end_time = TimeField(null=False)

    class Meta:
        indexes = ((("schedule", "order_number"), True),)


def verify_group_exists(group_id: int) -> bool:
    """Заглушка для Group Service"""
    return 1 <= group_id <= 20


def verify_subgroup_exists(subgroup_id: int) -> bool:
    """Заглушка для Subgroup Service"""
    return 0 <= subgroup_id <= 50


def create_tables():
    """Создаёт таблицы и заполняет дни недели"""
    with DB:
        DB.create_tables([DayOfWeek, Schedule, Timeslot])
        if not DayOfWeek.select().exists():
            for i in range(1, 8):
                DayOfWeek.create(day_number=i)


if __name__ == "__main__":
    create_tables()
