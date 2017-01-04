# -*- coding: utf-8 -*-
"""py.test tests on utilities.database PostreSQL class

.. moduleauthor:: Mathew Topper <mathew.topper@tecnalia.com>
"""

import pytest
from sqlalchemy.engine import Engine

from aneris.utilities.database import PostgreSQL, check_host_port

# pytestmark = pytest.mark.skipif(True,
                                # reason="Boring")

# Skip is psycopg2 or requests is missing
pytest.importorskip("psycopg2")
requests = pytest.importorskip("requests")

# Try to get a remote test DB, otherwise skip.
headers = {'Accept': 'application/json'}

try:
    details = requests.get("http://api.postgression.com",
                          headers=headers,
                          timeout=10).json()               
    port_open, _ = check_host_port(details['host'],  details['port'])
except:
    port_open = False

                            
@pytest.mark.skipif(port_open == False,
                    reason="Can't connect to remote DB")
class TestPostgresDB:

    # Using a py.test fixture to reduce boilerplate and test times.
    @pytest.fixture(scope="module")
    def database():
        
        db_adapter = "psycopg2"
     
        credentials = {'host':      details['host'],
                       'dbname':    details['dbname'],
                       'user':      details['username'],
                       'pwd':       details['password'],
                       'port':      details['port']
                       }
                       
        database = PostgreSQL(db_adapter)
        database.set_credentials(credentials)
                       
        database.configure()
        
        return database
    
    def test_connect(database):
        
        assert isinstance(database._engine, Engine)
        
    def test_get_table_names(database):
    
        tnames = database.get_table_names()
        
        assert 'pg_user' in tnames
        
    #def test_reflection(test_db, test_table="test_mapping"):
    #
    #    if not test_db.has_permission(test_table):
    #        
    #        errStr = ("User does not have permission to access "
    #                  "table {}").format(test_table)
    #        ValueError( errStr)
    #
    #    testtable = test_db.reflect_table("test_mapping")
    #    
    #    # rudimentary relationships are produced
    #    for c in testtable.columns:
    #        
    #        print c.name
    #        
    #    assert False
    #            
