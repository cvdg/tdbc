import duckdb


def test_duckdb():
    results = duckdb.sql("SELECT 42").fetchall()
    assert results == [(42,)]
