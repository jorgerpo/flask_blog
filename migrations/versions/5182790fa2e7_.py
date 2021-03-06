"""empty message

Revision ID: 5182790fa2e7
Revises: b53f0dd2474
Create Date: 2015-02-17 23:21:43.265846

"""

# revision identifiers, used by Alembic.
revision = '5182790fa2e7'
down_revision = 'b53f0dd2474'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('image', sa.String(length=255), nullable=True))
    op.alter_column('post', 'live',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column('user', 'is_author',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'is_author',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('post', 'live',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.drop_column('post', 'image')
    ### end Alembic commands ###
