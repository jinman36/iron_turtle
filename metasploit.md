What command allows you to search modules?
search
How do you select a module?    
use
How do you display information about a specific module?
info
How do you list options that you can set?
options
What command lets you view advanced options for a specific module?    
advanced
How do you show options in a specific category
search

Module Commands
===============

    Command       Description
    -------       -----------
    advanced      Displays advanced options for one or more modules
    back          Move back from the current context
    clearm        Clear the module stack
    info          Displays information about one or more modules
    listm         List the module stack
    loadpath      Searches for and loads modules from a path
    options       Displays global options or for one or more modules
    popm          Pops the latest module off the stack and makes it active
    previous      Sets the previously loaded module as the current module
    pushm         Pushes the active or list of modules onto the module stack
    reload_all    Reloads all modules from all defined module paths
    search        Searches module names and descriptions
    show          Displays modules of a given type, or all modules
    use           Interact with a module by name or search term/index

# Module Eternalblue
How do you select the eternalblue module?

use exploit/windows/smb/ms17_010_eternalblue
What option allows you to select the target host(s)?

rhosts
How do you set the target port?

rport
What command allows you to set options?
set
How would you set SMBPass to "username"?
set SMBPass username
How would you set the SMBUser to "password"?

set SMBUser password
What option sets the architecture to be exploited?
arch
What option sets the payload to be sent to the target machine?
payload
Once you've finished setting all the required options, how do you run the exploit?
exploit
What flag do you set if you want the exploit to run in the background?

-j
How do you list all current sessions?

-sessions
What flag allows you to go into interactive mode with a session("drops you either into a meterpreter or regular shell")
-j

# Meterpreter
What command allows you to download files from the machine?

download
What command allows you to upload files to the machine?

upload
How do you list all running processes?

ps
How do you change processes on the victim host(Ideally it will allow you to change users and gain the perms associated with that user)

migrate
What command lists files in the current directory on the remote machine?
ls
How do you execute a command on the remote host?

execute
What command starts an interactive shell on the remote host?

shell
How do you find files on the target host(Similar function to the linux command "find")

search
How do you get the output of a file on the remote host?

cat
How do you put a meterpreter shell into "background mode"(allows you to run other msf modules while also keeping the meterpreter shell as a session)?


