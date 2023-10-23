## liste des pages avec la mention et le parcours du master

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