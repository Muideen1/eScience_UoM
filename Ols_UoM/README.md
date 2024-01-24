# OLS Ontology Fetcher

A Python script to fetch and display information about ontologies from the [EBI Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols).

## Features

- Fetches ontology details including title, description, number of terms, and current status.
- Utilizes the OLS API to retrieve ontology information.
- Provides a command-line interface for easy interaction.

## Dependencies

- Python 3
- "requests" library
- "setuptools" library

Ensure you have Python installed on your system. 

- pip install requests
- pip install setuptools

Usage 

running the main code
- python ols.py


running from as CLI Tool - Navigate to the root directory of this package in terminal using:
- cd Ols_UoM
then run
- pip install .

to install the package locally

then run:

- ols

to execute the fetch_ontology_info function using that ID.


