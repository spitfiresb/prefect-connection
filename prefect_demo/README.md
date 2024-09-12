# Data Extraction and Processing Project

## Overview

This project includes Python scripts for extracting data from MongoDB collections and processing it using Prefect for orchestration. The main components are:

- `data_extractor.py`: Contains the `DataExtractor` class for extracting data from MongoDB collections.
- `data_processor.py`: Contains the `DataProcessor` class for processing the extracted data.
- `mongodb_connection.py`: Contains the `MongoDBConnection` class for verifying MongoDB connections.
- `mongo_flow.py`: Defines the main Prefect flow that integrates data extraction and processing tasks.

## Setup

### Prerequisites

- **Python 3.x**: Make sure you have Python 3.x installed. You can check your Python version by running:

  ```bash
  python --version
  ```
