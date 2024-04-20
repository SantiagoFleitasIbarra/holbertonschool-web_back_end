#!/usr/bin/env python3
"""Function that changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """Function that changes all topics of a school"""
    name_school = {"name": name}
    list_topics = {"$set": {"topics": topics}}
    mongo_collection.update_many(name_school, list_topics)
