#!/usr/bin/env python3
"""A Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    all_document = []
    if mongo_collection is None:
        return []
    else:
        for document in mongo_collection.find():
            all_document.append(document)
        return all_document
