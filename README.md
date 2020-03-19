<p style="font-size: 27px; font-family: Impact, Charcoal, sans-serif;">rx7 Module&nbsp; -&nbsp; Written By&nbsp; <em><span style="background-color: #ffffff;"><a style="background-color: #ffffff;" title="RX7" href="http://rx7.ir/" target="_blank" rel="noopener">Ramin RX7</a></span></em></p>
<h3>rx7 Module is here to help you make your code shorter!</h3>
<h3>(Most) Usefull function and methods are collected.</h3>
<p>&nbsp;</p>
<h2>List of Functions:</h2>
<table style="height: 471px; width: 567px; margin-left: 20px;">
<tbody>
<tr>
<td style="width: 150px;">p()</td>
<td style="width: 401px;">print() function. (Read Doc String)</td>
</tr>
<tr>
<td style="width: 150px;">re(F_Name,n)</td>
<td style="width: 401px;">Repeat F_Name function for n times.</td>
</tr>
<tr>
<td style="width: 150px;">rev(v)</td>
<td style="width: 401px;">Reverse v and returns it. (Everything like str,list,int)</td>
</tr>
<tr>
<td style="width: 150px;">read(file)</td>
<td style="width: 401px;">Return content of the file.</td>
</tr>
<tr>
<td style="width: 150px;">write(file,mode,text)</td>
<td style="width: 401px;">Write things you want in file content.&nbsp;(Read Doc String)</td>
</tr>
<tr>
<td style="width: 150px;">wait(n)</td>
<td style="width: 401px;">Stop code executing for n seconds</td>
</tr>
<tr>
<td style="width: 150px;">cls()</td>
<td style="width: 401px;">It Clears the Terminal</td>
</tr>
<tr>
<td style="width: 150px;">progressbar()</td>
<td style="width: 401px;">In-App Progressbar. (Read Doc String)</td>
</tr>
<tr>
<td style="width: 150px;">string(Frst_L,Lst_L)</td>
<td style="width: 401px;">Return string from Frst_L to Lst_L (Read Doc String)</td>
</tr>
<tr>
<td style="width: 150px;">force(tpl,*var)</td>
<td style="width: 401px;">Return tpl with adding var(s) to it.</td>
</tr>
<tr>
<td style="width: 150px;">erase(tpl,*var)</td>
<td style="width: 401px;">Return tpl with removing var(s) from it.</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h2>List of Classes:</h2>
<h3>&nbsp; &nbsp; Class rand:&nbsp; &nbsp;<em>Random&nbsp;Variable&nbsp;Generator&nbsp;Class.</em></h3>
<table style="height: 100px; width: 574px; margin-left: 40px;" cellpadding="5px">
<tbody>
<tr>
<td style="width: 173px;">choice(iter)</td>
<td style="width: 387px;">Choose random item from iterable or string.</td>
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
<h3>&nbsp; &nbsp; Class system:&nbsp; &nbsp;Some system actions.</h3>
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
</tbody>
</table>
<p>&nbsp;</p>
<h3>&nbsp; &nbsp; Class file:&nbsp; &nbsp;Actions and information about files.</h3>
<table style="height: 100px; width: 574px; margin-left: 40px;" cellpadding="5px">
<tbody>
<tr>
<td style="width: 173px;">size(path)</td>
<td style="width: 387px;">
<div>
<div>&nbsp;Return&nbsp;size&nbsp;of&nbsp;the&nbsp;file&nbsp;in&nbsp;byte(s).&nbsp;Also&nbsp;work&nbsp;on&nbsp;directories.</div>
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
<td style="width: 173px;">delete_dir(path)</td>
<td style="width: 387px;">
<div>
<div>Use&nbsp;this&nbsp;to&nbsp;delete&nbsp;folders.</div>
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
<td style="width: 387px;">Copy file from src to dst. (Also you can use it as rename)</td>
</tr>
<tr>
<td style="width: 173px;">copydir(src,dst)</td>
<td style="width: 387px;">
<div>
<div>Same&nbsp;as&nbsp;copy&nbsp;function&nbsp;except&nbsp;that&nbsp;it\'s&nbsp;for&nbsp;folders.</div>
</div>
</td>
</tr>
<tr>
<td style="width: 173px;">hide(path)</td>
<td style="width: 387px;">Hide given path. (It can be file or directory.)</td>
</tr>
<tr>
<td style="width: 173px; font-size: 12px;">read_only(path,mode=True)</td>
<td style="width: 387px;">Make file or folder read-only. (Read Doc String)</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h3>&nbsp; &nbsp; Class style:&nbsp; &nbsp; Changing text Color,BG &amp; Style. (Read Doc String)</h3>
<table style="height: 100px; width: 574px; margin-left: 40px;" cellpadding="5px">
<tbody>
<tr>
<td style="width: 173px;">text(txt,clr,BG,style)</td>
<td style="width: 387px;">Print txt with selected color,BG,style.(Read Doc String)</td>
</tr>
<tr>
<td style="width: 173px;">integer(Frst,Lst)</td>
<td style="width: 387px;">Choose integer in range [Frst,Lst]</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h3>&nbsp; &nbsp; Class record:&nbsp; &nbsp;Record time of a certain actions. (Read Doc String)</h3>
<table style="height: 100px; width: 574px; margin-left: 40px;" cellpadding="5px">
<tbody>
<tr>
<td style="width: 173px;">__init__()</td>
<td style="width: 387px;">Set Start Time.</td>
</tr>
<tr>
<td style="width: 173px;">self.Stop()</td>
<td style="width: 387px;">Return Time between creation and Stop</td>
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
<tr style="height: 44.8125px;">
<td style="height: 44.8125px; width: 259px;">
<h3><span class="n">pip</span> <span class="n">install</span> <span class="o">--</span><span class="n">upgrade</span>&nbsp;rx7</h3>
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
<p>&nbsp; &nbsp; &nbsp; &nbsp; <span style="background-color: #ffffff; color: #000000;">First number is very important bacause it's for Big new features and changes.</span></p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; Second number is not important as first but it contains small changes.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; But 3rd number is not important because it's for changing packege codes order and you won't lose anything if you don't install it.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; <em>Numbers are not always in order like: 1,2,3,4,...&nbsp; , Some times they are different like: 1.2.4.8,...</em></p>
<p>&nbsp;</p>
<h2>Releases:</h2>
<table style="height: 10px; margin-left: 40px; width: 501px;" cellpadding="5">
<tbody>
<tr style="height: 42.0156px;">
<td style="width: 119px; height: 42.0156px; text-align: center;"><strong>Version</strong></td>
<td style="width: 153px; height: 42.0156px; text-align: center;"><strong>Release Date</strong></td>
<td style="width: 489px; height: 42.0156px; text-align: center;"><strong>New Features &amp; Changes</strong></td>
</tr>
<tr style="height: 25px;">
<td style="width: 119px; height: 25px;">&nbsp; &nbsp; 1.0.0</td>
<td style="width: 153px; height: 25px;">&nbsp; &nbsp;03/18/2020</td>
<td style="width: 489px; height: 25px; text-align: center;">####</td>
</tr>
<tr style="height: 25px;">
<td style="width: 119px; height: 25px;">&nbsp; &nbsp; 1.0.1</td>
<td style="width: 153px; height: 25px;">&nbsp; &nbsp;03/19/2020</td>
<td style="width: 489px; height: 25px; text-align: center;">Change PyPi Module Page</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>