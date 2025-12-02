#!/usr/bin/env python3
"""
Return the list of schools that have a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Lists all documents in the collection where
    'topics' contains the given topic.

    Args:
        mongo_collection: pymongo collection object.
        topic (str): Topic to search for.

    Returns:
        List of documents containing the topic.
    """
    documents = list(mongo_collection.find({"topics": topic}))
    return documents
