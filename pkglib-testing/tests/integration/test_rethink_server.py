import distutils
import pytest

pytest_plugins = ['pkglib_testing.fixtures.server.rethink']

requires_rethink = pytest.mark.skipif(distutils.spawn.find_executable('rethinkdb') is None,
                                      reason="rethinkdb missing from $PATH")

@requires_rethink
def test_rethink_server(rethink_server):
    assert rethink_server.check_server_up()
    assert rethink_server.conn.db == 'test'


FIXTURE_TABLES = [('tbl_foo', 'code'), ('tbl_bar', 'id')]

# Lots of tests needed here!

@requires_rethink
def test_rethink_empty_db(rethink_empty_db):
    pass