import s3fs
from flowit_libs.io.readers.abstract_file_reader import AbstractFileReader


class S3Reader(AbstractFileReader):

    def __init__(self, path, endpoint_url, key, secret, extra_s3_params=None, partitioning='hive'):
        super().__init__(path=path, partitioning=partitioning)

        if extra_s3_params is None:
            self._fs = s3fs.S3FileSystem(endpoint_url=endpoint_url, key=key, secret=secret)
        else:
            self._fs = s3fs.S3FileSystem(endpoint_url=endpoint_url, key=key, secret=secret,
                                         s3_additional_kwargs=extra_s3_params)

    def get_file_system(self):
        return self._fs
