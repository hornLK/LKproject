"""empty message

Revision ID: 1d0cc801c49f
Revises: 56d773b3060b
Create Date: 2018-01-10 22:08:57.094228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d0cc801c49f'
down_revision = '56d773b3060b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('networks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('netname', sa.String(length=64), nullable=True),
    sa.Column('vlan', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_networks_netname'), 'networks', ['netname'], unique=True)
    op.create_index(op.f('ix_networks_vlan'), 'networks', ['vlan'], unique=False)
    op.create_table('ips',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip', sa.String(length=64), nullable=True),
    sa.Column('mac', sa.String(length=64), nullable=True),
    sa.Column('ports', sa.Text(), nullable=True),
    sa.Column('network_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['network_id'], ['networks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ips_ip'), 'ips', ['ip'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ips_ip'), table_name='ips')
    op.drop_table('ips')
    op.drop_index(op.f('ix_networks_vlan'), table_name='networks')
    op.drop_index(op.f('ix_networks_netname'), table_name='networks')
    op.drop_table('networks')
    # ### end Alembic commands ###