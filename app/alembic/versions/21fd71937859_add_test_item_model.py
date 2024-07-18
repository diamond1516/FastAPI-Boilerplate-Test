"""add Test Item Model

Revision ID: 21fd71937859
Revises: 
Create Date: 2024-07-18 17:59:21.636478

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from utils.customs import FileField

# revision identifiers, used by Alembic.
revision: str = "21fd71937859"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "test_models",
        sa.Column(
            "file", FileField(length=255), nullable=True
        ),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("test_models")
    # ### end Alembic commands ###