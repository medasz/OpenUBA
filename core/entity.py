'''
Copyright 2019-Present The OpenUBA Platform Authors
This file is part of the OpenUBA Platform library.
The OpenUBA Platform is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
The OpenUBA Platform is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public License
along with the OpenUBA Platform. If not, see <http://www.gnu.org/licenses/>.
'''

'''
@name entity
@description purposed for entity management
'''

import logging
from database import DBRead, DBWrite
from typing import Dict, Tuple, Sequence, List


'''
@name
@description
'''
class Entity():
    def __init__(self):
        logging.info("Entity is initiated")

'''
@name EntitySet
@description wrapper to hold a set of entities
'''
class EntitySet():
    def __init__(self):
        pass

'''
@name GetAllEntities
@description fetch all entities from the actual DB
'''
class GetAllEntities(DBRead):
    def get(self) -> dict:
        logging.info("read_user")
        entities = self.read()
        return {"entity1": {}, "entity2": {}}
