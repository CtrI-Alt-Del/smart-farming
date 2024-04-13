from .mysql import MySQL

from infra.constants.mysql_tables import MYSQL_TABLES

mysql = MySQL()


def init_database():
    for table_name, table_sql in MYSQL_TABLES.items():
        table_exists = bool(
            mysql.query(
                sql=f"""
                SELECT EXISTS (
                  SELECT 1 
                  FROM information_schema.tables 
                  WHERE table_name = '{table_name}'
                ) 
                AS table_exists;
                """,
            )["table_exists"]
        )

        if not table_exists:
            mysql.mutate(
                sql=table_sql,
                params=[],
            )
