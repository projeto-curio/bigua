class Capture(object):
    
    def __init__(self,
                 url, 
                 schema,
                 table,
                 database='projetocurio'
                 ):
        
        self.url = url
        self.schema = schema
        self.table = table
        self.database = database
        self.engine = self.connect_to_db()
        self.meta = self.load_db_schema()
        self.table_string = schema + '.' + table
        
        self.data = None

    def connect_to_db(self):
        return create_engine('postgresql://uploaddata:VgyBhu876%%%@104.155.150.247:5432/projetocurio')

    def load_db_schema(self):

        metadata = MetaData()
        metadata.reflect(self.engine, schema='camara_v1')
        return metadata

    def request(self):

        data = requests.get(self.url)

        if data.status_code == 200:
            self.data = data.text
        else:
            self.data = None

    def xml_to_dict(self):    
        self.data = xmltodict.parse(self.data)

    def to_default_dict(self, list_of_dic):
        return [defaultdict(lambda: None, dic) for dic in list_of_dic]
    
    def prepare_data(self):
        
        self.request()
        self.xml_to_dict()
    
    def insert_data(self, list_of_dic):
        
        with self.engine.connect() as conn:
            print('inserting data')
            for dic in list_of_dic:
                conn.execute(self.meta.tables[self.table_string].insert(), dic)
            print('closing connection')
