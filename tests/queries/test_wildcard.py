from tests.helpers.base_query import BaseQuery
import pyarrow as pa


class Wildcard(BaseQuery):
    def __init__(self, printer, cnx, working_dir_base='/tmp', **kwargs):
        super().__init__(printer, cnx, working_dir_base, name=self.__class__.__name__, has_data_file=False, separate_work_dir=True, **kwargs)
        self.in_schema = pa.schema([('id', pa.int32(), False),
                                    ('string1', pa.string(), False),
                                    ('string2', pa.string(), False)])

        self.in_schema_pk = 'id'

        self.out_schema = pa.schema([('id', pa.int32(), False),
                                    ('string1', pa.string(), False),
                                    ('string2', pa.string(), False)])

        self.query = """select * FROM `{0}`""".format(self.name)

