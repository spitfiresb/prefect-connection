"""
data_processor.py
This module contains the DataProcessor class for processing data extracted from MongoDB.
"""

import pandas as pd


class DataProcessor:
    @staticmethod
    def process_data(extracted_data):
        if extracted_data:
            print(f"First document: {extracted_data[0]}")

        # Tabulating
        df = pd.DataFrame(extracted_data)
        print(df.head())  # This prints the first few rows of the DataFrame

        # Check 1: Verify the length of the DataFrame
        expected_length = len(extracted_data)
        actual_length = len(df)
        if actual_length == expected_length:
            print(f"Length check passed: {actual_length} rows.")
        else:
            print(
                f"Length check failed: expected {expected_length}, but got {actual_length}."
            )

        # Check 2: Ensure all expected columns are present
        expected_columns = ["_id", "customerId", "topicId", "cimEvent", "_class"]
        missing_columns = [col for col in expected_columns if col not in df.columns]
        if not missing_columns:
            print("All expected columns are present.")
        else:
            print(f"Missing columns: {missing_columns}")

        # Check 3: Identify null or missing values in the DataFrame
        null_values = df.isnull().sum()
        if null_values.any():
            print("Warning: There are null values in the DataFrame.")
            print(null_values[null_values > 0])
        else:
            print("No null values found in the DataFrame.")
