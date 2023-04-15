"""empty message

Revision ID: 65446621209f
Revises: 3f41e229f6c6
Create Date: 2023-04-14 20:50:53.762787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65446621209f'
down_revision = '3f41e229f6c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('venda',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('valor_total', sa.Float(), nullable=False),
    sa.Column('valor_custo', sa.Float(), nullable=False),
    sa.Column('valor_lucro', sa.Float(), nullable=False),
    sa.Column('met_pagamento', sa.String(length=50), nullable=False),
    sa.Column('data_hora', sa.DateTime(), nullable=False),
    sa.Column('cliente_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cliente_id'], ['cliente.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venda')
    # ### end Alembic commands ###