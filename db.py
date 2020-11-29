from pymongo import MongoClient
from helper import constants

client = MongoClient(constants.DB_ENDPOINT)

db = client.notes

notes_table = db.notes


def get_notes():
      cursor = notes_table.find({})

      notes = []

      for document in cursor:
            title = document["title"]
            content = document["content"]
            note = {"title": title, "content": content}
            notes.append(note)

      return notes

