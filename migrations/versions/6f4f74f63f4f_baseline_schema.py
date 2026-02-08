"""baseline schema

Revision ID: 6f4f74f63f4f
Revises:
Create Date: 2026-02-08 18:45:00.000000

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "6f4f74f63f4f"
down_revision = None
branch_labels = None
depends_on = None

DEFAULT_PLANT_ID = "4544afe3-0661-11ef-9512-0242ac140002"


def upgrade():
    op.create_table(
        "plants",
        sa.Column(
            "id",
            sa.String(length=36),
            nullable=False,
            server_default=sa.text("(UUID())"),
        ),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("hex_color", sa.String(length=7), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.text("(NOW())"),
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )

    op.create_table(
        "user",
        sa.Column(
            "id",
            sa.String(length=36),
            nullable=False,
            server_default=sa.text("(UUID())"),
        ),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("password", sa.Text(), nullable=False),
        sa.Column(
            "active_plant_id",
            sa.String(length=36),
            nullable=True,
            server_default=sa.text(f"'{DEFAULT_PLANT_ID}'"),
        ),
        sa.ForeignKeyConstraint(["active_plant_id"], ["plants.id"], ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "sensors_records",
        sa.Column(
            "id",
            sa.String(length=36),
            nullable=False,
            server_default=sa.text("(UUID())"),
        ),
        sa.Column("soil_humidity", sa.Integer(), nullable=False),
        sa.Column("ambient_humidity", sa.Integer(), nullable=False),
        sa.Column("temperature", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("water_volume", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.text("CURRENT_TIMESTAMP"),
        ),
        sa.Column(
            "plant_id",
            sa.String(length=36),
            nullable=True,
            server_default=sa.text(f"'{DEFAULT_PLANT_ID}'"),
        ),
        sa.ForeignKeyConstraint(["plant_id"], ["plants.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "checklist_records",
        sa.Column(
            "id",
            sa.String(length=36),
            nullable=False,
            server_default=sa.text("(UUID())"),
        ),
        sa.Column("soil_ph", sa.Integer(), nullable=False),
        sa.Column("soil_humidity", sa.Integer(), nullable=False),
        sa.Column("air_humidity", sa.Integer(), nullable=False),
        sa.Column("water_consumption", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("temperature", sa.Numeric(precision=10, scale=1), nullable=False),
        sa.Column("illuminance", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("lai", sa.Numeric(precision=10, scale=2), nullable=True),
        sa.Column(
            "leaf_appearance",
            mysql.ENUM("SAUDAVEL", "MURCHA", "NÃO REGISTRADO"),
            nullable=True,
            server_default=sa.text("'NÃO REGISTRADO'"),
        ),
        sa.Column(
            "leaf_color",
            mysql.ENUM(
                "VERDE CLARO PREDOMINANTE",
                "VERDE ESCURO PREDOMINANTE",
                "VERDE CLARO COM ALGUMAS MANCHAS CLARAS",
                "VERDE CLARO COM VARIAS MANCHAS CLARAS",
                "VERDE CLARO COM ALGUMAS MANCHAS ESCURAS",
                "VERDE CLARO COM VARIAS MANCHAS ESCURAS",
                "VERDE ESCURO COM ALGUMAS MANCHAS CLARAS",
                "VERDE ESCURO COM VARIAS MANCHAS CLARAS",
                "VERDE ESCURO COM ALGUMAS MANCHAS ESCURAS",
                "VERDE ESCURO COM VARIAS MANCHAS ESCURAS",
                "OPACO PREDOMINANTE",
                "AVERMELHADO PREDOMINANTE",
                "NÃO REGISTRADO",
            ),
            nullable=True,
            server_default=sa.text("'NÃO REGISTRADO'"),
        ),
        sa.Column(
            "plantation_type",
            mysql.ENUM("PLANTIO INTERNO (FATEC)", "PLANTIO EXTERNO (CASA)"),
            nullable=True,
            server_default=sa.text("'PLANTIO INTERNO (FATEC)'"),
        ),
        sa.Column("fertilizer_expiration_date", sa.Date(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.text("CURRENT_TIMESTAMP"),
        ),
        sa.Column("report", sa.Text(), nullable=True),
        sa.Column(
            "plant_id",
            sa.String(length=36),
            nullable=True,
            server_default=sa.text(f"'{DEFAULT_PLANT_ID}'"),
        ),
        sa.ForeignKeyConstraint(["plant_id"], ["plants.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("checklist_records")
    op.drop_table("sensors_records")
    op.drop_table("user")
    op.drop_table("plants")
