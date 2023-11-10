import os


def deletef():
    os.system("cls")

    if delete == "y" or delete == "Y":
        os.system('del "runner_downloader.py" /f')
        print("File deleted!")
        wait = input("Press enter to exit...")
    elif delete == "n" or delete == "N":
        print("File not deleted!")
        exit()
    exit()


def downloadall():
    os.system('mkdir "Program Runner VERSION 0.5"')
    os.system(
        'curl -L -o "example_program.py" "https://raw.githubusercontent.com/iminurwalls1/Program-Runner-V0.5/main/example_program.py"'
    )
    os.system(
        'curl -L -o "command_log.txt" "https://raw.githubusercontent.com/iminurwalls1/Program-Runner-V0.5/main/command_log.txt"'
    )
    os.system(
        'curl -L -o "main.py" "https://raw.githubusercontent.com/iminurwalls1/Program-Runner-V0.5/main/main.py"'
    )
    os.system(
        'curl -L -o "readme.txt" "https://raw.githubusercontent.com/iminurwalls1/Program-Runner-V0.5/main/readme.txt"'
    )
    os.system(
        'curl -L -o "script_runner.py" "https://raw.githubusercontent.com/iminurwalls1/Program-Runner-V0.5/main/script_runner.py"'
    )
    
    os.system('move "example_program.py" "Program Runner VERSION 0.5"')
    os.system('move "command_log.txt" "Program Runner VERSION 0.5"')
    os.system('move "main.py" "Program Runner VERSION 0.5"')
    os.system('move "readme.txt" "Program Runner VERSION 0.5"')
    os.system('move "script_runner.py" "Program Runner VERSION 0.5"')
    global delete
    delete = input(
        """
                               Runner Downloaded!
                  
                  Do you want to delete the downloader file?(y/n)
             
                        
              
                                     Choice:"""
    )
    deletef()


downloadall()
