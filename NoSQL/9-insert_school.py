#!/usr/bin/env python3
"""Function that inserts a new document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """Returns the new _id"""
    new_school = kwargs
    result = mongo_collection.insert_one(new_school)
    return result.inserted_id
