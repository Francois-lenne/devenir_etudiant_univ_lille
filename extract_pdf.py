## configuration of the file 

from azure.storage.blob import BlobServiceClient

account_name = "github actions"
account_key = "github actions"

azure_connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key}"
container_name = "github actions"
blob_service_client = BlobServiceClient.from_connection_string(azure_connection_string)



## extract all the PDF that are already in the azure bloob containers

from azure.storage.blob import BlobServiceClient


blob_service_client = BlobServiceClient.from_connection_string(azure_connection_string)
container_client = blob_service_client.get_container_client(container_name)

blob_list = [blob.name for blob in container_client.list_blobs()]

print(blob_list)


## retrieve all the pdf files from the odif website 

import requests
from bs4 import BeautifulSoup
import re


url = "https://odif.univ-lille.fr/index.php?id=846"

response = requests.get(url)


regex_pdf = r'.pdf'  # regex pour test

if response.status_code == 200:
    # Analyser le contenu HTML de la page avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Trouver tous les liens (<a>) de la page
    links = soup.find_all('a')
    
    # Créer une liste pour stocker les noms des fichiers PDF
    pdf_links = []

    # Parcourir les liens et extraire les noms des fichiers PDF
    for link in links:
        href = link.get('href')
        href = str(href)
        href_pdf_name = href.split("/")[-1]
        if (
            re.search(regex_pdf, href)
            and href_pdf_name not in blob_list
            and href not in pdf_links # supprimer les doublons 
        ):
            response = requests.head(href) # condition if pour vérifier que l'URL fonctionne
            if response.status_code == 200:
                pdf_links.append(href)

    # Afficher la liste des noms des fichiers PDF
    for pdf_link in pdf_links:
        print(pdf_link)
else:
    print(f"Failed to retrieve content from {url}")


## add in the json file the pdf that need to be treat by the program

import os
import json

json_file_path = os.getcwd() + "/pdf_to_process.json"

if len(pdf_links) == 0:
    print("pas de fichier à charger")
else:
    with open(json_file_path, 'w') as json_file:
        json.dump(pdf_links, json_file)


# add the pdf to azure bloob

import requests
from azure.storage.blob import BlobServiceClient


for pdf_link in pdf_links:
    response = requests.get(pdf_link)
    if response.status_code == 200:
        blob_name = pdf_url.split("/")[-1]  # Utilisez le nom du fichier dans l'URL comme nom de blob
        blob_client = blob_service_client.get_blob_client(container_name, blob_name)
        
        with open("local_file.pdf", "wb") as pdf_file:
            pdf_file.write(response.content)

        with open("local_file.pdf", "rb") as pdf_file:
            blob_client.upload_blob(pdf_file)