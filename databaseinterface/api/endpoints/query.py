import psycopg2
from psycopg2 import sql
from fastapi import APIRouter

from databaseinterface.config import CONNECTION_DETAILS

setting_router = APIRouter()


@setting_router.post("/sql")
def query_sql(sql: str):
    try:
        conn = psycopg2.connect(**CONNECTION_DETAILS)
        conn.set_isolation_level( psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT )
        cursor = conn.cursor()
        cursor.execute(sql.SQL(sql))
    except Exception as e:
        return repr(e)
    finally:
        cursor.close()
        conn.close()
    return "Created Database"

