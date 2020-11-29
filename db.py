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
        object_id = document["_id"]
        identifier = str(object_id)
        note = {
            "id": identifier,
            "title": title,
            "content": content
        }
        notes.append(note)

    return notes


def add_note(title, content):
    entry = {'title': title, 'content': content}
    object_id = notes_table.insert_one(entry).inserted_id
    new_note = {
        'title': title,
        'content': content,
        'id': str(object_id)
    }

    return new_note
