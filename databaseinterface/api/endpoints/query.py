import psycopg2
from psycopg2 import sql
from pydantic import BaseModel
from fastapi import APIRouter

from databaseinterface.config import CONNECTION_DETAILS

query_router = APIRouter()

class SqlCommand(BaseModel):
    command: str

@query_router.post("/sql")
def query_sql(sqlCommand: SqlCommand):
    conn = None
    rows = None
    try:
        conn = psycopg2.connect(**CONNECTION_DETAILS)
        conn.set_isolation_level( psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT )
        cursor = conn.cursor()
        cursor.execute(sql.SQL(sqlCommand.command))
        if cursor.statusmessage.startswith("SELECT"):
            rows = cursor.fetchall()
        cursor.close()
        cursor.commit()
    except Exception as e:
        return repr(e)
    finally:
        if conn is not None:
            conn.close()
    return rows

