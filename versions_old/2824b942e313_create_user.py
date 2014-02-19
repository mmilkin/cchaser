"""create user

Revision ID: 2824b942e313
Revises: None
Create Date: 2014-01-20 22:04:19.988232

"""

# revision identifiers, used by Alembic.
revision = '2824b942e313'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('user_name', sa.String(64), nullable=False, unique=True),
        sa.Column('password', sa.String(320)),
        sa.Column('role', sa.SmallInteger()),
    )


def downgrade():
    op.drop_table('user')
