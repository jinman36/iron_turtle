## System Admin Bash Scripting

### Linux review
- Redirect STDOUT to a file:
  - $ command > file
- Append STDOUT to a file:
  - $ command >> file
- Redirect STDERR to a file:
  - $ command 2> file
- Redirect STDOUT and STDERR to a file:
  - $ command > file 2>&1
- Redirect STDIN from a file:
  - command < file
- These operators can be combined, as in:
  - $ command < infile > outfile 2>> errlog

Append Input using <<
  - $ cat << MyMarker
  - Accepts input until MyMarker is found
  - "myMarker" can be any arbitrary text
  - "MyMarker" is the "limit string" that is used to mark the end of the input "frame"

  - Can be combined with Append Output to create a file:
    - $ cat << MyMarker > file.txt
    - > this is line 1
    - > this is line 2
    - > myMarker
    - $ cat file.txt
      - this is line 1
      - this is line 2

- echo line 1 > myfile.txt - this will write 'line 1' to a new file
- echo line 2 >> myfile.txt - this will append 'line 2' tot he file


### Backtick `
- ls `echo '-la'` - ineffecient way to concatenat 'ls -la' as an example
- ifconfig eth0 | grep 'inet ' | awk '{print $2}' | sed 's/addr://' - address recovers and strips the ifconfig command down to only return the IP address
- ping `ifconfig eth0 | grep 'inet ' | awk '{print $2}' | sed 's/addr://'` - uses the back tick to ping the address once recovered


### Variables and parameters
- MESSAGE='Hello World'
- echo $MESSAGE

- RESULT=`ping -c 1 8.8.8.8`
- echo $RESULT - will ping google

- env - will show environment variables

- A=44
- echo $A
> 44

- B=$A+1
- echo $B
> 44+1

- Let B=$A+1
- echo $B
> 45