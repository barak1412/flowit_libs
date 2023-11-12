import polars as pl
from flowit.core import IStep
from flowit_libs.io.readers.constants import OUTPUT_DATAFRAME_NAME


class SQLReader(IStep):

    def __init__(self, query: str, connection_string: str):
        self._query = query
        self._connection_string = connection_string

    def process(self):
        pl_df = pl.read_database_uri(self._query, self._connection_string)
        return {OUTPUT_DATAFRAME_NAME: pl_df}

