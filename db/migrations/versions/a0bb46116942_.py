"""empty message

Revision ID: a0bb46116942
Revises: 
Create Date: 2023-10-15 02:17:28.965399

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a0bb46116942'
down_revision = None
branch_labels = None
depends_on = None

from sqlalchemy import create_engine
from sqlalchemy.sql import text
import json

# Замените эту строку подключения на свою
db_connection = 'postgresql://username:password@localhost:5432/your_database'

documents = [
    {
        'title': 'Отчет за март',
        'department': 'Бухгалтерия',
        'status': 'Принято',
        'date': '01.04.2023',
    },
    {
        'title': 'Презентация нового продукта',
        'department': 'Маркетинг',
        'status': 'В работе',
        'date': '05.04.2023',
    },
    {
        'title': 'Исправление ошибок на сайте',
        'department': 'IT',
        'status': 'Новые',
        'date': '10.04.2023',
    },
    {
        'title': 'Отчет за март',
        'department': 'Бухгалтерия',
        'status': 'Принято',
        'date': '01.04.2023',
    },
    {
        'title': 'Презентация нового продукта',
        'department': 'Маркетинг',
        'status': 'В работе',
        'date': '05.04.2023',
    },
    {
        'title': 'Исправление ошибок на сайте',
        'department': 'IT',
        'status': 'Новые',
        'date': '10.04.2023',
    },
    {
        'title': 'Отчет за март',
        'department': 'Бухгалтерия',
        'status': 'Принято',
        'date': '01.04.2023',
    },
    {
        'title': 'Презентация нового продукта',
        'department': 'Маркетинг',
        'status': 'В работе',
        'date': '05.04.2023',
    },
    {
        'title': 'Исправление ошибок на сайте',
        'department': 'IT',
        'status': 'Новые',
        'date': '10.04.2023',
    },
    {
        'title': 'Отчет за март',
        'department': 'Бухгалтерия',
        'status': 'Принято',
        'date': '01.04.2023',
    },
    {
        'title': 'Презентация нового продукта',
        'department': 'Маркетинг',
        'status': 'В работе',
        'date': '05.04.2023',
    },
    {
        'title': 'Исправление ошибок на сайте',
        'department': 'IT',
        'status': 'Новые',
        'date': '10.04.2023',
    },
    {
        'title': 'Отчет за март',
        'department': 'Бухгалтерия',
        'status': 'Принято',
        'date': '01.04.2023',
    },
    {
        'title': 'Презентация нового продукта',
        'department': 'Маркетинг',
        'status': 'В работе',
        'date': '05.04.2023',
    },
    {
        'title': 'Исправление ошибок на сайте',
        'department': 'IT',
        'status': 'Новые',
        'date': '10.04.2023',
    },
    {
        'title': 'Отчет за март',
        'department': 'Бухгалтерия',
        'status': 'Принято',
        'date': '01.04.2023',
    },
    {
        'title': 'Презентация нового продукта',
        'department': 'Маркетинг',
        'status': 'В работе',
        'date': '05.04.2023',
    },
    {
        'title': 'Исправление ошибок на сайте',
        'department': 'IT',
        'status': 'Новые',
        'date': '10.04.2023',
    },
    {
        'title': 'Отчет за март',
        'department': 'Бухгалтерия',
        'status': 'Принято',
        'date': '01.04.2023'
    },
    {
        'title': 'Презентация нового продукта',
        'department': 'Маркетинг',
        'status': 'В работе',
        'date': '05.04.2023'
    },
    {
        'title': 'Исправление ошибок на сайте',
        'department': 'IT',
        'status': 'Новые',
        'date': '10.04.2023',
    },
]


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('history',
                    sa.Column('title', sa.String(), nullable=True),
                    sa.Column('department', sa.String(), nullable=True),
                    sa.Column('status', sa.String(), nullable=True),
                    sa.Column('time', sa.String(), nullable=True),
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'),
                              nullable=False),
                    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'),
                              nullable=False),
                    sa.PrimaryKeyConstraint('id', name=op.f('pk_history')),
                    sa.UniqueConstraint('id', name=op.f('uq_history_id'))
                    )

    for record in documents:
        op.execute(f'''INSERT INTO history (title, department, status, time) VALUES ('{record['title']}', '{record['department']}', '{record['status']}', '{record['date']}');''')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('history')
    # ### end Alembic commands ###
