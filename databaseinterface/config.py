import os

CONNECTION_DETAILS = {
    "dbname": os.environ.get("DB_NAME", default="MAIN"),
    "host": os.environ.get("DB_HOST", default="172.17.0.2"),
    "user": os.environ.get("DB_USER", default="postgres"),
    "password": os.environ.get("DB_PW", default="postgres"),
    "port": os.environ.get("DB_PORT", default="5432"),
}
