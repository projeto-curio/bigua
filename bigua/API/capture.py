import requests
import sqlalchemy
import xmltodict
from sqlalchemy import create_engine, MetaData
from collections import defaultdict
import datetime
from pathlib import Path
from utils import *

class Capture(object):
    
    def __init__(self,
                 schema,
                 database='projetocurio'
                 ):
        

        self.schema = schema
        self.database = database
        self.engine = self.connect_to_db()
        self.meta = self.load_db_schema()
        
        self.url = None
        self.data = None

    def connect_to_db(self):
        return create_engine(open(Path(__file__).absolute().parent.parent.parent / 'dbconfig.txt', 'r').read())

    def load_db_schema(self):

        metadata = MetaData()
        metadata.reflect(self.engine, schema='camara_v1')
        return metadata

    def request(self, url):

        data = requests.get(url)

        if data.status_code == 200:
            self.data = data.text
        else:
            self.data = None

    def xml_to_dict(self):    
        self.data = xmltodict.parse(self.data)

    def to_default_dict(self, list_of_dic):

        return [defaultdict(lambda: None, dic) for dic in force_list(list_of_dic)]
    
    def capture_data(self, url):
        
        self.request(url)
        self.xml_to_dict()
    
    def insert_data(self, list_of_dic, table):
        
        table_string = self.schema + '.' + table
        with self.engine.connect() as conn:
            print('inserting data')
            for dic in list_of_dic:
                conn.execute(self.meta.tables[table_string].insert(), dic)
            print('closing connection')

    def update_data(self, list_of_dic, table_name, key, force_insert=True):
        
        table_string = self.schema + '.' + table_name
        table = self.meta.tables[table_string]
        
        with self.engine.connect() as conn:
            print('updating data')
            
            for dic in list_of_dic:
                if self.check_existing_date(table_name, key, dic[key]):
                    conn.execute(table.update(whereclause=table.c[key]==dic[key]),
                                dic)
                elif force_insert:
                    conn.execute(table.insert(),
                                 dic)
            print('closing connection')
    
    def check_existing_date(self, table_name, key, value):
        
        table_string = self.schema + '.' + table_name
        table = self.meta.tables[table_string]
        with self.engine.connect() as conn:
            res = list(conn.execute(table.select().where(table.c[key] == value)))
        
        if len(res) > 0:
            return True
        else:
            return False