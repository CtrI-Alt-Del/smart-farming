from infra.constants import MYSQL
from .mysql import MySQL

mysql = MySQL()


def init_database():
    return
    tables_names = list(MYSQL["tables"].keys())
    tables_sql = list(MYSQL["tables"].values())
    inserts = MYSQL["inserts"]

    tables_names.reverse()

    for table_name in tables_names:
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
        if table_exists:
            mysql.mutate(
                sql=f"DROP TABLE {table_name};",
                params=[],
            )

    for sql in tables_sql:
        mysql.mutate(
            sql=sql,
            params=[],
        )

    for insert in inserts:
        mysql.mutate(
            sql=insert,
            params=[],
        )
