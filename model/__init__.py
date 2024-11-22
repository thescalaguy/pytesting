from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    "postgres", user="postgres", password="my-secret-pw", host="localhost", port=5432
)
