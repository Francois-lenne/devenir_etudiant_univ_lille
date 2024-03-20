## package a importer
import re
import PyPDF2
import pdfplumber
import pandas as pd
import os
import glob
from azure.storage.blob import BlobServiceClient
import os
import requests
import warnings

# Ignorer tous les avertissements
warnings.filterwarnings('ignore')



# Settings pour la connexion à Azure Blob Storage
account_name = os.environ["account_name"]
account_key = os.environ["account_key"]

azure_connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key}"
container_name = "odif"
blob_service_client = BlobServiceClient.from_connection_string(azure_connection_string)

blob_service_client = BlobServiceClient.from_connection_string(azure_connection_string)
container_client = blob_service_client.get_container_client(container_name)

# fonction pour extraire les stat globales 

def stat_global(pdf_file):


    # mise en place du dico global 

    dic_stat = {} 


    # mise en place des clefs valeurs 


    dic_stat['num_pages'] = []

    dic_stat['mention'] = []

    dic_stat['parcours'] = []

    dic_stat['concern_enquete'] = []

    dic_stat['nb_en_emploi'] = []

    dic_stat['nb_en_recherche'] = []

    dic_stat['nb_autre_situations'] = []

    dic_stat['nb_en_etude'] = []

    dic_stat['taux_reponses'] = []




    # Phrase à rechercher pour recherche les éléments du texte
    phrase_a_rechercher = "RÉPERTOIRE DES EMPLOIS DES DIPLÔMÉS DE MASTER"

    # set up la liste pour ajouter le texte 

    texte = []


    # mise en place des regex


    regex_pattern_mention = r'Mention.+\n'



    regex_pattern_parcours = r'Parcours.+\n'


    regex_pattern_nb_diplomes = r"par l'enqu.+\n"


    regex_pattern_nb_emploi = r"En emploi.+\n"


    regex_pattern_nb_rech_emploi = r"En recherche d'emploi .+\n"


    regex_pattern_nb_aut_situ = r"Autre situation .+\n"


    regex_pattern_nb_etude = r"En études .+\n"



    regex_pattern_tx_reponse = r"Taux de réponse : .+\n"





    # mise en place de la boucle for pour remplir le dico


    # Ouverture du fichier pdf
    with open(pdf_file, 'rb') as pdf:
        pdf_reader = PyPDF2.PdfReader(pdf)
        
        # Parcourir chaque page du PDF
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            
            # Extraire le texte de la page
            page_text = page.extract_text()
            
            # Vérifier si la phrase recherchée est présente sur la page
            if phrase_a_rechercher in page_text or "Nombre de diplômé-e-s de la promotion 2016" in page_text:
                dic_stat['num_pages'].append(page_num + 1)  # Ajouter 1 car les numéros de page commencent à 1

                start_index = page_text.index(phrase_a_rechercher) # récupération de l'indice

                text = page_text[start_index + len(phrase_a_rechercher):].strip() # extraire le texte avec les infos

                ## extraction de la mention

                mention_match = re.search(regex_pattern_mention, text)

                extracted_text_mention = mention_match.group(0)

                extracted_substring_mention = extracted_text_mention.replace("Mention ", "").replace("\n", "").strip()

                dic_stat['mention'].append(extracted_substring_mention)

                ## extractions du parcours

                parcours_match = re.search(regex_pattern_parcours, text)

                extracted_text_parcours = parcours_match.group(0)

                extracted_substring_parcours = extracted_text_parcours.replace("Parcours ", "").replace("\n", "").strip()

                dic_stat['parcours'].append(extracted_substring_parcours)

                
                ## extraction du nombre de concernés par l'enquete 

                nbdiplo_match = re.search(regex_pattern_nb_diplomes, text)

                extracted_nbdiplo = nbdiplo_match.group(0)

                extracted_substring_nbdiplo = extracted_nbdiplo.replace("par l'enquête : ", "").replace("\n", "").strip()

                parts = extracted_substring_nbdiplo.split(" (hors") # modifié pour éviter que le commentaires sur les étangers soit ajoutés

                extracted_substring_nbdiplo = parts[0]

                dic_stat['concern_enquete'].append(extracted_substring_nbdiplo)

            
            ## extraction du nombre d'étudiant en emploi


                nb_emploi_match = re.search(regex_pattern_nb_emploi, text)
                if nb_emploi_match:
                    extracted_nb_emploi = nb_emploi_match.group(0)
                    extracted_substring_nb_emploi = extracted_nb_emploi.replace("En emploi ", "").replace("\n", "").strip()
                else:
                    extracted_substring_nb_emploi = "0"
                
                # Ajouter le nom de mention à la liste
                dic_stat['nb_en_emploi'].append(extracted_substring_nb_emploi)

            
            ## extraction du nombre d'étudiant en recherche d'emploi

                nb_rech_emploi_match = re.search(regex_pattern_nb_rech_emploi, text)
                if nb_rech_emploi_match:
                    extracted_nb_rech_emploi = nb_rech_emploi_match.group(0)
                    extracted_substring_nb_rech_emploi = extracted_nb_rech_emploi.replace("En recherche d'emploi ", "").replace("\n", "").strip()
                else:
                    extracted_substring_nb_rech_emploi = "0"
                
                # Ajouter le nom de mention à la liste
                dic_stat['nb_en_recherche'].append(extracted_substring_nb_rech_emploi)

            
            ## Nombre d'étudiant dans une autre situation
                nb_aut_situ_match = re.search(regex_pattern_nb_aut_situ, text)
                if nb_aut_situ_match:
                    extracted_nb_aut_situ = nb_aut_situ_match.group(0)
                    extracted_substring_nb_aut_situ = extracted_nb_aut_situ.replace("Autre situation ", "").replace("\n", "").strip()
                else:
                    extracted_substring_nb_aut_situ = "0"
                
                # Ajouter le nom de mention à la liste
                dic_stat['nb_autre_situations'].append(extracted_substring_nb_aut_situ)

            ## Nombre d'étudiant en étude
                nb_etude_match = re.search(regex_pattern_nb_etude, text)
                if nb_etude_match:
                    extracted_nb_etude = nb_etude_match.group(0)
                    extracted_substring_nb_etude = extracted_nb_etude.replace("En études ", "").replace("\n", "").strip()
                else:
                    extracted_substring_nb_etude = "0"
                
                # Ajouter le nom de mention à la liste
                dic_stat['nb_en_etude'].append(extracted_substring_nb_etude)
            

            ## Taux de réponse


                tx_reponse_match = re.search(regex_pattern_tx_reponse, text)
                if tx_reponse_match:
                    extracted_tx_reponse = tx_reponse_match.group(0)
                    extracted_substring_tx_reponse = extracted_tx_reponse.replace("Taux de réponse : ", "").replace("%\n", "").strip()
                else:
                    extracted_substring_tx_reponse = "0"

                dic_stat['taux_reponses'].append(extracted_substring_tx_reponse)

    # Convertir le dictionnaire en DataFrame
    df_stat_global = pd.DataFrame(dic_stat)

    return df_stat_global





# Extraire tout les tableaux avec le numéro de page correspondant du fichier pdf 



def rep_emploi(pdf_file):
    # Ouvrir le fichier PDF
    rep_emploi = pd.DataFrame()

    with pdfplumber.open(pdf_file) as pdf:
    # Parcourir les pages du PDF
        for page_number, page in enumerate(pdf.pages, start=1):  # Commencer la numérotation des pages à 1
        # Extraire le texte de la page
            text = page.extract_text()
        
        # Vérifier si les colonnes "Diplômé-e" et "Intitulé d'emploi" sont présentes dans le texte
            if "Mission(s)" in text and "Lieu d'emploi" in text:
            # Trouver et extraire le tableau
                table = page.extract_table()
            
            # Vérifier que le tableau contient au moins 2 colonnes
                if len(table[0]) >= 2:
                # Créer un DataFrame à partir du tableau
                    df = pd.DataFrame(table[1:], columns=table[0])
                
                # Ajouter une colonne pour le numéro de page
                    df['num_pages'] = page_number
                
                # Ajouter le DataFrame à tableau_final
                    rep_emploi = pd.concat([rep_emploi, df], ignore_index=True)
                    
    # suppression des "/n" dans les colonnes 

    rep_emploi.columns = rep_emploi.columns.astype(str).str.replace('\n', ' ')

    replacement_dict = {
        'Diplômé-e': {'\n': ' '},
        "Intitulé d'emploi": {'\n': ' '},
        "Mission(s)": {'\n': ' '},
        "Activité de l'employeur": {'\n': ' '},
        "Revenu net en €": {'\n': ' '}
    }

    rep_emploi = rep_emploi.replace(replacement_dict, regex=True)

    return rep_emploi





#   ajout de la mention et du parcours pour le répértoire d'emploi 

def add_mention_parcours(df_stat_global,rep_emploi):
    rep_emploi_merge = rep_emploi.merge(df_stat_global[['num_pages', 'mention', 'parcours']], on='num_pages', how='left')

    rep_emploi_merge['mention'].fillna(method='ffill', inplace=True)

    rep_emploi_merge['parcours'].fillna(method='ffill', inplace=True)

    return rep_emploi_merge






# récupéré l'année et la faculté 

def add_faculte_promo(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
    # Obtenir la première page local_file.pdf
        first_page = pdf.pages[0]



    # Extraire le texte de la première page
        text = first_page.extract_text()

    # Utiliser une expression régulière pour rechercher la première information entre "promotion" et le retour chariot
        info1_match = re.search(r'Promotion \d{4}', text)

        promo = info1_match.group(0).replace("Promotion ", "")

        faculte = text[74:-87].replace("\n", " ")

        return promo, faculte
    


# récupéré les fichiers pdf à traiter


from azure.storage.blob import BlobServiceClient
from datetime import datetime, timezone

def get_files_from_container(connection_string, container_name):
    # Create a BlobServiceClient using the connection string
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get a reference to the container
    container_client = blob_service_client.get_container_client(container_name)

    # List all the blobs in the container
    blobs = container_client.list_blobs()

    # Get today's date
    today = datetime.now(timezone.utc).date()

    # Get the names of the blobs that were added today
    file_names = [blob.name for blob in blobs if blob.last_modified.date() == today]

    return file_names

fichier_a_traiter = get_files_from_container(azure_connection_string, container_name)

print(fichier_a_traiter)



# traiter les fichiers pdf récupéré 



# Parcourez les blobs dans le conteneur
for blob in container_client.list_blobs():
    # Récupérez le nom du blob
    blob_name = blob.name
    print(blob_name)

    if blob_name not in fichier_a_traiter:
        print(f"Le fichier {blob_name} ne sera pas traité.")
        continue

    blob_client = container_client.get_blob_client(blob_name)
    blob_url = blob_client.url

    print(f"L'URL du fichier {blob_name} est {blob_url}")

    pdf_file = f"{blob_name}"
    # Téléchargez le fichier
    with open(pdf_file, 'wb') as download_file:
        download_file.write(blob_client.download_blob().readall())



    if 'df_stat_global' not in locals():
    # ajouter les fonctions d'extraction des données
        df_stat_global = stat_global(pdf_file)
       
        df_rep_emploi = rep_emploi(pdf_file)
        
        rep_emploi_merge = add_mention_parcours(df_stat_global,df_rep_emploi)
        
        df_stat_global["promo"] = add_faculte_promo(pdf_file)[0]

        df_stat_global["faculte"] = add_faculte_promo(pdf_file)[1]

        rep_emploi_merge["promo"] = add_faculte_promo(pdf_file)[0]

        rep_emploi_merge["faculte"] = add_faculte_promo(pdf_file)[1]
    
    else:
        df_stat_global_suite = stat_global(pdf_file)

        df_rep_emploi_suite = rep_emploi(pdf_file)

        rep_emploi_merge_suite = add_mention_parcours(df_stat_global_suite,df_rep_emploi_suite)

        df_stat_global_suite["promo"] = add_faculte_promo(pdf_file)[0]

        df_stat_global_suite["faculte"] = add_faculte_promo(pdf_file)[1]

        rep_emploi_merge_suite["promo"] = add_faculte_promo(pdf_file)[0]

        rep_emploi_merge_suite["faculte"] = add_faculte_promo(pdf_file)[1]

        df_stat_global = pd.concat([df_stat_global, df_stat_global_suite])
        print(df_stat_global)

        df_rep_emploi = pd.concat([df_rep_emploi, rep_emploi_merge_suite])

        print(df_stat_global)

    



# vérification stat global 
        
def verification_stat_global(df):

    # Supprimer les lignes contenant uniquement des valeurs nulles
    df = df.dropna(how='all')

    # Vérifier si le DataFrame contient des doublons

    df = df.drop_duplicates()

    # vérifier si stat global ne contient pas de valeur nul
    if df.isnull().any().any():
        raise ValueError("Le DataFrame contient des valeurs manquantes")
    
    # Liste des colonnes à vérifier
    colonnes_a_verifier = ['num_pages', 'taux_reponses', 'concern_enquete',"nb_en_emploi","nb_en_recherche","nb_autre_situations","nb_en_etude","promo"]

# Parcourir chaque colonne
    for colonne in colonnes_a_verifier:
    # Convertir la colonne en chaîne de caractères
        df[colonne] = df[colonne].astype(str)
    
        # Vérifier si la colonne contient uniquement des chiffres
        if not df[colonne].str.isnumeric().all():
            print(df[colonne].dtype)
            # Supprimer les caractères non numériques
            df[colonne] = df[colonne].replace('\D', '', regex=True)
            # Convertir la colonne en entier
            df[colonne] = pd.to_numeric(df[colonne], errors='coerce').astype('Int64')

        df[colonne] = pd.to_numeric(df[colonne], errors='coerce').astype('Int64')
        
            
            
    

    # Vérifier que 'taux_reponses' est compris entre 0 et 100 inclus
    if not ((df['taux_reponses'] >= 0) & (df['taux_reponses'] <= 100)).all():
        raise ValueError("La colonne 'taux_reponses' contient des valeurs en dehors de l'intervalle [0, 100]")    
    

    if not df['promo'].astype(str).str.match('^20\d{2}$').all():
        raise ValueError("La colonne 'promo' contient des valeurs qui ne sont pas des années commençant par '20'")
    

    # Liste des colonnes à vérifier
    colonnes_a_verifier_str = ['mention', 'parcours', 'faculte']

    # Parcourir chaque colonne
    for colonne in colonnes_a_verifier_str:
        # Supprimer les chiffres
        df[colonne] = df[colonne].astype(str).str.replace('\d', '', regex=True)
        # Convertir la colonne en string
        df[colonne] = df[colonne].astype(str)
        # Suprimer les espaces à droites et a gauche
        df[colonne] = df[colonne].str.strip()

    return df

df_stat_global = verification_stat_global(df_stat_global)





# chargement en pré prod sur snowflake


# pour les stat global

import pandas as pd
from sqlalchemy import create_engine

# Snowflake connection details
user = os.environ["user"]
password = os.environ["password"]
account = os.environ["snow_account"]
warehouse = os.environ["warehouse"]
database = os.environ["database"]
schema = os.environ["schema"]
table_name_rep_emploi = 'rep_emploi_lille_master'
table_name_stat_global = "stat_global_lille_master"





def load_df_snowlfake(df,user,password,account,warehouse,database,schema,table):

    connection_string = f'snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}'

    engine = create_engine(connection_string)

    df.to_sql(table, engine, if_exists='replace', index=False)

    return "Success"


# load_df_snowlfake(df_stat_global,user,password,account, warehouse, database,table_name_stat_global)





# load_df_snowlfake(rep_emploi_merge,user,password,account, warehouse, database,table_name_rep_emploi)



def delete_pdf():
    import os
    import glob

    # Obtenez une liste de tous les fichiers .pdf dans le répertoire courant
    pdf_files = glob.glob(os.path.join(os.getcwd(), '*.pdf'))

    # Parcourez la liste des fichiers .pdf et supprimez chaque fichier
    for pdf_file in pdf_files:
        os.remove(pdf_file)

    return "All PDF files deleted"

delete_pdf()