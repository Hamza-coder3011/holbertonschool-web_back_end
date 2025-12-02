#!/usr/bin/env python3
"""
Update the topics of a school document in MongoDB
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates all documents with the given school name,
    setting the topics field.

    Args:
        mongo_collection: pymongo collection object.
        name (str): Name of the school to update.
        topics (list of str): List of topics to set.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
