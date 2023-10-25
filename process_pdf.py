## liste des pages avec la mention et le parcours du master
import re
import PyPDF2

# Chemin vers le fichier PDF
pdf_file = 'local_file.pdf'

# Phrase à rechercher
phrase_a_rechercher = "RÉPERTOIRE DES EMPLOIS DES DIPLÔMÉS DE MASTER"

# Liste pour stocker les numéros de page
pages_avec_phrase = []

# Ouvrir le fichier PDF en mode lecture binaire
with open(pdf_file, 'rb') as pdf:
    pdf_reader = PyPDF2.PdfReader(pdf)
    
    # Parcourir chaque page du PDF
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        
        # Extraire le texte de la page
        page_text = page.extract_text()
        
        # Vérifier si la phrase recherchée est présente sur la page
        if phrase_a_rechercher in page_text:
            pages_avec_phrase.append(page_num + 1)  # Ajouter 1 car les numéros de page commencent à 1

# Afficher la liste des numéros de page contenant la phrase
print("Les pages contenant la phrase sont :", pages_avec_phrase)


## Récupérer les mentions 


import PyPDF2

# Chemin vers le fichier PDF

# Phrase à rechercher
phrase_a_rechercher = "RÉPERTOIRE DES EMPLOIS DES DIPLÔMÉS DE MASTER"

# Liste pour stocker les noms de mention
noms_mentions = []

# regex 

regex_pattern_mention = r'Mention.+\n'

# Ouvrir le fichier PDF en mode lecture binaire
with open(pdf_file, 'rb') as pdf:
    pdf_reader = PyPDF2.PdfReader(pdf)
    
    # Parcourir chaque page du PDF
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        
        # Extraire le texte de la page
        page_text = page.extract_text()
        
        # Vérifier si la phrase recherchée est présente sur la page
        if phrase_a_rechercher in page_text:
            # Trouver l'indice de la phrase
            start_index = page_text.index(phrase_a_rechercher)
            
            # Extraire le texte après la phrase (en supprimant les caractères indésirables)
            text = page_text[start_index + len(phrase_a_rechercher):].strip()
            # Apply the regex pattern to extract the "Mention" line
            mention_match = re.search(regex_pattern_mention, text)

            extracted_text_mention = mention_match.group(0)
            extracted_substring_mention = extracted_text_mention.replace("Mention ", "").replace("\n", "").strip()
            
            # Ajouter le nom de mention à la liste
            noms_mentions.append(extracted_substring_mention)

# Afficher la liste des noms de mention
print("Les noms de mention sont :", noms_mentions)


## Récupérer les parcours 

import PyPDF2

# Chemin vers le fichier PDF

# Phrase à rechercher
phrase_a_rechercher = "RÉPERTOIRE DES EMPLOIS DES DIPLÔMÉS DE MASTER"

# Liste pour stocker les noms de mention
noms_parcours = []
texte = []
# regex 

regex_pattern_parcours = r'Parcours.+\n'

# Ouvrir le fichier PDF en mode lecture binaire
with open(pdf_file, 'rb') as pdf:
    pdf_reader = PyPDF2.PdfReader(pdf)
    
    # Parcourir chaque page du PDF
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        
        # Extraire le texte de la page
        page_text = page.extract_text()
        
        # Vérifier si la phrase recherchée est présente sur la page
        if phrase_a_rechercher in page_text:
            # Trouver l'indice de la phrase
            start_index = page_text.index(phrase_a_rechercher)
            
            # Extraire le texte après la phrase (en supprimant les caractères indésirables)
            text = page_text[start_index + len(phrase_a_rechercher):].strip()
            texte.append(text)
            # Apply the regex pattern to extract the "Mention" line
            parcours_match = re.search(regex_pattern_parcours, text)

            extracted_text_parcours = parcours_match.group(0)
            extracted_substring_parcours = extracted_text_parcours.replace("Parcours ", "").replace("\n", "").strip()
            
            # Ajouter le nom de mention à la liste
            noms_parcours.append(extracted_substring_parcours)

# Afficher la liste des noms de mention
print("Les noms des parcours sont :", noms_parcours)

## Nombre de diplomés

import PyPDF2

# Chemin vers le fichier PDF

# Phrase à rechercher
phrase_a_rechercher = "RÉPERTOIRE DES EMPLOIS DES DIPLÔMÉS DE MASTER"

# Liste pour stocker les noms de mention
nb_diplome = []
texte = []
# regex 

regex_pattern_nb_diplomes = r"concerné-e-s par l'enqu.+\n"

# Ouvrir le fichier PDF en mode lecture binaire
with open(pdf_file, 'rb') as pdf:
    pdf_reader = PyPDF2.PdfReader(pdf)
    
    # Parcourir chaque page du PDF
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        
        # Extraire le texte de la page
        page_text = page.extract_text()
        
        # Vérifier si la phrase recherchée est présente sur la page
        if phrase_a_rechercher in page_text:
            # Trouver l'indice de la phrase
            start_index = page_text.index(phrase_a_rechercher)
            
            # Extraire le texte après la phrase (en supprimant les caractères indésirables)
            text = page_text[start_index + len(phrase_a_rechercher):].strip()
            texte.append(text)
            # Apply the regex pattern to extract the "Mention" line
            nbdiplo_match = re.search(regex_pattern_nb_diplomes, text)

            extracted_nbdiplo = nbdiplo_match.group(0)
            extracted_substring_nbdiplo = extracted_nbdiplo.replace("concerné-e-s par l'enquête : ", "").replace("\n", "").strip()
            parts = extracted_substring_nbdiplo.split(" (hors") # modifié pour éviter que le commentaires sur les étangers soit ajoutés
            extracted_substring_nbdiplo = parts[0]
            
            # Ajouter le nom de mention à la liste
            nb_diplome.append(extracted_substring_nbdiplo)

# Afficher la liste des noms de mention
print("Les noms des parcours sont :", nb_diplome)


# nombre d'étudiant en emploi 


import PyPDF2

# Chemin vers le fichier PDF

# Phrase à rechercher
phrase_a_rechercher = "RÉPERTOIRE DES EMPLOIS DES DIPLÔMÉS DE MASTER"

# Liste pour stocker les noms de mention
nb_emploi = []
texte = []
# regex 

regex_pattern_nb_emploi = r"En emploi.+\n"

# Ouvrir le fichier PDF en mode lecture binaire
with open(pdf_file, 'rb') as pdf:
    pdf_reader = PyPDF2.PdfReader(pdf)
    
    # Parcourir chaque page du PDF
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        
        # Extraire le texte de la page
        page_text = page.extract_text()
        
        # Vérifier si la phrase recherchée est présente sur la page
        if phrase_a_rechercher in page_text:
            # Trouver l'indice de la phrase
            start_index = page_text.index(phrase_a_rechercher)
            
            # Extraire le texte après la phrase (en supprimant les caractères indésirables)
            text = page_text[start_index + len(phrase_a_rechercher):].strip()
            texte.append(text)
            # Apply the regex pattern to extract the "Mention" line
            nb_emploi_match = re.search(regex_pattern_nb_emploi, text)
            if nb_emploi_match:
                extracted_nb_emploi = nb_emploi_match.group(0)
                extracted_substring_nb_emploi = extracted_nb_emploi.replace("En emploi ", "").replace("\n", "").strip()
            else:
                extracted_substring_nb_emploi = "0"
            
            # Ajouter le nom de mention à la liste
            nb_emploi.append(extracted_substring_nb_emploi)

# Afficher la liste des noms de mention
print("Les noms des parcours sont :", nb_emploi)






# Nombre d'étudiant au chômage 


import PyPDF2

# Chemin vers le fichier PDF

# Phrase à rechercher
phrase_a_rechercher = "RÉPERTOIRE DES EMPLOIS DES DIPLÔMÉS DE MASTER"

# Liste pour stocker les noms de mention
nb_rech_emploi = []
texte = []
# regex 

regex_pattern_nb_rech_emploi = r"En recherche d'emploi .+\n"

# Ouvrir le fichier PDF en mode lecture binaire
with open(pdf_file, 'rb') as pdf:
    pdf_reader = PyPDF2.PdfReader(pdf)
    
    # Parcourir chaque page du PDF
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        
        # Extraire le texte de la page
        page_text = page.extract_text()
        
        # Vérifier si la phrase recherchée est présente sur la page
        if phrase_a_rechercher in page_text:
            # Trouver l'indice de la phrase
            start_index = page_text.index(phrase_a_rechercher)
            
            # Extraire le texte après la phrase (en supprimant les caractères indésirables)
            text = page_text[start_index + len(phrase_a_rechercher):].strip()
            texte.append(text)
            # Apply the regex pattern to extract the "Mention" line
            nb_rech_emploi_match = re.search(regex_pattern_nb_rech_emploi, text)
            if nb_rech_emploi_match:
                extracted_nb_rech_emploi = nb_rech_emploi_match.group(0)
                extracted_substring_nb_rech_emploi = extracted_nb_rech_emploi.replace("En recherche d'emploi ", "").replace("\n", "").strip()
            else:
                extracted_substring_nb_rech_emploi = "0"
            
            # Ajouter le nom de mention à la liste
            nb_rech_emploi.append(extracted_substring_nb_rech_emploi)

# Afficher la liste des noms de mention
print("Les noms des parcours sont :", nb_rech_emploi)


# Nombre d'étudiants dans une autre situations

import PyPDF2

# Chemin vers le fichier PDF

# Phrase à rechercher
phrase_a_rechercher = "RÉPERTOIRE DES EMPLOIS DES DIPLÔMÉS DE MASTER"

# Liste pour stocker les noms de mention
nb_aut_situ = []
texte = []
# regex 

regex_pattern_nb_aut_situ = r"Autre situation .+\n"

# Ouvrir le fichier PDF en mode lecture binaire
with open(pdf_file, 'rb') as pdf:
    pdf_reader = PyPDF2.PdfReader(pdf)
    
    # Parcourir chaque page du PDF
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        
        # Extraire le texte de la page
        page_text = page.extract_text()
        
        # Vérifier si la phrase recherchée est présente sur la page
        if phrase_a_rechercher in page_text:
            # Trouver l'indice de la phrase
            start_index = page_text.index(phrase_a_rechercher)
            
            # Extraire le texte après la phrase (en supprimant les caractères indésirables)
            text = page_text[start_index + len(phrase_a_rechercher):].strip()
            texte.append(text)
            # Apply the regex pattern to extract the "Mention" line
            nb_aut_situ_match = re.search(regex_pattern_nb_aut_situ, text)
            if nb_aut_situ_match:
                extracted_nb_aut_situ = nb_aut_situ_match.group(0)
                extracted_substring_nb_aut_situ = extracted_nb_aut_situ.replace("Autre situation ", "").replace("\n", "").strip()
            else:
                extracted_substring_nb_aut_situ = "0"
            
            # Ajouter le nom de mention à la liste
            nb_aut_situ.append(extracted_substring_nb_aut_situ)

# Afficher la liste des noms de mention
print("Les noms des parcours sont :", nb_aut_situ)



# Nombre d'étudiant en études 


import PyPDF2

# Chemin vers le fichier PDF

# Phrase à rechercher
phrase_a_rechercher = "RÉPERTOIRE DES EMPLOIS DES DIPLÔMÉS DE MASTER"

# Liste pour stocker les noms de mention
nb_etude = []
texte = []
# regex 

regex_pattern_nb_etude = r"En études .+\n"

# Ouvrir le fichier PDF en mode lecture binaire
with open(pdf_file, 'rb') as pdf:
    pdf_reader = PyPDF2.PdfReader(pdf)
    
    # Parcourir chaque page du PDF
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        
        # Extraire le texte de la page
        page_text = page.extract_text()
        
        # Vérifier si la phrase recherchée est présente sur la page
        if phrase_a_rechercher in page_text:
            # Trouver l'indice de la phrase
            start_index = page_text.index(phrase_a_rechercher)
            
            # Extraire le texte après la phrase (en supprimant les caractères indésirables)
            text = page_text[start_index + len(phrase_a_rechercher):].strip()
            texte.append(text)
            # Apply the regex pattern to extract the "Mention" line
            nb_etude_match = re.search(regex_pattern_nb_etude, text)
            if nb_etude_match:
                extracted_nb_etude = nb_etude_match.group(0)
                extracted_substring_nb_etude = extracted_nb_etude.replace("En études ", "").replace("\n", "").strip()
            else:
                extracted_substring_nb_etude = "0"
            
            # Ajouter le nom de mention à la liste
            nb_etude.append(extracted_substring_nb_etude)

# Afficher la liste des noms de mention
print("Les noms des parcours sont :", nb_etude)


# Taux de réponse aux questionnaires 


import PyPDF2

# Chemin vers le fichier PDF

# Phrase à rechercher
phrase_a_rechercher = "RÉPERTOIRE DES EMPLOIS DES DIPLÔMÉS DE MASTER"

# Liste pour stocker les noms de mention
tx_reponse = []
texte = []
# regex 

regex_pattern_tx_reponse = r"Taux de réponse : .+\n"

# Ouvrir le fichier PDF en mode lecture binaire
with open(pdf_file, 'rb') as pdf:
    pdf_reader = PyPDF2.PdfReader(pdf)
    
    # Parcourir chaque page du PDF
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        
        # Extraire le texte de la page
        page_text = page.extract_text()
        
        # Vérifier si la phrase recherchée est présente sur la page
        if phrase_a_rechercher in page_text:
            # Trouver l'indice de la phrase
            start_index = page_text.index(phrase_a_rechercher)
            
            # Extraire le texte après la phrase (en supprimant les caractères indésirables)
            text = page_text[start_index + len(phrase_a_rechercher):].strip()
            texte.append(text)
            # Apply the regex pattern to extract the "Mention" line
            tx_reponse_match = re.search(regex_pattern_tx_reponse, text)
            if tx_reponse_match:
                extracted_tx_reponse = tx_reponse_match.group(0)
                extracted_substring_tx_reponse = extracted_tx_reponse.replace("Taux de réponse : ", "").replace("%\n", "").strip()
            else:
                extracted_substring_nb_etude = "0"
            
            # Ajouter le nom de mention à la liste
            tx_reponse.append(extracted_substring_tx_reponse)

# Afficher la liste des noms de mention
print("Les noms des parcours sont :", tx_reponse)



# Extraire tout les tableaux avec le numéro de page correspondant du fichier pdf 

import pdfplumber
import pandas as pd

# Ouvrir le fichier PDF
pdf_file = 'local_file.pdf'
tableau_final = pd.DataFrame()

with pdfplumber.open(pdf_file) as pdf:
    # Parcourir les pages du PDF
    for page_number, page in enumerate(pdf.pages, start=1):  # Commencer la numérotation des pages à 1
        # Extraire le texte de la page
        text = page.extract_text()
        
        # Vérifier si les colonnes "Diplômé-e" et "Intitulé d'emploi" sont présentes dans le texte
        if "Diplômé-e" in text and "Intitulé d'emploi" in text:
            # Trouver et extraire le tableau
            table = page.extract_table()
            
            # Vérifier que le tableau contient au moins 2 colonnes
            if len(table[0]) >= 2:
                # Créer un DataFrame à partir du tableau
                df = pd.DataFrame(table[1:], columns=table[0])
                
                # Ajouter une colonne pour le numéro de page
                df['Page'] = page_number
                
                # Ajouter le DataFrame à tableau_final
                tableau_final = pd.concat([tableau_final, df], ignore_index=True)