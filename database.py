import sqlalchemy
# print(sqlalchemy.__version__)
from sqlalchemy import create_engine,text ,bindparam
import os
# engine = create_engine("mysql+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")
db_con_str = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_con_str,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })
# if(engine.connect()): print('working')

def from_database():
    with engine.connect() as conn:
        result = conn.execute(text ("select * from jobs"))
        result_dicts =[]
        for row in result.all():
            result_dicts.append(dict(row._mapping))
        return (result_dicts)
def from_database_job(id):
    with engine.connect() as conn:
        t = f'SELECT * FROM jobs WHERE id = {id}'
        stmt = text(t)
#  bindparams :val

        result = conn.execute(
            stmt)
        row = result.all()
        if len(row)==0:
            return None
        else:
            return(dict(row[0]._mapping))