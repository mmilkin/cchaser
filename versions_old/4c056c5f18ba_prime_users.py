"""prime users

Revision ID: 4c056c5f18ba
Revises: 2824b942e313
Create Date: 2014-01-20 23:24:49.387409

"""

# revision identifiers, used by Alembic.

revision = '4c056c5f18ba'
down_revision = '2824b942e313'

from sqlalchemy.sql import table, column
import sqlalchemy as sa
from alembic import op



def upgrade():

    user = table('user',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('user_name', sa.String(64), nullable=False, unique=True),
        sa.Column('password', sa.String(320)),
        sa.Column('role', sa.SmallInteger()),
    )
    op.execute(
        user.insert().values(
            user_name='redawn',
            role=1,
            password='$6$rounds=106743$Aerhh6b4o0Vm/zN3$nPE1YpiarhEG/vCFzNJxgFqdGo3C.UUZR7VpV1B3G/BYMMMprNMvYZCBiaoZQMbvLXCP5i2uPy/6bhrSdSvqI.'
        )
    )



def downgrade():
    user = table('user',
        column('id', Integer),
        column('user_name', String),
        column('password', String),
        column('role', SmallInteger),
    )
    op.execute(
        user.delete().where(user.c.user_name == 'redawn')
    )
