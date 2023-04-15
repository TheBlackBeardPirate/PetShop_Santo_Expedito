"""empty message

Revision ID: 3f41e229f6c6
Revises: c5e31c0602cd
Create Date: 2023-04-14 15:25:50.047204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f41e229f6c6'
down_revision = 'c5e31c0602cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('produto',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('codigo', sa.String(length=20), nullable=False),
    sa.Column('descricao', sa.String(length=50), nullable=False),
    sa.Column('unidade_medida', sa.String(length=20), nullable=False),
    sa.Column('medida', sa.Float(), nullable=False),
    sa.Column('quantidade_estoque', sa.Integer(), nullable=False),
    sa.Column('valor_custo', sa.Float(), nullable=False),
    sa.Column('valor_venda', sa.Float(), nullable=False),
    sa.Column('cor', sa.String(length=50), nullable=False),
    sa.Column('tipo', sa.String(length=50), nullable=False),
    sa.Column('fabricante', sa.String(length=50), nullable=False),
    sa.Column('quantidade_min_estoque', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('produto')
    # ### end Alembic commands ###
