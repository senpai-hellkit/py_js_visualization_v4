import pymysql
from pymysql.cursors import DictCursor
from typing import Dict, List, Union

from config import env


class DataBase:
    def __init__(self, host: str = env['host'], user: str = env['user'],
                 password: str = env['password'], db_name: str = env['db_name']):
        self.connect = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db_name,
            charset='utf8mb4',
            cursorclass=DictCursor,
            autocommit=True
        )

    def create_database(self):
        self.connect.ping(reconnect=True)
        query: str = """
            create table if not exists random_gens (
                id int(11) primary key auto_increment,
                dttm datetime default current_timestamp,
                some_number int not null
            )
        """
        with self.connect.cursor() as cursor:
            cursor.execute(query)

    def insert_data(self, value: int):
        self.connect.ping(reconnect=True)
        query: str = f"""
            insert into random_gens (some_number)
            values ({value})
        """
        with self.connect.cursor() as cursor:
            cursor.execute(query)
        self.connect.commit()

    def get_data(self):
        self.connect.ping(reconnect=True)
        query: str = "select * from random_gens order by dttm desc limit 30"
        with self.connect.cursor() as cursor:
            cursor.execute(query)
            data: List[Dict[str, Union[str, int]]] = []
            for some_data in cursor.fetchall():
                some_data['dttm'] = some_data['dttm'].strftime("%d-%m-%Y %H:%M:%S")
                data.append(some_data)
        return data


db: DataBase = DataBase()
