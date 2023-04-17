"""empty message

Revision ID: c5e31c0602cd
Revises: 
Create Date: 2023-04-13 23:07:48.039516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5e31c0602cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('endereco', sa.String(length=150), nullable=False),
    sa.Column('cidade', sa.String(length=30), nullable=False),
    sa.Column('uf', sa.String(length=2), nullable=False),
    sa.Column('cep', sa.String(length=8), nullable=False),
    sa.Column('tel_resid', sa.String(length=10), nullable=False),
    sa.Column('tel_cel', sa.String(length=11), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('rg', sa.String(length=8), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('nascimento', sa.Date(), nullable=False),
    sa.Column('is_premium', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('consulta',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('horario', sa.DateTime(), nullable=False),
    sa.Column('nome_cliente', sa.String(length=100), nullable=False),
    sa.Column('cpf_cliente', sa.String(length=11), nullable=False),
    sa.Column('cliente_premium', sa.Boolean(), nullable=False),
    sa.Column('nome_animal', sa.String(length=50), nullable=False),
    sa.Column('raca', sa.String(length=50), nullable=False),
    sa.Column('emergencia', sa.Boolean(), nullable=False),
    sa.Column('nome_vet', sa.String(length=100), nullable=False),
    sa.Column('vet_efetivo', sa.Boolean(), nullable=False),
    sa.Column('crmv', sa.String(length=8), nullable=False),
    sa.Column('valor', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('veterinario',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('crmv', sa.String(length=8), nullable=False),
    sa.Column('endereco', sa.String(length=150), nullable=False),
    sa.Column('cidade', sa.String(length=30), nullable=False),
    sa.Column('uf', sa.String(length=2), nullable=False),
    sa.Column('cep', sa.String(length=8), nullable=False),
    sa.Column('tel_emergencia', sa.String(length=11), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('hora_atendimento', sa.String(length=70), nullable=False),
    sa.Column('efetivo', sa.Boolean(), nullable=False),
    sa.Column('valor_pagar', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('animal',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('raca', sa.String(length=50), nullable=False),
    sa.Column('cor', sa.String(length=50), nullable=False),
    sa.Column('idade', sa.Integer(), nullable=False),
    sa.Column('alergico', sa.Boolean(), nullable=False),
    sa.Column('hora_comer', sa.String(length=50), nullable=False),
    sa.Column('racao', sa.String(length=50), nullable=False),
    sa.Column('registro', sa.String(length=50), nullable=False),
    sa.Column('cliente_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cliente_id'], ['cliente.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('animal')
    op.drop_table('veterinario')
    op.drop_table('consulta')
    op.drop_table('cliente')
    # ### end Alembic commands ###