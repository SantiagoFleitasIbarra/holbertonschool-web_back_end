#!/usr/bin/env python3
"""Python function that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Function that returns the list of school"""
    list_document = {"topics": topic}
    return mongo_collection.find_one(list_document)
