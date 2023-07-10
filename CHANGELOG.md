# Changelog


###        (+ for new features, \* for changes, - for removed features)

<br>

<table>
  <tbody>

  <tr style="height: 42px;">
    <td style="width: 119px; height: 42px; text-align: center;"><strong>Version</strong></td>
    <td style="width: 153px; height: 42px; text-align: center;"><strong>Release Date</strong></td>
    <td style="width: 513px; height: 42px; text-align: center;"><strong>New Features &amp; Changes</strong></td>
  </tr>

  <tr>
    <td>
      <p style="text-align: center;">4.0.0</p>
    </td>
    <td style="text-align: center;">13/07/2023</td>
    <td>
      <div>* Use `pyproject.toml` instead of `setup.py`</div>
      <div>* Separate modules by files instead of classes</div>
      <div>- p()</div>
      <div>- func_info()</div>
      <div>* renamed Progressbar() to progressbar()</div>
      <div>+ internet.get()</div>
      <div>+ internet.post()</div>
    </td>
  </tr>


  <tr>
    <td>
      <p style="text-align: center;">3.3.0</p>
    </td>
    <td style="text-align: center;">29/04/2023</td>
    <td>
      <div>+ Files.basename()</div>
      <div>+ Files.dirname()</div>
      <div>+ Files.join_paths()</div>
      <div>* `pre_action` and `post_action` in IO  selective_input</div>
      <div>+ Record.timer decorator</div>
      <div>+ System.os_name()  </div>
    </td>
  </tr>

  <tr>
    <td>
      <p style="text-align: center;">3.2.0</p>
    </td>
    <td style="text-align: center;">10/03/2023</td>
    <td>
      <div>+ `environ` variable: environment variables as a dict</div>
      <div>+ `Terminal.size()`</div>
      <div>+ `exit()`: sys.exit()</div>
      <div>+ `files.get_drives()`</div>
      <div>+ IO.selective_input `choices` argument upgrade</div>
      <div>+ IO.selective_input `action` parameter</div>
      <div>- IO.selective_input `error` parameter is removed</div>
      <div>* Fixed `files.size()` for directories</div>
      <div>* `files.is_readonly()` now also works on Unix</div>
      <div>* Improved module call</div>
    </td>
  </tr>


  <tr>
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">3.1.0</p>
  </td>
  <td style="text-align: center;">23/12/2022</td>
  <td>
  <div>+ Record.timeit has default parameters now</div>
  <div>- removed progressbar()</div>
  <div>* Improved Style object creation</div>
  <div>* Improved Style.print implementation</div>
  <div>* Improved Style.log_ methods implementation</div>
  <div>* Terminal.run() now return exit code</div>
  <div>- Removed "Tuple" object</div>
  </td>
  </tr>

  <tr>
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">3.0.0</p>
  </td>
  <td style="text-align: center;">01/09/2021</td>
  <td>
  <div><b>+ class Internet</b></div>
  <div><b>+ class DateTime</b></div>
  <div>+ "Style.log" now has time prefix</div>
  <div>+ call = call_later</div>
  <div>+ IO.Input()</div>
  <div>+ IO.getpass()</div>
  <div>* io.selective_input choices can be dict</div>
  <div>+ System.mac_address()</div>
  </td>
  </tr>

  <tr>
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">2.9.0</p>
  </td>
  <td style="text-align: center;">15/12/2020</td>
  <td>
  <div>+ <b>IO Class</b>(wait_for_input() - selective_input() - yesno_input())</div>
  <div>* IMPORT SPEED IS 20x FASTER!</div>
  <div>+ argv (sys.argv)</div>
  <div>- Record.EndError</div>
  <div>+ overload (Decorator.overload)</div>
  <div>+ ABC,ABCMeta</div>
  </td>
  </tr>
  <tr>
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">2.8.0</p>
  </td>
  <td style="text-align: center;">15/11/2020</td>
  <td>
  <div>+ Decorator Class (attach_to_all --- Check_Type)</div>
  <div>+ pop()</div>
  <div>+ Tuple.pop()</div>
  <div>+ Record.timeit()</div>
  </td>
  </tr>
  <tr>
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">2.7.0</p>
  </td>
  <td style="text-align: center;">15/10/2020</td>
  <td>
  <div>+ getpass()</div>
  <div>+ style.log_ Family</div>
  <div>+ style.reset() = style.switch_default()</div>
  <div>+ load_module()</div>
  <div>+ record.last_lap()</div>
  </td>
  </tr>
  <tr>
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">2.6.0</p>
  </td>
  <td style="text-align: center;">01/10/2020</td>
  <td>
  <div>+ system.cpu_percent()</div>
  <div>+ system.pid_exists()</div>
  <div>+ Progressbar()<em> (Generator)</em></div>
  <div>+ pixel_color()</div>
  </td>
  </tr>
  <tr>
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">2.5.0</p>
  </td>
  <td style="text-align: center;">15/09/2020</td>
  <td>
  <div>+ Check_Type decorator</div>
  <div>+ system.pyshell_execute_bit()</div>
  <div>+ system.pids()</div>
  <div>+ record.lap round arg</div>
  </td>
  </tr>
  <tr>
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">2.4.0</p>
  </td>
  <td style="text-align: center;">01/09/2020</td>
  <td>
  <div>* rand -&gt; random</div>
  <div>+ random.shuffle()</div>
  <div>+ repeat function supports parameters</div>
  <div>+ sleep = wait&nbsp; &nbsp;---&nbsp; &nbsp;clear = cls&nbsp; &nbsp;---&nbsp; &nbsp;default_input = Input</div>
  <div>+ system.cpu_count()</div>
  </td>
  </tr>
  <tr>
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">2.3.0</p>
  </td>
  <td style="text-align: center;">19/08/2020</td>
  <td>
  <div>+ extract()</div>
  <div>+ screenshot()</div>
  <div>+ func_info()</div>
  </td>
  </tr>
  <tr>
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">2.2.0</p>
  </td>
  <td style="text-align: center;">03/08/2020</td>
  <td>
  <div>+ download()</div>
  <div>+ system.ip_website()</div>
  <div>+ system.win10_notification</div>
  </td>
  </tr>
  <tr>
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;">2.1.0</p>
  </td>
  <td style="text-align: center;">15/07/2020</td>
  <td>
  <div>* style class better performance in linux</div>
  <div>+&nbsp;<span style="text-align: center;">MEMBERS&nbsp;group&nbsp;in&nbsp;files&nbsp;class</span></div>
  <div><span style="text-align: center;">+ File object:&nbsp; self.basename, self.ext</span></div>
  <div><span style="text-align: center;">+ system.device_name()</span></div>
  <div><span style="text-align: center;">+&nbsp;</span><span style="text-align: center;">active_window_title() --- open_image()</span></div>
  </td>
  </tr>
  <tr>
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">
  <p style="text-align: center;"><strong>2.0.0</strong></p>
  </td>
  <td style="text-align: center;"><strong>01/07/2020</strong></td>
  <td>
  <div>+ <strong>Tuple object</strong></div>
  <div>rxobject</div>
  <div>+ record.reset()</div>
  <div>record.lap new arg</div>
  <div>+ New methods of files</div>
  <div>&nbsp; &nbsp; &nbsp; files.is_readonly()&nbsp; &nbsp;---&nbsp; &nbsp;files.is_hidden()</div>
  <div>&nbsp; &nbsp; &nbsp; files.search_file()&nbsp; &nbsp;---&nbsp; &nbsp;files.search_content()</div>
  <div>&nbsp; &nbsp; &nbsp; files.copy new arg&nbsp; &nbsp;---&nbsp; &nbsp;files.generate_tree()</div>
  <div><strong>+ File.MEMBERS </strong>(when in File(path), path is a directory&nbsp; (self.MEMBERS.TYPE_PATH)</div>
  <div>+ File.tree&nbsp; &nbsp; ---&nbsp; &nbsp; &nbsp;File.tree_dirs</div>
  <div>+ Input()&nbsp; <em>(Only on windows)</em></div>
  <div>+ restart_app()</div>
  </td>
  </tr>
  <tr>
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">1.9.0</td>
  <td style="width: 153px; height: 25px;">&nbsp; 09/06/2020</td>
  <td>
  <div>* re() --&gt; repeat()</div>
  <div>+ New Methods of System Class:</div>
  <div>&nbsp; &nbsp; &nbsp; &nbsp; ip_global(),&nbsp;ip_local(),</div>
  <div>&nbsp; &nbsp; &nbsp; &nbsp; ram_free(), ram_percent(),</div>
  <div>&nbsp; &nbsp; &nbsp; &nbsp; ram_total(),&nbsp;ram_used(),</div>
  <div>&nbsp; &nbsp; &nbsp; &nbsp; boot_time()</div>
  <div>+ convert_bytes()</div>
  </td>
  </tr>
  <tr>
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">1.8.0</td>
  <td style="text-align: center;">24/05/2020</td>
  <td>
  <div>+ style.switch_default()</div>
  <div>
  <div>+ Now Linux&nbsp;supports&nbsp;cls()</div>
  <div>
  <div>+ style&nbsp;object:&nbsp;supports&nbsp;multiply,add,index</div>
  <div>
  <div>+ rand.choice Choose &gt;1 &amp; duplicate</div>
  <div>* rand.choice --&gt; rand.choose</div>
  </div>
  </div>
  </div>
  </td>
  </tr>
  <tr>
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">1.7.0</td>
  <td style="text-align: center;">&nbsp; 08/05/2020</td>
  <td>
  <div>
  <div>+ call_later()&nbsp;&nbsp;-&nbsp;&nbsp;wait_for()</div>
  <div>+ terminal_size()&nbsp;&nbsp;-&nbsp;&nbsp;cwd()</div>
  <div>+ right_port,left_port arg for progressbar()</div>
  <div>+ file.remove() for static usage</div>
  <div>+ self.type in file class</div>
  <div>+ if in file(x), x is a directory:<br />x.files , x.file_list , x.all_files , x.all_files_sep</div>
  <div>+ file.isdir() , file.isfile() for static usage.</div>
  <div>* string() =&gt; cons_int()</div>
  <div>* progressbar() arg names</div>
  <div>* file.delete() and file.delete_dir()&nbsp;=&gt;&nbsp;delete()</div>
  <div>* Change replace() and insert() args oreder</div>
  </div>
  </td>
  </tr>
  <tr>
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">1.5.0</td>
  <td style="text-align: center;">21/04/2020</td>
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
  <tr>
  <td style="width: 119px; height: 25px; text-align-last: center; text-align: center;">1.3.0</td>
  <td style="width: 153px; height: 25px;">
  <p style="text-align: center;">08/04/2020</p>
  </td>
  <td>
  <div>+ __init__ &amp; read &amp; write &amp; content&nbsp; func&nbsp;of&nbsp;file&nbsp;class</div>
  <div>* Prgoressbar&nbsp;default&nbsp;args</div>
  </td>
  </tr>
  <tr>
  <td style="width: 119px; height: 25px; text-align-last: center;">
  <p style="text-align: center;">1.0.0</p>
  </td>
  <td style="width: 153px; height: 25px;">
  <p style="text-align: center;">18/03/2020</p>
  </td>
  <td><i>Initial release</i></td>
  </tr>
  </tbody>
</table>
</body>