from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=10)),
    Column('email', VARCHAR(length=120)),
    Column('account', VARCHAR(length=100)),
    Column('authority', INTEGER),
    Column('passwd', VARCHAR(length=100)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=10)),
    Column('email', String(length=120)),
    Column('account', String(length=100)),
    Column('passwrd', String(length=100)),
    Column('authority', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['passwd'].drop()
    post_meta.tables['user'].columns['passwrd'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['passwd'].create()
    post_meta.tables['user'].columns['passwrd'].drop()
