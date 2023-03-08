from django.shortcuts import render
from django.http import HttpResponse
from utils import db
import json

DB_SETTINGS = {
'database':'myLibrary_01',
'host':'localhost',
'port':'27017',
'username':'',
'password':''
}

# db_name, client = db.dbConnect(DB_SETTINGS)

def index(request):
  # db.insertBook(db_name)
  return HttpResponse(f"""SchoolCat Library System 🐈‍⬛""")

def getAllBooks(request):
  # gets all books
  book_db = db.BookDB(DB_SETTINGS)
  books = book_db.get_all()
  book_list = []
  for book in books:
     print(book)
     book_list.append(book)
  return HttpResponse(f"ALL BOOKS: {book_list}")

"""
addbook
  takes: http request
  returns:

  adds books details to the database
"""
def addBook(request):
  book_db = db.BookDB(DB_SETTINGS)
  result = book_db.create(db.book1)
  print(result)
  objID = "ObjectId:" + result
  
  return HttpResponse(f"{result} - {one}")


# IN BOOKS
def isInBooks(isbn, collection='books'):
    # database and collection code goes here
    client, coll = db.dbConnect(collection)
    # find code goes here
    cursor = coll.find({"ISBN-13":isbn})
    curList = list(cursor)
    print(len(curList))
    if len(curList) == 0:
        print("This book is not in our database")
        return False
        # insertDoc(bookData)
    else:
        print("--Already in the DB")
        return True
    # iterate code goes here
    for doc in cursor:
        print(doc)