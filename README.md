<p style="font-size: 27px; font-family: Impact, Charcoal, sans-serif;">rx7 Module&nbsp; -&nbsp; Written By&nbsp; <em><span style="background-color: #ffffff;"><a style="background-color: #ffffff;" title="RX7" href="http://rx7.ir/" target="_blank" rel="noopener">Ramin RX7</a></span></em></p>
<h3>rx7 Module is here to help you make your code shorter!</h3>
<h3>(Most) Usefull function and methods are collected.</h3>
### See Features Preview [Here](#FeaturesPreview "Here")
<p>&nbsp;</p>
<h2>List of Functions:</h2>
<table style="height: 471px; width: 567px; margin-left: 20px;">
<tbody>
<tr>
<td style="width: 155px;">p()</td>
<td style="width: 396px;">print() function. (Read Doc String)</td>
</tr>
<tr>
<td style="width: 155px;">repeat(function,n)</td>
<td style="width: 396px;">Repeat F_Name function for n times.</td>
</tr>
<tr>
<td style="width: 155px;">rev(v)</td>
<td style="width: 396px;">Reverse v and returns it. (Everything like str,list,int)</td>
</tr>
<tr>
<td style="width: 155px;">read(file)</td>
<td style="width: 396px;">Return content of the file.</td>
</tr>
<tr>
<td style="width: 155px;">write(file,mode,text)</td>
<td style="width: 396px;">Write things you want in file content.&nbsp;(Read Doc String)</td>
</tr>
<tr>
<td style="width: 155px;">wait(n)</td>
<td style="width: 396px;">Stop code executing for n seconds</td>
</tr>
<tr>
<td style="width: 155px;">cls()</td>
<td style="width: 396px;">It Clears the Terminal</td>
</tr>
<tr>
<td style="width: 155px;">progressbar()</td>
<td style="width: 396px;">In-App Progressbar. (Read Doc String)</td>
</tr>
<tr>
<td style="width: 155px;">cons_integer(Frst,Lst)</td>
<td style="width: 396px;">Return string from Frst to Lst (Read Doc String) (v1.7)</td>
</tr>
<tr>
<td style="width: 155px;">force(tpl,*var)</td>
<td style="width: 396px;">Return tpl with adding var(s) to it.</td>
</tr>
<tr>
<td style="width: 155px;">erase(tpl,*var)</td>
<td style="width: 396px;">Return tpl with removing var(s) from it.</td>
</tr>
<tr>
<td style="width: 155px;">replace(tpl,ind,var)</td>
<td style="width: 396px;">Replace tpl[ind] with var</td>
</tr>
<tr>
<td style="width: 155px;">insert(tpl,ind,var)</td>
<td style="width: 396px;">Set tpl[ind] to var. (Note that tpl[ind] will be tpl[ind+1])</td>
</tr>
<tr>
<td style="width: 155px;">wait_for(button)</td>
<td style="width: 396px;">Waits for user to press specific button.&nbsp;</td>
</tr>
<tr>
<td style="width: 155px;">call_later(func,args,delay)</td>
<td style="width: 396px;">Call func(args) after delay time.&nbsp;</td>
</tr>
</tbody>
</table>
<h2>List of Classes:</h2>
<h3>&nbsp;Class rand:&nbsp; &nbsp;<em>Random&nbsp;Variable&nbsp;Generator&nbsp;Class.</em></h3>
<table style="height: 100px; width: 574px; margin-left: 40px;" cellpadding="5px">
<tbody>
<tr>
<td style="width: 173px;">choose(iter,k,duplicate)</td>
<td style="width: 387px;">Choose k random items from iterable or string.</td>
</tr>
<tr>
<td style="width: 173px;">integer(Frst,Lst)</td>
<td style="width: 387px;">Choose integer in range [Frst,Lst]</td>
</tr>
<tr>
<td style="width: 173px;">O1(decimal_nom=17)</td>
<td style="width: 387px;">Return x in interval [0,1)</td>
</tr>
<tr>
<td style="width: 173px;">number(Frst,Lst)</td>
<td style="width: 387px;">Return x in interval [Frst,Lst]</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h3>&nbsp; Class system:&nbsp; &nbsp;<em>Some system actions and information.</em></h3>
<table style="height: 100px; width: 574px; margin-left: 40px;" cellpadding="5px">
<tbody>
<tr>
<td style="width: 173px;">accname()</td>
<td style="width: 387px;">
<div>
<div>return&nbsp;account&nbsp;username&nbsp;you&nbsp;have&nbsp;logged&nbsp;in.</div>
</div>
</td>
</tr>
<tr>
<td style="width: 173px;">pid()</td>
<td style="width: 387px;">
<div>
<div>Get&nbsp;pid&nbsp;number&nbsp;of&nbsp;terminal&nbsp;and&nbsp;return&nbsp;it.</div>
</div>
</td>
</tr>
<tr>
<td style="width: 173px;">disk_usage(path)</td>
<td style="width: 387px;">########</td>
</tr>
<tr>
<td style="width: 173px;">chdir</td>
<td style="width: 387px;">Change directory of terminal.</td>
</tr>
<tr>
<td style="width: 173px;">SHUT_DOWN()</td>
<td style="width: 387px;">Shut Down the PC.</td>
</tr>
<tr>
<td style="width: 173px;">RESTART()</td>
<td style="width: 387px;">Restart the PC.</td>
</tr>
<tr>
<td style="width: 173px;">terminal_size()</td>
<td style="width: 387px;">Return terminal size in tuple&nbsp; (columns,lines).&nbsp;</td>
</tr>
<tr>
<td style="width: 173px;">cwd()</td>
<td style="width: 387px;">Return Carrent Working Directory.&nbsp;</td>
</tr>
<tr>
<td style="width: 173px;">ip_global()</td>
<td style="width: 387px;">Returns Global IP.</td>
</tr>
<tr>
<td style="width: 173px;">ip_local()</td>
<td style="width: 387px;">Returns Local IP.</td>
</tr>
<tr>
<td style="width: 173px;">ram_total()</td>
<td style="width: 387px;">Returns total ram of the system.</td>
</tr>
<tr>
<td style="width: 173px;">ram_used()</td>
<td style="width: 387px;">Returns Used Space of the ram of the system.</td>
</tr>
<tr>
<td style="width: 173px;">ram_free()</td>
<td style="width: 387px;">Returns Available (Free) space of system ram.</td>
</tr>
<tr>
<td style="width: 173px;">boot_time()</td>
<td style="width: 387px;">Return system boot time in seconds since the epoch.</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h3>&nbsp; Class file: (C<strong>lass methods)&nbsp;</strong><em>Actions and information about files.</em></h3>
<table style="height: 100px; width: 574px; margin-left: 40px;" cellpadding="5px">
<tbody>
<tr style="height: 36px;">
<td style="width: 173px; height: 36px;">__init__(self,path)</td>
<td style="width: 387px; height: 36px;">Creating file object.</td>
</tr>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">self.size</td>
<td style="width: 387px; height: 18px;">
<div>
<div>size&nbsp;of&nbsp;the&nbsp;file&nbsp;in&nbsp;byte(s).&nbsp;Also&nbsp;work&nbsp;on&nbsp;directories.</div>
</div>
</td>
</tr>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">self.abspath</td>
<td style="width: 387px; height: 18px;">
<div>
<div>Return&nbsp;absolute&nbsp;path&nbsp;of&nbsp;given&nbsp;path.</div>
</div>
</td>
</tr>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">self.exists</td>
<td style="width: 387px; height: 18px;">Return Boolean. If exists True, else: False</td>
</tr>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">self.mdftime</td>
<td style="width: 387px; height: 18px;">
<div>
<div>Get&nbsp;last&nbsp;modify&nbsp;time&nbsp;of&nbsp;the&nbsp;file.</div>
</div>
</td>
</tr>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">self.acstime</td>
<td style="width: 387px; height: 18px;">
<div>
<div>Get&nbsp;last&nbsp;access&nbsp;time&nbsp;of&nbsp;the&nbsp;file.</div>
</div>
</td>
</tr>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">self.type</td>
<td style="width: 387px; height: 18px;">
<div>
<div>'file' for files and 'dir' for directories.</div>
</div>
</td>
</tr>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">self.content&nbsp;&nbsp;(only for files)</td>
<td style="width: 387px; height: 18px;">
<div>
<div>If self.type=='file': content is files.read(self.path)</div>
</div>
</td>
</tr>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">self.files&nbsp; &nbsp; &nbsp; &nbsp;(only for dirs)</td>
<td style="width: 387px; height: 18px;">
<div>
<div>A list that contains only Files in Self (NOT subdirs)</div>
</div>
</td>
</tr>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">self.file_list&nbsp; (only for dirs)</td>
<td style="width: 387px; height: 18px;">
<div>
<div>List of all files and dirs of self (seprated pro)</div>
</div>
</td>
</tr>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">self.all_files&nbsp;(only for dirs)</td>
<td style="width: 387px; height: 18px;">
<div>
<div>List of all files of self (their path depends on self.path)</div>
</div>
</td>
</tr>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">self.all_files_sep (only for dirs)</td>
<td style="width: 387px; height: 18px;">
<div>
<div>self.all_files but seprated by directories.</div>
</div>
</td>
</tr>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">self.delete()</td>
<td style="width: 387px; height: 18px;">
<div>
<div>Use&nbsp;this&nbsp;to&nbsp;delete file or folder.</div>
</div>
</td>
</tr>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">self.rename(new_name)</td>
<td style="width: 387px; height: 18px;">
<div>
<div>Rename&nbsp;file with&nbsp;this&nbsp;method.</div>
</div>
</td>
</tr>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">self.move(dst)</td>
<td style="width: 387px; height: 18px;">Move file from path to dst. (Read Doc String of copy func)</td>
</tr>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">self.copy(dst)</td>
<td style="width: 387px; height: 18px;">Copy file from self.path to dst. (Also you can use it as rename)</td>
</tr>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">self.hide(path)</td>
<td style="width: 387px; height: 18px;">Hide given path. (It can be file or directory.)</td>
</tr>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">self.read_only(mode=True)</td>
<td style="width: 387px; height: 18px;">Make file or folder read-only. (Read Doc String)</td>
</tr>
</tbody>
</table>
<h3>Class files: (Static<strong>&nbsp;methods)&nbsp;</strong><em>Actions and information about files.</em></h3>
<table style="height: 100px; width: 574px; margin-left: 40px;" cellpadding="5px">
<tbody>
<tr>
<td style="width: 173px;">size(path)</td>
<td style="width: 387px;">
<div>
<div>Return&nbsp;size&nbsp;of&nbsp;the&nbsp;file&nbsp;in&nbsp;byte(s).&nbsp;Also&nbsp;work&nbsp;on&nbsp;directories.</div>
</div>
</td>
</tr>
<tr>
<td style="width: 173px;">delete(path)</td>
<td style="width: 387px;">
<div>
<div>Use&nbsp;this&nbsp;to&nbsp;delete&nbsp;a&nbsp;file&nbsp;(Not&nbsp;folder).</div>
</div>
</td>
</tr>
<tr>
<td style="width: 173px;">rename(path)</td>
<td style="width: 387px;">
<div>
<div>Rename&nbsp;files&nbsp;with&nbsp;this&nbsp;function.</div>
</div>
</td>
</tr>
<tr>
<td style="width: 173px;">abspath(path)</td>
<td style="width: 387px;">
<div>
<div>Return&nbsp;absolute&nbsp;path&nbsp;of&nbsp;given&nbsp;path.</div>
</div>
</td>
</tr>
<tr>
<td style="width: 173px;">exists(path)</td>
<td style="width: 387px;">Return Boolean. If exists True, else: False</td>
</tr>
<tr>
<td style="width: 173px;">mdftime(path)</td>
<td style="width: 387px;">
<div>
<div>Get&nbsp;last&nbsp;modify&nbsp;time&nbsp;of&nbsp;the&nbsp;file.</div>
</div>
</td>
</tr>
<tr>
<td style="width: 173px;">acstime(path)</td>
<td style="width: 387px;">
<div>
<div>Get&nbsp;last&nbsp;access&nbsp;time&nbsp;of&nbsp;the&nbsp;file.</div>
</div>
</td>
</tr>
<tr>
<td style="width: 173px;">move(src,dst)</td>
<td style="width: 387px;">Move file from src to dst. (Read Doc String of copy func)</td>
</tr>
<tr>
<td style="width: 173px;">copy(src,dst)</td>
<td style="width: 387px;">Copy file from src to dst. (Also work on folders)</td>
</tr>
<tr>
<td style="width: 173px;">hide(path)</td>
<td style="width: 387px;">Hide given path. (It can be file or directory.)</td>
</tr>
<tr>
<td style="width: 173px;">read_only(path,mode=True)</td>
<td style="width: 387px;">Make file or folder read-only. (Read Doc String)</td>
</tr>
<tr>
<td style="width: 173px;">read(path)</td>
<td style="width: 387px;">Return content of the path</td>
</tr>
<tr>
<td style="width: 173px;">write(path,text='',...)</td>
<td style="width: 387px;">Same as write function.</td>
</tr>
<tr>
<td style="width: 173px;">isdir(path)</td>
<td style="width: 387px;">Return True for directory and False for others.</td>
</tr>
<tr>
<td style="width: 173px;">isfile(path)</td>
<td style="width: 387px;">Return True for file and False for others.</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h3>&nbsp;Class style:&nbsp; &nbsp; <em>Changing text Color,BG &amp; Style. (Read Doc String)</em></h3>
<table style="height: 100px; width: 574px; margin-left: 40px;" cellpadding="5px">
<tbody>
<tr style="height: 15.0625px;">
<td style="width: 173px; height: 15.0625px;">
<p>print(txt,clr,BG,style,end)<br />(from v1.5.0)</p>
</td>
<td style="width: 387px; height: 15.0625px;">Print txt with selected color,BG,style.(Read Doc String)</td>
</tr>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">switch(color,BG,style)</td>
<td style="width: 387px; height: 18px;">Change Terminal Attributes Until another Call.</td>
</tr>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">
<div>
<div>switch_default()</div>
</div>
</td>
<td style="width: 387px; height: 18px;">Restore Terminal Attributes.</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h3>&nbsp;Class record:&nbsp; &nbsp;<em>Record time of a certain actions. (Read Doc String)</em></h3>
<table style="height: 100px; width: 574px; margin-left: 40px;" cellpadding="5px">
<tbody>
<tr style="height: 18px;">
<td style="width: 173px; height: 18px;">__init__()</td>
<td style="width: 387px; height: 18px;">Set Start Time.</td>
</tr>
<tr style="height: 30px;">
<td style="width: 173px; height: 30px;">self.stop()</td>
<td style="width: 387px; height: 30px;">Stops Recording (You can not lap anymore)</td>
</tr>
<tr style="height: 23.8125px;">
<td style="width: 173px; height: 23.8125px;">self.lap()</td>
<td style="width: 387px; height: 23.8125px;">Rreturn time between start time and self.lap()Also add that time to self.laps</td>
</tr>
<tr style="height: 23.8125px;">
<td style="width: 173px; height: 23.8125px;">self.laps</td>
<td style="width: 387px; height: 23.8125px;">A list that contains all laps you have done</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h2>Recommended to:</h2>
<p><span style="text-decoration: underline; color: #000080;"><strong>&nbsp; - Using an IDE that shows Function and Class Help is highly recommended.</strong></span>&nbsp;<strong>(<span style="color: #ff6600;"><a style="color: #0066b8;" title="Microsoft Visual Studio Code" href="https://code.visualstudio.com/" target="_blank" rel="noopener">VS Code</a></span>)</strong></p>
<h4>&nbsp;- Using "from rx7 import ."</h4>
<h4>&nbsp;- Using "import rx7 as rx"</h4>
<p>&nbsp;</p>
<h2>&nbsp;Upgrade:</h2>
<table style="margin-left: 40px; height: 62px;" border="3" width="269">
<tbody>
<tr>
<td style="width: 237px;">
<h3>pip install --upgrade&nbsp;rx7</h3>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h2>Versions Information:</h2>
<p>&nbsp; &nbsp; &nbsp; &nbsp; Releases are like this:&nbsp; &nbsp; &nbsp; &nbsp; 1.0.0</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 1.1.1</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;⋮</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 1.2.0</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; <span style="background-color: #ffffff; color: #000000;">First number is very important bacause it's for Realy Big new features and changes.</span></p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; Second number is important but not like first number because it contains some changes and new features. (RECOMMENDED for upgrading package)</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; But 3rd number is not important because it's for changing packege codes order and you won't lose anything if you&nbsp; &nbsp; &nbsp; &nbsp; don't install it.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; <em>Numbers are not always in order like: 1,2,3,4,...&nbsp; , Some times they are different like: 1.2.4.8,...</em></p>
<p>&nbsp;</p>
<h2>Releases:</h2>
<h4>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;(+ for new features, * for changes)</h4>
<table style="height: 10px; margin-left: 40px; width: 519px;" cellpadding="5">
<tbody>
<tr style="height: 42px;">
<td style="width: 119px; height: 42px; text-align: center;"><strong>Version</strong></td>
<td style="width: 153px; height: 42px; text-align: center;"><strong>Release Date</strong></td>
<td style="width: 513px; height: 42px; text-align: center;"><strong>New Features &amp; Changes</strong></td>
</tr>
<tr style="height: 25px;">
<td style="width: 119px; height: 25px; text-align-last: center;">1.9.0</td>
<td style="width: 153px; height: 25px; text-align: center;">09/06/20</td>
<td style="width: 513px; height: 25px; text-align: center;">
<p>* re() --&gt; repeat()</p>
<p>+ New Methods of System Class:&nbsp; ip_global(),&nbsp;ip_local(),&nbsp;ram_free(), ram_percent(),&nbsp;ram_total(),&nbsp;ram_used(), boot_time()</p>
<p>+ convert_bytes()</p>
</td>
</tr>
<tr style="height: 25px;">
<td style="width: 119px; height: 25px; text-align-last: center;">1.8.0</td>
<td style="width: 153px; height: 25px; text-align: center;">05/24/2020</td>
<td style="width: 513px; height: 25px; text-align: center;">
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
<tr style="height: 25px;">
<td style="width: 119px; height: 25px; text-align-last: center;">1.7.0</td>
<td style="width: 153px; height: 25px; text-align: center;">&nbsp; 05/08/2020</td>
<td style="width: 513px; height: 25px; text-align: center;">
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
<tr style="height: 25px;">
<td style="width: 119px; height: 25px; text-align-last: center;">1.5.0</td>
<td style="width: 153px; height: 25px; text-align: center;">04/21/2020</td>
<td style="width: 513px; height: 25px; text-align: center;">
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
<td style="width: 119px; height: 25px; text-align-last: center;">1.3.0</td>
<td style="width: 153px; height: 25px; text-align: center;">&nbsp;04/08/2020</td>
<td style="width: 513px; height: 25px; text-align: center;">
<div>+ __init__ &amp; read &amp; write &amp; content&nbsp; func&nbsp;of&nbsp;file&nbsp;class</div>
<div>* Prgoressbar&nbsp;default&nbsp;args</div>
</td>
</tr>
<tr style="height: 25px;">
<td style="width: 119px; height: 25px; text-align-last: center;">
<p>1.0.0</p>
</td>
<td style="width: 153px; height: 25px;">
<p style="text-align: center;">03/18/2020</p>
</td>
<td style="width: 513px; height: 25px; text-align: center;">####</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<a href="#FeaturesPreview">## Features Preview</a>
[![Tuple](https://media.giphy.com/media/fUpibnvWjv2WsZ1NYW/giphy.gif "Tuple")](http://https://media.giphy.com/media/fUpibnvWjv2WsZ1NYW/giphy.gif "Tuple")
