def check_database(db_path=None):
    from urllib.request import pathname2url
    import sqlite3

    try:
        db_uri = f"file:{pathname2url(db_path)}?mode=rw"
        conn = sqlite3.connect(db_uri, uri=True)
        conn.close()
        return True
    except sqlite3.OperationalError as err:
        print(err)
        return False

