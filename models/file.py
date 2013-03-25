from google.appengine.ext import ndb
from datastore_mapper.mapper import Mapper
import lib_import


class File(ndb.Model):
    name = ndb.StringProperty(required=True)
    download_count = ndb.IntegerProperty(required=True)


class MetricEntity(ndb.Model):
    date = ndb.DateProperty(required=True, auto_now_add=True)
    file_count = ndb.IntegerProperty(required=True)
    download_count = ndb.IntegerProperty(required=True)


class DownloadCountMapper(Mapper):
    KIND = File

    def __init__(self):
        self.file_count = 0
        self.download_count = 0

    def map(self, file):
        self.file_count += 1
        self.download_count += file.download_count

    def finish(self):
        total = MetricEntity(file_count=self.file_count,
                             download_count=self.download_count)
        total.put()
