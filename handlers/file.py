import random
import uuid
import logging
import lib_import
import datetime

from handlers.base import BaseHandler
from models.file import File
from lib.datastore_mapper.querymapper import DeleteMapper
from lib.datastore_mapper.querymapper import FileCounter


class FileHandler(BaseHandler):
    def generate_files(self):
        """
        generate_data method

        generate random file data so we can map it

        """

        # generate 500 file records
        total_records = 500
        messagelog = []

        for i in range(total_records):
            # create new file entity
            download_count = random.randint(1, 10)
            file_name = uuid.uuid4()
            new_file = File()
            new_file.name = str(file_name) + '.txt'
            new_file.download_count = download_count
            new_file.put()
            messagelog.append("File added: {0} - {1}".format(i, new_file.name))

        context = {'messagelog': messagelog}

        self.render_response('file.html', context=context)

    def count_files(self):
        """
        kick off the mapping task to generate download counts

        """
        file_counter_mapper = FileCounter(File)
        file_counter_mapper.metric_name = 'file_counter_totals'
        file_counter_mapper.start()

        download_counter_mapper = FileCounter(File,
                                              filters={'gt': ('download_count', 5)},
                                              deferred_batch_size=10)
        download_counter_mapper.metric_name = 'file_download_count_gt_5'
        download_counter_mapper.start()

        download_counter_le_5_mapper = FileCounter(File,
                                                   filters={'le': ('download_count', 5)},
                                                   deferred_batch_size=10)
        download_counter_le_5_mapper.metric_name = 'file_download_count_le_5'
        download_counter_le_5_mapper.start()

        context = {}
        self.render_response('file.html', context=context)

    def cleanup_files(self):
        """
        kick off the mapping task to generate download counts

        """
        mapper = DeleteMapper(File)
        mapper.start()

        return self.response.write('DeleteMapper started...')
