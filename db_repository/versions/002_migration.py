from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=10)),
    Column('email', String(length=120)),
    Column('account', String(length=100)),
    Column('passwd', String(length=100)),
    Column('authority', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['account'].create()
    post_meta.tables['user'].columns['authority'].create()
    post_meta.tables['user'].columns['passwd'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['account'].drop()
    post_meta.tables['user'].columns['authority'].drop()
    post_meta.tables['user'].columns['passwd'].drop()
