# To install and use a Virtual Enviournment

    # install virtualenv in the terminal first
    
    # Then create a virtual enviournment by writing - virtualenv <name> - in the terminal

    # A folder with the <name> will be created in the folder path the command was run (can be changed with 'cd')

    # This virtual enviourment can be used to code in an isolated manner without affect preinstalled libraries and system enviourment elements

    # To access the virtual eniourment:
       # Open Window's Powershell Terminal or the VScode Terminal
       # Go to the folder path where the env exists (using- cd "<Path>")
       # wite: .\<env name>\Scripts\Activate.ps1

       NOTE:
       If there is an error because of "UnauthorizedAccess"-
            # Open Administrator Powershell Terminal
            # Run : Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
            # If prompted, write: Yes or Y
            # Now, The virtual enviournment can be used
    
    # Every package installed in this remote enviourment will be isolated from the main system and they will cease to exist when the enviournment is closed

    # TO exit the enviournment, write- "deactivate"
    
