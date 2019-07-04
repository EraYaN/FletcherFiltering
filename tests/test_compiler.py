#  Copyright (c) 2019 Erwin de Haan. All rights reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  This file is part of the FletcherFiltering project

import mysql.connector
from . import test_settings
from pathlib import Path

def test_query(printer, test_class):
    printer('Started')
    if 'sql' in test_settings.TEST_PARTS:
        cnx = mysql.connector.connect(user=test_settings.MYSQL_USER, password=test_settings.MYSQL_PASSWORD,
                                      host=test_settings.MYSQL_HOST,
                                      database=test_settings.MYSQL_DATABASE)
    else:
        cnx = None
    test = test_class(printer, cnx, working_dir_base=Path('.'), clean_workdir=test_settings.CLEAN_WORKDIR)

    try:
        assert test.setup()
        assert test.run()
    finally:
        test.cleanup()

    cnx.close()
