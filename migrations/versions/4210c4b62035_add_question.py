"""Add Question

Revision ID: 4210c4b62035
Revises: 1c28d5831b2b
Create Date: 2020-05-08 11:12:15.411511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4210c4b62035'
down_revision = '1c28d5831b2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=64), nullable=True),
    sa.Column('right_answer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['right_answer_id'], ['country.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_question_type'), 'question', ['type'], unique=False)
    op.create_table('q_c_association_table',
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('question_id', 'country_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('q_c_association_table')
    op.drop_index(op.f('ix_question_type'), table_name='question')
    op.drop_table('question')
    # ### end Alembic commands ###
