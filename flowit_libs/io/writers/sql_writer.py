import polars as pl
from flowit.core import IStep


class SQLWriter(IStep):

    def __init__(self, table: str, connection_string: str):
        self._table = table
        self._connection_string = connection_string

    def process(self, df: pl.DataFrame):
        df.write_database(self._table, self._connection_string)

