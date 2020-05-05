from sqlalchemy import (
    Table,
    Integer,
    Text,
    VARCHAR,
    MetaData,
    Column
)

meta = MetaData()

post = Table(
    'post', meta,
    Column('id', Integer, primary_key=True),
    Column('title', VARCHAR, nullable=False),
    Column('body', Text)
)