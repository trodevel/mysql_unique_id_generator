#!/usr/bin/python3

'''
MySQL Unique Id Generator.

Copyright (C) 2023 Dr. Sergey Kolevatov

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

'''

import python_mysql_executor.db
from python_mysql_executor.db import DB
from aux_logger.aux_logger import create_timed_rotating_logger

##########################################################

def set_logger( l ):
    python_mysql_executor.db.set_logger( l )

##########################################################

class UniqueIdGenerator:

    def __init__(self, user: str, password: str, host: str, db: str, sql_path: str ):
        self.db = DB( user, password, host, db, sql_path )

    def init_table( self ) -> None:
        self.db.execute_query_from_file( "create_table_sequence_gen.sql" )

    def generate_id( self ) -> int:
        all_res = self.db.execute_query_from_file( "create_table_users.sql" )

        if len( all_res ) == 0:
            return 0

        res = all_res[0][0]

        return res
