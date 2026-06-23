from pathlib import Path
import time, sys

# To set the directory of the task file
if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys.executable).parent 
else:
    BASE_DIR = Path(__file__).parent
TASK_FILE = BASE_DIR/"task.txt"

if not TASK_FILE.exists(): # creates a new taskfile if it does'nt exist 
    f= open(TASK_FILE,"w")
    f.write(f"{"NAME":<20}{"STATUS"}\n")
    f.close()

def create():
    print("\033[36m==========================================")
    print("\033[1;93m               ADD TASK \033[0m")
    print("\033[36m==========================================\033[0m")
    
    # To add a new task to keep track of
    with open(TASK_FILE,"a") as f:
       task = input("\033[1;36mEnter the task to keep track:\033[0m\n")
       f.write(f"{f"{task.title()}":<20}{"[False]"}\n")
    
    return
       

def view_task():
    print("\033[36m==========================================")
    print("\033[1;93m               VIEW TASKS \033[0m")
    print("\033[36m==========================================\033[0m")
    time.sleep(0.5)
    print(f"\033[1;93m{"NO.":<5}{"TASK":<20}{"STATUS"} \033[0m")

    finalline_index = 0
    # To view the list of the tasks 
    with open(TASK_FILE,"r") as f:
        task= f.readlines()
        for index, line in enumerate(task[1:],start=1):
            finalline_index =index
            if "True" in line:
                newline=line.replace("True", "\u2714")
            elif "False" in line:
                newline= line.replace("False", " ")
            
            print(f"{f"{index}.":<5}{f"{newline}"}")
            time.sleep(0.3)
    time.sleep(0.5)
    print("\033[1;92mALL THE TASKS HAVE BEEN LISTED\033[0m")
    time.sleep(1)
    return finalline_index

def update(to_complete):
    print("\033[36m==========================================")
    print("\033[1;93m               TASK UPDATION \033[0m")
    print("\033[36m==========================================\033[0m")
    time.sleep(0.5)
    print("\033[1;95mHere is the list of ongoing task\033[0m")
    time.sleep(0.7)

    # To view the list of the tasks and get theindex of the last line
    finalline_index = view_task()

    # To check if any task exists, before proceeding
    if (finalline_index == 0):
        print("\033[1;93mNo Tasks Available\033[0m")
        return

    task =[]
    if to_complete: # To mark complete
        with open(TASK_FILE,"r") as f:
            #To prompt for user input and check its validity
            task_choice = 0
            valid = False
            while not(valid):
                try:
                    task_choice = int(input("\033[1;97mPLEASE CHOOSE THE TASK TO MARK COMPLETE\033[0m\n"))
                except ValueError:
                    print("\033[1;91mENTER A VALID INPUT\033[0m\n")
                    time.sleep(1)
                    continue
                if ( 1<= task_choice<=(finalline_index)):
                    valid = True
                else:
                    print(f"\033[1;91mENTER A VALID CHOICE BETWEEN 1 AND {finalline_index} \033[0m\n")
                    time.sleep(1)
            
            task = f.readlines()
            print("\033[1;95mPlease wait while tasks are being updated...\033[0m")
            if "True" in task[task_choice]:
                print("\033[1;93mTASK IS ALREADY MARKED COMPLETE\033[0m")
            else:
                task[task_choice] = task[task_choice].replace("False", "True")
            time.sleep(1)
            print("\033[1;92mTHE TASK HAS BEEN UPDATED SUCCESSFULLY\033[0m")

    else: # To mark incomplete
        with open(TASK_FILE,"r") as f:
            #To prompt for user input and check its validity
            task_choice = 0
            valid = False
            while not(valid):
                try:
                    task_choice = int(input("\033[1;97mPLEASE CHOOSE THE TASK TO MARK INCOMPLETE\033[0m\n"))
                except ValueError:
                    print("\033[1;91mENTER A VALID INPUT\033[0m\n")
                    time.sleep(1)
                    continue
                if ( 1<= task_choice<=(finalline_index)):
                    valid = True
                else:
                    print(f"\033[1;91mENTER A VALID CHOICE BETWEEN 1 AND {finalline_index} \033[0m\n")
                    time.sleep(1)
            
            task = f.readlines()
            print("\033[1;95mPlease wait while tasks are being updated...\033[0m")
            if "False" in task[task_choice]:
                print("\033[1;93mTASK IS ALREADY MARKED InCOMPLETE\033[0m")
            else:
                task[task_choice] = task[task_choice].replace("True", "False")
            time.sleep(1)
            print("\033[1;92mTHE TASK HAS BEEN UPDATED SUCCESSFULLY\033[0m")
        
    with open(TASK_FILE,"w") as f:
        f.writelines(task)
    
    time.sleep(1)
    return
    
def delete():
    print("\033[36m==========================================")
    print("\033[1;93m               TASK DELETION \033[0m")
    print("\033[36m==========================================\033[0m")
    time.sleep(0.5)
    print("\033[1;95mHere is the list of ongoing task\033[0m")
    time.sleep(0.7)

    # To view the list of the tasks and get theindex of the last line
    finalline_index = view_task()

    # To check if any task exists, before proceeding
    if (finalline_index == 0):
        print("\033[1;93mNo Tasks Available\033[0m")
        return
    
    task = []
    with open(TASK_FILE,"r") as f:
        #To prompt for user input and check its validity
        task_choice = 0
        valid = False
        while not(valid):
            try:
                task_choice = int(input("\033[1;97mPLEASE CHOOSE THE TASK TO DELETE\033[0m\n"))
            except ValueError:
                print("\033[1;91mENTER A VALID INPUT\033[0m\n")
                time.sleep(1)
                continue
            if (1<= task_choice<=(finalline_index)):
                valid = True
            else:
                print(f"\033[1;91mENTER A VALID CHOICE BETWEEN 1 AND {finalline_index} \033[0m\n")
                time.sleep(1)
        task = f.readlines()
        print("\033[1;95mPlease wait while task is being updated...\033[0m")
        del task[task_choice]
        time.sleep(1)
        print("\033[1;92mTHE TASK HAS BEEN UPDATED SUCCESSFULLY\033[0m")
    
    with open(TASK_FILE,"w") as f:
        f.writelines(task)
    
    time.sleep(1)
    return  

def menu():
    # menu
    print("\033[36m==========================================")
    print("\033[1;96m         TO-DO LIST MANAGER \033[0m")
    print("\033[36m==========================================\033[0m")
    print("\033[1;36m1 : Add new Task\n2 : View Tasks\n3 : Mark Complete\n4 : Mark Incomplete\n5 : Delete Task\n6 : Exit\033[0m\n")
    #To prompt for user input and check its validity
    valid = False
    while not(valid):
        try:
            choice = int(input("\033[1;97mEnter a choice:\033[0m\n"))
        except ValueError:
            print("\033[1;91mENTER A VALID INPUT\033[0m\n")
            time.sleep(1)
            continue
        if (1<=choice<=6):
            valid = True
        else:
            print("\033[1;91mENTER A VALID CHOICE\033[0m\n")
            time.sleep(1)
    return choice

replay = True
while(replay):
    choice = menu()
    if choice==1:
        create()
    elif choice==2:
        view_task()
    elif choice==3:
        update(True)
    elif choice==4:
        update(False)
    elif choice==5:
        delete()
    else:
        break


time.sleep(0.5)
print(f"\033[1;93mExiting the program...\033[0m")
time.sleep(1)
print("\n\033[1;95m!!Thank you for using!!\033[0m")
time.sleep(0.5)
print("\033[1;95mCoded by: Aishik Ghosh\033[0m")
time.sleep(0.5)
input("\nPress Enter to Exit...")