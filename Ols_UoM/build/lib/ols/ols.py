from turtle import home
import requests
import json

# Define the OLS API base URL
OLS_API_BASE_URL = "https://www.ebi.ac.uk/ols/api/ontologies/"

def fetch_ontology_info(ontology_id):
    try:
        # Construct the URL for the ontology
        ontology_url = f"{OLS_API_BASE_URL}{ontology_id}"

        # Send a GET request to the OLS API
        response = requests.get(ontology_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            ontology_data = response.json()
            
            # Check if the 'config' key exists in the response
            if 'config' in ontology_data:

                number_of_terms = ontology_data.get("numberOfTerms" , 'N/A' '\n')
                current_status = ontology_data.get("status" , 'N/A' '\n')
                ontology_info = ontology_data['config']
                ontology_title = ontology_info.get("title" , 'N/A' '\n')
                ontology_description = ontology_info.get("description" , 'N/A' '\n')

                # Display the information
                print(f"Ontology Title: {ontology_title}")
                print(f"Ontology Description: {ontology_description}")
                print(f"Number of Terms: {number_of_terms}")
                print(f"Current Status: {current_status}")
                
            else:
                print("Error: 'config' key not found in the API response.")
        else:
            print("Error: Unable to fetch ontology information. Please check the ontology ID.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

#define function for command line interaction tool
def fetch_ontology_info_cli():
    ontology_id = input("Enter the ontology ID: ")
    fetch_ontology_info(ontology_id)

if __name__ == "__main__":
    #ontology_id = input("Enter the ontology ID: ")
    #fetch_ontology_info(ontology_id)
    fetch_ontology_info_cli()
