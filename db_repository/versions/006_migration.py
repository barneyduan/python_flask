from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
project = Table('project', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('project_name', String(length=100)),
    Column('last_version', String(length=20)),
    Column('version_count', Integer),
)

note = Table('note', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('version', String(length=10)),
    Column('author', String(length=10)),
    Column('note', String(length=100)),
    Column('enable', Boolean),
    Column('user_id', Integer),
    Column('project_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['project'].create()
    post_meta.tables['note'].columns['enable'].create()
    post_meta.tables['note'].columns['project_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['project'].drop()
    post_meta.tables['note'].columns['enable'].drop()
    post_meta.tables['note'].columns['project_id'].drop()
