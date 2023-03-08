from pymongo import MongoClient



# def dbConnect(database, host, port, username, password):
def dbConnect(db_settings):
  client = MongoClient(host=db_settings['host'],
                      port=int(db_settings['port']),
                      username=db_settings['username'],
                      password=db_settings['password']
                     )
  db_handle = client[db_settings['database']]   #db_handle 
  return db_handle, client

class BookDB:
    def __init__(self, db_settings):
        # self.client, self.db_handle = dbConnect
        self.client = MongoClient(host=db_settings['host'],
                      port=int(db_settings['port']),
                      username=db_settings['username'],
                      password=db_settings['password']
                     )
        self.db = self.client[db_settings['database']]
        self.collection = self.db['books']

    def get_all(self):
        return self.collection.find()

    def get_one(self, id):
        return self.collection.find_one({'_id': id})

    def create(self, book_data):
        result = self.collection.insert_one(book_data)
        return str(result.inserted_id)

    def update(self, id, book_data):
        result = self.collection.update_one({'_id': id}, {'$set': book_data})
        return result.modified_count > 0

    def delete(self, id):
        result = self.collection.delete_one({'_id': id})
        return result.deleted_count > 0









book1 = {
  "ISBN-13": "9780552779319",
  "Title": "Computing With Quantum Cats - From Colossus To Qubits",
  "Authors": [
    "John Gribbin"
  ],
  "Publisher": "Random House",
  "Year": "2015",
  "Language": "en",
  "BSMID": "BSM1001",
  "Interest_level": "UY",
  "Book_level": 0,
  "quantity": 1
  }


   