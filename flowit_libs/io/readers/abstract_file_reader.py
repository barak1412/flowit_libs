import polars as pl
from abc import abstractmethod
import pyarrow.dataset as ds
from flowit.core import IStep


class AbstractFileReader(IStep):

    def __init__(self, path, partitioning='hive'):
        self._path = path
        self._partitioning = partitioning

    @abstractmethod
    def get_file_system(self):
        pass

    def process(self):
        read_dataset = ds.dataset(self._path, partitioning=self._partitioning, filesystem=self.get_file_system())
        read_scanned_df = pl.scan_pyarrow_dataset(read_dataset)

        return {'df': read_scanned_df}




