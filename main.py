import subprocess

# Replace 'child_program.py' with the name of the Python program you want to run
program_to_run = "extract_pdf.py"

try:
    # Run the child Python program
    subprocess.run(["python", program_to_run], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running {program_to_run}: {e}")
except FileNotFoundError:
    print(f"Python executable not found or {program_to_run} does not exist.")
