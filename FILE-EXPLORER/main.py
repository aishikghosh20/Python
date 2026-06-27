from logic.organiser import organize
from pathlib import Path
from time import sleep
from logic.utils import directory, title, exit_app, main_drives

def set_drive(choice):
    current 

def main():
    # to get the source folder and check if the folder exists
    check = False
    while (not check):
        folder = Path((input("\033[1;97mENTER THE SOURCE FOLDER:\033[0m\n")).strip().strip('"').strip("'"))

        if not folder.exists():
            print(f"{" ":<12}{"\033[1;97m❌ FOLDER DOES NOT EXIST...\033[0m"}")
            sleep(0.5)
            continue
        if not folder.is_dir():
            print(f"{" ":<12}{"\033[1;97m❌ THE PATH IS NOT A FOLDER...\033[0m"}")
            sleep(0.5)
            continue
       
        check = True
    
    print(f"{" ":<12}{"\033[1;27m✔️ FOLDER EXISTS...\033[0m"}")
    sleep(0.5)

    organize(folder)
    return
          
    
if __name__ == "__main__":
    print(f"{" ":<12}{"\033[1;92mSTARTUP SUCCESSFUL!!\033[0m"}")
    sleep(0.5)
    choice = title()
    sleep(0.3)
    current = main_drives()
    print(f"{" ":<12}{"\033[1;95mPlease Wait...\033[0m"}")
    print("\n")
    sleep(0.5)
    directory(current)



