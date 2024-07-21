#!/usr/bin/python3

'''
Python MySQL Executor.

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

import unique_id_generator
import db_config
from aux_logger.aux_logger import create_timed_rotating_logger

unique_id_generator.set_logger( create_timed_rotating_logger( "logs/id_gen", "id_gen" ) )

##########################################################

def my_gen():
    return unique_id_generator.UniqueIdGenerator( db_config.USER, db_config.PASSWORD, db_config.HOST, db_config.MYDB, db_config.SQL_PATH )

##########################################################

def test_00():

    uig = my_gen()

##########################################################

def test_01():

    uig = my_gen()

    uig.create_table()

##########################################################

def test_02():

    uig = my_gen()

    id = uig.generate_id()

    print( f"test_02: id = {id}" )

##########################################################

def test_03():

    uig = my_gen()

    for s in range( 1, 10 ):
        id = uig.generate_id()

        print( f"test_03: id = {id}" )

##########################################################

def test():

    test_00()
    test_01()
    test_02()
    test_03()

##########################################################

if __name__ == "__main__":
   test()
