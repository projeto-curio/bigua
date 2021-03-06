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
        return create_engine(open(Path(__file__).absolute().parent.parent / 'dbconfig.txt', 'r').read())

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
    
    def insert_data(self, list_of_dic, table_name, if_exists='replace', key=None):
        
        table_string = self.schema + '.' + table_name
        table = self.meta.tables[table_string]

        with self.engine.connect() as conn:
            print('inserting data')

            for dic in list_of_dic:
                if (key is None) or (if_exists == 'append'):
                    conn.execute(table.insert(), dic)
                else:
                    
                    if len(list(conn.execute(table.select().where(table.c[key] == dic[key])))) > 0:
                        if if_exists == 'replace':
                            conn.execute(table.update(whereclause=table.c[key]==dic[key]),
                                    dic)
                        elif if_exists == 'pass':
                            continue
                    else:
                        conn.execute(table.insert(), dic)

            
            print('closing connection')

 
    
