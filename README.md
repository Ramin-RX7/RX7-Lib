![PyPI - License](https://img.shields.io/badge/downloads-32k%2Fmonth-brightgreen?style=plastic) ![PyPI - License](https://img.shields.io/pypi/l/rx7?color=orange&style=plastic) ![PyPI - License](https://img.shields.io/badge/status-stable-success?style=plastic)
--------------------------------------------------------

"rx7" library is here to help you make your code shorter!
--------------------------------------------------------

### \- Most Usefull function and mexthods are collected.

### \- Special Features

### \- Simple and easy to understad API

<hr />

### Install
    pip install rx7
### Upgrade
    pip install --upgrade rx7


<br />


# Here is the brief documentaion:
### *(Complete documentation with details will be added soon in the Wiki section)*
<!--### *if you need more info about variables, functions and classes of rx7-lib, check out the full Documentaion in [Here](https://github.com/Ramin-RX7/RX7-Lib/wiki)*
-->


<h2>List of Variables:</h2>

|         |                                                         |
|---------|---------------------------------------------------------|
| argv    | sys.argv (return list of given arguments from terminal) |
| ABC     | Parent for classes which have abstractmethods           |
| exit    | Equivalent sys.exit (returning exit code to terminal)   |
| environ | Returns environment variables in a dictionary format    |


<br>


List of Functions:
------------------
|                                                          |                                                                                                  |
|----------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| p()                                                      | print() function.                                                                                |
| repeat(function,n)                                       | Repeat F_Name function for n times.                                                              |
| rev(v)  (REMOVED 2.4.0)                                  | Reverse v and returns it. (Everything like str,list,int)                                         |
| read(file)                                               | Return content of the file.                                                                      |
| write(file,mode,text)                                    | Write things you want in file content. (Read Doc String)                                         |
| wait(n)sleep(n)                                          | Stop code executing for n seconds                                                                |
| cls()clear()                                             | It Clears the Terminal                                                                           |
| progressbar() (*removed in v3.1)                         | In-App Progressbar. (Read Doc String)                                                            |
| cons_integer(Frst,Lst)                                   | Return string from Frst to Lst (Read Doc String) (v1.7)                                          |
| force(tpl,*var)                                          | Return tpl with adding var(s) to it.                                                             |
| erase(tpl,*var)                                          | Return tpl with removing var(s) from it.                                                         |
| replace(tpl,ind,var)                                     | Replace tpl[ind] with var                                                                        |
| insert(tpl,ind,var)                                      | Set tpl[ind] to var. (Note that tpl[ind] will be tpl[ind+1])                                     |
| pop(tpl,index)                                           | Remove member with index of 'index' from a tuple                                                 |
| wait_for(button)                                         | Waits for user to press specific button.                                                         |
| call_later(func,args,delay)                              | Call func(args) after delay time.                                                                |
| convert_bytes(num)                                       | convert bytes to (KB,MB,GB,TB)                                                                   |
| Input(prompt,default)                                    | Prompt an input message with default answer (value) (ONLY ON WINDOWS)                            |
| default_input()                                          | Same as `default_input`                                                                          |
| restart_app()                                            | Restart running python program                                                                   |
| active_window_title()                                    | Return Active Window Title                                                                       |
| open_image(path)                                         | Open image with default image viewer (Mac OS is not supported)                                   |
| download(url)                                            | To download files with memory saver and progressbar                                              |
| extract(file,path,pwd)                                   | Extract Zip file with password to path                                                           |
| screenshot(name)                                         | Take a screenshot and save it.                                                                   |
| func_info(function)                                      | Print information of function                                                                    |
| Check_Type                                               | Decorator that raise TypeError if function argument type is wrong (Read Help)                    |
| Progressbar()                                            | Generator of progressbar() which you can use it to do some stuff between your delays (Read Help) |
| pixel_color(X,Y)                                         | Return RGB color of pixel[X,Y]                                                                   |
| getpass(prompt)                                          | Prompt for a password, with echo turned off.                                                     |
| import_module(path)                                      | Return given path (file with any extension) as a Module                                          |


<br>


<h2>List of Classes:</h2>

<h3>&nbsp; Class Random:&nbsp; &nbsp;<em>Random Variable Generator Class.</em></h3>

|                          |                                                |
|--------------------------|------------------------------------------------|
| choose(iter,k,duplicate) | Choose k random items from iterable or string. |
| integer(Frst,Lst)        | Choose integer in range [Frst,Lst]             |
| O1(decimal_nom=17)       | Return x in interval [0,1)                     |
| number(Frst,Lst)         | Return x in interval [Frst,Lst]                |
| shuffle(iterable)        | Return shuffled version of iterable            |

<br>


<h3>&nbsp; Class System:&nbsp; &nbsp;<em>Some system actions and information.</em></h3>

|                               |                                                                                  |
|-------------------------------|----------------------------------------------------------------------------------|
| accname()                     |         return account username you have logged in.                              |
| pid()                         |         Get pid number of terminal and return it.                                |
| disk_usage(path)              | ########                                                                         |
| chdir                         | Change directory of terminal.                                                    |
| SHUT_DOWN()                   | Shut Down the PC.                                                                |
| RESTART()                     | Restart the PC.                                                                  |
| terminal_size()               | Return terminal size in tuple  (columns,lines).                                  |
| cwd()                         | Return Carrent Working Directory.                                                |
| ip_global()                   | Returns Global IP.                                                               |
| ip_local()                    | Returns Local IP.                                                                |
| ram_total()                   | Returns total ram of the system.                                                 |
| ram_used()                    | Returns Used Space of the ram of the system.                                     |
| ram_free()                    | Returns Available (Free) space of system ram.                                    |
| boot_time()                   | Return system boot time in seconds since the epoch.                              |
| device_name()                 | Returns Device Name                                                              |
| ip_website(url)               | Returns url ip address                                                           |
| win10_notification()          | Display windows 10 notification (READ DOCSTRING) (ONLY WIN10 SUPPORTED)          |
| cpu_count(logical=True)       |         Return the number of logical/physical CPUs in the system                 |
| pyshell_execute_bit()         |         To determine whether Python shell is executing in 32bit or 64bit         |
| pids()                        |                 Return a list of current running PIDs                            |
| pid_exists(pid)               | Return True if pid exists else False                                             |
|         cpu_percent()         |         Return the current CPU utilization as a percentage                       |



<br>


<h3>&nbsp; Class Files: (Static<strong style="font-size: 14px;">&nbsp;methods)&nbsp;</strong><em style="font-size: 14px;">Actions and information about files.</em></h3>

| METHOD                                                        | DESCRIPTION                                                                   |
|---------------------------------------------------------------|-------------------------------------------------------------------------------|
| size(path)                                                    | Return size of the file in byte(s). Also work on                              |
| delete(path)                                                  | Use this to delete a file (Not folder).                                       |
| rename(path)                                                  | Rename files with this function.                                              |
| abspath(path)                                                 | Return absolute path of given path.                                           |
| exists(path)                                                  | Return Boolean. If exists True, else: False                                   |
| mdftime(path)                                                 | Get last modify time of the file.                                             |
| acstime(path)                                                 | Get last access time of the file.                                             |
| move(src,dst)                                                 | Move file from src to dst. (Read Doc String of copy func)                     |
| copy(src,dst,metadata=True)                                   | Copy file (with metadata) from src to dst. (Also work on folders)             |
| hide(path)                                                    | Hide given path. (It can be file or directory.)                               |
| read_only(path,mode=True)                                     | Make file or folder read-only. (Read Doc String)                              |
| read(path)                                                    | Return content of the path                                                    |
| write(path,text='',...)                                       | Same as write function.                                                       |
| isdir(path)                                                   | Return True for directory and False for others.                               |
| isfile(path)                                                  | Return True for file and False for others.                                    |
| is_hidden(path)                                               | Check whether path is hidden or not                                           |
| is_readonly(path)                                             | Check whether path is readonly or not                                         |
| search_file(pattern,path,mode)                                | search for pattern in path (Read function doc string)                         |
| search_content(path,word)                                     | Search for word in all files in path, return list of files that contain word  |
| mkdir(path)                                                   | Make directory (More than one if its possible!)                               |
| generate_tree(dir_path)                                       | Returns a visual tree of dir_path                                             |
| get_drives()                                                  | (Windows only) Get currently available drives                                 |
| &nbsp; &nbsp; &nbsp; &nbsp; MEMBERS (Family)                  |                                                                               |
| MEMBERS.all_exactdir                                          | List of all things those are in exact directory                               |
| MEMBERS.files_exactdir                                        | List of files which are in exact directory                                    |
| MEMBERS.dirs_exactdir                                         | List of dirs which are in exact directory                                     |
| MEMBERS.files_all                                             | List of files which are in exact directory and all sub-directories            |
| MEMBERS.files_all_sep                                         | List of files which are in exact directory and all sub-directories seprated by their directories |
| MEMBERS.dirs_all                                              | List of directories (Exact dir and all sub-dirs)                              |
| MEMBERS.all_all_sep                                           | List of everything thing in path (exact dir &amp; sub-dirs)                   |


<br>


<h3>&nbsp; Class Style:&nbsp; &nbsp; <em>Changing text Color,BG &amp; Style. (Read Doc String)</em></h3>

|                                                         |                                                             |
|---------------------------------------------------------|-------------------------------------------------------------|
| print\(\*values, color, BG, style, end, sep\)           | Print txt with selected color,BG,style\.\(Read Doc String\) |
| switch\(color,BG,style\)                                | Change Terminal Attributes Until another Call\.             |
| switch\_default\(\)                                     | Restore Terminal Attributes\.                               |
| reset                                                   | =switch\_default                                            |
| log\_&nbsp; \(Family\)                                  | 5 Different Style\.print with ready color and style         |


<br>


<h3>&nbsp; Class Record:&nbsp; &nbsp;<em>Record time of a certain actions. (Read Doc String)</em></h3>

|                                                                     |                                                                            |
|---------------------------------------------------------------------|----------------------------------------------------------------------------|
| __init__()                                                          | Set Start Time.                                                            |
| self.stop(self)                                                     | Stops Recording (You can not lap anymore)                                  |
| self.lap(self, save=True, round=15)                                 | Rreturn time between start time. if save==True: add that time to self.laps |
| self.laps                                                           | A list that contains all laps you have done                                |
| self.reset(self, start=False)                                       | Empty self.laps, if start is True: set start time to now                   |
| self.last_lap(save=True)                                            | Return elapsed time from last lap (save it in self.laps if save is true)   |
| timeit(code,setup, times,globals_) | Run the 'code' for 'times' times and return time it needs (all, not once)  |


<br>


<h3>&nbsp; Class Decorator:&nbsp; &nbsp;<em>Useful decorators you might want to use</em></h3>

| **Method**     | **Description**                                                                                    |
|----------------|----------------------------------------------------------------------------------------------------|
| Check_Type     | Decorator that raise TypeError if function argument type is wrong (Read Help)                      |
| overload       | Make your function accept different kind of argument and structure with defining it more than once |
| attach_to_all  | Attach Decorator.decorator_all to all functions of a class (Class decorator)                       |
| abstractmethod | A decorator indicating abstract methods.                                                           |
<br />


<h3>&nbsp; Class Terminal:&nbsp; &nbsp;<em>functions related to working with terminal</em></h3>

| **Method**          | **Description**                                             |
|:------------------- |:----------------------------------------------------------- |
| run(command)        | executes `command` live in terminal                         |
| getoutput(commands) | runs the `command` in the background and returns the output |
| size()              | Returns the size of terminal in tuple (columns,rows)        |
<br>


<h3>&nbsp; Class IO:&nbsp; &nbsp;<em>Useful methods when working with user input</em></h3>

| **Method**                   | **Description**                                                          |
|------------------------------|--------------------------------------------------------------------------|
| wait_for_input(prompt)       | Asks for user input, until they enter something else than whitespaces    |
| selective_input()            | Check repository wiki for full documentation                             |
| yesno_input(prompt, default) | wait for user to enter one of (`yes`,`no`, `y`, `n`). (Case insensitive) |
| Input(prompt, default_value) | (Windows only) Types default value before getting user's input           |
| getpass(prompt)              | Gets users input without showing their input (`getpass.getpass()`)       |
<br>


<h3>&nbsp; Class Internet:&nbsp; &nbsp;<em>Methods for working with network and internet related stuffs</em></h3>

| **METHOD**            | **DESCRIPTION**                                                                                 |
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



## Recommendations:

 <!-- - Using an IDE that shows Function and Class Help is highly recommended. *([VS Code](https://code.visualstudio.com/ "Microsoft VS Code")* -- *[PyCharm](https://www.jetbrains.com/pycharm/ "Jetbrains PyCharm"))* -->

 - Using `from rx7 import FUNC_or_CLASS`
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

####        (+ for new features, \* for changes, - for removed features)

<table style="height: 10px; margin-left: 10px; width: 519px;" cellpadding="5">
  <tbody>

  <tr style="height: 42px;">
    <td style="width: 119px; height: 42px; text-align: center;"><strong>Version</strong></td>
    <td style="width: 153px; height: 42px; text-align: center;"><strong>Release Date</strong></td>
    <td style="width: 513px; height: 42px; text-align: center;"><strong>New Features &amp; Changes</strong></td>
  </tr>


  <tr style="height: 25px;">
    <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
      <p style="text-align: center;">3.2.0</p>
    </td>
    <td style="width: 153px; height: 25px; text-align: center;">10/03/2023</td>
    <td style="width: 513px; height: 25px; text-align: center;">
      <div style="text-align: left;">+ `environ` variable: environment variables as a dict</div>
      <div style="text-align: left;">+ `Terminal.get_size()`</div>
      <div style="text-align: left;">+ `exit()`: sys.exit()</div>
      <div style="text-align: left;">+ `files.get_drives()`</div>
      <div style="text-align: left;">+ IO.selective_input `choices` argument upgrade</div>
      <div style="text-align: left;">+ IO.selective_input `action` parameter</div>
      <div style="text-align: left;">- IO.selective_input `error` parameter is removed</div>
      <div style="text-align: left;">* Fixed `files.size()` for directories</div>
      <div style="text-align: left;">* `files.is_readonly()` now also works on Unix</div>
      <div style="text-align: left;">* Improved module call</div>
    </td>
  </tr>


  <tr style="height: 25px;">
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">3.1.0</p>
  </td>
  <td style="width: 153px; height: 25px; text-align: center;">23/12/2022</td>
  <td style="width: 513px; height: 25px; text-align: center;">
  <div style="text-align: left;">+ Record.timeit has default parameters now</div>
  <div style="text-align: left;">- removed progressbar()</div>
  <div style="text-align: left;">* Improved Style object creation</div>
  <div style="text-align: left;">* Improved Style.print implementation</div>
  <div style="text-align: left;">* Improved Style.log_ methods implementation</div>
  <div style="text-align: left;">* Terminal.run() now return exit code</div>
  <div style="text-align: left;">- Removed "Tuple" object</div>
  </td>
  </tr>

  <tr style="height: 25px;">
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">3.0.0</p>
  </td>
  <td style="width: 153px; height: 25px; text-align: center;">01/09/2021</td>
  <td style="width: 513px; height: 25px; text-align: center;">
  <div style="text-align: left;"><b>+ class Internet</b></div>
  <div style="text-align: left;"><b>+ class DateTime</b></div>
  <div style="text-align: left;">+ "Style.log" now has time prefix</div>
  <div style="text-align: left;">+ call = call_later</div>
  <div style="text-align: left;">+ IO.Input()</div>
  <div style="text-align: left;">+ IO.getpass()</div>
  <div style="text-align: left;">* io.selective_input choices can be dict</div>
  <div style="text-align: left;">+ System.mac_address()</div>
  </td>
  </tr>

  <tr style="height: 25px;">
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">2.9.0</p>
  </td>
  <td style="width: 153px; height: 25px; text-align: center;">15/12/2020</td>
  <td style="width: 513px; height: 25px; text-align: center;">
  <div style="text-align: left;">+ <b>IO Class</b>(wait_for_input() - selective_input() - yesno_input())</div>
  <div style="text-align: left;">+ <b>Decorator Class</b> (attach_to_all ---&nbsp;Check_Type)</div>
  <div style="text-align: left;">* IMPORT SPEED IS 20x FASTER!</div>
  <div style="text-align: left;">+ argv (sys.argv)</div>
  <div style="text-align: left;">- Record.EndError</div>
  <div style="text-align: left;">+ overload (Decorator.overload)</div>
  <div style="text-align: left;">+ ABC,ABCMeta</div>
  </td>
  </tr>
  <tr style="height: 25px;">
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">2.8.0</p>
  </td>
  <td style="width: 153px; height: 25px; text-align: center;">15/11/2020</td>
  <td style="width: 513px; height: 25px; text-align: center;">
  <div style="text-align: left;">+ Decorator Class (attach_to_all ---&nbsp;Check_Type)</div>
  <div style="text-align: left;">+ pop()</div>
  <div style="text-align: left;">+ Tuple.pop()</div>
  <div style="text-align: left;">+ Record.timeit()</div>
  </td>
  </tr>
  <tr style="height: 25px;">
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">2.7.0</p>
  </td>
  <td style="width: 153px; height: 25px; text-align: center;">15/10/2020</td>
  <td style="width: 513px; height: 25px; text-align: center;">
  <div style="text-align: left;">+ getpass()</div>
  <div style="text-align: left;">+ style.log_ Family</div>
  <div style="text-align: left;">+ style.reset() = style.switch_default()</div>
  <div style="text-align: left;">+ load_module()</div>
  <div style="text-align: left;">+ record.last_lap()</div>
  </td>
  </tr>
  <tr style="height: 25px;">
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">2.6.0</p>
  </td>
  <td style="width: 153px; height: 25px; text-align: center;">01/10/2020</td>
  <td style="width: 513px; height: 25px; text-align: center;">
  <div style="text-align: left;">+ system.cpu_percent()</div>
  <div style="text-align: left;">+ system.pid_exists()</div>
  <div style="text-align: left;">+ Progressbar()&nbsp;<em>(Generator)</em></div>
  <div style="text-align: left;">+ pixel_color()</div>
  </td>
  </tr>
  <tr style="height: 25px;">
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">2.5.0</p>
  </td>
  <td style="width: 153px; height: 25px; text-align: center;">15/09/2020</td>
  <td style="width: 513px; height: 25px; text-align: center;">
  <div style="text-align: left;">+ Check_Type decorator</div>
  <div style="text-align: left;">+ system.pyshell_execute_bit()</div>
  <div style="text-align: left;">+ system.pids()</div>
  <div style="text-align: left;">+ record.lap&nbsp;round&nbsp;arg</div>
  </td>
  </tr>
  <tr style="height: 25px;">
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">2.4.0</p>
  </td>
  <td style="width: 153px; height: 25px; text-align: center;">01/09/2020</td>
  <td style="width: 513px; height: 25px; text-align: center;">
  <div style="text-align: left;">* rand -&gt; random</div>
  <div>
  <div style="text-align: left;">+ random.shuffle()</div>
  <div>
  <div style="text-align: left;">+ repeat function supports parameters</div>
  <div>
  <div style="text-align: left;">+ sleep = wait&nbsp; &nbsp;---&nbsp; &nbsp;clear = cls&nbsp; &nbsp;---&nbsp; &nbsp;default_input = Input</div>
  <div style="text-align: left;">+ system.cpu_count()</div>
  </div>
  </div>
  </div>
  </td>
  </tr>
  <tr style="height: 25px;">
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">2.3.0</p>
  </td>
  <td style="width: 153px; height: 25px; text-align: center;">19/08/2020</td>
  <td style="width: 513px; height: 25px; text-align: center;">
  <p style="text-align: left;">+ extract()</p>
  <p style="text-align: left;">+ screenshot()</p>
  <p style="text-align: left;">+ func_info()</p>
  </td>
  </tr>
  <tr style="height: 25px;">
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">2.2.0</p>
  </td>
  <td style="width: 153px; height: 25px; text-align: center;">03/08/2020</td>
  <td style="width: 513px; height: 25px; text-align: center;">
  <p style="text-align: left;">+ download()</p>
  <p style="text-align: left;">+ system.ip_website()</p>
  <p style="text-align: left;">+ system.win10_notification</p>
  </td>
  </tr>
  <tr style="height: 25px;">
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">2.1.0</p>
  </td>
  <td style="width: 153px; height: 25px; text-align: center;">15/07/2020</td>
  <td style="width: 513px; height: 25px; text-align: center;">
  <p style="text-align: left;">* style class better performance in linux</p>
  <p style="text-align: left;">+&nbsp;<span style="text-align: center;">MEMBERS&nbsp;group&nbsp;in&nbsp;files&nbsp;class</span></p>
  <p style="text-align: left;"><span style="text-align: center;">+ File object:&nbsp; self.basename, self.ext</span></p>
  <p style="text-align: left;"><span style="text-align: center;">+ system.device_name()</span></p>
  <p style="text-align: left;"><span style="text-align: center;">+&nbsp;</span><span style="text-align: center;">active_window_title() --- open_image()</span></p>
  </td>
  </tr>
  <tr style="height: 25px;">
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;"><strong>2.0.0</strong></p>
  </td>
  <td style="width: 153px; height: 25px; text-align: center;"><strong>01/07/2020</strong></td>
  <td style="width: 513px; height: 25px; text-align: center;">
  <p style="text-align: left;">+ <strong>Tuple object&nbsp; &nbsp;---&nbsp; &nbsp;rxobject</strong></p>
  <p style="text-align: left;">+ record.reset()&nbsp; &nbsp;---&nbsp; &nbsp;record.lap new arg</p>
  <p style="text-align: left;">+ New methods of files</p>
  <p style="text-align: left;">&nbsp; &nbsp; &nbsp; files.is_readonly()&nbsp; &nbsp;---&nbsp; &nbsp;files.is_hidden()</p>
  <p style="text-align: left;"><strong>&nbsp; &nbsp; &nbsp; files.search_file()&nbsp; &nbsp;---&nbsp; &nbsp;files.search_content()</strong></p>
  <p style="text-align: left;">&nbsp; &nbsp; &nbsp; files.copy new arg</p>
  <p style="text-align: left;"><strong>&nbsp; &nbsp; &nbsp; files.generate_tree()</strong></p>
  <p style="text-align: left;"><strong>+ File.MEMBERS </strong>(when in File(path), path is a directory&nbsp; (self.MEMBERS.TYPE_PATH)</p>
  <p style="text-align: left;"><strong>+ File.tree&nbsp; &nbsp; ---&nbsp; &nbsp; &nbsp;File.tree_dirs</strong></p>
  <p style="text-align: left;"><strong>+ Input()</strong>&nbsp; <em>(Only on windows)</em></p>
  <p style="text-align: left;">+ restart_app()</p>
  </td>
  </tr>
  <tr style="height: 25px;">
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">1.9.0</td>
  <td style="width: 153px; height: 25px;">&nbsp; 09/06/2020</td>
  <td style="width: 513px; height: 25px; text-align: center;">
  <p style="text-align: left;">* re() --&gt; repeat()</p>
  <p style="text-align: left;">+ New Methods of System Class:&nbsp; ip_global(),&nbsp;ip_local(),&nbsp;ram_free(), ram_percent(),&nbsp;ram_total(),&nbsp;ram_used(), boot_time()</p>
  <p style="text-align: left;">+ convert_bytes()</p>
  </td>
  </tr>
  <tr style="height: 25px;">
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">1.8.0</td>
  <td style="width: 153px; height: 25px; text-align: center;">24/05/2020</td>
  <td style="width: 513px; height: 25px; text-align: center;">
  <div style="text-align: left;">+ style.switch_default()</div>
  <div>
  <div style="text-align: left;">+ Now Linux&nbsp;supports&nbsp;cls()</div>
  <div>
  <div style="text-align: left;">+ style&nbsp;object:&nbsp;supports&nbsp;multiply,add,index</div>
  <div>
  <div style="text-align: left;">+ rand.choice Choose &gt;1 &amp; duplicate</div>
  <div style="text-align: left;">* rand.choice --&gt; rand.choose</div>
  </div>
  </div>
  </div>
  </td>
  </tr>
  <tr style="height: 25px;">
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">1.7.0</td>
  <td style="width: 153px; height: 25px; text-align: center;">&nbsp; 08/05/2020</td>
  <td style="width: 513px; height: 25px; text-align: center;">
  <div>
  <div style="text-align: left;">+ call_later()&nbsp;&nbsp;-&nbsp;&nbsp;wait_for()</div>
  <div style="text-align: left;">+ terminal_size()&nbsp;&nbsp;-&nbsp;&nbsp;cwd()</div>
  <div style="text-align: left;">+ right_port,left_port arg for progressbar()</div>
  <div style="text-align: left;">+ file.remove() for static usage</div>
  <div style="text-align: left;">+ self.type in file class</div>
  <div style="text-align: left;">+ if in file(x), x is a directory:<br />x.files , x.file_list , x.all_files , x.all_files_sep</div>
  <div style="text-align: left;">+ file.isdir() , file.isfile() for static usage.</div>
  <div style="text-align: left;">* string() =&gt; cons_int()</div>
  <div style="text-align: left;">* progressbar() arg names</div>
  <div style="text-align: left;">* file.delete() and file.delete_dir()&nbsp;=&gt;&nbsp;delete()</div>
  <div style="text-align: left;">* Change replace() and insert() args oreder</div>
  </div>
  </td>
  </tr>
  <tr style="height: 25px;">
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">1.5.0</td>
  <td style="width: 153px; height: 25px; text-align: center;">21/04/2020</td>
  <td style="width: 513px; height: 25px; text-align: left;">
  <div>
  <div>
  <div>+ 'replace' and insert 'functions' for tuples</div>
  <div>+ 'end' arg for style.print()</div>
  <div>+ 'self.laps' in record class will display all laps</div>
  <div>* style.text =&gt; style.print</div>
  <div>* record.stop =&gt; record.lap</div>
  <div>* now 'record.stop()' will stop recording.</div>
  </div>
  </div>
  </td>
  </tr>
  <tr style="height: 25px;">
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">1.3.0</td>
  <td style="width: 153px; height: 25px;">
  <p style="text-align: center;">08/04/2020</p>
  </td>
  <td style="width: 513px; height: 25px; text-align: center;">
  <div style="text-align: left;">+ __init__ &amp; read &amp; write &amp; content&nbsp; func&nbsp;of&nbsp;file&nbsp;class</div>
  <div style="text-align: left;">* Prgoressbar&nbsp;default&nbsp;args</div>
  </td>
  </tr>
  <tr style="height: 25px;">
  <td style="width: 119px; height: 25px; text-align-last: center;">
  <p style="text-align: center;">1.0.0</p>
  </td>
  <td style="width: 153px; height: 25px;">
  <p style="text-align: center;">18/03/2020</p>
  </td>
  <td style="width: 513px; height: 25px; text-align: center;">####</td>
  </tr>
  </tbody>
</table>