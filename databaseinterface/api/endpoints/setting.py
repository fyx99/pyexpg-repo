import psycopg2
from psycopg2 import sql
from fastapi import APIRouter

from databaseinterface.config import CONNECTION_DETAILS

setting_router = APIRouter()


@setting_router.post("/createdb")
def createdb():
    conn = None
    try:
        CONNECTION_DETAILS_neutral = CONNECTION_DETAILS.copy()
        CONNECTION_DETAILS_neutral["dbname"] = "postgres"
        conn = psycopg2.connect(**CONNECTION_DETAILS_neutral)
        conn.set_isolation_level( psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT )
        cursor = conn.cursor()
        DB_NAME = "MAIN"
        cursor.execute(sql.SQL("DROP DATABASE IF EXISTS {}").format(sql.Identifier( DB_NAME )))
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier( DB_NAME )))
        cursor.close()
    except Exception as e:
        return repr(e)
    finally:
        if conn is not None:
            conn.close()
    return "Created Database"

    
@setting_router.post("/createtables")
def createtables():
    conn = None
    try:
        conn = psycopg2.connect(**CONNECTION_DETAILS)
        cursor = conn.cursor()
        cmd = """
            CREATE TABLE ticker (
                ticker_symbol VARCHAR(10) PRIMARY KEY,
                ticker_name VARCHAR(255) NOT NULL
            )
        """
        cursor.execute(sql.SQL(cmd))
        cursor.close()
        conn.commit()
    except Exception as e:
        return repr(e)
    finally:
        if conn is not None:
            conn.close()
    return "Tables Created"