"""
mongo_flow.py
This module defines the main Prefect flow that ties together the MongoDB connection, 
data extraction, and data processing tasks. It imports functionality from other modules.
"""

from prefect import flow, task
from mongodb_connection import MongoDBConnection
from data_extractor import DataExtractor
from data_processor import DataProcessor


@task
def verify_mongo_connection():
    connection_string = (
        "your_connection_string"
    )
    mongo_connection = MongoDBConnection(connection_string)
    mongo_connection.verify_connection()


@task
def extract_data_from_mongo():
    connection_string = (
        "your_connection_string"
    )
    data_extractor = DataExtractor(
        connection_string, "database_name", "collection_name"
    )
    return data_extractor.extract_data()


@task
def process_data(extracted_data):
    data_processor = DataProcessor()
    data_processor.process_data(extracted_data)


@flow
def mongo_connection_and_extraction_flow():
    verify_mongo_connection()
    extracted_data = extract_data_from_mongo()
    process_data(extracted_data)


# To run the flow
if __name__ == "__main__":
    mongo_connection_and_extraction_flow()
