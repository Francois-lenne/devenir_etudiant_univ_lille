import subprocess

# Replace 'child_program.py' with the name of the Python program you want to run
program_to_run = "extract_pdf.py"

second_program = "process_pdf.py"

try:
    # Run the child Python program
    subprocess.run(["python", program_to_run], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running {program_to_run}: {e}")
except FileNotFoundError:
    print(f"Python executable not found or {program_to_run} does not exist.")


import json

# Ouvrir le fichier JSON
with open('pdf_to_process.json', 'r') as file:
    try:
        # Charger les données JSON
        data = json.load(file)
        
        # Vérifier si le fichier JSON est vide
        if not data:
            print("Hello, World")
        else:
            try:
                subprocess.run(["python", second_program], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error running {second_program}: {e}")
            except FileNotFoundError:
                print(f"Python executable not found or {second_program} does not exist.")

    except json.JSONDecodeError:
        # Le fichier JSON est vide ou non valide
        print("JSON file is empty")
