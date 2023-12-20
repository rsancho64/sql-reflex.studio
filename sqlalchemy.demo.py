import sqlalchemy
print(sqlalchemy.__version__)

# https://docs.sqlalchemy.org/en/20/tutorial/engine.html

from sqlalchemy import create_engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

# https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
    )

## conn

