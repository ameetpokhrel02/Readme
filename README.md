Linux Command Notes for Beginners

 File and Directory Management

| Command                     | Description                                                                 | Example                                      |
|-----------------------------|-----------------------------------------------------------------------------|---------------------------------------------|
| pwd                         | Prints the current working directory.                                      | pwd                                         |
| ls                          | Lists the contents of a directory.                                         | ls                                          |
| ls -al                      | Lists all files, including hidden ones, in long format.                    | ls -al                                      |
| cd <directory>              | Changes the current directory to <directory>.                              | cd /home/user/docs                          |
| cd ..                       | Moves one directory up (to the parent directory).                          | cd ..                                       |
| mkdir <directory>           | Creates a new directory.                                                   | mkdir project                               |
| mkdir -p <dir1>/<dir2>      | Creates nested directories in one command.                                 | mkdir -p project/phase1/docs                |
| rmdir <directory>           | Removes an empty directory.                                                | rmdir empty_folder                          |
| rm -r <directory>           | Removes a directory and its contents recursively.                          | rm -r project                               |
| touch <file>                | Creates an empty file or updates the timestamp of an existing file.        | touch notes.txt                             |
| cp <source> <destination>   | Copies a file or directory to another location.                            | cp notes.txt backup/notes_backup.txt        |
| mv <source> <destination>   | Moves or renames a file or directory.                                      | mv notes.txt docs/notes_final.txt           |
| rm <file>                   | Deletes a file.                                                            | rm old_file.txt                             |


 File Viewing and Editing

| Command                     | Description                                                                 | Example                                      |
|-----------------------------|-----------------------------------------------------------------------------|---------------------------------------------|
| cat <file>                  | Displays the contents of a file.                                           | cat notes.txt                               |
| cat > <file>                | Creates or overwrites a file with input from the terminal (use CTRL+D).    | cat > notes.txt                             |
| echo <text> >> <file>       | Appends text to a file.                                                    | echo "Hello, World!" >> notes.txt           |
| nano <file>                 | Opens a file in the Nano text editor for editing.                          | nano notes.txt                              |
| less <file>                 | Opens a file for reading (allows navigation).                              | less largefile.txt                          |
| wc <file>                   | Counts lines, words, and characters in a file.                             | wc notes.txt                                |
| head <file>                 | Displays the first 10 lines of a file.                                     | head notes.txt                              |
| tail <file>                 | Displays the last 10 lines of a file.                                      | tail logs.txt                               |

 Searching and Filtering

| Command                     | Description                                                                 | Example                                      |
|-----------------------------|-----------------------------------------------------------------------------|---------------------------------------------|
| grep <pattern> <file>       | Searches for a pattern in a file and displays matching lines.              | grep Linux notes.txt                        |
| grep -i <pattern> <file>    | Searches for a pattern (case-insensitive) in a file.                       | grep -i linux notes.txt                     |
| grep -n <pattern> <file>    | Displays line numbers for matching lines.                                  | grep -n Linux notes.txt                     |
| find <directory> -name <name>| Searches for a file or directory by name.                                 | find /home -name notes.txt                  |

---

### File Permissions

| Command                     | Description                                                                 | Example                                      |
|-----------------------------|-----------------------------------------------------------------------------|---------------------------------------------|
| ls -l                      | Lists files with detailed information, including permissions.               | ls -l                                       |
| chmod <permissions> <file> | Changes permissions for a file or directory.                                | chmod 644 notes.txt                         |
| chmod u+rwx <file>         | Grants read, write, and execute permissions to the user.                    | chmod u+rwx script.sh                       |
| chmod o-rwx <file>         | Removes all permissions for others.                                         | chmod o-rwx notes.txt                       |


 Networking and Processes

| Command                     | Description                                                                 | Example                                      |
|-----------------------------|-----------------------------------------------------------------------------|---------------------------------------------|
| ping <hostname>             | Sends ICMP packets to a host to check connectivity.                        | ping google.com                             |
| top                         | Displays running processes and system resource usage.                      | top                                         |
| ps                          | Lists active processes for the current session.                            | ps                                          |
| kill <PID>                  | Terminates a process by its process ID (PID).                              | kill 1234                                   |

 History and Aliases

| Command                     | Description                                                                 | Example                                      |
|-----------------------------|-----------------------------------------------------------------------------|---------------------------------------------|
| history                     | Displays a list of previously executed commands.                           | history                                     |
| !<number>                   | Executes a command from history by its number.                             | !15                                        |
| alias <name>=<command>      | Creates a shortcut for a command.                                          | alias ll='ls -al'                           |
| unalias <name>              | Removes an alias.                                                          | unalias ll                                  |

Exam Practice Tips
1. Practice Basic Commands**: Focus on creating directories, navigating paths, and managing files.
2. Understand Paths**: Be comfortable with absolute and relative paths.
3. Experiment with Permissions**: Learn chmod thoroughly.
4. Search Files**: Use grep and find for pattern searching.
5. History and Aliases**: Use history and define aliases to save time.
6. Simulate Real Tasks**: Set up simple directory structures and perform file operations.

