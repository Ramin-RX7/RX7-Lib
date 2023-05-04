![PyPI - License](https://img.shields.io/badge/downloads-32k%2Fmonth-brightgreen?style=plastic) ![PyPI - License](https://img.shields.io/pypi/l/rx7?color=orange&style=plastic) ![PyPI - License](https://img.shields.io/badge/status-stable-success?style=plastic)
--------------------------------------------------------

"rx7" is a library help you code faster and shorter
--------------------------------------------------------

### \- Most Usefull function and mexthods are collected.

### \- Special features

### \- Simple and easy to understad API

<hr />

### Installation
    pip install rx7
### Upgrade
    pip install --upgrade rx7


<br />


# Here is the brief documentaion:
### *(Complete documentation with details will be added soon in the Wiki section)*


<h2>List of Variables:</h2>

| **Variable** | **Description**                                         |
|--------------|---------------------------------------------------------|
| argv         | sys.argv (return list of given arguments from terminal) |
| ABC          | Parent for classes which have abstractmethods           |
| exit         | Equivalent sys.exit (returning exit code to terminal)   |
| environ      | Returns environment variables in a dictionary format    |


<br>


List of Functions:
------------------
| **Function**                     | **Description**                                                                                  |
|----------------------------------|--------------------------------------------------------------------------------------------------|
| p()                              | print() function.                                                                                |
| repeat(function,n)               | Repeat F_Name function for n times.                                                              |
| rev(v)  (REMOVED 2.4.0)          | Reverse v and returns it. (Everything like str,list,int)                                         |
| read(file)                       | Return content of the file.                                                                      |
| write(file,mode,text)            | Write things you want in file content. (Read Doc String)                                         |
| wait(n)sleep(n)                  | Stop code executing for n seconds                                                                |
| cls()clear()                     | It Clears the Terminal                                                                           |
| progressbar() (*removed in v3.1) | In-App Progressbar. (Read Doc String)                                                            |
| cons_integer(Frst,Lst)           | Return string from Frst to Lst (Read Doc String) (v1.7)                                          |
| force(tpl,*var)                  | Return tpl with adding var(s) to it.                                                             |
| erase(tpl,*var)                  | Return tpl with removing var(s) from it.                                                         |
| replace(tpl,ind,var)             | Replace tpl[ind] with var                                                                        |
| insert(tpl,ind,var)              | Set tpl[ind] to var. (Note that tpl[ind] will be tpl[ind+1])                                     |
| pop(tpl,index)                   | Remove member with index of 'index' from a tuple                                                 |
| wait_for(button)                 | Waits for user to press specific button.                                                         |
| call_later(func,args,delay)      | Call func(args) after delay time.                                                                |
| convert_bytes(num)               | convert bytes to (KB,MB,GB,TB)                                                                   |
| Input(prompt,default)            | Prompt an input message with default answer (value) (ONLY ON WINDOWS)                            |
| default_input()                  | Same as `default_input`                                                                          |
| restart_app()                    | Restart running python program                                                                   |
| active_window_title()            | Return Active Window Title                                                                       |
| open_image(path)                 | Open image with default image viewer (Mac OS is not supported)                                   |
| download(url)                    | To download files with memory saver and progressbar                                              |
| extract(file,path,pwd)           | Extract Zip file with password to path                                                           |
| screenshot(name)                 | Take a screenshot and save it.                                                                   |
| func_info(function)              | Print information of function                                                                    |
| Check_Type                       | Decorator that raise TypeError if function argument type is wrong (Read Help)                    |
| Progressbar()                    | Generator of progressbar() which you can use it to do some stuff between your delays (Read Help) |
| pixel_color(X,Y)                 | Return RGB color of pixel[X,Y]                                                                   |
| getpass(prompt)                  | Prompt for a password, with echo turned off.                                                     |
| import_module(path)              | Return given path (file with any extension) as a Module                                          |


<br>


<h2>List of Classes:</h2>

<h3>&nbsp; Class Random:&nbsp; &nbsp;<em>Random Variable Generator Class.</em></h3>

| **Function**             | **Description**                                |
|--------------------------|------------------------------------------------|
| choose(iter,k,duplicate) | Choose k random items from iterable or string. |
| integer(Frst,Lst)        | Choose integer in range [Frst,Lst]             |
| O1(decimal_nom=17)       | Return x in interval [0,1)                     |
| number(Frst,Lst)         | Return x in interval [Frst,Lst]                |
| shuffle(iterable)        | Return shuffled version of iterable            |

<br>


<h3>&nbsp; Class System:&nbsp; &nbsp;<em>Some system actions and information.</em></h3>

| **Function**            | **Description**                                                         |
|-------------------------|-------------------------------------------------------------------------|
| accname()               | return account username you have logged in.                             |
| pid()                   | Get pid number of terminal and return it.                               |
| disk_usage(path)        | ########                                                                |
| chdir                   | Change directory of terminal.                                           |
| SHUT_DOWN()             | Shut Down the PC.                                                       |
| RESTART()               | Restart the PC.                                                         |
| terminal_size()         | Return terminal size in tuple  (columns,lines).                         |
| cwd()                   | Return Carrent Working Directory.                                       |
| ip_global()             | Returns Global IP.                                                      |
| ip_local()              | Returns Local IP.                                                       |
| ram_total()             | Returns total ram of the system.                                        |
| ram_used()              | Returns Used Space of the ram of the system.                            |
| ram_free()              | Returns Available (Free) space of system ram.                           |
| boot_time()             | Return system boot time in seconds since the epoch.                     |
| device_name()           | Returns Device Name                                                     |
| ip_website(url)         | Returns url ip address                                                  |
| win10_notification()    | Display windows 10 notification (READ DOCSTRING) (ONLY WIN10 SUPPORTED) |
| cpu_count(logical=True) | Return the number of logical/physical CPUs in the system                |
| pyshell_execute_bit()   | To determine whether Python shell is executing in 32bit or 64bit        |
| pids()                  | Return a list of current running PIDs                                   |
| pid_exists(pid)         | Return True if pid exists else False                                    |
| cpu_percent()           | Return the current CPU utilization as a percentage                      |
| os_name()               | Returns OS name of machine                                              |



<br>


<h3>&nbsp; Class Files: (Static<strong style="font-size: 14px;">&nbsp;methods)&nbsp;</strong><em style="font-size: 14px;">Actions and information about files.</em></h3>

| **Function**                                 | **Description**                                                               |
|----------------------------------------------|-------------------------------------------------------------------------------|
| size(path)                                   | Return size of the file in byte(s). Also work on                              |
| delete(path)                                 | Use this to delete a file (Not folder).                                       |
| rename(path)                                 | Rename files with this function.                                              |
| abspath(path)                                | Return absolute path of given path.                                           |
| exists(path)                                 | Return Boolean. If exists True, else: False                                   |
| mdftime(path)                                | Get last modify time of the file.                                             |
| acstime(path)                                | Get last access time of the file.                                             |
| move(src,dst)                                | Move file from src to dst. (Read Doc String of copy func)                     |
| copy(src,dst,metadata=True)                  | Copy file (with metadata) from src to dst. (Also work on folders)             |
| hide(path)                                   | Hide given path. (It can be file or directory.)                               |
| read_only(path,mode=True)                    | Make file or folder read-only. (Read Doc String)                              |
| read(path)                                   | Return content of the path                                                    |
| write(path,text='',...)                      | Same as write function.                                                       |
| isdir(path)                                  | Return True for directory and False for others.                               |
| isfile(path)                                 | Return True for file and False for others.                                    |
| is_hidden(path)                              | Check whether path is hidden or not                                           |
| is_readonly(path)                            | Check whether path is readonly or not                                         |
| search_file(pattern,path,mode)               | search for pattern in path (Read function doc string)                         |
| search_content(path,word)                    | Search for word in all files in path, return list of files that contain word  |
| mkdir(path)                                  | Make directory (More than one if its possible!)                               |
| generate_tree(dir_path)                      | Returns a visual tree of dir_path                                             |
| get_drives()                                 | (Windows only) Get currently available drives                                 |
| basename(path)                               | Returns the final component of a pathname                                     |
| dirname(path)                                | Returns the directory component of a pathname                                 |
| join_paths(path)                             | Joins multiple paths together and returns it                                  |
| &nbsp; &nbsp; &nbsp; &nbsp; MEMBERS (Family) |                                                                               |
| MEMBERS.all_exactdir                         | List of all things those are in exact directory                               |
| MEMBERS.files_exactdir                       | List of files which are in exact directory                                    |
| MEMBERS.dirs_exactdir                        | List of dirs which are in exact directory                                     |
| MEMBERS.files_all                            | List of files which are in exact directory and all sub-directories            |
| MEMBERS.files_all_sep                        | List of files which are in exact directory and all sub-directories seprated by their directories |
| MEMBERS.dirs_all                             | List of directories (Exact dir and all sub-dirs)                              |
| MEMBERS.all_all_sep                          | List of everything thing in path (exact dir &amp; sub-dirs)                   |


<br>


<h3>&nbsp; Class Style:&nbsp; &nbsp; <em>Changing text Color,BG &amp; Style. (Read Doc String)</em></h3>

| **Function**                                  | **Description**                                             |
|-----------------------------------------------|-------------------------------------------------------------|
| print\(\*values, color, BG, style, end, sep\) | Print txt with selected color,BG,style\.\(Read Doc String\) |
| switch\(color,BG,style\)                      | Change Terminal Attributes Until another Call\.             |
| switch\_default\(\)                           | Restore Terminal Attributes\.                               |
| reset                                         | =switch\_default                                            |
| log\_&nbsp; \(Family\)                        | 5 Different Style\.print with ready color and style         |


<br>


<h3>&nbsp; Class Record:&nbsp; &nbsp;<em>Record time of a certain actions. (Read Doc String)</em></h3>

| **Function**                        | **Description**                                                            |
|-------------------------------------|----------------------------------------------------------------------------|
| __init__()                          | Set Start Time.                                                            |
| self.stop(self)                     | Stops Recording (You can not lap anymore)                                  |
| self.lap(self, save=True, round=15) | Rreturn time between start time. if save==True: add that time to self.laps |
| self.laps                           | A list that contains all laps you have done                                |
| self.reset(self, start=False)       | Empty self.laps, if start is True: set start time to now                   |
| self.last_lap(save=True)            | Return elapsed time from last lap (save it in self.laps if save is true)   |
| timeit(code,setup, times,globals_)  | Run the 'code' for 'times' times and return time it needs (all, not once)  |
| timer(f)                            | Decorator for functions to print out how much each call takes              |


<br>


<h3>&nbsp; Class Decorator:&nbsp; &nbsp;<em>Useful decorators you might want to use</em></h3>

| **Function**   | **Description**                                                                                    |
|----------------|----------------------------------------------------------------------------------------------------|
| Check_Type     | Decorator that raise TypeError if function argument type is wrong (Read Help)                      |
| overload       | Make your function accept different kind of argument and structure with defining it more than once |
| attach_to_all  | Attach Decorator.decorator_all to all functions of a class (Class decorator)                       |
| abstractmethod | A decorator indicating abstract methods.                                                           |
<br />


<h3>&nbsp; Class Terminal:&nbsp; &nbsp;<em>functions related to working with terminal</em></h3>

| **Function**        | **Description**                                             |
|:------------------- |:----------------------------------------------------------- |
| run(command)        | executes `command` live in terminal                         |
| getoutput(commands) | runs the `command` in the background and returns the output |
| size()              | Returns the size of terminal in tuple (columns,rows)        |
<br>


<h3>&nbsp; Class IO:&nbsp; &nbsp;<em>Useful methods when working with user input</em></h3>

| **Function**                 | **Description**                                                          |
|------------------------------|--------------------------------------------------------------------------|
| wait_for_input(prompt)       | Asks for user input, until they enter something else than whitespaces    |
| selective_input()            | Check repository wiki for full documentation                             |
| yesno_input(prompt, default) | wait for user to enter one of (`yes`,`no`, `y`, `n`). (Case insensitive) |
| Input(prompt, default_value) | (Windows only) Types default value before getting user's input           |
| getpass(prompt)              | Gets users input without showing their input (`getpass.getpass()`)       |
<br>


<h3>&nbsp; Class Internet:&nbsp; &nbsp;<em>Methods for working with network and internet related stuffs</em></h3>

| **Function**          | **Description**                                                                                 |
|-----------------------|-------------------------------------------------------------------------------------------------|
| is_connected(website) | Check for internet connection with trying to connect to `website`                               |
| connection_checker    | Decorator to check if internet is connected before calling the function                         |
| ip_local()            | Returns local ip                                                                                |
| ip_global()           | Returns global ip                                                                               |
| ip_global(website)    | returns ip of the given website                                                                 |
| url_exists(url)       | Checks if a url exists (with requests module) (needs http[s])                                   |
| url_links(URL)        | Get all links that are used in a specific URL (All "a" tags from html source) (Needs 'http[s]') |
| find_urls(text)       | returns list of all urls in a string using regex                                                |
| is_url(URL)           | checks if the string has the expression of a real url                                           |
| open_browser(url)     | opens given url in the new tab of default browser                                               |
<br>



#### Recommendations:

 - Using `import rx7 as rx`

<br />


Commands in Terminal:
--------------------------------
    $ python -m rx7 --wiki          (To open wiki page in browser)
    $ python -m rx7 --colors        (To show help for style class)
    $ python -m rx7 --help          (To open help menu)

<br />


Releases and Changelog:
---------
Take a look at [here](https://github.com/Ramin-RX7/RX7-Lib/blob/master/CHANGELOG.md) for the changelog
