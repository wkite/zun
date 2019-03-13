#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


"""add dns to container

Revision ID: 4c4ea24ddd43
Revises: 5f97e44127d6
Create Date: 2019-03-12 15:13:49.517406

"""

# revision identifiers, used by Alembic.
revision = '4c4ea24ddd43'
down_revision = '5f97e44127d6'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('container', sa.Column('dns', sa.String(32), nullable=True))
