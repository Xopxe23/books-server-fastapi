"""create user

Revision ID: 79cae6f47a1f
Revises: 
Create Date: 2023-06-29 10:57:28.633833

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '79cae6f47a1f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books_user')
    # ### end Alembic commands ###
