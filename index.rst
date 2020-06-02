
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="None">
        
        
        <link rel="shortcut icon" href="./img/favicon.ico">
        <title>PySimpleGUI</title>
        <link href="./css/bootstrap-custom.min.css" rel="stylesheet">
        <link href="./css/font-awesome-4.5.0.css" rel="stylesheet">
        <link href="./css/base.css" rel="stylesheet">
        <link rel="stylesheet" href="./css/highlight.css">
        <link href="https://assets.readthedocs.org/static/css/badge_only.css" rel="stylesheet">
        <link href="https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css" rel="stylesheet">
        <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
            <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
        <![endif]-->

        <script src="./js/jquery-1.10.2.min.js"></script>
        <script src="./js/bootstrap-3.0.3.min.js"></script>
        <script src="./js/highlight.pack.js"></script> 
    </head>

    <body class="homepage">

        <div class="navbar navbar-default navbar-fixed-top" role="navigation">
    <div class="container">

        <!-- Collapsed navigation -->
        <div class="navbar-header">
            <!-- Expander button -->
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href=".">PySimpleGUI</a>
        </div>

        <!-- Expanded navigation -->
        <div class="navbar-collapse collapse">
                <!-- Main navigation -->
                <ul class="nav navbar-nav">
                    <li class="active">
                        <a href=".">Home</a>
                    </li>
                    <li >
                        <a href="call reference/">Call reference</a>
                    </li>
                    <li >
                        <a href="cookbook/">Cookbook</a>
                    </li>
                </ul>

            <ul class="nav navbar-nav navbar-right">
                <li>
                    <a href="#" data-toggle="modal" data-target="#mkdocs_search_modal">
                        <i class="fa fa-search"></i> Search
                    </a>
                </li>
                    <li class="disabled">
                        <a rel="next" >
                            <i class="fa fa-arrow-left"></i> Previous
                        </a>
                    </li>
                    <li >
                        <a rel="prev" href="call reference/">
                            Next <i class="fa fa-arrow-right"></i>
                        </a>
                    </li>
            </ul>
        </div>
    </div>
</div>

        <div class="container">
                <div class="col-md-3"><div class="bs-sidebar hidden-print affix well" role="complementary">
    <ul class="nav bs-sidenav">
        <li class="main active"><a href="#pysimplegui-users-manual">PySimpleGUI User's Manual</a></li>
            <li><a href="#python-gui-for-humans-transforms-tkinter-qt-remi-wxpython-into-portable-people-friendly-pythonic-interfaces">Python GUI For Humans - Transforms tkinter, Qt, Remi, WxPython into portable people-friendly Pythonic interfaces</a></li>
            <li><a href="#the-call-reference-section-moved-to-here">The Call Reference Section Moved to here</a></li>
        <li class="main "><a href="#jump-start">Jump-Start</a></li>
            <li><a href="#install">Install</a></li>
            <li><a href="#gui-development-does-not-have-to-be-difficult-nor-painful-it-can-be-and-is-fun">GUI Development does not have to be difficult nor painful.  It can be (and is) FUN</a></li>
        <li class="main "><a href="#about-the-pysimplegui-documentation-system">About The PySimpleGUI Documentation System</a></li>
            <li><a href="#documentation-and-demos-get-out-of-date">Documentation and Demos Get Out of Date</a></li>
        <li class="main "><a href="#platforms">Platforms</a></li>
            <li><a href="#hardware-and-os-support">Hardware and OS Support</a></li>
            <li><a href="#output-devices">Output Devices</a></li>
            <li><a href="#a-complete-pysimplegui-program-getting-the-gist">A Complete PySimpleGUI Program (Getting The Gist)</a></li>
            <li><a href="#the-underlying-gui-frameworks-status-of-each">The Underlying GUI Frameworks &amp; Status of Each</a></li>
        <li class="main "><a href="#the-pysimplegui-family">The PySimpleGUI "Family"</a></li>
            <li><a href="#whats-the-big-deal-what-is-it">What's The Big Deal? What is it?</a></li>
            <li><a href="#the-ports">The "Ports"</a></li>
            <li><a href="#qt-version">Qt Version</a></li>
            <li><a href="#wxpython-version">WxPython Version</a></li>
            <li><a href="#web-version-remi">Web Version (Remi)</a></li>
            <li><a href="#android-version">Android Version</a></li>
            <li><a href="#source-code-compatibility">Source code compatibility</a></li>
            <li><a href="#replit-version">repl.it Version</a></li>
            <li><a href="#macs">Macs</a></li>
        <li class="main "><a href="#support">Support</a></li>
            <li><a href="#dont-suffer-silently">Don't Suffer Silently</a></li>
        <li class="main "><a href="#learning-resources">Learning Resources</a></li>
            <li><a href="#the-pysimplegui-developer-centric-model">The PySimpleGUI, Developer-Centric Model</a></li>
            <li><a href="#this-readme-and-cookbook">This Readme and Cookbook</a></li>
            <li><a href="#demo-programs">Demo Programs</a></li>
        <li class="main "><a href="#the-quick-tour">The Quick Tour</a></li>
            <li><a href="#the-beauty-of-simplicity">The Beauty of Simplicity</a></li>
        <li class="main "><a href="#some-examples">Some Examples</a></li>
            <li><a href="#polishing-your-windows-building-beautiful-windows">Polishing Your Windows = Building "Beautiful Windows"</a></li>
        <li class="main "><a href="#pi-windows">Pi Windows</a></li>
        <li class="main "><a href="#games">Games</a></li>
        <li class="main "><a href="#windows-programs-that-look-like-windows-programs">Windows Programs That Look Like Windows Programs</a></li>
        <li class="main "><a href="#background-why-pysimplegui-came-to-be">Background - Why PySimpleGUI Came to Be</a></li>
            <li><a href="#the-non-oo-and-non-event-driven-model">The Non-OO and Non-Event-Driven Model</a></li>
        <li class="main "><a href="#features">Features</a></li>
            <li><a href="#design-goals">Design Goals</a></li>
        <li class="main "><a href="#getting-started-with-pysimplegui">Getting Started with PySimpleGUI</a></li>
            <li><a href="#installing-pysimplegui">Installing PySimpleGUI</a></li>
            <li><a href="#ides">IDEs</a></li>
            <li><a href="#using-python-3">Using  - Python 3</a></li>
            <li><a href="#python-27">Python 2.7</a></li>
        <li class="main "><a href="#pep8-bindings-for-methods-and-functions">PEP8 Bindings For Methods and Functions</a></li>
            <li><a href="#the-non-pep8-methods-and-functions">The Non-PEP8 Methods and Functions</a></li>
            <li><a href="#the-renaming-convention">The Renaming Convention</a></li>
            <li><a href="#class-variables">Class Variables</a></li>
        <li class="main "><a href="#high-level-api-calls-popups">High Level API Calls  - Popup's</a></li>
            <li><a href="#popup-output">Popup Output</a></li>
            <li><a href="#popup-input">Popup Input</a></li>
        <li class="main "><a href="#progress-meters">Progress Meters!</a></li>
        <li class="main "><a href="#debug-output-easy_print-print-eprint">Debug Output (easy_print = Print = eprint)</a></li>
            <li><a href="#printing-to-multiline-elements">Printing To Multiline Elements</a></li>
        <li class="main "><a href="#custom-window-api-calls-your-first-window">Custom window API Calls  (Your First window)</a></li>
            <li><a href="#the-window-designer">The window Designer</a></li>
        <li class="main "><a href="#copy-these-design-patterns">Copy these design patterns!</a></li>
            <li><a href="#pattern-1-a-one-shot-window-read-a-window-one-time-then-close-it">Pattern 1 A - "One-shot Window" - Read a window one time then close it</a></li>
            <li><a href="#pattern-1-b-one-shot-window-read-a-window-one-time-then-close-it-compact-format">Pattern 1 B - "One-shot Window" - Read a window one time then close it (compact format)</a></li>
            <li><a href="#pattern-2-a-persistent-window-multiple-reads-using-an-event-loop">Pattern 2 A - Persistent window (multiple reads using an event loop)</a></li>
            <li><a href="#pattern-2-b-persistent-window-multiple-reads-using-an-event-loop-updates-data-in-window">Pattern 2 B - Persistent window (multiple reads using an event loop + updates data in window)</a></li>
            <li><a href="#how-gui-programming-in-python-should-look-at-least-for-beginners">How GUI Programming in Python Should Look?  At least for beginners ?</a></li>
            <li><a href="#return-values">Return values</a></li>
            <li><a href="#events">Events</a></li>
            <li><a href="#the-event-loop-callback-functions">The Event Loop / Callback Functions</a></li>
        <li class="main "><a href="#building-custom-windows">Building Custom Windows</a></li>
            <li><a href="#synchronous-asynchronous-windows">Synchronous / Asynchronous Windows</a></li>
        <li class="main "><a href="#themes-automatic-coloring-of-your-windows">Themes - Automatic Coloring of Your Windows</a></li>
            <li><a href="#default-is-dark-blue-3">Default is Dark Blue 3</a></li>
            <li><a href="#theme-name-formula">Theme Name Formula</a></li>
            <li><a href="#theme-functions">Theme Functions</a></li>
        <li class="main "><a href="#window-object-beginning-a-window">Window Object - Beginning a window</a></li>
            <li><a href="#window-location">Window Location</a></li>
            <li><a href="#window-size">Window Size</a></li>
            <li><a href="#element-sizes">Element Sizes</a></li>
            <li><a href="#no-titlebar">No Titlebar</a></li>
            <li><a href="#grab-anywhere">Grab Anywhere</a></li>
            <li><a href="#always-on-top">Always on top</a></li>
            <li><a href="#focus">Focus</a></li>
            <li><a href="#ttk-buttons">TTK Buttons</a></li>
            <li><a href="#ttk-themes">TTK Themes</a></li>
            <li><a href="#closing-windows">Closing Windows</a></li>
            <li><a href="#window-methods-that-complete-formation-of-window">Window Methods That Complete Formation of Window</a></li>
        <li class="main "><a href="#layouts">Layouts</a></li>
        <li class="main "><a href="#generated-layouts-for-sure-want-to-read-if-you-have-5-repeating-elementsrows">Generated Layouts (For sure want to read if you have &gt; 5 repeating elements/rows)</a></li>
            <li><a href="#example-list-comprehension-to-concatenate-multiple-rows-to-do-list-example">Example - List Comprehension To Concatenate Multiple Rows - "To Do" List Example</a></li>
            <li><a href="#example-list-comprehension-to-build-rows-table-simulation-grid-of-inputs">Example - List Comprehension to Build Rows - Table Simulation - Grid of Inputs</a></li>
            <li><a href="#user-defined-elements-compound-elements">User Defined Elements / Compound Elements</a></li>
        <li class="main "><a href="#elements">Elements</a></li>
            <li><a href="#keys">Keys</a></li>
            <li><a href="#common-element-parameters">Common Element Parameters</a></li>
            <li><a href="#shortcut-functions-multiple-function-names">Shortcut Functions / Multiple Function Names</a></li>
            <li><a href="#text-element-t-txt-text">Text Element | T == Txt == Text</a></li>
            <li><a href="#windowfindelementkey-shortened-to-windowkey">Window.FindElement(key) shortened to Window[key]</a></li>
            <li><a href="#multiline-element">Multiline Element</a></li>
            <li><a href="#text-input-element-inputtext-input-in">Text Input Element  | InputText == Input == In</a></li>
            <li><a href="#combo-element-combo-inputcombo-dropdown-drop">Combo Element | Combo == InputCombo == DropDown == Drop</a></li>
            <li><a href="#listbox-element">Listbox Element</a></li>
            <li><a href="#slider-element">Slider Element</a></li>
            <li><a href="#radio-button-element">Radio Button Element</a></li>
            <li><a href="#checkbox-element-cbox-cb-check">Checkbox Element | CBox == CB == Check</a></li>
            <li><a href="#spin-element">Spin Element</a></li>
            <li><a href="#image-element">Image Element</a></li>
            <li><a href="#button-element">Button Element</a></li>
            <li><a href="#buttonmenu-element">ButtonMenu Element</a></li>
            <li><a href="#verticalseparator-element">VerticalSeparator Element</a></li>
            <li><a href="#horizontalseparator-element">HorizontalSeparator Element</a></li>
            <li><a href="#progressbar-element">ProgressBar Element</a></li>
            <li><a href="#output-element">Output Element</a></li>
            <li><a href="#column-element-frame-tab-container-elements">Column Element &amp; Frame, Tab "Container" Elements</a></li>
            <li><a href="#sizer-element">Sizer Element</a></li>
            <li><a href="#frame-element-labelled-frames-frames-with-a-title">Frame Element (Labelled Frames, Frames with a title)</a></li>
            <li><a href="#canvas-element">Canvas Element</a></li>
            <li><a href="#graph-element">Graph Element</a></li>
            <li><a href="#table-element">Table Element</a></li>
            <li><a href="#tree-element">Tree Element</a></li>
            <li><a href="#tab-and-tab-group-elements">Tab and Tab Group Elements</a></li>
            <li><a href="#colors_1">Colors</a></li>
        <li class="main "><a href="#systemtray">SystemTray</a></li>
            <li><a href="#tkinter-version">Tkinter version</a></li>
            <li><a href="#systemtray-object">SystemTray Object</a></li>
            <li><a href="#system-tray-design-pattern">System Tray Design Pattern</a></li>
            <li><a href="#menu-definition">Menu Definition</a></li>
            <li><a href="#systemtray-methods">SystemTray Methods</a></li>
        <li class="main "><a href="#global-settings">Global Settings</a></li>
        <li class="main "><a href="#persistent-windows-window-stays-open-after-button-click">Persistent windows (Window stays open after button click)</a></li>
            <li><a href="#input-fields-that-auto-clear">Input Fields that Auto-clear</a></li>
            <li><a href="#basic-persistent-window-design-pattern">Basic Persistent Window Design Pattern</a></li>
            <li><a href="#readtimeout-t-timeout_keytimeout_key-closefalse">Read(timeout = t, timeout_key=TIMEOUT_KEY, close=False)</a></li>
            <li><a href="#sgtimeout_key">sg.TIMEOUT_KEY</a></li>
            <li><a href="#persistent-window-example-running-timer-that-updates">Persistent Window Example - Running timer that updates</a></li>
            <li><a href="#instead-of-a-non-blocking-read-use-enable_events-true-or-return_keyboard_events-true">Instead of a Non-blocking Read --- Use enable_events = True or return_keyboard_events = True</a></li>
        <li class="main "><a href="#updating-elements-changing-elements-values-in-an-active-window">Updating Elements (changing element's values in an active window)</a></li>
            <li><a href="#locating-elements-findelement-element-elem">Locating Elements (FindElement == Element == Elem == [ ])</a></li>
            <li><a href="#progressbar-progress-meters">ProgressBar / Progress Meters</a></li>
        <li class="main "><a href="#keyboard-mouse-capture">Keyboard &amp; Mouse Capture</a></li>
        <li class="main "><a href="#menus">Menus</a></li>
            <li><a href="#menubar">MenuBar</a></li>
            <li><a href="#methods">Methods</a></li>
            <li><a href="#buttonmenus">ButtonMenus</a></li>
            <li><a href="#right-click-menus">Right Click Menus</a></li>
            <li><a href="#menu-shortcut-keys">Menu Shortcut keys</a></li>
            <li><a href="#disabled-menu-entries">Disabled Menu Entries</a></li>
            <li><a href="#keys-for-menus">Keys for Menus</a></li>
            <li><a href="#the-menu-definitions">The Menu Definitions</a></li>
        <li class="main "><a href="#running-multiple-windows">Running Multiple Windows</a></li>
            <li><a href="#the-golden-rule-of-window-layouts">THE GOLDEN RULE OF WINDOW LAYOUTS</a></li>
            <li><a href="#demo-programs-for-multiple-windows">Demo Programs For Multiple Windows</a></li>
            <li><a href="#multi-window-design-pattern-1-both-windows-active">Multi-Window Design Pattern 1 - both windows active</a></li>
            <li><a href="#multi-window-design-pattern-2-only-1-active-window">Multi-Window Design Pattern 2 - only 1 active window</a></li>
        <li class="main "><a href="#the-pysimplegui-debugger">The PySimpleGUI Debugger</a></li>
            <li><a href="#what-is-it-why-use-it-what-the-heck-i-already-have-an-ide">What is it?  Why use it?  What the heck?  I already have an IDE.</a></li>
            <li><a href="#preparing-to-run-the-debugger">Preparing To Run the Debugger</a></li>
            <li><a href="#a-sample-program-for-us-to-use">A Sample Program For Us To Use</a></li>
            <li><a href="#debugger-windows">Debugger Windows</a></li>
            <li><a href="#the-repl-prompt">The REPL Prompt</a></li>
            <li><a href="#how-to-use-the-debugger-to-find-the-version-number-of-a-package">How To Use the Debugger to Find The Version Number of a Package</a></li>
        <li class="main "><a href="#extending-pysimplegui">Extending PySimpleGUI</a></li>
            <li><a href="#widget-access">Widget Access</a></li>
            <li><a href="#window-level-access">Window Level Access</a></li>
            <li><a href="#binding-tkiner-events">Binding tkiner "events"</a></li>
            <li><a href="#there-is-no-way-to-unbind-and-event-at-this-time-sorry-didnt-think-of-it-before-releasing">There is no way to "unbind" and event at this time.  (sorry, didn't think of it before releasing)</a></li>
        <li class="main "><a href="#demo-programs-applications">"Demo Programs" Applications</a></li>
            <li><a href="#packages-used-in-demos">Packages Used In Demos</a></li>
        <li class="main "><a href="#creating-a-windows-exe-file">Creating a Windows .EXE File</a></li>
        <li class="main "><a href="#creating-a-mac-app-file">Creating a Mac App File</a></li>
        <li class="main "><a href="#debug-output">Debug Output</a></li>
        <li class="main "><a href="#look-and-feel">Look and Feel</a></li>
            <li><a href="#changlelookandfeel">ChangleLookAndFeel</a></li>
        <li class="main "><a href="#known-issues">Known Issues</a></li>
            <li><a href="#macs-tkinter">MACS &amp; tkinter</a></li>
            <li><a href="#multiple-threads">Multiple threads</a></li>
        <li class="main "><a href="#contributing-to-pysimplegui">Contributing to PySimpleGUI</a></li>
            <li><a href="#open-source-license-but-private-development">Open Source License, but Private Development</a></li>
            <li><a href="#thank-you">Thank You</a></li>
            <li><a href="#github-repos">GitHub Repos</a></li>
            <li><a href="#versions">Versions</a></li>
            <li><a href="#release-notes">Release Notes</a></li>
            <li><a href="#3180-11-dec-2018">3.18.0  11-Dec-2018</a></li>
            <li><a href="#3192-13-dec-2018">3.19.2  13-Dec-2018</a></li>
            <li><a href="#3200-1200-18-dec-2018">3.20.0 &amp; 1.20.0 18-Dec-2018</a></li>
            <li><a href="#3210-1210-28-dec-2018">3.21.0 &amp; 1.21.0 28-Dec-2018</a></li>
        <li class="main "><a href="#3220-pysimplegui-1220-pysimplegui27">3.22.0 PySimpleGUI / 1.22.0 PySimpleGUI27</a></li>
        <li class="main "><a href="#320-pysimplegui-1230-pysimplegui27-16-jan-2019">3.2.0 PySimpleGUI /  1.23.0 PySimpleGUI27 16-Jan-2019</a></li>
        <li class="main "><a href="#3240-1240-16-jan-2019">3.24.0 1.24.0 16-Jan-2019</a></li>
        <li class="main "><a href="#325-125-20-feb-2019">3.25 &amp; 1.25 20-Feb-2019</a></li>
            <li><a href="#3270-pysimplegui-31-mar-2019">3.27.0 PySimpleGUI  31-Mar-2019</a></li>
            <li><a href="#3280-11-apr-2019-pysimplegui">3.28.0 11-Apr-2019 PySimpleGUI</a></li>
            <li><a href="#329-22-apr-2019">3.29 22-Apr-2019</a></li>
            <li><a href="#3320-pysimplegui-24-may-2019">3.32.0 PySimpleGUI 24-May-2019</a></li>
            <li><a href="#3330-and-133-pysimplegui-25-may-2019">3.33.0 and 1.33 PySimpleGUI 25-May-2019</a></li>
            <li><a href="#3340-pysimplegui-1340-pysimplegui27-25-may-2019">3.34.0 PySimpleGUI &amp; 1.34.0 PySimpleGUI27 25-May-2019</a></li>
            <li><a href="#335-pysimplegui-135-pysimplegui27-27-may-2019">3.35 PySimpleGUI &amp; 1.35 PySimpleGUI27 27-May-2019</a></li>
            <li><a href="#336-pysimplegui-136-pysimplegui27-29-may-2019">3.36 PySimpleGUI &amp; 1.36 PySimpleGUI27 29-May-2019</a></li>
            <li><a href="#337-pysimplegui-137-pysimplegui27-1-june-2019">3.37 PySimpleGUI &amp; 1.37 PySimpleGUI27 1-June-2019</a></li>
            <li><a href="#338-pysimplegui-138-pysimplegui27">3.38 PySimpleGUI, 1.38 PySimpleGUI27</a></li>
            <li><a href="#339-pysimplegui-139-pysimplegui27-13-june-2019">3.39 PySimpleGUI &amp; 1.39 PySimpleGUI27 13-June-2019</a></li>
        <li class="main "><a href="#400-pysimplegui-200-pysimplegui27-19-june-2019">4.0.0 PySimpleGUI &amp; 2.0.0 PySimpleGUI27   19-June-2019</a></li>
            <li><a href="#pysimplegui-41-anniversary-release-4-aug-2019">PySimpleGUI 4.1 Anniversary Release!  4-Aug-2019</a></li>
            <li><a href="#43-pysimplegui-release-22-aug-2019">4.3 PySimpleGUI Release 22-Aug-2019</a></li>
            <li><a href="#44-pysimplegui-release-5-sep-2019">4.4 PySimpleGUI Release 5-Sep-2019</a></li>
            <li><a href="#45-pysimplegui-release-04-nov-2019">4.5 PySimpleGUI Release 04-Nov-2019</a></li>
            <li><a href="#46-pysimplegui-16-nov-2019">4.6 PySimpleGUI 16-Nov-2019</a></li>
            <li><a href="#470-pysimplegui-26-nov-2019">4.7.0 PySimpleGUI 26-Nov-2019</a></li>
            <li><a href="#480-pysimplegui-4-dec-2019">4.8.0 PySimpleGUI 4-Dec-2019</a></li>
            <li><a href="#490-pysimplegui-7-dec-2019">4.9.0 PySimpleGUI 7-Dec-2019</a></li>
            <li><a href="#4100-pysimplegui-9-dec-2019">4.10.0 PySimpleGUI 9-Dec-2019</a></li>
            <li><a href="#4110-pysimplegui-10-dec-2019">4.11.0 PySimpleGUI 10-Dec-2019</a></li>
            <li><a href="#4120-pysimplegui-14-dec-2019">4.12.0 PySimpleGUI 14-Dec-2019</a></li>
            <li><a href="#4130-pysimplegui-18-dec-2019">4.13.0 PySimpleGUI 18-Dec-2019</a></li>
            <li><a href="#4140-pysimplegui-23-dec-2019">4.14.0 PySimpleGUI 23-Dec-2019</a></li>
            <li><a href="#4150-pysimplegui-08-jan-2020">4.15.0 PySimpleGUI 08-Jan-2020</a></li>
            <li><a href="#4151-pysimplegui-09-jan-2020">4.15.1 PySimpleGUI 09-Jan-2020</a></li>
            <li><a href="#4152-pysimplegui-15-jan-2020">4.15.2 PySimpleGUI 15-Jan-2020</a></li>
            <li><a href="#4160-pysimplegui-20-feb-2020">4.16.0 PySimpleGUI 20-Feb-2020</a></li>
            <li><a href="#4170-pysimplegui-24-mar-2020">4.17.0 PySimpleGUI 24-Mar-2020</a></li>
            <li><a href="#4180-pysimplegui-26-mar-2020">4.18.0 PySimpleGUI 26-Mar-2020</a></li>
            <li><a href="#4181-pysimplegui-12-apr-2020">4.18.1 PySimpleGUI 12-Apr-2020</a></li>
            <li><a href="#4182-pysimplegui-12-apr-2020">4.18.2 PySimpleGUI 12-Apr-2020</a></li>
            <li><a href="#4190-pysimplegui-5-may-2020">4.19.0 PySimpleGUI 5-May-2020</a></li>
            <li><a href="#code-condition">Code Condition</a></li>
            <li><a href="#design">Design</a></li>
            <li><a href="#author-owner">Author &amp; Owner</a></li>
            <li><a href="#license">License</a></li>
            <li><a href="#acknowledgments">Acknowledgments</a></li>
            <li><a href="#support_1">Support</a></li>
    </ul>
</div></div>
                <div class="col-md-9" role="main">

<p><img alt="pysimplegui_logo" src="https://user-images.githubusercontent.com/13696193/43165867-fe02e3b2-8f62-11e8-9fd0-cc7c86b11772.png" /></p>
<p><a href="http://pepy.tech/project/pysimplegui"><img alt="tkinter" src="http://pepy.tech/badge/pysimplegui" /></a> tkinter
<a href="https://pepy.tech/project/pysimplegui27"><img alt="tkinter27" src="https://pepy.tech/badge/pysimplegui27" /></a> tk 2.7
<a href="https://pepy.tech/project/pysimpleguiqt"><img alt="Downloads" src="https://pepy.tech/badge/pysimpleguiqt" /></a> Qt
<a href="https://pepy.tech/project/pysimpleguiWx"><img alt="Downloads" src="https://pepy.tech/badge/pysimpleguiwx" /></a> WxPython
<a href="https://pepy.tech/project/pysimpleguiWeb"><img alt="Downloads" src="https://pepy.tech/badge/pysimpleguiweb" /></a> Web (Remi)</p>
<p><img alt="Documentation Status" src="https://readthedocs.org/projects/pysimplegui/badge/?version=latest" />
<img alt="Python Version" src="https://img.shields.io/badge/Python-2.7_3.4+-yellow.svg" /></p>
<p><a href="https://pypi.org/project/pysimplegui/"><img alt="PyPI Version" src="https://img.shields.io/pypi/v/pysimplegui.svg?style=for-the-badge" /></a> tkinter
<a href="https://pypi.org/project/pysimpleguiqt/"><img alt="PyPI Version" src="https://img.shields.io/pypi/v/pysimpleguiqt.svg?style=for-the-badge" /></a> Qt
<a href="https://pypi.org/project/pysimpleguiweb/"><img alt="PyPI Version" src="https://img.shields.io/pypi/v/pysimpleguiweb.svg?style=for-the-badge" /></a> Web
<a href="https://pypi.org/project/pysimpleguiwx/"><img alt="PyPI Version" src="https://img.shields.io/pypi/v/pysimpleguiwx.svg?style=for-the-badge" /></a> Wx
<img alt="GitHub issues" src="https://img.shields.io/github/issues-raw/PySimpleGUI/PySimpleGUI?color=blue" />  <img alt="GitHub closed issues" src="https://img.shields.io/github/issues-closed-raw/PySimpleGUI/PySimpleGUI?color=blue" />
<a href="./../../commits/master"><img alt="Commit activity" src="https://img.shields.io/github/commit-activity/m/PySimpleGUI/PySimpleGUI.svg?style=for-the-badge" /></a>
<a href="./../../commits/master"><img alt="Last commit" src="https://img.shields.io/github/last-commit/PySimpleGUI/PySimpleGUI.svg?style=for-the-badge" /></a></p>
<h1 id="pysimplegui-users-manual">PySimpleGUI User's Manual</h1>
<h2 id="python-gui-for-humans-transforms-tkinter-qt-remi-wxpython-into-portable-people-friendly-pythonic-interfaces">Python GUI For Humans - Transforms tkinter, Qt, Remi, WxPython into portable people-friendly Pythonic interfaces</h2>
<h2 id="the-call-reference-section-moved-to-here"><span>The Call Reference Section Moved to <a href="https://pysimplegui.readthedocs.io/en/latest/call%20reference/">here</a></span></h2>
<h3 id="this-manual-is-crammed-full-of-answers-so-start-your-search-for-answers-here-readsearch-this-prior-to-opening-an-issue-on-github-press-control-f-and-type">This manual is crammed full of answers so start your search for answers here. Read/Search this prior to opening an Issue on GitHub.  Press Control F and type.</h3>
<hr />
<h1 id="jump-start">Jump-Start</h1>
<h2 id="install">Install</h2>
<pre><code>pip install pysimplegui
or
pip3 install pysimplegui
</code></pre>

<h3 id="this-code">This Code</h3>
<pre><code class="python">import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process &quot;events&quot; and get the &quot;values&quot; of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
</code></pre>

<h3 id="makes-this-window">Makes This Window</h3>
<p>and returns the value input as well as the button clicked.</p>
<p><img alt="image" src="https://user-images.githubusercontent.com/46163555/68713283-7cb38200-056b-11ea-990a-aa1603af5a11.png" /></p>
<h3 id="any-questions-its-that-simple">Any Questions?  It's that simple.</h3>
<hr />
<h4 id="looking-for-a-gui-package-are-you">Looking for a GUI package?     Are you....</h4>
<ul>
<li>looking to take your Python code from the world of command lines and into the convenience of a GUI? </li>
<li>sitting on a Raspberry <strong>Pi</strong> with a touchscreen that's going to waste because you don't have the time to learn a GUI SDK?</li>
<li>into Machine Learning and are sick of the command line?</li>
<li>an IT guy/gal that has written some cool tools but due to corporate policies are unable to share unless an EXE file?</li>
<li>want to share your program with your friends or families (that aren't so freakish that they have Python running)</li>
<li>wanting to run a program in your system tray?</li>
<li>a teacher wanting to teach your students how to program using a GUI?</li>
<li>a student that wants to put a GUI onto your project that will blow away your teacher?</li>
<li>looking for a GUI package that is "supported" and is being constantly developed to improve it?</li>
<li>longing for documentation and scores of examples?</li>
</ul>
<p><strong>Look no further, you've found your GUI package</strong>.</p>
<h4 id="the-basics">The basics</h4>
<ul>
<li>Create windows that look and operate <em>identically</em> to those created directly with tkinter, Qt, WxPython, and Remi.</li>
<li>Requires 1/2 to 1/10th the amount of code as underlying frameworks.</li>
<li>One afternoon is all that is required to learn the PySimpleGUI package <em>and</em> write your first custom GUI.</li>
<li>Students can begin using within their first week of Python education.</li>
<li>No callback functions. You do not need to write the word <code>class</code> <em>anywhere</em> in your code.</li>
<li>Access to nearly every underlying GUI Framework's Widgets.</li>
<li>Supports both Python 2.7 &amp; 3 when using tkinter</li>
<li>Supports both PySide2 and PyQt5 (limited support)</li>
<li>Effortlessly move across tkinter, Qt, WxPython, and the Web (Remi) by changing only the import statement</li>
<li>The <em>only</em> way to write both desktop and web based GUIs at the same time in Python</li>
<li>Developed from nothing as a pure Python implementation with Python friendly interfaces.</li>
<li>Run your program in the System Tray using WxPython. Or, change the import and run it on Qt with no other changes.</li>
<li>Works with Qt Designer</li>
<li>Built in Debugger</li>
<li>Actively maintained and enhanced - 4 ports are underway, all being used by users.</li>
<li>Corporate as well as home users.</li>
<li>Appealing to both newcomers to Python and experienced Pythonistas. </li>
<li>The focus is entirely on the developer (you) and making their life easier, simplified, and in control.</li>
<li>170+ Demo Programs teach you how to integrate with many popular packages like OpenCV, Matplotlib, PyGame, etc. </li>
<li>200 pages of documentation, a Cookbook, built-in help using docstrings, in short it's heavily documented</li>
</ul>
<h4 id="july-2019-note-this-readme-is-being-generated-from-the-pysimpleguipy-file-located-on-github-as-a-result-some-of-the-calls-or-parameters-may-not-match-the-pysimplegui-that-you-pip-installed">July-2019 Note - This readme is being generated from the PySimpleGUI.py file located on GitHub.  As a result, some of the calls or parameters may not match the PySimpleGUI that you pip installed.</h4>
<h2 id="gui-development-does-not-have-to-be-difficult-nor-painful-it-can-be-and-is-fun">GUI Development does not have to be difficult nor painful.  It can be (and is) FUN</h2>
<h4 id="what-users-are-saying-about-pysimplegui">What users are saying about PySimpleGUI</h4>
<p><strong><em>(None of these comments were solicited &amp; are not paid endorsements - other than a huge thank you they received!)</em></strong></p>
<p>"I've been working to learn PyQT for the past week in my off time as an intro to GUI design and how to apply it to my existing scripts... Took me ~30 minutes to figure out PySimpleGUI and get my scripts working with a GUI."</p>
<p>"Python has been an absolute nightmare for me and I've avoided it like the plague.  Until I saw PySimpleGUI."</p>
<p>"I've been pretty amazed at how much more intuitive it is than raw tk/qt. The dude developing it is super active on the project too so if you come across situations that you just can't get the code to do what you want you can make bug/enhancement issues that are almost assured to get a meaningful response."</p>
<p>"This library is the easiest way of GUI programming in python! I'm totally in love with it"</p>
<p>"Wow that readme is extensive and great." (hear the love for docs often)</p>
<p>"Coming from R, Python is absolutely slick for GUIs. PySimpleGUI is a dream."</p>
<p>"I have been writing Python programs for about 4 or 5 months now. Up until this week I never had luck with any UI libraries like Tkinter, Qt, Kivy.  I went from not even being able to load a window in Tkinter reliably to making a loading screen, and full program in one night with PySimpleGUI."</p>
<p>"I love PySimpleGUI! I've been teaching it in my Python classes instead of Tkinter."</p>
<p>"I wish PySimpleGUI was available for every friggin programming language"</p>
<h3 id="start-here-user-manual-with-table-of-contents">START HERE - User Manual with Table of Contents</h3>
<p><a href="http://www.PySimpleGUI.org">ReadTheDocs</a>  &lt;------ THE best place to read the docs due to TOC, all docs in 1 place, and better formatting. START here in your education.  Easy to remember PySimpleGUI.org.</p>
<p><a href="http://calls.PySimpleGUI.org">The Call Reference</a> documentation is located on the same ReadTheDocs page as the main documentation, but it's on another tab that you'll find across the top of the page.</p>
<p>The quick way to remember the documentation addresses is to use these addresses:</p>
<p>http://docs.PySimpleGUI.org
http://calls.PySimpleGUI.org</p>
<h4 id="quick-links-to-help-and-the-latest-news-and-releases">Quick Links To Help and The Latest News and Releases</h4>
<p><a href="http://www.PySimpleGUI.com">Homepage - Lastest Readme and Code - GitHub</a>  Easy to remember: PySimpleGUI.com</p>
<p><a href="https://github.com/PySimpleGUI/PySimpleGUI/issues/142">Announcements of Latest Developments, Release news, Misc</a></p>
<p><a href="http://Cookbook.PySimpleGUI.org">COOKBOOK!</a></p>
<p><a href="http://Trinket.PySimpleGUI.org">Trinket an online Cookbook</a></p>
<p><a href="http://Tutorial.PySimpleGUI.org">Brief Tutorial</a></p>
<p><a href="https://github.com/PySimpleGUI/PySimpleGUI/tree/master/DemoPrograms">Latest Demos and Master Branch on GitHub</a></p>
<p><a href="https://repl.it/@PySimpleGUI">Repl.it Home for PySimpleGUI</a></p>
<p><a href="https://www.bountysource.com/issues/60766522-screen-shots">Lots of screenshots</a></p>
<p><a href="https://github.com/PySimpleGUI/PySimpleGUI/issues/1646">How to submit an Issue</a></p>
<p><a href="http://YouTube.PySimpleGUI.org">The YouTube videos</a> - If you like instructional videos, there are over 15 videos made by PySimpleGUI project over the first 18 months.
In 2020 a new series was begun.  As of May 2020 there are 12 videos completed so far with many more to go....
- <a href="https://www.youtube.com/playlist?list=PLl8dD0doyrvFfzzniWS7FXrZefWWExJ2e">PySimpleGUI 2020 - The most up to date information about PySimpleGUI</a>
- <a href="https://www.youtube.com/playlist?list=PLl8dD0doyrvHMoJGTdMtgLuHymaqJVjzt">5 part series of basics</a>
- <a href="https://www.youtube.com/playlist?list=PLl8dD0doyrvGyXjORNvirTIZxKopJr8s0">10 part series of more detail</a>
- <a href="https://youtu.be/BFTxBmihsUY">The Naked Truth (An update on the technology)</a>
- There are numerous short videos also on that channel that demonstrate PySimpleGUI being used</p>
<p>YouTube Videos made by others.  These have much higher production values than the above videos.</p>
<ul>
<li>A <strong><em>fantastic</em></strong> tutorial <a href="https://youtu.be/cLcfLm_GgiM">PySimpleGUI Concepts - Video 1</a></li>
<li>Build a calculator <a href="https://youtu.be/x5LSTDdffFk">Python Calculator with GUI | PySimpleGUI | Texas Instruments DataMath II</a></li>
<li>Notepad <a href="https://youtu.be/JQY641uynKo">Notepad in Python - PySimpleGUI</a></li>
<li>File Search Engine <a href="https://youtu.be/IWDC9vcBIFQ">File Search Engine | Project for Python Portfolio with GUI | PySimpleGUI</a></li>
</ul>
<h1 id="about-the-pysimplegui-documentation-system">About The PySimpleGUI Documentation System</h1>
<p>This User's Manual (also the project's readme) is one <strong><em>vital</em></strong> part of the PySimpleGUI programming environment.  The best place to read it is at http://www.PySimpleGUI.org</p>
<p>If you are a professional or skilled in how to develop software, then you understand the role of documentation in the world of technology development.  You can skip this bit.... look for the bold "<strong>GO TO HERE</strong>" below.</p>
<p>RTFM is not a new acronym. It stretches back to 1979, the dawn of the computer-era and in particular the microprocessor.  The point is that this is not a new problem.  It's a very old problem.</p>
<p>Bluntness is required here as the subtle approach has not worked in the past:</p>
<p><strong><em>It WILL be required, at times, for you to read or search this document in order to be successful.</em></strong></p>
<p>Re-read that statement.  This <strong>will</strong> be a serious problem for you if you're the type of person that finds it "quicker and easier to post on StackOverflow rather than reading documentation".  </p>
<p>If you have not yet matured to the point you are able to understand this skill or choose to not follow it, then please save <strong><em>everyone</em></strong> the pain of doing <strong>for you</strong> what you, as a developer, software engineer, or wanna be coder, must do on your own.  It's a vital skill for you to learn.  </p>
<p>Want to be a "real engineer"? Then follow "real engineering practices" such as "reading".  You are learning a NEW GUI package.  You've not seen anything like it.  Don't be so arrogant as to believe you will never need to read documentation.</p>
<p>UGH, why does this need to be said?</p>
<p><strong><em>GO TO HERE</em></strong> if instructed above.</p>
<p>I apologize to the other 95% of you that this..... pathetic.... reminder needs to be added, but sadly there's a need for it.</p>
<p>There are 5 resources that work together to provide to you the fastest path to success.  They are:</p>
<ol>
<li>This User's Manual</li>
<li>The Cookbook</li>
<li>The 170+ Demo Programs</li>
<li>Docstrings enable you to access help directly from Python or your IDE</li>
<li>Searching the GitHub Issues as a last resort (search both open and closed issues)</li>
</ol>
<p>Pace yourself.  The initial progress is exciting and FAST PACED.  However, GUIs take time and thought to build.  Take a deep breath and use the provided materials and you'll do fine.  Don't skip the design phase of your GUI after you run some demos and get the hang of things.  If you've tried other GUI frameworks before, successful or not, then you know you're already way ahead of the game using PySimpleGUI versus the underlying GUI frameworks.  It may feel like the 3 days you've been working on your code has been forever, but by comparison of 3 days learning Qt, PySimpleGUI will look trivial to learn.</p>
<p>It is not by accident that this section, about documentation, is at the TOP of this document.</p>
<p>This documentation is not HUGE in length for a package this size. In fact it's still one document and it's the readme for the GitHub.  It's not written in complex English.  It is understandable by complete beginners.  And pressing <code>Control+F</code> is all you need to do to search this document.  USUALLY you'll find less than 6 matches.</p>
<h2 id="documentation-and-demos-get-out-of-date">Documentation and Demos Get Out of Date</h2>
<p>Sometimes the documentation doesn't match exactly the version of the code you're running.  Sometimes demo programs haven't been updated to match a change made to the SDK.  Things don't happen simultaneously generally speaking.  So, it may very well be that you find an error or inconsistency or something no longer works with the latest version of an external library.</p>
<p>If you've found one of these problems, and you've searched to make sure it's not a simple mistake on your part, then by ALL means log an Issue on the GitHub.  Don't be afraid to report problems if you've taken the simple steps of checking out the docs first.</p>
<h1 id="platforms">Platforms</h1>
<h2 id="hardware-and-os-support">Hardware and OS Support</h2>
<p>PySimpleGUI runs on Windows, Linux and Mac, just like tkinter, Qt, WxPython and Remi do.  If you can get the underlying GUI Framework installed / running on your machine then PySimpleGUI will also run there.</p>
<h3 id="hardware">Hardware</h3>
<ul>
<li>PC's, Desktop, Laptops</li>
<li>Macs of all types</li>
<li>Raspberry Pi</li>
<li>Android devices like phones and tablets</li>
<li>Virtual machine online (no hardware) - repl.it</li>
</ul>
<h3 id="os">OS</h3>
<ul>
<li>Windows 7, 8, 10</li>
<li>Linux on PC - Tested on several distributions</li>
<li>Linux on Raspberry Pi</li>
<li>Linux on Android - Can use either Termux or PyDroid3</li>
<li>Mac OS</li>
</ul>
<h4 id="python-versions">Python versions</h4>
<p>As of 9/25/2018 <strong>both Python 3 and Python 2.7 are supported</strong> when using <strong>tkinter version</strong> of PySimpleGUI! The Python 3 version is named <code>PySimpleGUI</code>. The Python 2.7 version is <code>PySimpleGUI27</code>.  They are installed separately and the imports are different. See instructions in Installation section for more info.  <strong>None</strong> of the other ports can use Python 2.</p>
<h6 id="python-27-code-will-be-deleted-from-this-github-on-dec-31-2019">Python 2.7 Code will be deleted from this GitHub on Dec 31, 2019</h6>
<p>Note that the 2.7 port will <em>cease to exist on this GitHub</em> on Jan 1, 2020.  If you would like to know how much time you have to move over to the Python 3 version of PySimpleGUI, then go here: https://pythonclock.org/.  The only thing that will be available is an unsupported PyPI release of PySimpleGUI27.</p>
<p>By "will cease to exist on this GitHub" I mean, it will be deleted entirely.  No source code, no supporting programs.  Nothing.  If you're stuck using 2.7 in December, it would behoove you to fork the 2.7 code on Dec 31, 2019.  Legacy Python doesn't have a permanent home here.  It sounds cruel, but experts in security particularly says 2.7 is a huge risk. Furthering it use only hurts the computing world.</p>
<h4 id="warning-tkinter-python-373-and-later-including-38-has-problems">Warning - tkinter + Python 3.7.3 and later, including 3.8 has problems</h4>
<p>The version of tkinter that is being supplied with the 3.7.3 and later versions of Python is known to have a problem with table colors.  Basically, they don't work.  As a result, if you want to use the plain PySimpleGUI running on tkinter, you should be using 3.7.2 or less.  3.6 is the version PySimpleGUI has chosen as the recommended version for most users.</p>
<h2 id="output-devices">Output Devices</h2>
<p>In addition to running as a desktop GUI, you can also run your GUI in a web browser by running PySimpleGUIWeb. </p>
<p>This is ideal for "headless" setups like a Raspberry Pi that is at the core of a robot or other design that does not have a normal display screen.  For these devices, run a PySimpleGUIWeb program that never exits.  </p>
<p>Then connect to your application by going to the Pi's IP address (and port #) using a browser and you'll be in communication with your application.  You can use it to make configuration changes or even control a robot or other piece of hardware using buttons in your GUI</p>
<h2 id="a-complete-pysimplegui-program-getting-the-gist">A Complete PySimpleGUI Program (Getting The Gist)</h2>
<p>Before diving into details, here's a description of what PySimpleGUI is/does and why that is so powerful.</p>
<p>You keep hearing "custom window" in this document because that's what you're making and using... your own custom windows.</p>
<p><strong>ELEMENTS</strong> is a word you'll see everywhere... in the code, documentation, ... Elements == PySimpleGUI's Widgets.  As to not confuse a tkinter Button Widget with a PySimpleGUI Button Element, it was decided that PySimpleGUI's Widgets will be called Elements to avoid confusion.</p>
<p>Wouldn't it be nice if a GUI with 3 "rows" of Elements was defined in 3 lines of code?  That's exactly how it's done.  Each row of Elements is a list.  Put all those lists together and you've got a window.</p>
<p>What about handling button clicks and stuff.  That's 4 lines of the code below beginning with the while loop.  </p>
<p>Now look at the <code>layout</code> variable and then look at the window graphic below.  Defining a window is taking a design you can see visually and then visually creating it in code.  One row of Elements = 1 line of code (can span more if your window is crowded).  The window is exactly what we see in the code.  A line of text, a line of text and an input area, and finally ok and cancel buttons.</p>
<p>This makes the coding process extremely quick and the amount of code very small</p>
<pre><code class="python">import PySimpleGUI as sg
sg.theme('DarkAmber')   # Add a little color to your windows
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.OK(), sg.Cancel()]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process &quot;events&quot;
while True:             
    event, values = window.read()
    if event in (None, 'Cancel'):
        break

window.close()
</code></pre>

<p><img alt="image" src="https://user-images.githubusercontent.com/46163555/68713283-7cb38200-056b-11ea-990a-aa1603af5a11.png" /></p>
<p>You gotta admit that the code above is a lot more "fun" looking that tkinter code you've studied before.  Adding stuff to your GUI is <strong><em>trivial</em></strong>.  You can clearly see the "mapping" of those 3 lines of code to specific Elements laid out in a Window.   It's not a trick.  It's how easy it is to code in PySimpleGUI.  With this simple concept comes the ability to create any window layout you wish.  There are parameters to move elements around inside the window should you need more control.</p>
<p>It's a thrill to complete your GUI project way ahead of what you estimated.  Some people take that extra time to polish their GUI to make it even nicer, adding more bells and whistles because it's so easy and it's a lot of fun to see success after success as you write your program.</p>
<p>Some are more advanced users and push the boundaries out and extend PySimpleGUI using their own extensions.</p>
<p>Others, like IT people and hackers are busily cranking out GUI program after GUI program, and creating tools that others can use.  Finally there's an easy way to throw a GUI onto your program and give it to someone.  It's a pretty big leap in capability for some people.  It's GREAT to hear these successes.  It's motivating for everyone in the end.  Your success can easily motivate the next person to give it a try and also potentially be successful.</p>
<p>Usually there's a one to one mapping of a PySimpleGUI Element to a GUI Widget. A "Text Element" in PySimpleGUI == "Label Widget" in tkinter.  What remains constant for you across all PySimpleGUI platforms is that no matter what the underlying GUI framework calls the thing that places text in your window, you'll always use the PySimpleGUI Text Element to access it.</p>
<h3 id="the-final-bit-of-magic-is-in-how-elements-are-created-and-changed">The final bit of magic is in how Elements are created and changed.</h3>
<p>So far you've seen simply layouts with no customization of the Elements.  Customizing and configuring Elements is another place PySimpleGUI utilizes the Python language to make your life easier.  </p>
<p>What about Elements that have settings other than the standard system settings?   What if I want my Text to be blue, with a Courier font on a green background.  It's written quite simply:</p>
<pre><code class="python">Text('This is some text', font='Courier 12', text_color='blue', background_color='green')
</code></pre>

<p>The Python named parameters are <strong><em>extensively</em></strong> in PySimpleGUI. They are key in making the code compact, readable, and trivial to write.</p>
<p>As you'll learn in later sections that discuss the parameters to the Elements, there are a LOT of options available to you should you choose to use them.  The <code>Text Element</code> has 15 parameters that you can change.  This is one reason why PyCharm is suggested as your IDE... it does a fantastic job of displaying documentation as you type in your code.</p>
<h3 id="thats-the-basics">That's <em>The</em> <em>Basics</em></h3>
<p>What do you think?  Easier so far than your previous run-ins with GUIs in Python?  Some programs, many in fact, are as simple as this example has been.</p>
<p>But PySimpleGUI certainly does <strong>not</strong> end here.  This is the beginning. The scaffolding you'll build upon.</p>
<h2 id="the-underlying-gui-frameworks-status-of-each">The Underlying GUI Frameworks &amp; Status of Each</h2>
<p>At the moment there are 4 actively developed and maintained "ports" of PySimpleGUI.  These include:</p>
<ol>
<li>tkinter - Fully complete</li>
<li>Qt using Pyside2 - Alpha stage.  Not all features for all Elements are done</li>
<li>WxPython - Development stage, pre-releaser.  Not all Elements are done. Some known problems with multiple windows</li>
<li>Remi (Web browser support) - Development stage, pre-release.</li>
</ol>
<p>While PySimpleGUI, the tkinter port, is the only 100% completed version of PySimpleGUI, the other 3 ports have a LOT of functionality in them and are in active use by a large portion of the installations.  You can see the number of Pip installs at the very top of this document to get a comparison as to the size of the install base for each port.  The "badges" are right after the logo.</p>
<h1 id="the-pysimplegui-family">The PySimpleGUI "Family"</h1>
<h2 id="whats-the-big-deal-what-is-it">What's The Big Deal? What is it?</h2>
<p>PySimpleGUI wraps tkinter, Qt, WxPython and Remi so that you get all the same widgets, but you interact with them in a more friendly way that's common across the ports. </p>
<p>What does a wrapper do (Yo! PSG in the house!)?  It does the layout, boilerplate code, creates and manages the GUI Widgets for you and presents you with a <strong>simple, efficient interface.</strong>   Most importantly, it maps the Widgets in tkinter/Qt/Wx/Remi into PySimpleGUI Elements.  Finally, it replaces the GUIs' event loop with one of our own.  </p>
<p>You've seen examples of the code already.  The big deal of all this is that anyone can create a GUI simply and quickly that matches GUIs written in the native GUI framework.  You can create complex layouts with complex element interactions.  And, that code you wrote to run on tkinter will also run on Qt by changing your import statement.</p>
<p>If you want a deeper explanation about the <a href="https://pysimplegui.readthedocs.io/en/latest/architecture/">architecture of PySimpleGUI</a>, you'll find it on ReadTheDocs in the same document as the Readme &amp; Cookbook. There is a tab at the top with labels for each document.</p>
<h2 id="the-ports">The "Ports"</h2>
<p>There are distinct ports happening as mentioned above.  Each have their own location on GitHub under the main project.  They have their own Readme with is an <em>augmentation</em> of this document... they are meant to be used together.</p>
<p>PySimpleGUI is released on PyPI as 5 distinct packages.
1. PySimpleGUI - tkinter version
2. PySimpleGUI27 - tkinter version that runs on 2.7
3. PySimpleGUIWx - WxPython version
4. PySimpleGUIQt - PySided2 version
5. PySimpleGUIWeb - The web (Remi) version</p>
<p>You will need to install them separately</p>
<p>There is also an accompanying debugger known as <code>imwatchingyou</code>.  If you are running the tkinter version of PySimpleGUI, you will not need to install the debugger as there is a version embedded directly into PySimpleGUI.</p>
<h2 id="qt-version">Qt Version</h2>
<p>Qt was the second port after tkinter.  It is the 2nd most complete with the original PySimpleGUI (tkinter) being the most complete and is likely to continue to be the front-runner.  All of the Elements are available on PySimpleGUIQt.</p>
<p>As mentioned previously each port has an area.  For Qt, you can learn more on the <a href="https://github.com/MikeTheWatchGuy/PySimpleGUI/tree/master/PySimpleGUIQt">PySimpleGUIQt GitHub site</a>.  <strong>There is a separate Readme file for the Qt version</strong> that you'll find there.  This is true for all of the PySimpleGUI ports.</p>
<p>Give it a shot if you're looking for something a bit more "modern".  PySimpleGUIQt is currently in <strong>Alpha</strong>.  <em>All of the widgets are operational but some may not yet be full-featured.</em>  If one is missing and your project needs it, log an Issue.  It's how new features are born.</p>
<p>Here is a summary of the Qt Elements with no real effort spent on design clearly.  It's an example of the "test harness" that is a part of each port. If you run the PySimpleGUI.py file itself then you'll see one of these tests.</p>
<p>As you can see, you've got a full array of GUI Elements to work with.  All the standard ones are there in a single window.  So don't be fooled into thinking PySimpleGUIQt is barely working or doesn't have many widgets to choose from.  You even get TWO "Bonus Elements" - <code>Dial</code> and <code>Stretch</code></p>
<h2 id="wxpython-version">WxPython Version</h2>
<p><a href="https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWx">PySimpleGUIWx GitHub site</a>.  <strong>There is a separate Readme file for the WxPython version</strong>.</p>
<p>Started in late December 2018 PySimpleGUIWx started with the SystemTray Icon feature.    This enabled the package to have one fully functioning feature that can be used along with tkinter to provide a complete program.    The System Tray feature is complete and working very well.  It was used not long ago in a corporate setting and has been performing with few problems reported.</p>
<p>The Windowing code was coming together with Reads operational.  The elements were getting completed on a regular basis. But I ran into multiwindow problems.  And it was at about this time that Remi was suggested as a port.</p>
<p>Remi (the "web port") overnight leapt the WxPython effort and Web became a #1 priority and continues to be.  The thought is that the desktop was well represented with PySimpleGUI, PySimpleGUIQt, and PySimpleGUIWx.  Between those ports is a solid windowing system and 2 system tray implementations and a nearly feature complete Qt effort.  So, the team was switched over to PySimpleGUIWeb.</p>
<h2 id="web-version-remi">Web Version (Remi)</h2>
<p><a href="https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWeb">PySimpleGUIWeb GitHub site</a>.  <strong>There is a separate Readme file for the Web version</strong>.</p>
<p>New for 2019, PySimpleGUIWeb.  This is an exciting development!  PySimpleGUI in your Web Browser!</p>
<p>The underlying framework supplying the web capability is the Python package Remi.  https://github.com/dddomodossola/remi  Remi provides the widgets as well as a web server for you to connect to.  It's an exiting new platform to be running on and has temporarily bumped the WxPython port from the highest priority.  PySimpleGUIWeb is the current high priority project.</p>
<p><strong>Use this solution for your Pi projects</strong> that don't have anything connected in terms of input devices or display.  Run your Pi in "headless" mode and then access it via the Web interface.  This allows you to easily access and make changes to your Pi without having to hook up anything to it.</p>
<p><strong><em>*It's not meant to "serve up web pages"</em></strong>*</p>
<p>PySimpleGUIWeb is first and foremost a <strong>GUI</strong>, a program's front-end. It is designed to have a single user connect and interact with the <strong>GUI</strong>.</p>
<p>If more than 1 person connects at a time, then both users will see the exact same stuff and will be interacting with the program as if a single user was using it.</p>
<h2 id="android-version">Android Version</h2>
<p>PySimpleGUI runs on Android devices with the help of either the PyDroid3 app or the Termux app.  Both are capable of running tkinter programs which means both are capable of running PySimpleGUI.</p>
<p>To use with PyDroid3 you will need to add this import to the top of all of your PySimpleGUI program files:</p>
<pre><code class="python">import tkinter
</code></pre>

<p>This evidently triggers PyDroid3 that the application is going to need to use the GUI.</p>
<p>You will also want to create your windows with the <code>location</code> parameter set to <code>(0,0)</code>.</p>
<p>Here's a quick demo that uses OpenCV2 to display your webcam in a window that runs on PyDroid3:</p>
<pre><code class="python">import tkinter
import cv2, PySimpleGUI as sg
USE_CAMERA = 0      # change to 1 for front facing camera
window, cap = sg.Window('Demo Application - OpenCV Integration', [[sg.Image(filename='', key='image')], ], location=(0, 0), grab_anywhere=True), cv2.VideoCapture(USE_CAMERA)
while window(timeout=20)[0] is not None:
    window['image'](data=cv2.imencode('.png', cap.read()[1])[1].tobytes())
</code></pre>

<p>You will need to pip install opencv-python as well as PySimpleGUI to run this program.</p>
<p>Also, you must be using the Premium, yes paid, version of PyDroid3 in order to run OpenCV.  The cost is CHEAP when compared to the rest of things in life.  A movie ticket will cost you more.  Which is more fun, seeing <strong>your Python program</strong> running on your phone and using your phone's camera, or some random movie currently playing?  From experience, the Python choice is a winner.  If you're cheap, well, then you won't get to use OpenCV. No, there is no secret commercial pact between the PySimpleGUI project and the PyDroid3 app team.  </p>
<h2 id="source-code-compatibility">Source code compatibility</h2>
<p>In theory, your source code is completely portable from one platform to another by simply changing the import statement.  That's the GOAL and surprisingly many times this 1-line change works.  Seeing your code run on tkinter, then change the import to <code>import  PySimpleGUIWeb as sg</code> and instead of a tkinter window, up pops your default browser with your window running on it is an incredible feeling.</p>
<p>But, <strong><em>caution is advised.</em></strong>  As you've read already, some ports are further along than others.  That means when you move from one port to another, some features may not work.  There also may be some alignment tweaks if you have an application that precisely aligns Elements.</p>
<p>What does this mean, assuming it works?  It means it takes a trivial amount of effort to move across GUI Frameworks.  Don't like the way your GUI looks on tkinter?  No problem, change over to try PySimpleGUIQt.  Made a nice desktop app but want to bring it to the web too?  Again, no problem, use PySimpleGUIWeb.</p>
<h2 id="replit-version">repl.it Version</h2>
<p><strong><em>Want to really get your mind blown?</em></strong>  Check out this <a href="https://repl.it/@PySimpleGUI/PySimpleGUIWeb-Demos">PySimpleGUI program</a> running in your web browser.</p>
<p>Thanks to the magic of repl.it and Remi it's possible to run PySimpleGUI code in a browser window without having Python running on your computer.  This should be viewed as a teaching and demonstration aid.  It is not meant to be a way of serving up web pages. It wouldn't work any way as each user forks and gets their own, completely different, workspace.</p>
<p>There are 2 ports of PySimpleGUI that run on repl.it - PySimpleGUI and PySimpleGUIWeb.</p>
<h3 id="pysimplegui-tkinter-based">PySimpleGUI (tkinter based)</h3>
<p>The primary PySimpleGUI port works very well on repl.it due to the fact they've done an outstanding job getting tkinter to run on these virtual machines.  Creating a program from scratch, you will want to choose the "Python with tkinter" project type.</p>
<p>The virtual screen size for the rendered windows isn't very large, so be mindful of your window's size or else you may end up with buttons you can't get to.</p>
<p>You may have to "install" the PySimpleGUI package for your project.  If it doesn't automatically install it for you, then click on the cube along the left edge of the browser window and then type in PySimpleGUI or PySimpleGUIWeb depending on which you're using.</p>
<h3 id="pysimpleguiweb-remi-based">PySimpleGUIWeb (Remi based)</h3>
<p>For PySimpleGUIWeb programs you run using repl.it will automatically download and install the latest PySimpleGUIWeb from PyPI onto a virtual Python environment.  All that is required is to type <code>import PySimpleGUIWeb</code> you'll have a Python environment up and running with the latest PyPI release of PySimpleGUIWeb.</p>
<h3 id="creating-a-replit-project-from-scratch-troubleshooting">Creating a repl.it project from scratch / troubleshooting</h3>
<p>To create your own repl.it PySimpleGUI project from scratch, first choose the type of Python virtual machine you want.  For PySimpleGUI programs, choose the "Python with tkinter" project type.  For PySimpleGUIWeb, choose the normal Python project.</p>
<p>There have been times where repl.it didn't do the auto import thing.  If that doesn't work for some reason, you can install packages by clicking on the package button on the left side of the interface, typing in the package name (PySimpleGUI or PySimpleGUIWeb) and install it. </p>
<h3 id="why-this-is-so-cool-listen-up-teachers-tutorial-writers">Why this is so cool (listen up Teachers, tutorial writers)</h3>
<p><strong><em>Educators</em></strong> in particular should be interested.  Students can not only post their homework easily for their teacher to access, but teachers can also run the students programs online.  No downloading needed.  Run it and check the results.</p>
<p>For people wanting to share their code, especially when helping someone with a problem, it's a great place to do it.  Those wishing to see your work do not have to be running Python nor have PySimpleGUI installed.</p>
<p>The way I use it is to first write my PySimpleGUI code on Windows, then copy and paste it into Repl.it.</p>
<p>Finally, you can embed these Repl.it windows into web pages, forum posts, etc.  The "Share" button is capable of giving you the block of code for an "iframe" that will render into a working repl.it program in your page.  It's amazing to see, but it can be slow to load.</p>
<h3 id="replit-is-not-a-web-server-for-you-to-deploy-applications">Repl.it is NOT a web server for you to "deploy" applications!</h3>
<p>Repl.it is not meant to serve up applications and web pages.  Trying to use it that way will not result in satisfactory results.  It's simply too slow and too technical of an interface for trying to "deploy" using it.  PySimpleGUIWeb isn't a great choice in serving web pages.  It's purpose is more to build a GUI that runs in a browser.</p>
<h2 id="macs">Macs</h2>
<p>It's surprising that Python GUI code is completely cross platform from Windows to Mac to Linux.  No source code changes.  This is true for both  PySimpleGUI and PySimpleGUIQt.</p>
<p>Historically, PySimpleGUI using tkinter have struggled on Macs.  This was because of a problem setting button colors on the Mac.  However, two events has turned this problem around entirely.</p>
<ol>
<li>Use of ttk Buttons for Macs</li>
<li>Ability for Mac users to install Python from python.org rather than the Homebrew version with button problems</li>
</ol>
<p>It's been a long road for Mac users with many deciding to use PySimpleGUIQt so that multi-colored windows could be made.  It's completely understandable to want to make attractive windows that utilize colors.  </p>
<p>PySimpleGUI now supports Macs, Linux, and Windows equally well. They all are able to use the "Themes" that automatically add color to your windows.  </p>
<p>Be aware that Macs default to using ttk buttons.  You can override this setting at the Window and Button levels.  If you installed Python from python.org, then it's likely you can use the non-ttk buttons should you wish.</p>
<h1 id="support">Support</h1>
<h2 id="dont-suffer-silently">Don't Suffer Silently</h2>
<p>The GitHub Issues are checked <em>often</em>.  Very often.  <strong>Please</strong> post your questions and problems there and there only.  Please don't post on Reddit, Stackoverflow, on forums, until you've tried posting on the GitHub.</p>
<p>Why?  <em>It will get you the best support possible.</em>  Second, you'll be helping the project as what you're experiencing might very well be a bug, or even a <em>known</em> bug. Why spend hours thrashing, fighting against a known bug?</p>
<p>It's not a super-buggy package, but users do experience problems just the same.  Maybe something's not explained well enough in the docs.  Maybe you're making a common mistake.  Maybe that feature isn't complete yet.</p>
<p>You won't look stupid posting an Issue on GitHub.  It's just the opposite.</p>
<h3 id="how-to-log-issues">How to log issues</h3>
<p><strong>PySimpleGUI is an active project.</strong>  Bugs are fixed, features are added, often.  Should you run into trouble, <strong>open an issue</strong> on the <a href="http://www.PySimpleGUI.com">GitHub site</a> and you'll receive help.  Posting questions on StackOverflow, Forums, Mailing lists, Reddit, etc, is not the fastest path to support and taking it may very well lead you astray as folks not familiar with the package struggle to help you. You may also run into the common response of "I don't know PySimpleGUI (and perhaps dislike it as a result), but I know you can do that with Qt".</p>
<p>Why only 1 location?  It's simple.... it's where the bugs, enhancements, etc are tracked.  It's THE spot on the Internet for this project.  There's not driven by a freakish being in control, telling people how to do things, reasoning.  It's so that YOU get the best and quickest support possible.</p>
<p>So, <a href="https://github.com/PySimpleGUI/PySimpleGUI/issues/new/choose">open an Issue</a>, choose "custom form" and fill it out completely.  There are very good reasons behind all of the questions.  Cutting corners only cuts your chances of getting help and getting quality help as it's difficult enough to debug remotely.  Don't handicap people that want to help by not providing enough information.</p>
<p><strong>Be sure and run your program outside of your IDE*<em> </em></strong>first***.  Start your program from the shell using <code>python</code> or <code>python3</code> command.  On numerous occasions much time was spent chasing problems caused by the IDE.  By running from a command line, you take that whole question out of the problem, an important step.</p>
<p><strong><em>Don't sit and stew, trying the same thing over and over</em></strong>, until you hate life... stop, and post an Issue on the GitHub.  Someone <strong>WILL</strong> answer you.  Support is included in the purchase price for this package (the quality level matches the price as well I'm afraid).  Just don't be too upset when your free support turns out to be a little bit crappy, but it's free and typically good advice.</p>
<h3 id="target-audience">Target Audience</h3>
<p>PySimpleGUI is trying to serve the 80% of GUI <em>problems</em>. The other 20% go straight to tkinter, Qt, WxPython, Remi, or whatever fills that need.  That 80% is <strong>a huge problem space</strong>.  </p>
<p><strong><em>The "Simple" of PySimpleGUI describes how easy it is to use, not the nature of the problem space it solves.</em></strong>  Note that people are not part of that description.  It's not trying to solve GUI problems for 80% of the people trying it.  PySimpleGUI tries to solve 80% of GUI <strong><em>problems</em></strong>, regardless of the programmer's experience level.</p>
<p>Is file I/O in Python limited to only certain people?  Is starting a thread, building a multi-threaded Python program incredibly difficult such that it takes a year to learn?  No.  It's quite easy.  Like most things Python, you import the object from package and you use it.  It is 2 lines of Python code to create and start a thread.</p>
<p>Why can't it be 2 lines of code to show a GUI window?  What's SO special about the Python GUI libraries that they require you to follow a specific Object Oriented model of development?  Other parts and packages of Python don't tend to do that.  </p>
<p>The reason is because they didn't originate in Python. They are strangers in a strange land and they had to be "adapted".  They started as C++ programs / SDKs, and remain that way too.  There's a vaneer of Python slapped onto the top of them, but that sure didn't make them fit the language as well as they could have.</p>
<p>PySimpleGUI is designed with both the beginner and the experienced developer in mind.  Why?  Because both tend to like compact code.  Most like people, we just want to get sh*t done, right?  And, why not do it in a way that's like how most of Python works?</p>
<p>The beginners can begin working with GUIs <strong><em>in their first week of Python education</em></strong>.  The professionals can jump right into the deep end of the pool to use the entire array of Elements and their capabilities to build stuff like a database application.</p>
<p>Here's a good example of how PySimpleGUI serves these 2 groups.... the <code>InputText</code> Element has 16 potential parameters, yet you'll find 0 or 1 parameters set by beginners. Look at the examples throughout this document and you'll see the code fragments utilize a tiny fraction of the potential parameters / settings.  Simple... <strong>keep it simple for the default case</strong>.  This is part of the PySimpleGUI mission.  </p>
<p>Some developers are heavily wedded to the existing GUI Framework Architectures (Qt, WxPython, tkinter).  They like the existing GUI architectures (they're all roughly the same, except this one).  If you're in that crowd, join the "20% Club" just down the street.  There's plenty of room there with plenty of possible solutions.</p>
<p>But how about a quick stop-in for some open mindedness exercises.  Maybe you will come up with an interesting suggestion even if you don't use it.  Or maybe PySimpleGUI does something that inspires you to write something similar directly in Qt.  And please, at least be civil about it.  There is room for multiple architectures.  Remember, you will not be <em>harmed</em> by writing some PySimpleGUI code just like you won't by writing some tkinter or Qt code.  Your chances of feeling harmed is more likely from one of those 2.</p>
<h4 id="beginners-easier-programs">Beginners &amp; Easier Programs</h4>
<p>There are a couple of reasons beginners stop in for a look.  The first is to simply throw a simple GUI onto the front of an existing command line application.  Or maybe you need to popup a box to get a filename.  These can often be simple 1-line <code>popup</code> calls.  Of course, you don't have to be a beginner to add a GUI onto one of your existing command line programs.  Don't feel like because you're an advanced programmer, you need to have an advanced solution.</p>
<p>If you have a more intricate, complete, perhaps multi-window design in mind, then PySimpleGUI still could be your best choice.</p>
<p>This package is not only great to use as your first GUI package, but it also teaches how to design and utilize a GUI. It does it better than the existing GUIs by removing the syntax, and lengthy code that can take an otherwise very simple appearing program into something that's completely unrecognizable.  With PySimpleGUI your 'layout' is all you need to examine to see the different GUI Elements that are being used.</p>
<p>Why does PySimpleGUI make it any easier to learn about GUIs?  Because it removes the classes, callback functions, object oriented design to better get out of your way and let you focus entirely on your GUI and not how to represent it in code.  </p>
<p>The result is 1/2 to 1/10th the amount of code that implements the exact same layout and widgets as you would get from coding yourself directly in Qt5.  It's been tested many times... again and again, PySimpleGUI produces significantly less code than Qt and the frameworks it runs on.</p>
<p>Forget syntax completely and just look on the overall activities of a PySimpleGUI programmer.  You have to design your window.... determine your inputs and your outputs, place buttons in strategic places, create menus, .... You'll be busy just doing all those things to design and define your GUI completely independent upon the underlying framework. </p>
<p>After you get all those design things done and are ready to build your GUI, it's then that you face the task of learning a GUI SDK.  Why not start with the easy one that gives you many successes?  You're JUST getting <strong><em>started</em></strong>, so cut yourself a break and use PySimpleGUI so that you can quickly get the job done and move on to the next GUI challenge.</p>
<h4 id="advanced-programmers-sharp-old-timers-code-slingers-and-code-jockeys">Advanced Programmers, Sharp Old-Timers, Code Slingers and Code Jockeys</h4>
<p>It's not perfect, but PySimpleGUI is an amazing bit of technology.  It's the programmer, the computer scientist, that has experience working with GUIs in the past that will recognize the power of this simple architecture.</p>
<p>What I hear from seasoned professionals is that PySimpleGUI saves them a <strong>ton</strong> of time.  They've written GUI code before.  They know how to lay out a window.  These folks just want to get their window working and quick.</p>
<p>With the help of IDE's like PyCharm, Visual Studio and Wing (the officially supported IDE list) you get instant documentation on the calls you are making.  On PyCharm you instantly see both the call signature but also the explanations about each parameter.</p>
<p>If the screenshots, demo programs and documentation don't convince you to at least <strong>give it a try, once</strong>, then you're way too busy, or .....  I dunno, I stopped guessing "why?" some time ago.  </p>
<p>Some of the most reluctant of people to try PySimpleGUI have turned out to be some of the biggest supporters.</p>
<h4 id="a-moment-of-thanks-to-the-pysimplegui-users">A Moment of Thanks To The PySimpleGUI Users</h4>
<p>I want to thank the early users of PySimpleGUI that started in 2018.  Your suggestions helped shape the package and have kept it moving forward at a fast pace.</p>
<p>For all the users, while I can't tell you the count of the number of times someone has said "thank you for PySimpleGUI" as part of logging and Issue, or a private message or email, but I can tell you that it's been significant.</p>
<p><strong><em>EVERY one of those "thank you" phrases, no matter how small you may think it is, helps tremendously.</em></strong></p>
<p>Sometimes it's what gets me past a problem or gets me to write yet more documentation to try and help people understand quicker and better.  Let's just say the effect is always positive and often significant.</p>
<p>PySimpleGUI users have been super-nice.  I doubt all Open Source Projects are this way, but I could be wrong and every GitHub repository has awesome users.  If so, that's even more awesome!</p>
<p><strong>THANK YOU PySimpleGUI USERS!</strong></p>
<hr />
<h1 id="learning-resources">Learning Resources</h1>
<p><strong><em>This document.... you must be willing to read this document if you expect to learn and use PySimpleGUI.</em></strong> </p>
<p>If you're unwilling to even try to figure out how to do something or find a solution to a problem and have determined it's "easier to post a question first than to look at the docs", then this is not the GUI package for you.  <em>If you're unwilling to help yourself, then don't expect someone else to try first.</em>  You need to hold up your end of the bargain by at least doing some searches of this document.</p>
<p>While PySimpleGUI enables you to write code easily, it doesn't mean that it magically fills your head with knowledge on how to use it.  The built-in docstrings help, but they can only go so far.  </p>
<p><strong><em>Searching this document is as easy as pressing Control + F.</em></strong></p>
<p>This document is on the GitHub homepage, as the readme. http://www.PySimpleGUI.com will get you there.  If you prefer a version with a Table of Contents on the left edge then you want to go to http://www.PySimpleGUI.org .  </p>
<h2 id="the-pysimplegui-developer-centric-model">The PySimpleGUI, Developer-Centric Model</h2>
<p>You may think that you're being fed a line about all these claims that PySimpleGUI is built specifically to make your life easier and a lot more fun than the alternatives.... especially after reading the bit above about reading this manual.</p>
<h3 id="psychological-warfare">Psychological Warfare</h3>
<p>Brainwashed. Know that there is an active campaign to get you to be successful using PySimpleGUI.  The "Hook" to draw you in and keep you working on your program until you're satisfied is to work on the dopamine in your brain. Yes, your a PySimpleGUI rat, pressing on that bar that drops a food pellet reward in the form of a working program.</p>
<p>The way this works is to give you success after success, with very short intervals between.  For this to work, what you're doing must work.  The code you run must work.  Make small changes to your program and run it over and over and over instead of trying to do one big massive set of changes.  Turn one knob at a time and you'll be fine.</p>
<p>Find the keyboard shortcut for your IDE to run the currently shown program so that running the code requires 1 keystroke.  On PyCharm, the key to run what you see is Control + Shift + F10.  That's a lot to hold down at once.  I programmed a hotkey on my keyboard so that it emits that combination of keys when I press it.  Result is a single button to run.</p>
<h3 id="tools">Tools</h3>
<p>These tools were created to help you achieve a steady stream of these little successes.</p>
<ul>
<li>This readme and its example pieces of code</li>
<li>The Cookbook - Copy, paste, run, success</li>
<li>Demo Programs - Copy these small programs to give yourself an instant headstart</li>
<li>Documentation shown in your IDE (docstrings) means you do not need to open any document to get the full assortment of options available to you for each Element &amp; function call</li>
</ul>
<p>The initial "get up and running" portion of PySimpleGUI should take you less than 5 minutes.  The goal is 5 minutes from your decision "I'll give it a try" to having your first window up on the screen "Oh wow, it was that easy?!"</p>
<p>The primary learning paths for PySimpleGUI are:</p>
<ul>
<li>This readme document over 100 pages of PySimpleGUI User Manual <ul>
<li>http://www.PySimpleGUI.org</li>
</ul>
</li>
<li>The Cookbook - Recipes to get you going and quick<ul>
<li>http://Cookbook.PySimpleGUI.org</li>
</ul>
</li>
<li>The Demo Programs - Start hacking on one of these running solutions<ul>
<li>http://www.PySimpleGUI.com</li>
</ul>
</li>
<li>The YouTube videos - If you like instructional videos, there are 15+ videos<ul>
<li><a href="https://www.youtube.com/playlist?list=PLl8dD0doyrvHMoJGTdMtgLuHymaqJVjzt">5 part series of basics</a></li>
<li><a href="https://www.youtube.com/playlist?list=PLl8dD0doyrvGyXjORNvirTIZxKopJr8s0">10 part series of more detail</a></li>
</ul>
</li>
</ul>
<p>Everything is geared towards giving you a "quick start" whether that be a Recipe or a Demo Program.  The idea is to give you something running and let you hack away at it.  As a developer this saves tremendous amounts of time.</p>
<p>You <strong>start</strong> with a working program, a GUI on the screen.  Then have at it.  If you break something (<code>"a happy little accident"</code> as Bob Ross put it), then you can always backtrack a little to a known working point.</p>
<p>A high percentage of users report both learning PySimpleGUI and completing their project in a single day.</p>
<p>This isn't a rare event and it's not bragging.  GUI programming doesn't HAVE to be difficult by definition and PySimpleGUI has certainly made it much much more approachable and easier (not to mention simpler).</p>
<p>But, you need to look at this document when pushing into new, unknown territory.  Don't guess... or more specifically, don't guess and then give up when it doesn't work.</p>
<h2 id="this-readme-and-cookbook">This Readme and Cookbook</h2>
<p>The readme and Cookbook, etc are best viewed on ReadTheDocs.  The quickest way there is to visit:
http://www.PySimpleGUI.org</p>
<p>You will be auto-forwarded to the right destination.  There are multiple tabs on ReadTheDocs.  One for the main readme and one for the Cookbook.  There are other documents there like an architectural design doc.</p>
<p>The Cookbook has approx 27 "Recipes" or short programs that can be easily copied and pasted.</p>
<h2 id="demo-programs">Demo Programs</h2>
<p>The GitHub repo has the Demo Programs.  There are ones built for plain PySimpleGUI that are usually portable to other versions of PySimpleGUI.  And there are some that are associated with one of the other ports.  The easiest way to the GitHub:</p>
<p>http://www.PySimpleGUI.com</p>
<p>As of this writing, on 2019-07-10 there are 177 Demo Programs for you to choose from.  </p>
<p>These programs demonstrate to you how to use the Elements and especially how to integrate PySimpleGUI with some of the popular open source technologies such as OpenCV, PyGame, PyPlot, and Matplotlib to name a few.</p>
<p>Many Demo Programs that are in the main folder will run on multiple ports of PySimpleGUI.  There are also port-specific Demo Programs.  You'll find those in the folder with the port.  So, Qt specific Demo Programs are in the PySimpleGUIQt folder.</p>
<hr />
<h1 id="the-quick-tour">The Quick Tour</h1>
<p>Let's take a super-brief tour around PySimpleGUI before digging into the details.  There are 2 levels of windowing support in PySimpleGUI -  High Level and Customized.</p>
<p>The high-level calls are those that perform a lot of work for you. These are not custom made windows (those are the other way of interacting with PySimpleGUI).</p>
<p>Let's use one of these high level calls, the <code>popup</code> and use it to create our first window, the obligatory "Hello World".  It's a single line of code.  You can use these calls like print statements, adding as many parameters and types as you desire.</p>
<pre><code class="python">import PySimpleGUI as sg

sg.popup('Hello From PySimpleGUI!', 'This is the shortest GUI program ever!')
</code></pre>

<p><img alt="hello world" src="https://user-images.githubusercontent.com/13696193/44960047-1f7f6380-aec6-11e8-9d5e-12ef935bcade.jpg" /></p>
<p>Or how about a <strong><em>custom GUI</em></strong> in 1 line of code?  No kidding this is a valid program and it uses Elements and produce the same Widgets like you normally would in a tkinter program.  It's just been compacted together is all, strictly for demonstration purposes as there's no need to go that extreme in compactness, unless you have a reason to and then you can be thankful it's possible to do.</p>
<pre><code class="python">import PySimpleGUI as sg

event, values = sg.Window('Get filename example', [[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).read(close=True)
</code></pre>

<p><img alt="get filename" src="https://user-images.githubusercontent.com/13696193/44960039-f1018880-aec5-11e8-8a43-3d7f8ff93b67.jpg" /></p>
<h2 id="the-beauty-of-simplicity">The Beauty of Simplicity</h2>
<blockquote>
<p>One day I will find the right words, and they will be simple.
― Jack Kerouac</p>
</blockquote>
<p>That's nice that you can crunch things into 1 line, like in the above example, but it's not readable.  Let's add some whitespace so you can see the <strong>beauty</strong> of the PySimpleGUI code.</p>
<p>Take a moment and look at the code below.  Can you "see" the window looking at the <code>layout</code> variable, knowing that each line of code represents a single row of Elements?  There are 3 "rows" of Elements shown in the window and there are 3 lines of code that define it.</p>
<p>Creating and reading the user's inputs for the window occupy the last 2 lines of code, one to create the window, the last line shows the window to the user and gets the input values (what button they clicked, what was input in the Input Element)</p>
<pre><code class="python">import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your creations colorful

layout = [  [sg.Text('Filename')],
            [sg.Input(), sg.FileBrowse()], 
            [sg.OK(), sg.Cancel()]] 

window = sg.Window('Get filename example', layout)

event, values = window.read()
window.close()
</code></pre>

<p><img alt="get filename" src="https://user-images.githubusercontent.com/13696193/44960039-f1018880-aec5-11e8-8a43-3d7f8ff93b67.jpg" /></p>
<p>Unlike other GUI SDKs, you can likely understand every line of code you just read, even though you have not yet read a single instructional line from this document about how you write Elements in a layout.</p>
<p>There are no pesky classes you are <em>required</em> to write, no callback functions to worry about.  None of that is required to show a window with some text, an input area and 2 buttons using PySimpleGUI.  </p>
<p>The same code, in tkinter, is 5 times longer and I'm guessing you won't be able to just read it and understand it.  While you were reading through the code, did you notice there are no comments, yet you still were able to understand, using intuition alone.</p>
<p>You will find this theme of Simple everywhere in and around PySimpleGUI.  It's a way of thinking as well as an architecture direction.  Remember, you, Mr./Ms. Developer, are at the center of the package.  So, from your vantage point, of course everything should look and feel simple.</p>
<p>Not only that, it's the Pythonic thing to do.  Have a look at line 3 of the "Zen of Python".</p>
<blockquote>
<p>The Zen of Python, by Tim Peters</p>
<p>Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than <em>right</em> now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!</p>
</blockquote>
<p>I just hope reading all these pages of documentation is going to make you believe that we're breaking suggestion:</p>
<blockquote>
<p>If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.</p>
</blockquote>
<p>I don't think PySimpleGUI is <strong><em>difficult</em></strong> to explain, but I am striving to fully explain it so that you don't do this:</p>
<blockquote>
<p>In the face of ambiguity, refuse the temptation to guess.</p>
</blockquote>
<p>Sometimes you can guess and be fine.  Other times, things may work, but the side effects are potentially significant.  There may be a much better way to solve a problem - Log an Issue on GitHub!  </p>
<hr />
<h1 id="some-examples">Some Examples</h1>
<h2 id="polishing-your-windows-building-beautiful-windows">Polishing Your Windows = Building "Beautiful Windows"</h2>
<p>And STILL the Zen of Python fits:</p>
<blockquote>
<p>Beautiful is better than ugly.</p>
</blockquote>
<p>but this fits too:</p>
<blockquote>
<p>Although practicality beats purity.</p>
</blockquote>
<p>Find a balance that works for you.</p>
<p>"But tkinter sucks"
"It looks like the 1990s" (this one is often said by people that were not alive in the 1990s)
"What Python GUI SDK will make my window look beautiful?"  (posted to Reddit at least every 2 weeks)</p>
<p>These windows below were ALL made using PySimpleGUI, the tkinter version and they look good enough to not be simply scoffed at and dismissed.  Remember, developer, you have a rather significant hand in how your application looks and operates.  You certainly cannot pin it all on the GUIs you're using.</p>
<p>So many posts on Reddit asking which GUI is going to result in a "beautiful window", as if there's a magic GUI library that pretties things up for you.  There are some calls in PySimpleGUI that will help you.  For example, you can make a single call to "Chang the look and feel" which loads predefined color pallets so your windows can have some instant color and it matches.</p>
<p>Beautiful windows are created, not simply given to you.  There are people that design and create artwork for user interfaces, you know that right?  Artists draw buttons, artwork that you include in the window to make it nicer.</p>
<p>Some of these have been "polished", others like the Matplotlib example is more a functional example to show you it works.</p>
<p><img alt="batterup" src="https://user-images.githubusercontent.com/46163555/77781297-b624ef80-702b-11ea-857a-b0809f061dc9.png" /></p>
<p><img alt="Uno" src="https://user-images.githubusercontent.com/46163555/77781360-d05ecd80-702b-11ea-90f9-cb9fb3339c05.png" /></p>
<p>This chess program is capable of running multiple AI chess engines and was written by another user using PySimpleGUI.</p>
<p><img alt="image" src="https://user-images.githubusercontent.com/13696193/61083102-e9214780-a3f8-11e9-9d1d-7c0a388625be.png" /></p>
<p>This downloader can download files as well as YouTube videos and metadata.  If you're worried about multiple windows working, don't.  Worried your project is "too much" or "too complex" for PySimpleGUI?  Do an initial assessment if you want.  Check out what others have done.  </p>
<p>Your program have 2 or 3 windows and you're concerned?  Below you'll see 11 windows open, each running independently with multiple tabs per window and progress meters that are all being updated concurrently.  </p>
<p><img alt="concurrent_windows" src="https://user-images.githubusercontent.com/13696193/62832448-3eb96180-bbfc-11e9-8777-6f2669566c93.png" /></p>
<p><img alt="pyplot 1" src="https://user-images.githubusercontent.com/13696193/44683336-11d46480-aa14-11e8-9d6c-f656796fc915.jpg" /></p>
<p>Just because you can't match a pair of socks doesn't mean your windows have to all look the same gray color.  Choose from over 100 different "Themes".  Add 1 line call to <code>theme</code> to instantly transform your window from gray to something more visually pleasing to interact with.  If you misspell the theme name badly or specify a theme name is is missing from the table of allowed names, then a theme will be randomly assigned for you.  Who knows, maybe the theme chosen you'll like and want to use instead of your original plan.</p>
<p>In PySimpleGUI release 4.6 the number of themes was dramatically increased from a couple dozen to over 100.  To use the color schemes shown in the window below, add a call to <code>theme('Theme Name)</code> to your code, passing in the name of the desired color theme. To see this window and the list of available themes on your release of software, call the function <code>theme_previewer()</code>.  This will create a window with the frames like those below.  It will shows you exactly what's available in your version of PySimpleGUI.</p>
<p>In release 4.9 another 32 Color Themes were added... here are the current choices</p>
<p><img alt="Dec 2019 Look And Feel Themes" src="https://user-images.githubusercontent.com/46163555/70382042-796da500-1923-11ea-8432-80d08cd5f503.jpg" /></p>
<p>Make beautiful looking, alpha-blended (partially transparent) Rainmeter-style Desktop Widgets that run in the background.</p>
<p><img alt="cpumeter" src="https://user-images.githubusercontent.com/46163555/77781418-ec626f00-702b-11ea-90b3-668fb71d63b5.png" /></p>
<p>Want to build a Crossword Puzzle?  No problem, the drawing primitives are there for you.</p>
<p><img alt="snag-0185" src="https://user-images.githubusercontent.com/13696193/47968340-98ba4480-e036-11e8-9d44-8a39ac174533.jpg" /></p>
<p>There are built-in drawing primitives</p>
<p><img alt="snag-0168" src="https://user-images.githubusercontent.com/13696193/47753225-2ed42080-dc6d-11e8-88d1-cf833db6c7ef.jpg" /></p>
<p>Frame from integration with a YOLO Machine Learning program that does object identification in realtime while allowing the user to adjust the algorithms settings using the sliders under the image.  This level of interactivity with an AI algorithm is still unusual to find due to difficulty of merging the technologies of AI and GUI.  It's no longer difficult.  This program is under 200 lines of code.</p>
<p><img alt="snag-0278" src="https://user-images.githubusercontent.com/13696193/48845583-e4752980-ed6a-11e8-9b2f-6c3d5d2442ba.jpg" /></p>
<h1 id="pi-windows">Pi Windows</h1>
<p>Perhaps you're looking for a way to interact with your <strong>Raspberry Pi</strong> in a more friendly way.  Your PySimpleGUI code will run on a Pi with no problem.  Tkinter is alive and well on the Pi platform. Here is a selection of some of the Elements shown on the Pi.  You get the same Elements on the Pi as you do Windows and Linux.</p>
<p><img alt="raspberry pi everything demo" src="https://user-images.githubusercontent.com/13696193/44279694-5b58ce80-a220-11e8-9ab6-d6021f5a944f.jpg" /></p>
<p>You can add custom artwork to make it look nice, like the Demo Program - Weather Forecast shown in this image:</p>
<p><img alt="weather pi" src="https://user-images.githubusercontent.com/13696193/47305324-1d4ca200-d5f7-11e8-8584-24a3992283ee.jpg" /></p>
<p><img alt="weather alone" src="https://user-images.githubusercontent.com/13696193/47305323-1d4ca200-d5f7-11e8-8fb1-44b0a7a4580f.jpg" /></p>
<p>One thing to be aware of with Pi Windows, you cannot make them semi-transparent.  This means that the <code>Window.Disappear</code> method will not work.  Your window will not disappear.  Setting the Alpha Channel will have no effect.</p>
<p>Don't forget that you can use custom artwork anywhere, including on the Pi.  The weather application looks beautiful on the Pi.  Notice there are no buttons or any of the normal looking Elements visible.  It's possible to build nice looking applications, even on the lower-end platforms.</p>
<h1 id="games">Games</h1>
<p>It's possible to create some cool games by simply using the built-in PySimpleGUI graphic primitives' like those used in this game of pong.  PyGame can also be embedded into a PySimpleGUI window and code is provided to you demonstrating how.  There is also a demonstration of using the pymunk physics package that can also be used for games.</p>
<p>Games haven't not been explored much, yet, using PySimpleGUI.</p>
<p><img alt="pong" src="https://user-images.githubusercontent.com/46163555/77781526-1c117700-702c-11ea-901b-4cb5f7a34cb4.png" /></p>
<h1 id="windows-programs-that-look-like-windows-programs">Windows Programs That Look Like Windows Programs</h1>
<p><strong><em>Do you have the desire to share your code with other people in your department, or with friends and family?</em></strong> Many of them may not have Python on their computer.  And in the corporate environment, it may not be possible for you to install Python on their computer.</p>
<p><code>PySimpleGUI + PyInstaller</code> to the rescue!!</p>
<p>Combining PySimpleGUI with PyInstaller creates something truly remarkable and special, a Python program that looks like a Windows WinForms application.  </p>
<p>The application you see below with a working menu was created in 20 lines of Python code.  It is a single .EXE file that launches straight into the screen you see.  And more good news, the only icon you see on the taskbar is the window itself... there is no pesky shell window.  Nice, huh? </p>
<p><img alt="windowsprogram" src="https://user-images.githubusercontent.com/46163555/77781479-03a15c80-702c-11ea-9408-903e022e0418.png" /></p>
<p>With a simple GUI, it becomes practical to "associate" .py files with the python interpreter on Windows.  Double click a py file and up pops a GUI window, a more pleasant experience than opening a dos Window and typing a command line.</p>
<p>There is even a PySimpleGUI program that will take your PySimpleGUI program and turn it into an EXE.  It's nice because you can use a GUI to select your file and all of the output is shown in the program's window, in realtime.</p>
<h1 id="background-why-pysimplegui-came-to-be">Background - Why PySimpleGUI Came to Be</h1>
<p>Feel free to skip all this if you don't care to know the backstory and reasons behind decisions.</p>
<p>There was a project looming and a GUI was needed.  It wasn't a very complex GUI so thus began a search for a simplified GUI package that would enable me to work with tkinter easier.  I found a few, and they were pretty popular too, but they lacked the full-compliment of Widgets and it was impossible to define my own window using those widgets.</p>
<p>A whacky idea came to mind... what if I wrote a simplified GUI and then used THAT to write my application.  It would be a lot less code and it would be "easy" to write my application then.  And that is exactly what was done.</p>
<p>First an early version of PySimpleGUI was written that had a subset of the Elements available today.  It had just enough for my application.  Then I wrote my application in PySimpleGUI.</p>
<p>Thus PySimpleGUI was born out of necessity and it's been the necessity of others that have helped evolve it into the package it is today.  It would not be 1/2 as good without the help of the community.</p>
<p>Once PySimpleGUI was done, it was time to start working on "the ports".  And, of course, also this documentation.</p>
<h2 id="the-non-oo-and-non-event-driven-model">The Non-OO and Non-Event-Driven Model</h2>
<p>The two "advanced concepts" that beginning Python students have with GUIs are the use of classes and callbacks with their associated communication and coordination mechanisms (semaphores, queues, etc)</p>
<p>How do you make a GUI interface easy enough for first WEEK Python students? </p>
<p>This meant classes could be used to build and use it, but classes can not be part of the code the user writes.  Of course, an OO design is quite possible to use with PySimpleGUI, but it's not a <strong><em>requirement</em></strong>.  The sample code and docs stay away from writing new classes in the user space for the most part.</p>
<p>What about those pesky callbacks?  They're difficult for beginners to grasp and they're a bit of a pain in the ass to deal with.  The way PySimpleGUI got around events was to utilize <strong><em>a "message passing" architecture</em></strong> instead.  </p>
<p>Instead of a user function being called when there's some event, instead the information is "passed" to the user when they call the function <code>Window.read()</code> </p>
<p><strong><em>Everything</em></strong> is returned through this <code>Window.read</code> call.  Of course the underlying GUI frameworks still perform callbacks, but they all happen inside of PySimpleGUI where they are turned into messages to pass to you.</p>
<p>All of the boilerplate code, the event handling, widget creation, frames containing widgets, etc, are <strong>exactly the same</strong> objects and calls that you would be writing if you wrote directly in tkinter, Qt, etc.  With all of this code out of the way and done for you, that leaves you with the task of doing something useful with the information the user entered.  THAT, after all, is the goal here.... getting user information and acting on it.</p>
<p>The full complement of Widgets are available to you via PySimpleGUI Elements.  And those widgets are presented to you in a unique and fun way.</p>
<p>If you wish to learn more about the Architecture of PySimpleGUI, take a look at the <a href="https://pysimplegui.readthedocs.io/en/latest/architecture/">Architecture document located on ReadTheDocs</a>.</p>
<h3 id="the-result">The Result</h3>
<p>A GUI that's appealing to a broad audience that is highly customizable, easy to program, and is solid with few bugs and rarely crashes (99% of the time it's some other error that causes a crash).</p>
<p>PySimpleGUI is becoming more and more popular. The number of installs and the number of successes grows daily.  Pip installs have exceeded 350,000 in the first year of existence.  Over 300 people a day visit the GitHub and the project has 1,800 stars (thank you awesome users!)</p>
<p>The number of ports is up to 4.  The number of integrations with other technologies is constantly being expanded.  It's a great time to try PySimpleGUI!  You've got no more than 5 or 10 minutes to lose.</p>
<p>Caution is needed, however, when working with the unfinished ports.  PySimpleGUI, the tkinter version, is the only fully complete port.  Qt is next.  All of its Elements are completed, but not all of the options of each element are done.  PySimpleGUIWeb is next in order of completeness and then finally PySimpleGUIWx.</p>
<h1 id="features">Features</h1>
<p>While simple to use, PySimpleGUI has significant depth to be explored by more advanced programmers.  The feature set goes way beyond the requirements of a beginner programmer, and into the  required features needed for complex multi-windowed GUIs.</p>
<p>For those of you that have heard PySimpleGUI is only good for doing the most simplest of GUIs, this feature list should put that myth to rest.  <strong>The SIMPLE part of PySimpleGUI is how much effort <em>you</em> expend to write a GUI, not the complexity of the program you are able to create.</strong>  It's literally "simple" to do... and it is not limited to simple problems.</p>
<p>Features of PySimpleGUI include:</p>
<ul>
<li>Support for Python versions 2.7 and 3</li>
<li>Text</li>
<li>Single Line Input</li>
<li>Buttons including these types:<ul>
<li>File Browse</li>
<li>Files Browse</li>
<li>Folder Browse</li>
<li>SaveAs</li>
<li>Normal button that returns event</li>
<li>Close window</li>
<li>Realtime</li>
<li>Calendar chooser</li>
<li>Color chooser</li>
<li>Button Menu</li>
</ul>
</li>
<li>TTK Buttons or "normal" TK Buttons</li>
<li>Checkboxes</li>
<li>Radio Buttons</li>
<li>Listbox</li>
<li>Option Menu</li>
<li>Menubar</li>
<li>Button Menu</li>
<li>Slider</li>
<li>Spinner</li>
<li>Dial</li>
<li>Graph</li>
<li>Frame with title</li>
<li>Icons</li>
<li>Multi-line Text Input</li>
<li>Scroll-able Output</li>
<li>Images</li>
<li>Tables</li>
<li>Trees</li>
<li>Progress Bar            Async/Non-Blocking Windows</li>
<li>Tabbed windows</li>
<li>Paned windows</li>
<li>Persistent Windows</li>
<li>Multiple Windows - Unlimited number of windows can be open at the same time</li>
<li>Redirect Python Output/Errors to scrolling window</li>
<li>'Higher level' APIs (e.g. MessageBox, YesNobox, ...)</li>
<li>Single-Line-Of-Code Progress Bar &amp; Debug Print</li>
<li>Complete control of colors, look and feel</li>
<li>Selection of pre-defined palettes</li>
<li>Button images</li>
<li>Horizontal and Vertical Separators</li>
<li>Return values as dictionary</li>
<li>Set focus</li>
<li>Bind return key to buttons</li>
<li>Group widgets into a column and place into window anywhere</li>
<li>Scrollable columns</li>
<li>Keyboard low-level key capture</li>
<li>Mouse scroll-wheel support</li>
<li>Get Listbox values as they are selected</li>
<li>Get slider, spinner, combo as they are changed</li>
<li>Update elements in a live window</li>
<li>Bulk window-fill operation</li>
<li>Save / Load window to/from disk</li>
<li>Borderless (no titlebar) windows (very classy looking)</li>
<li>Always on top windows</li>
<li>Menus with ALT-hotkey</li>
<li>Right click pop-up menu</li>
<li>Tooltips</li>
<li>Clickable text</li>
<li>Transparent windows</li>
<li>Movable windows</li>
<li>Animated GIFs</li>
<li>No async programming required (no callbacks to worry about)</li>
<li>Built-in debugger and REPL</li>
<li>User expandable by accessing underlying GUI Framework widgets directly</li>
</ul>
<hr />
<h2 id="design-goals">Design Goals</h2>
<p>With the developer being the focus, the center of it all, it was important to keep this mindset at all times, including now, today.  Why is this such a big deal?  Because this package was written so that the universe of Python applications can grow and can <strong>include EVERYONE into the GUI tent.</strong>  </p>
<blockquote>
<p>Up in 5 minutes</p>
</blockquote>
<p>Success #1 has to happen immediately.  Installing and then running your first GUI program.  FIVE minutes is the target.  The Pip install is under 1 minute.  Depending on your IDE and development environment, running your first piece of code could be a copy, paste, and run.  This isn't a joke target; it's for real serious.</p>
<blockquote>
<p>Beginners and Advanced Together</p>
</blockquote>
<p>Design an interface that both the complete beginner can understand and use that has enough depth that an advanced programmer can make some very nice looking GUIs amd not feel like they're playing with a "toy".</p>
<blockquote>
<p>Success After Success</p>
</blockquote>
<p>Success after success.... this is the model that will win developer's hearts.  This is what users love about PySimpleGUI.  Make your development progress in a way you can run and test your code often.  Add a little bit, run it, see it on your screen, smile, move on.</p>
<blockquote>
<p>Copy, Paste, Run.</p>
</blockquote>
<p>The Cookbook and Demo Programs are there to fulfill this goal.  First get the user seeing on their screen a working GUI that's similar in some way to what they want to create.  </p>
<p>If you're wanting to play with OpenCV download the OpenCV Demo Programs and give them a try.  Seeing your webcam running in the middle of a GUI window is quite a thrill if you're trying to integrate with the OpenCV package.  </p>
<p>"Poof" instant running OpenCV based application == Happy Developer</p>
<blockquote>
<p>Make Simpler Than Expected Interfaces</p>
</blockquote>
<p>The Single Line Progress Meter is a good example. It requires one and only 1 line of code.  Printing to a debug window is as easy as replacing <code>print</code> with <code>sg.Print</code> which will route your console output to a scrolling debug window.</p>
<blockquote>
<p>Be Pythonic</p>
</blockquote>
<p>Be Pythonic... </p>
<p>This one is difficult for me to define.  The code implementing PySimpleGUI isn't PEP8 compliant, but it is consistent.  The important thing was what the user saw and experienced while coding, NOT the choices for naming conventions in the implementation code.  The user interface to PySimpleGUI now has a PEP8 compliant interface.  The methods are snake_case now (in addition to retaining the older CamelCase names)</p>
<p>I ended up defining it as - attempt to use language constructs in a natural way and to exploit some of Python's interesting features.  It's Python's lists and optional parameters make PySimpleGUI work smoothly. </p>
<p>Here are some Python-friendly aspects to PySimpleGUI:</p>
<ul>
<li>Windows are represented as Python lists of Elements </li>
<li>Return values are an "event" such a button push and a list/dictionary of input values</li>
<li>The SDK calls collapse down into a single line of Python code that presents a custom GUI and returns values should you want that extreme of a single-line solution</li>
<li>Elements are all classes. Users interact with elements using class methods but are not required to write their own classes</li>
<li>Allow keys and other identifiers be any format you want. Don't limit user to particular types needlessly.</li>
<li>While some disagree with the single source file, I find the benefits greatly outweigh the negatives</li>
</ul>
<h4 id="lofty-goals">Lofty Goals</h4>
<blockquote>
<p>Teach GUI Programming to Beginners</p>
</blockquote>
<p>By and large PySimpleGUI is a "pattern based" SDK.  Complete beginners can copy these standard design patterns or demo programs and modify them without necessarily understanding all of the nuts and bolts of what's happening.  For example, they can modify a layout by adding elements even though they may not yet grasp the list of lists concept of layouts.  </p>
<p>Beginners certainly can add more <code>if event == 'my button':</code> statements to the event loop that they copied from the same design pattern.  They will not have to write classes to use this package.</p>
<blockquote>
<p>Capture Budding Graphic Designers &amp; Non-Programmers</p>
</blockquote>
<p>The hope is that beginners that are interested in graphic design, and are taking a Python course, will have an easy way to express themselves, right from the start of their Python experience.  Even if they're not the best programmers they will be able express themselves to show custom GUI layouts, colors and artwork with ease.</p>
<blockquote>
<p>Fill the GUI Gap (Democratize GUIs)</p>
</blockquote>
<p>There is a noticeable gap in the Python GUI solution.  Fill that gap and who knows what will happen.  At the moment, to make a traditional GUI window using tkinter, Qt, WxPython and Remi, it takes much more than a week, or a month of Python education to use these GUI packages.  </p>
<p>They are out of reach of the beginners.  Often WAY out of reach.  And yet, time and time again, beginners that say they JUST STARTED with Python will ask on a Forum or Reddit for a GUI package recommendation.  9 times out of 10 Qt is recommended.  (smacking head with hand).  What a waste of characters.  You might as well have just told them, "give up".</p>
<blockquote>
<p>Is There a There?</p>
</blockquote>
<p>Maybe there's no "there there".  <strong><em>Or</em></strong> maybe a simple GUI API will enable Python to dominate yet another computing discipline like it has so many others.  This is one attempt to find out.  So far, it sure looks like there's PLENTY of demand in this area.</p>
<h1 id="getting-started-with-pysimplegui">Getting Started with PySimpleGUI</h1>
<p>There is a "Troubleshooting" section towards the end of this document should you run into real trouble.  It goes into more detail about what you can do to help yourself.</p>
<h2 id="installing-pysimplegui">Installing PySimpleGUI</h2>
<p>Of course if you're installing for Qt, WxPython, Web, you'll use PySimpleGUIQt, PySimpleGUIWx, and PySimpleGUIWeb instead of straight PySimpleGUI in the instructions below.  You should already have the underlying GUI Framework installed and perhaps tested.  This includes tkinter, PySide2, WxPython, Remi</p>
<h3 id="installing-on-python-3">Installing on Python 3</h3>
<p><code>pip install --upgrade PySimpleGUI</code></p>
<p>On some systems you need to run pip3. (Linux and Mac)</p>
<p><code>pip3 install --upgrade PySimpleGUI</code></p>
<p>On a Raspberry Pi, this is should work:</p>
<p><code>sudo pip3 install --upgrade pysimplegui</code></p>
<p>Some users have found that upgrading required using an extra flag on the pip <code>--no-cache-dir</code>.</p>
<p><code>pip install --upgrade --no-cache-dir PySimpleGUI</code></p>
<p>On some versions of Linux you will need to first install pip.  Need the Chicken before you can get the Egg (get it... Egg?)</p>
<p><code>sudo apt install python3-pip</code></p>
<p><code>tkinter</code> is a requirement for PySimpleGUI (the only requirement).  Some OS variants, such as Ubuntu, do not some with <code>tkinter</code> already installed.  If you get an error similar to:</p>
<p><code>ImportError: No module named tkinter</code></p>
<p>then you need to install <code>tkinter</code>.</p>
<p>For python 2.7</p>
<p><code>sudo apt-get install python-tk</code></p>
<p>For python 3
<code>sudo apt-get install python3-tk</code></p>
<p>More information about installing tkinter can be found here: https://www.techinfected.net/2015/09/how-to-install-and-use-tkinter-in-ubuntu-debian-linux-mint.html</p>
<h3 id="installing-typing-module-for-python-34-raspberry-pi">Installing typing module for Python 3.4 (Raspberry Pi)</h3>
<p>In order for the docstrings to work correctly the <code>typing</code> module is used.  In Python version 3.4 the typing module is not part of Python and must be installed separately. You'll see a warning printed on the console if this module isn't installed.</p>
<p>You can pip install <code>typing</code> just like PySimpleGUI.  However it's not a requirement as PySimpleGUI will run fine without typing installed as it's only used by the docstrings.</p>
<h3 id="installing-for-python-27">Installing for Python 2.7</h3>
<p><strong>IMPORTANT</strong> PySimpleGUI27 will disappear from the GitHub on Dec 31, 2019. PLEASE migrate to 3.6 at least.  It's not painful for most people.</p>
<p><code>pip install --upgrade PySimpleGUI27</code>
or
<code>pip2 install --upgrade PySimpleGUI27</code></p>
<p>You may need to also install "future" for version 2.7</p>
<p><code>pip install future</code>
or
<code>pip2 install future</code></p>
<p>Like above, you may have to install either pip or tkinter.  To do this on Python 2.7:</p>
<p><code>sudo apt install python-pip</code></p>
<p><code>sudo apt install python-tkinter</code></p>
<h3 id="upgrading-from-github-using-pysimplegui">Upgrading from GitHub Using PySimpleGUI</h3>
<p>Starting in version 4.17.0 there is code in the PySimpleGUI package that upgrades your previously pip installed package using the latest version checked into GitHub.  </p>
<p>Previously if you wanted to run the GitHub version, you would:
* Download the PySimpleGUI.py file from GitHub
* Place it in your applications's folder</p>
<p>This required you to go back later and delete this file when you want to move on to the next version released to PyPI.  </p>
<p>The new capability is the ability to overwrite your PySimpleGUI.py file that you installed using <code>pip</code> with the currently posted version on GitHub.  Using this method when you're ready to install the next version from PyPI or you want to maybe roll back to a PyPI release, you only need to run <code>pip</code>.  You don't have to find and delete any PySimpleGUI.py files.</p>
<p><strong><em>Important - Linux Users</em></strong> - There is currently a problem using this utility on Linux systems.  It's being worked on and a patch will be released as soon as something is figured out.</p>
<h4 id="command-line-upgrade">Command Line Upgrade</h4>
<p>To upgrade PySimpleGUI from the command line type this command into your dos window</p>
<p><code>python -m PySimpleGUI upgrade</code></p>
<p>You will first be shown a confirmation window:</p>
<p><img alt="image" src="https://user-images.githubusercontent.com/46163555/77477572-f0f01300-6df2-11ea-812f-98a36e7c28e0.png" /></p>
<p>If you choose yes, then the new version will be installed and you'll see a red "completed" window</p>
<p><img alt="image" src="https://user-images.githubusercontent.com/46163555/77477619-006f5c00-6df3-11ea-8b01-44b1bea22989.png" /></p>
<h4 id="gui-upgrade">GUI Upgrade</h4>
<p>The PySimpleGUI Test Harness is another mechanism you can use to upgrade.  To start the test harness you "run" the PySimpleGUI package.  </p>
<p><code>python -m PySimpleGUI.PySimpleGUI</code></p>
<p>Of course if you're running Linux you may run <code>python3</code> instead.</p>
<p>From your code you can call <code>PySimpleGUI.main()</code>.  This window may not look exactly like the one you see, but the thing that should be there is the red "Install" button.</p>
<p><img alt="image" src="https://user-images.githubusercontent.com/46163555/77478381-437dff00-6df4-11ea-994e-a443ff967917.png" /></p>
<p>Clicking the install button will bring up the same confirmation window shown as the command line upgrade above.</p>
<h3 id="testing-your-installation-and-troubleshooting">Testing your installation and Troubleshooting</h3>
<p>Once you have installed, or copied the .py file to your app folder, you can test the installation using python.  At the command prompt start up Python.</p>
<h4 id="the-quick-test">The Quick Test</h4>
<p>The PySimpleGUI Test Harness pictured in the previous section on GUI upgrades is the short program that's built into PySimpleGUI that serves multiple purposes.  It exercises many/most of the available Elements, displays version and location data and works as a quick self-test.</p>
<p>From your command line type:
<code>python -m PySimpleGUI.PySimpleGUI</code></p>
<p>If you're on Linux/Mac and need to run using the command <code>python3</code> then of course type that.</p>
<p>This will display the test harness window.  </p>
<p>You can also test by using the REPL....</p>
<h4 id="instructions-for-testing-python-27">Instructions for Testing Python 2.7:</h4>
<pre><code class="python">&gt;&gt;&gt; import PySimpleGUI27
&gt;&gt;&gt; PySimpleGUI27.main()
</code></pre>

<h4 id="instructions-for-testing-python-3">Instructions for Testing Python 3:</h4>
<pre><code class="python3">&gt;&gt;&gt; import PySimpleGUI
&gt;&gt;&gt; PySimpleGUI.main()
</code></pre>

<p>You will see a "test harness" that exercises the SDK, tells you the version number, allows you to try a number of features as well as access the built-in GitHub upgrade utility.</p>
<h3 id="finding-out-where-your-pysimplegui-is-coming-from">Finding Out Where Your PySimpleGUI Is Coming From</h3>
<p>It's <strong>critical</strong> for you to be certain where your code is coming from and which version you're running.</p>
<p>Sometimes when debugging, questions arise as to exactly which PySimpleGUI you are running.  The quick way to find this out is to again, run Python from the command line.  This time you'll type:</p>
<pre><code class="python3">&gt;&gt;&gt; import PySimpleGUI as sg
&gt;&gt;&gt; sg
</code></pre>

<p>When you type sg, Python will tell you the full patch to your PySimpleGUI file / package.  This is critical information to know when debugging because it's really easy to forget you've got an old copy of PySimpleGUI laying around somewhere.</p>
<h3 id="finding-out-where-your-pysimplegui-is-coming-from-from-within-your-code">Finding Out Where Your PySimpleGUI Is Coming From (from within your code)</h3>
<p>If you continue to have troubles with getting the right version of PySimpleGUI loaded, THE <strong><em>definitive</em></strong> way to determine where your program is getting PySimpleGUI from is to add a print to your program.  It's that <em>simple</em>!  You can also get the version you are running by also printing</p>
<pre><code class="python">import PySimpleGUI as sg

print(sg)
print(sg.version)
</code></pre>

<p>Just like when using the REPL &gt;&gt;&gt; to determine the location, this <code>print</code> in your code will display the same path information.</p>
<h3 id="manual-installation">Manual installation</h3>
<p>If you're not connected to the net on your target machine, or pip isn't working, or you want to run the latest code from GitHub, then all you have to do is place the single PySimpleGUI source file <code>PySimpleGUI.py</code> (for tkinter port) and place it in your application's folder (the folder where the py file is that imports PySimpleGUI).  Your application will load that local copy of PySimpleGUI as if it were a package.</p>
<p>Be <strong><em>sure</em></strong> that you delete this PySimpleGUI.py file if you install a newer pip version.  Often the sequence of events is that a bug you've reported was fixed and checked into GitHub.  You download the PySimpleGUI.py file (or the appropriately named one for your port) and put with your app.  Then later your fix is posted with a new release on PyPI.  You'll want to delete the GitHub one before you install from pip.</p>
<h3 id="prerequisites">Prerequisites</h3>
<p>Python 2.7 or Python 3
tkinter</p>
<p>PySimpleGUI Runs on all Python3 platforms that have tkinter running on them.  It has been tested on Windows, Mac, Linux, Raspberry Pi.  Even runs on <code>pypy3</code>.</p>
<h3 id="exe-file-creation">EXE file creation</h3>
<p>If you wish to create an EXE from your PySimpleGUI application, you will need to install <code>PyInstaller</code>.  There are instructions on how to create an EXE at the bottom of this document.</p>
<h2 id="ides">IDEs</h2>
<p>A lot of people ask about IDEs, and many outright fear PyCharm.  Listen up.... compared to your journey of learning Python, learning to use PyCharm as your IDE is NOTHING.  It's a DAY typically (from 1 to 8 hours).  Or, if you're really really new, perhaps as much as a week <em>to get used to</em>.  So, we're not talking about you needing to learn to flap your arms and fly.</p>
<p>To sum up that paragraph, stop whining like a little b*tch.  You're a grown man/woman, act like it.  "But it's hard..."  If you found this package, then you're a bright person :-)  Have some confidence in yourself for Christ sake.... I do.  Not going to lead you off some cliff, promise!</p>
<p>Some IDEs provide virtual environments, but it's optional.  PyCharm is one example.  For these, you will either use their GUI interface to add packages or use their built-in terminal to do pip installs.  <strong>It's not recommended for beginners to be working with Virtual Environments.</strong>  They can be quite confusing.  However, if you are a seasoned professional developer and know what you're doing, there is nothing about PySimpleGUI that will prevent you from working this way.  It's mostly a caution for beginners because more often than not, they get really messed up and confused.</p>
<h3 id="officially-supported-ides">Officially Supported IDEs</h3>
<p>A number of IDEs have <strong>known problems with PySimpleGUI*<em>.  IDLE, Spyder, and Thonny all have known, demonstrable, problems with intermittent or inconsistent results, <strong>especially when a program exits</strong> and you want to continue to work with it. </em></strong> Any IDE that is based on tkinter is going to have issues with the straight PySimpleGUI port.***  This is NOT a PySimpleGUI problem.</p>
<p>The official list of supported IDEs is:
1. PyCharm (or course this is THE IDE to use for use with PySimpleGUI)
2. Wing
3. Visual Studio</p>
<p>If you're on a Raspberry Pi or some other limited environment, then you'll may have to use IDLE or Thonny.  Just be aware there could be problems using the debugger to debug due to both using tkinter.</p>
<h3 id="using-the-docstrings-dont-skip-this-section">Using The Docstrings (Don't skip this section)</h3>
<p>Beginning with the 4.0 release of PySimpleGUI, the tkinter port, a whole new world opened up for PySimpleGUI programmers, one where referencing the readme and ReadTheDocs documentation is no longer needed.  PyCharm and Wing both support these docstrings REALLY well and I'm sure Visual Studio does too.  Why is this important?  Because it will teach you the PySimpleGUI SDK as you use the package.  </p>
<p>Don't know the parameters and various options for the <code>InputText</code> Element?  It's a piece of cake with PyCharm.  You can set PyCharm to automatically display documentation about the class, function, method, etc, that your cursor is currently sitting on.  You can also manually bring up the documentation by pressing CONTROL+Q.  When you do, you'll be treated to a window similar to this:</p>
<p><img alt="image" src="https://user-images.githubusercontent.com/13696193/61997565-46f89500-b071-11e9-968e-83a99ecb718a.png" /></p>
<p>Note that my cursor is on <code>InputText</code>.  On the left side of the screen, the <code>InputText</code> element's parameters are not just shown to you, but they are each individually described to you, and, the type is shown as well.  <em>I mean, honestly, how much more could you ask for?</em></p>
<p>OK, I suppose you could ask for a smaller window that just shows the parameters are you're typing them in.  Well, OK, in PyCharm, when your cursor is between the  <code>(   )</code> press CONTROL+P.  When you do, you'll be treated to a little window like this one:</p>
<p><img alt="image" src="https://user-images.githubusercontent.com/13696193/61997590-aa82c280-b071-11e9-8d76-7d9c811f8fcc.png" /></p>
<p>See.... written with the "Developer" in mind, at all times.  It's about YOU, Mr/Ms Developer!  So enjoy your package.</p>
<p>The other ports of PySimpleGUI (Qt, WxPython, Web) have not yet had their docstrings updated.  They're NEXT in line to be better documented.  Work on a tool has already begun to make that happen sooner than later.</p>
<h4 id="type-checking-with-docstrings">Type Checking With Docstrings</h4>
<p>In version 4.17.0 a new format started being used for docstrings.  This new format more clearly specified the types for each parameter.  It will take some time to get all of the parameter types correctly identified and documented.  </p>
<p>Pay attention when you're working with PyCharm and you'll see where you may have a mismatch... or where there's a bad docstring, take your pick. It will shade your code in a way that makes mismatched types very clear to see.</p>
<h2 id="using-python-3">Using  - Python 3</h2>
<p>To use in your code, simply import....
<code>import PySimpleGUI as sg</code></p>
<p>Then use either "high level" API calls or build your own windows.</p>
<p><code>sg.popup('This is my first popup')</code></p>
<p><img alt="first popup" src="https://user-images.githubusercontent.com/13696193/44957300-c7813680-ae9e-11e8-9a8c-c70198db7907.jpg" /></p>
<p>Yes, it's just that easy to have a window appear on the screen using Python.  With PySimpleGUI, making a custom window appear isn't much more difficult.  The goal is to get you running on your GUI within <strong><em>minutes</em></strong>, not hours nor days.</p>
<h3 id="python-37">Python 3.7</h3>
<p>If you must run 3.7, try 3.7.2.  It does work with PySimpleGUI with no known issues.</p>
<p><strong><em>PySimpleGUI with Python 3.7.3 and 3.7.4+.</em></strong>  tkinter is having issues with all the newer releases.  Things like Table colors stopped working entirely.  </p>
<p>March 2020 - Still not quite sure if all issues have been ironed out with tkinter in the 3.7 and 3.8 releases.</p>
<h2 id="python-27">Python 2.7</h2>
<p>On December 31, 2019 the Python 2.7 version of PySimpleGUI will be <strong>deleted</strong> from the GitHub.  Sorry but Legacy Python has no permanent home here.  The security experts claim that supporting 2.7 is doing a disservice to the Python community.  I understand why.  There are some very narrow cases where 2.7 is required.  If you have one, make a copy of PySimpleGUI27.py quickly before it disappears for good.</p>
<hr />
<h1 id="pep8-bindings-for-methods-and-functions">PEP8 Bindings For Methods and Functions</h1>
<p>Beginning with release 4.3 of PySimpleGUI, <strong><em>all methods and function calls</em></strong> have PEP8 equivalents.  This capability is only available, for the moment, on the PySimpleGUI tkinter port.  It is being added, as quickly as possible, to all of the ports.</p>
<p>As long as you know you're sticking with tkinter for the short term, it's safe to use the new bindings.</p>
<h2 id="the-non-pep8-methods-and-functions">The Non-PEP8 Methods and Functions</h2>
<p>Why the need for these bindings?  Simply put, the PySimpleGUI SDK has a PEP8 violation in the method and function names.  PySimpleGUI uses CamelCase names for methods and functions.  PEP8 suggests using snake_case_variables instead.  </p>
<p>This has not caused any problems and few complaints, but it's important the the interfaces into PySimpleGUI be compliant.  Perhaps one of the reasons for lack of complaints is that the Qt library also uses SnakeCase for its methods.  This practice has the effect of labelling a package as being "not Pythonic" and also suggests that this package was originally used in another language and then ported to Python.  This is exactly the situation with Qt.  It was written for C++ and the interfaces continue to use C++ conventions.</p>
<p><strong><em>PySimpleGUI was written in Python, for Python.</em></strong>  The reason for the name problem was one of ignorance.  The PEP8 convention wasn't understood by the developers when PySimpleGUI was designed and implemented.  </p>
<p>You can, and will be able to for some time, use both names.  However, at some point in the future, the CamelCase names will disappear.  A utility is planned to do the conversion for the developer when the old names are remove from PySimpleGUI.</p>
<p>The help system will work with both names as will your IDE's docstring viewing.  However, the result found will show the CamelCase names.  For example <code>help(sg.Window.read)</code> will show the CamelCase name of the method/function.  This is what will be returned:</p>
<p><code>Read(self, timeout=None, timeout_key='__TIMEOUT__')</code></p>
<h2 id="the-renaming-convention">The Renaming Convention</h2>
<p>To convert a CamelCase method/function name to snake_case, you simply place an <code>_</code> where the Upper Case letter is located.  If there are none, then only the first letter is changed.</p>
<p><code>Window.FindElement</code> becomes <code>Window.find_element</code></p>
<h2 id="class-variables">Class Variables</h2>
<p>For the time being, class variables will remain the way they are currently.  It is unusual, in PySimpleGUI, for class variables to be modified or read by the user code so the impact of leaving them is rarely seen in your code.</p>
<h1 id="high-level-api-calls-popups">High Level API Calls  - Popup's</h1>
<p>"High level calls" are those that start with "popup".    They are the most basic form of communications with the user.   They are named after the type of window they create, a pop-up window.  These windows are meant to be short lived while, either delivering information or collecting it, and then quickly disappearing.</p>
<p>Think of Popups as your first windows, sorta like your first bicycle. It worked well, but was limited.  It probably wasn't long before you wanted more features and it seemed too limiting for your newly found sense of adventure.</p>
<p>When you've reached the point with Popups that you are thinking of filing a GitHub "Enhancement Issue" to get the Popup call extended to include a new feature that you think would be helpful.... not just to you but others is what you had in mind, right?  For the good of others. </p>
<p>Well, don't file that enhancement request.  Instead, it's at THIS time that you should immediately turn to the section entitled "Custom Window API Calls - Your First Window".  Congratulations, you just graduated and are now an official "GUI Designer".  Oh, never mind that you only started learning Python 2 weeks ago, you're a real GUI Designer now so buck up and start acting like one.  Write a popup function of your own.  And then, compact that function down to a <strong>single line of code</strong>.  Yes, these popups can be written in 1 line of code.  The secret is to use the <code>close</code> parameter on your call to <code>window.read()</code></p>
<p>But, for now, let's stick with these 1-line window calls, the Popups.   This is the list of popup calls available to you:</p>
<p>popup_animated
popup_annoying
popup_auto_close 
popup_cancel
popup_error
popup_get_file 
popup_get_folder 
popup_get_text
popup_no_border
popup_no_buttons
popup_no_frame 
popup_no_titlebar
popup_no_wait
popup_notify
popup_non_blocking
popup_ok
popup_ok_cancel
popup_quick
popup_quick_message
popup_scrolled
popup_timed
popup_yes_no</p>
<h2 id="popup-output">Popup Output</h2>
<p>Think of the <code>popup</code> call as the GUI equivalent of a  <code>print</code> statement.  It's your way of displaying results to a user in the windowed world.  Each call to Popup will create a new Popup window.</p>
<p><code>popup</code> calls are normally blocking.  your program will stop executing until the user has closed the Popup window.  A non-blocking window of Popup discussed in the async section.</p>
<p>Just like a print statement, you can pass any number of arguments you wish.  They will all be turned into strings and displayed in the popup window.</p>
<p>There are a number of Popup output calls, each with a slightly different look or functionality (e.g. different button labels, window options).</p>
<p>The list of Popup output functions are:
- popup
- popup_ok
- popup_yes_no
- popup_cancel
- popup_ok_cancel
- popup_error
- popup_timed, popup_auto_close, popup_quick, popup_quick_message
- popup_no_waitWait, popup_non_blocking
- popup_notify</p>
<p>The trailing portion of the function name after Popup indicates what buttons are shown.  <code>PopupYesNo</code> shows a pair of button with Yes and No on them.   <code>PopupCancel</code> has a Cancel button, etc..</p>
<p>While these are "output" windows, they do collect input in the form of buttons.  The Popup functions return the button that was clicked.  If the Ok button was clicked, then Popup returns the string 'Ok'.  If the user clicked the X button to close the window, then the button value returned is <code>None</code> or <code>WIN_CLOSED</code> is more explicit way of writing it.</p>
<p>The function <code>popup_timed</code> or <code>popup_auto_close</code> are popup windows that will automatically close after come period of time.</p>
<p>Here is a quick-reference showing how the Popup calls look.</p>
<pre><code class="python">sg.popup('popup')  # Shows OK button
sg.popup_ok('popup_ok')  # Shows OK button
sg.popup_yes_no('popup_yes_no')  # Shows Yes and No buttons
sg.popup_cancel('popup_cancel')  # Shows Cancelled button
sg.popup_ok_cancel('popup_ok_cancel')  # Shows OK and Cancel buttons
sg.popup_error('popup_error')  # Shows red error button
sg.popup_timed('popup_timed')  # Automatically closes
sg.popup_auto_close('popup_auto_close')  # Same as PopupTimed
</code></pre>

<p>Preview of popups:</p>
<p style="display: flex;justify-content: space-around;">
    <img src="https://user-images.githubusercontent.com/13696193/44957394-1380ab00-aea0-11e8-98b1-1ab7d7bd5b37.jpg">
    <img src="https://user-images.githubusercontent.com/13696193/44957400-167b9b80-aea0-11e8-9d42-2314f24e62de.jpg">
    <img src="https://user-images.githubusercontent.com/13696193/44957399-154a6e80-aea0-11e8-9580-e716f839d400.jpg">
</p>

<p style="display: flex;justify-content: space-around;">
    <img src="https://user-images.githubusercontent.com/13696193/44957398-14b1d800-aea0-11e8-9e88-c2b36a248447.jpg">
    <img src="https://user-images.githubusercontent.com/13696193/44957397-14b1d800-aea0-11e8-950b-6d0b4f33841a.jpg">
    <img src="https://user-images.githubusercontent.com/13696193/44957396-14194180-aea0-11e8-8eef-bb2e1193ecfa.jpg">
    <img src="https://user-images.githubusercontent.com/13696193/44957595-9e15da00-aea1-11e8-8909-6b6121b74509.jpg">
</p>

<p>Popup - Display a popup Window with as many parms as you wish to include.  This is the GUI equivalent of the
"print" statement.  It's also great for "pausing" your program's flow until the user can read some error messages.</p>
<pre><code>Popup(args=*&lt;1 or N object&gt;,
    title=None,
    button_color=None,
    background_color=None,
    text_color=None,
    button_type=0,
    auto_close=False,
    auto_close_duration=None,
    custom_text=(None, None),
    non_blocking=False,
    icon=None,
    line_width=None,
    font=None,
    no_titlebar=False,
    grab_anywhere=False,
    keep_on_top=False,
    location=(None, None))
</code></pre>

<p>Parameter Descriptions:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>Any</td>
<td>*args</td>
<td>Variable number of your arguments. Load up the call with stuff to see!</td>
</tr>
<tr>
<td>str</td>
<td>title</td>
<td>Optional title for the window. If none provided, the first arg will be used instead.</td>
</tr>
<tr>
<td>Tuple[str, str]</td>
<td>button_color</td>
<td>Color of the buttons shown (text color, button color)</td>
</tr>
<tr>
<td>str</td>
<td>background_color</td>
<td>Window's background color</td>
</tr>
<tr>
<td>str</td>
<td>text_color</td>
<td>text color</td>
</tr>
<tr>
<td>int</td>
<td>button_type</td>
<td>NOT USER SET! Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). There are many Popup functions and they call Popup, changing this parameter to get the desired effect.</td>
</tr>
<tr>
<td>bool</td>
<td>auto_close</td>
<td>If True the window will automatically close</td>
</tr>
<tr>
<td>int</td>
<td>auto_close_duration</td>
<td>time in seconds to keep window open before closing it automatically</td>
</tr>
<tr>
<td>Union[Tuple[str, str], str]</td>
<td>custom_text</td>
<td>A string or pair of strings that contain the text to display on the buttons</td>
</tr>
<tr>
<td>bool</td>
<td>non_blocking</td>
<td>If True then will immediately return from the function without waiting for the user's input.</td>
</tr>
<tr>
<td>Union[str, bytes]</td>
<td>icon</td>
<td>icon to display on the window. Same format as a Window call</td>
</tr>
<tr>
<td>int</td>
<td>line_width</td>
<td>Width of lines in characters. Defaults to MESSAGE_BOX_LINE_WIDTH</td>
</tr>
<tr>
<td>Union[str, tuple(font name, size, modifiers]</td>
<td>font</td>
<td>specifies the font family, size, etc</td>
</tr>
<tr>
<td>bool</td>
<td>no_titlebar</td>
<td>If True will not show the frame around the window and the titlebar across the top</td>
</tr>
<tr>
<td>bool</td>
<td>grab_anywhere</td>
<td>If True can grab anywhere to move the window. If no_titlebar is True, grab_anywhere should likely be enabled too</td>
</tr>
<tr>
<td>Tuple[int, int]</td>
<td>location</td>
<td>Location on screen to display the top left corner of window. Defaults to window centered on screen</td>
</tr>
<tr>
<td>Union[str, None]</td>
<td><strong>RETURN</strong></td>
<td>Returns text of the button that was pressed.  None will be returned if user closed window with X</td>
</tr>
</tbody>
</table>
<p>The other output Popups are variations on parameters.  Usually the button_type parameter is the primary one changed.</p>
<p>The choices for button_type are (you should not specify these yourself however):</p>
<pre><code>POPUP_BUTTONS_YES_NO
POPUP_BUTTONS_CANCELLED
POPUP_BUTTONS_ERROR
POPUP_BUTTONS_OK_CANCEL
POPUP_BUTTONS_OK
POPUP_BUTTONS_NO_BUTTONS
</code></pre>

<p><strong>Note that you should not call Popup yourself with different button_types.</strong>  Rely on the Popup function named that sets that value for you.  For example <code>popup_yes_no</code> will set the button type to POPUP_BUTTONS_YES_NO for you.</p>
<h3 id="scrolled-output">Scrolled Output</h3>
<p>There is a scrolled version of Popups should you have a lot of information to display.</p>
<p>Show a scrolled Popup window containing the user's text that was supplied.  Use with as many items to print as you
want, just like a print statement.</p>
<pre><code>popup_scrolled(args=*&lt;1 or N object&gt;,
    title=None,
    button_color=None,
    background_color=None,
    text_color=None,
    yes_no=False,
    auto_close=False,
    auto_close_duration=None,
    size=(None, None),
    location=(None, None),
    non_blocking=False,
    no_titlebar=False,
    grab_anywhere=False,
    keep_on_top=False,
    font=None)
</code></pre>

<p>Parameter Descriptions:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>Any</td>
<td>*args</td>
<td>Variable number of items to display</td>
</tr>
<tr>
<td>str</td>
<td>title</td>
<td>Title to display in the window.</td>
</tr>
<tr>
<td>Tuple[str, str]</td>
<td>button_color</td>
<td>button color (foreground, background)</td>
</tr>
<tr>
<td>bool</td>
<td>yes_no</td>
<td>If True, displays Yes and No buttons instead of Ok</td>
</tr>
<tr>
<td>bool</td>
<td>auto_close</td>
<td>if True window will close itself</td>
</tr>
<tr>
<td>Union[int, float]</td>
<td>auto_close_duration</td>
<td>Older versions only accept int. Time in seconds until window will close</td>
</tr>
<tr>
<td>Tuple[int, int]</td>
<td>size</td>
<td>(w,h) w=characters-wide, h=rows-high</td>
</tr>
<tr>
<td>Tuple[int, int]</td>
<td>location</td>
<td>Location on the screen to place the upper left corner of the window</td>
</tr>
<tr>
<td>bool</td>
<td>non_blocking</td>
<td>if True the call will immediately return rather than waiting on user input</td>
</tr>
<tr>
<td>Union[str, None, TIMEOUT_KEY]</td>
<td><strong>RETURN</strong></td>
<td>Returns text of the button that was pressed.  None will be returned if user closed window with X</td>
</tr>
</tbody>
</table>
<p>Typical usage:</p>
<pre><code class="python">sg.popup_scrolled(my_text)
</code></pre>

<p><img alt="scrolledtextbox 2" src="https://user-images.githubusercontent.com/13696193/43667324-712aa0d4-9745-11e8-83a9-a0d0570d0865.jpg" /></p>
<p>The <code>popup_scrolled</code> will auto-fit the window size to the size of the text.  Specify <code>None</code> in the height field of a <code>size</code> parameter to get auto-sized height. </p>
<p>This call will create a scrolled box 80 characters wide and a height dependent upon the number of lines of text. </p>
<p><code>sg.popup_scrolled(my_text, size=(80, None))</code>  </p>
<p>Note that the default max number of lines before scrolling happens is set to 50. At 50 lines the scrolling will begin. </p>
<p>If <code>non_blocking</code> parameter is set, then  the call will not blocking waiting for the user to close the window.  Execution will immediately return to the user.  Handy when you want to dump out debug info without disrupting the program flow. </p>
<h3 id="non-blocking-popups-popup_no_wait-and-the-non_blocking-parameter">Non-Blocking Popups - popup_no_wait and the non_blocking parameter</h3>
<p>Show Popup window and immediately return (does not block)</p>
<pre><code>popup_no_wait(args=*&lt;1 or N object&gt;,
    title=None,
    button_type=0,
    button_color=None,
    background_color=None,
    text_color=None,
    auto_close=False,
    auto_close_duration=None,
    non_blocking=True,
    icon=None,
    line_width=None,
    font=None,
    no_titlebar=False,
    grab_anywhere=False,
    keep_on_top=False,
    location=(None, None))
</code></pre>

<p>Parameter Descriptions:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>Any</td>
<td>*args</td>
<td>Variable number of items to display</td>
</tr>
<tr>
<td>str</td>
<td>title</td>
<td>Title to display in the window.</td>
</tr>
<tr>
<td>int</td>
<td>button_type</td>
<td>Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK).</td>
</tr>
<tr>
<td>Tuple[str, str]</td>
<td>button_color</td>
<td>button color (foreground, background)</td>
</tr>
<tr>
<td>str</td>
<td>background_color</td>
<td>color of background</td>
</tr>
<tr>
<td>str</td>
<td>text_color</td>
<td>color of the text</td>
</tr>
<tr>
<td>bool</td>
<td>auto_close</td>
<td>if True window will close itself</td>
</tr>
<tr>
<td>Union[int, float]</td>
<td>auto_close_duration</td>
<td>Older versions only accept int. Time in seconds until window will close</td>
</tr>
<tr>
<td>bool</td>
<td>non_blocking</td>
<td>if True the call will immediately return rather than waiting on user input</td>
</tr>
<tr>
<td>Union[bytes, str]</td>
<td>icon</td>
<td>filename or base64 string to be used for the window's icon</td>
</tr>
<tr>
<td>int</td>
<td>line_width</td>
<td>Width of lines in characters</td>
</tr>
<tr>
<td>Union[str, Tuple[str, int]]</td>
<td>font</td>
<td>specifies the font family, size, etc</td>
</tr>
<tr>
<td>bool</td>
<td>no_titlebar</td>
<td>If True no titlebar will be shown</td>
</tr>
<tr>
<td>bool</td>
<td>grab_anywhere</td>
<td>If True: can grab anywhere to move the window (Default = False)</td>
</tr>
<tr>
<td>Tuple[int, int]</td>
<td>location</td>
<td>Location of upper left corner of the window</td>
</tr>
</tbody>
</table>
<p>The <code>popup</code> call <code>popup_no_wait</code> or <code>popup_non_blocking</code> will create a popup window and then immediately return control back to you.  You can turn other popup calls into non-blocking popups if they have a <code>non_blocking</code> parameter.  Setting <code>non_blocking</code> to True will cause the function to return immediately rather than waiting for the window to be closed.</p>
<p>This function is very handy for when you're <strong>debugging</strong> and want to display something as output but don't want to change the programs's overall timing by blocking.  Think of it like a <code>print</code> statement. There are no return values on one of these Popups. </p>
<h3 id="popup-parameter-combinations">Popup Parameter Combinations</h3>
<p>So that you don't have to specify a potentially long list common parameters there are a number of popup functions that set combinations of parameters.  For example <code>popup_quick_message</code> will show a non-blocking popup that autocloses and does not have a titlebar.  You could achieve this same end result using the plain <code>popup</code> call.</p>
<h2 id="popup-input">Popup Input</h2>
<p>There are Popup calls for single-item inputs. These follow the pattern of <code>popup_get</code> followed by the type of item to get.  There are 3 of these input Popups to choose from, each with settings enabling customization. </p>
<ul>
<li><code>popup_get_text</code> - get a single line of text</li>
<li><code>popup_get_file</code> - get a filename</li>
<li><code>popup_get_folder</code> - get a folder name</li>
</ul>
<p>Use these Popups instead of making  a custom window to get one data value, call the Popup input function to get the item from the user.  If you find the parameters are unable to create the kind of window you are looking for, then it's time for you to create your own window.</p>
<h3 id="popup_get_text">popup_get_text</h3>
<p>Use this Popup to get a line of text from the user.</p>
<p>Display Popup with text entry field. Returns the text entered or None if closed / cancelled</p>
<pre><code>popup_get_text(message,
    title=None,
    default_text=&quot;&quot;,
    password_char=&quot;&quot;,
    size=(None, None),
    button_color=None,
    background_color=None,
    text_color=None,
    icon=None,
    font=None,
    no_titlebar=False,
    grab_anywhere=False,
    keep_on_top=False,
    location=(None, None))
</code></pre>

<p>Parameter Descriptions:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>str</td>
<td>message</td>
<td>(str) message displayed to user</td>
</tr>
<tr>
<td>str</td>
<td>title</td>
<td>(str) Window title</td>
</tr>
<tr>
<td>str</td>
<td>default_text</td>
<td>(str) default value to put into input area</td>
</tr>
<tr>
<td>str</td>
<td>password_char</td>
<td>(str) character to be shown instead of actually typed characters</td>
</tr>
<tr>
<td>Tuple[int, int]</td>
<td>size</td>
<td>(width, height) of the InputText Element</td>
</tr>
<tr>
<td>Tuple[str, str]</td>
<td>button_color</td>
<td>Color of the button (text, background)</td>
</tr>
<tr>
<td>str</td>
<td>background_color</td>
<td>(str) background color of the entire window</td>
</tr>
<tr>
<td>str</td>
<td>text_color</td>
<td>(str) color of the message text</td>
</tr>
<tr>
<td>Union[bytes, str]</td>
<td>icon</td>
<td>filename or base64 string to be used for the window's icon</td>
</tr>
<tr>
<td>Union[str, Tuple[str, int]]</td>
<td>font</td>
<td>specifies the font family, size, etc</td>
</tr>
<tr>
<td>bool</td>
<td>no_titlebar</td>
<td>(bool) If True no titlebar will be shown</td>
</tr>
<tr>
<td>bool</td>
<td>grab_anywhere</td>
<td>(bool) If True can click and drag anywhere in the window to move the window</td>
</tr>
<tr>
<td>bool</td>
<td>keep_on_top</td>
<td>(bool) If True the window will remain above all current windows</td>
</tr>
<tr>
<td>Tuple[int, int]</td>
<td>location</td>
<td>(x,y) Location on screen to display the upper left corner of window</td>
</tr>
<tr>
<td>Union[str, None]</td>
<td><strong>RETURN</strong></td>
<td>Text entered or None if window was closed or cancel button clicked</td>
</tr>
</tbody>
</table>
<pre><code class="python">import PySimpleGUI as sg
text = sg.popup_get_text('Title', 'Please input something')
sg.popup('Results', 'The value returned from PopupGetText', text)
</code></pre>

<p><img alt="popupgettext" src="https://user-images.githubusercontent.com/13696193/44957281-8721b880-ae9e-11e8-98cd-d06369f4187e.jpg" /></p>
<p><img alt="popup gettext response" src="https://user-images.githubusercontent.com/13696193/44957282-8721b880-ae9e-11e8-84ae-dc8bb30504a0.jpg" /></p>
<h3 id="popup_get_file">popup_get_file</h3>
<p>Gets one or more filenames from the user.  There are options to configure the type of dialog box to show.  Normally an "Open File" dialog box is shown.</p>
<p>Display popup window with text entry field and browse button so that a file can be chosen by user.</p>
<pre><code>popup_get_file(message,
    title=None,
    default_path=&quot;&quot;,
    default_extension=&quot;&quot;,
    save_as=False,
    multiple_files=False,
    file_types=(('ALL Files', '*.*'),),
    no_window=False,
    size=(None, None),
    button_color=None,
    background_color=None,
    text_color=None,
    icon=None,
    font=None,
    no_titlebar=False,
    grab_anywhere=False,
    keep_on_top=False,
    location=(None, None),
    initial_folder=None)
</code></pre>

<p>Parameter Descriptions:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>str</td>
<td>message</td>
<td>message displayed to user</td>
</tr>
<tr>
<td>str</td>
<td>title</td>
<td>Window title</td>
</tr>
<tr>
<td>str</td>
<td>default_path</td>
<td>path to display to user as starting point (filled into the input field)</td>
</tr>
<tr>
<td>str</td>
<td>default_extension</td>
<td>If no extension entered by user, add this to filename (only used in saveas dialogs)</td>
</tr>
<tr>
<td>bool</td>
<td>save_as</td>
<td>if True, the "save as" dialog is shown which will verify before overwriting</td>
</tr>
<tr>
<td>bool</td>
<td>multiple_files</td>
<td>if True, then allows multiple files to be selected that are returned with ';' between each filename</td>
</tr>
<tr>
<td>Tuple[Tuple[str,str]]</td>
<td>file_types</td>
<td>List of extensions to show using wildcards. All files (the default) = (("ALL Files", "<em>.</em>"),)</td>
</tr>
<tr>
<td>bool</td>
<td>no_window</td>
<td>if True, no PySimpleGUI window will be shown. Instead just the tkinter dialog is shown</td>
</tr>
<tr>
<td>Tuple[int, int]</td>
<td>size</td>
<td>(width, height) of the InputText Element</td>
</tr>
<tr>
<td>Tuple[str, str]</td>
<td>button_color</td>
<td>Color of the button (text, background)</td>
</tr>
<tr>
<td>str</td>
<td>background_color</td>
<td>background color of the entire window</td>
</tr>
<tr>
<td>str</td>
<td>text_color</td>
<td>color of the text</td>
</tr>
<tr>
<td>Union[bytes, str]</td>
<td>icon</td>
<td>filename or base64 string to be used for the window's icon</td>
</tr>
<tr>
<td>Union[str, Tuple[str, int]]</td>
<td>font</td>
<td>specifies the font family, size, etc</td>
</tr>
<tr>
<td>bool</td>
<td>no_titlebar</td>
<td>If True no titlebar will be shown</td>
</tr>
<tr>
<td>bool</td>
<td>grab_anywhere</td>
<td>If True: can grab anywhere to move the window (Default = False)</td>
</tr>
<tr>
<td>bool</td>
<td>keep_on_top</td>
<td>If True the window will remain above all current windows</td>
</tr>
<tr>
<td>Tuple[int, int]</td>
<td>location</td>
<td>Location of upper left corner of the window</td>
</tr>
<tr>
<td>str</td>
<td>initial_folder</td>
<td>location in filesystem to begin browsing</td>
</tr>
<tr>
<td>Union[str, None]</td>
<td><strong>RETURN</strong></td>
<td>string representing the file(s) chosen, None if cancelled or window closed with X</td>
</tr>
</tbody>
</table>
<p>If configured as an Open File Popup then (save_as is not True)  the dialog box will look like this. </p>
<p><img alt="snag-0060" src="https://user-images.githubusercontent.com/13696193/46761050-9831c680-cca1-11e8-8de9-68b15efe2c46.jpg" /></p>
<p>If you set the parameter save_As to True, then the dialog box looks like this:</p>
<p><img alt="snag-0061" src="https://user-images.githubusercontent.com/13696193/46761330-2b6afc00-cca2-11e8-953b-f6b5c5ce57f5.jpg" /></p>
<p>If you choose a filename that already exists, you'll get a warning popup box asking if it's OK.  You can also specify a file that doesn't exist.  With an "Open" dialog box you cannot choose a non-existing file.</p>
<p>A typical call produces this window.</p>
<pre><code class="python">text = sg.popup_get_file('Please enter a file name')
sg.popup('Results', 'The value returned from popup_get_file', text)
</code></pre>

<p><img alt="popupgetfile" src="https://user-images.githubusercontent.com/13696193/44957857-2fd31680-aea5-11e8-8eb7-f6b91c202cc8.jpg" /></p>
<h3 id="popup_get_folder">popup_get_folder</h3>
<p>The window created to get a folder name looks the same as the get a file name.  The difference is in what the browse button does.  <code>popup_get_file</code> shows an Open File dialog box while <code>popup_get_folder</code>  shows an Open Folder dialog box.</p>
<p>Display popup with text entry field and browse button so that a folder can be chosen.</p>
<pre><code>popup_get_folder(message,
    title=None,
    default_path=&quot;&quot;,
    no_window=False,
    size=(None, None),
    button_color=None,
    background_color=None,
    text_color=None,
    icon=None,
    font=None,
    no_titlebar=False,
    grab_anywhere=False,
    keep_on_top=False,
    location=(None, None),
    initial_folder=None)
</code></pre>

<p>Parameter Descriptions:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>str</td>
<td>message</td>
<td>message displayed to user</td>
</tr>
<tr>
<td>str</td>
<td>title</td>
<td>Window title</td>
</tr>
<tr>
<td>str</td>
<td>default_path</td>
<td>path to display to user as starting point (filled into the input field)</td>
</tr>
<tr>
<td>bool</td>
<td>no_window</td>
<td>if True, no PySimpleGUI window will be shown. Instead just the tkinter dialog is shown</td>
</tr>
<tr>
<td>Tuple[int, int]</td>
<td>size</td>
<td>(width, height) of the InputText Element</td>
</tr>
<tr>
<td>Tuple[str, str]</td>
<td>button_color</td>
<td>button color (foreground, background)</td>
</tr>
<tr>
<td>str</td>
<td>background_color</td>
<td>color of background</td>
</tr>
<tr>
<td>str</td>
<td>text_color</td>
<td>color of the text</td>
</tr>
<tr>
<td>Union[bytes, str]</td>
<td>icon</td>
<td>filename or base64 string to be used for the window's icon</td>
</tr>
<tr>
<td>Union[str, Tuple[str, int]]</td>
<td>font</td>
<td>specifies the font family, size, etc</td>
</tr>
<tr>
<td>bool</td>
<td>no_titlebar</td>
<td>If True no titlebar will be shown</td>
</tr>
<tr>
<td>bool</td>
<td>grab_anywhere</td>
<td>If True: can grab anywhere to move the window (Default = False)</td>
</tr>
<tr>
<td>bool</td>
<td>keep_on_top</td>
<td>If True the window will remain above all current windows</td>
</tr>
<tr>
<td>Tuple[int, int]</td>
<td>location</td>
<td>Location of upper left corner of the window</td>
</tr>
<tr>
<td>str</td>
<td>initial_folder</td>
<td>location in filesystem to begin browsing</td>
</tr>
<tr>
<td>Union[str, None]</td>
<td><strong>RETURN</strong></td>
<td>string representing the path chosen, None if cancelled or window closed with X</td>
</tr>
</tbody>
</table>
<p>This is a typical call</p>
<pre><code class="python">    text = sg.popup_get_folder('Please enter a folder name')
    sg.popup('Results', 'The value returned from popup_get_folder', text)
</code></pre>

<p><img alt="popupgetfolder" src="https://user-images.githubusercontent.com/13696193/44957861-45484080-aea5-11e8-926c-cf607a45251c.jpg" /></p>
<h3 id="popup_animated">popup_animated</h3>
<p><img alt="ring" src="https://user-images.githubusercontent.com/13696193/51296743-6ee4ad00-19eb-11e9-91f5-cd8086ad1b50.gif" /></p>
<p>The animated Popup enables you to easily display a "loading" style animation specified through a GIF file that is either stored in a file or a base64 variable.</p>
<p>Show animation one frame at a time.  This function has its own internal clocking meaning you can call it at any frequency
 and the rate the frames of video is shown remains constant.  Maybe your frames update every 30 ms but your
 event loop is running every 10 ms.  You don't have to worry about delaying, just call it every time through the
 loop.</p>
<pre><code>popup_animated(image_source,
    message=None,
    background_color=None,
    text_color=None,
    font=None,
    no_titlebar=True,
    grab_anywhere=True,
    keep_on_top=True,
    location=(None, None),
    alpha_channel=None,
    time_between_frames=0,
    transparent_color=None,
    title=&quot;&quot;,
    icon=None)
</code></pre>

<p>Parameter Descriptions:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>Union[str, bytes]</td>
<td>image_source</td>
<td>Either a filename or a base64 string.</td>
</tr>
<tr>
<td>str</td>
<td>message</td>
<td>An optional message to be shown with the animation</td>
</tr>
<tr>
<td>str</td>
<td>background_color</td>
<td>color of background</td>
</tr>
<tr>
<td>str</td>
<td>text_color</td>
<td>color of the text</td>
</tr>
<tr>
<td>Union[str, tuple]</td>
<td>font</td>
<td>specifies the font family, size, etc</td>
</tr>
<tr>
<td>bool</td>
<td>no_titlebar</td>
<td>If True then the titlebar and window frame will not be shown</td>
</tr>
<tr>
<td>bool</td>
<td>grab_anywhere</td>
<td>If True then you can move the window just clicking anywhere on window, hold and drag</td>
</tr>
<tr>
<td>bool</td>
<td>keep_on_top</td>
<td>If True then Window will remain on top of all other windows currently shownn</td>
</tr>
<tr>
<td>(int, int)</td>
<td>location</td>
<td>(x,y) location on the screen to place the top left corner of your window. Default is to center on screen</td>
</tr>
<tr>
<td>float</td>
<td>alpha_channel</td>
<td>Window transparency 0 = invisible 1 = completely visible. Values between are see through</td>
</tr>
<tr>
<td>int</td>
<td>time_between_frames</td>
<td>Amount of time in milliseconds between each frame</td>
</tr>
<tr>
<td>str</td>
<td>transparent_color</td>
<td>This color will be completely see-through in your window. Can even click through</td>
</tr>
<tr>
<td>str</td>
<td>title</td>
<td>Title that will be shown on the window</td>
</tr>
<tr>
<td>str</td>
<td>icon</td>
<td>Same as Window icon parameter. Can be either a filename or Base64 value. For Windows if filename, it MUST be ICO format. For Linux, must NOT be ICO</td>
</tr>
</tbody>
</table>
<p><strong><em>To close animated popups</em></strong>, call PopupAnimated with <code>image_source=None</code>.  This will close all of the currently open PopupAnimated windows.</p>
<h1 id="progress-meters">Progress Meters!</h1>
<p>We all have loops in our code.  'Isn't it joyful waiting, watching a counter scrolling past in a text window?  How about one line of code to get a progress meter, that contains statistics about your code?</p>
<pre><code>one_line_progress_meter(title,
    current_value,
    max_value,
    key,
    args=*&lt;1 or N object&gt;,
    orientation=&quot;v&quot;,
    bar_color=(None, None),
    button_color=None,
    size=(20, 20),
    border_width=None,
    grab_anywhere=False,
    no_titlebar=False)
</code></pre>

<p>Parameter Descriptions:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>str</td>
<td>title</td>
<td>text to display in eleemnt</td>
</tr>
<tr>
<td>int</td>
<td>current_value</td>
<td>current value</td>
</tr>
<tr>
<td>int</td>
<td>max_value</td>
<td>max value of QuickMeter</td>
</tr>
<tr>
<td>Union[str, int, tuple]</td>
<td>key</td>
<td>Used with window.FindElement and with return values to uniquely identify this element</td>
</tr>
<tr>
<td>Any</td>
<td>*args</td>
<td>stuff to output</td>
</tr>
<tr>
<td>str</td>
<td>orientation</td>
<td>'horizontal' or 'vertical' ('h' or 'v' work) (Default value = 'vertical' / 'v')</td>
</tr>
<tr>
<td>Tuple(str, str)</td>
<td>bar_color</td>
<td>color of a bar line</td>
</tr>
<tr>
<td>Tuple[str, str]</td>
<td>button_color</td>
<td>button color (foreground, background)</td>
</tr>
<tr>
<td>Tuple[int, int]</td>
<td>size</td>
<td>(w,h) w=characters-wide, h=rows-high (Default value = DEFAULT_PROGRESS_BAR_SIZE)</td>
</tr>
<tr>
<td>int</td>
<td>border_width</td>
<td>width of border around element</td>
</tr>
<tr>
<td>bool</td>
<td>grab_anywhere</td>
<td>If True: can grab anywhere to move the window (Default = False)</td>
</tr>
<tr>
<td>bool</td>
<td>no_titlebar</td>
<td>If True: no titlebar will be shown on the window</td>
</tr>
<tr>
<td>(bool)</td>
<td><strong>RETURN</strong></td>
<td>True if updated successfully. False if user closed the meter with the X or Cancel button</td>
</tr>
</tbody>
</table>
<p>Here's the one-line Progress Meter in action!</p>
<pre><code class="python">for i in range(1,10000):
    sg.one_line_progress_meter('My Meter', i+1, 10000, 'key','Optional message')
</code></pre>

<p>That line of code resulted in this window popping up and updating.</p>
<p><img alt="preogress meter" src="https://user-images.githubusercontent.com/13696193/43667625-d47da702-9746-11e8-91e6-e5177883abae.jpg" /></p>
<p>A meter AND fun statistics to watch while your machine grinds away, all for the price of 1 line of code.
With a little trickery you can provide a way to break out of your loop using the Progress Meter window.  The cancel button results in a <code>False</code> return value from <code>one_line_progress_meter</code>.  It normally returns <code>True</code>.</p>
<p><strong><em>Be sure and add one to your loop counter</em></strong> so that your counter goes from 1 to the max value.  If you do not add one, your counter will never hit the max value.  Instead it will go from 0 to max-1.</p>
<h1 id="debug-output-easy_print-print-eprint">Debug Output (easy_print = Print = eprint)</h1>
<p>Another call in the 'Easy' families of APIs is <code>EasyPrint</code>.  As is with other commonly used PySimpleGUI calls, there are other names for the same call.  You can use <code>Print</code> or <code>eprint</code> in addition to <code>EasyPrint</code>.  They all do the same thing, output to a debug window.  If the debug window isn't open, then the first call will open it.  No need to do anything but stick an 'sg.Print' call in your code. You can even replace your 'print' calls with calls to EasyPrint by simply sticking the statement</p>
<pre><code class="python">print = sg.Print
</code></pre>

<p>at the top of your code.</p>
<p><code>Print</code> is one of the better ones to use as it's easy to remember.   It is simply <code>print</code> with a capital P. <code>sg.Print('this will go to the debug window')</code></p>
<pre><code class="python">import PySimpleGUI as sg

for i in range(100):
    sg.Print(i)
</code></pre>

<p><img alt="snap0125" src="https://user-images.githubusercontent.com/13696193/43114979-a696189e-8ecf-11e8-83c7-473fcf0ccc66.jpg" /></p>
<p>Or if you didn't want to change your code:</p>
<pre><code class="python">import PySimpleGUI as sg

print=sg.Print
for i in range(100):
    print(i)
</code></pre>

<p>Just like the standard print call, <code>easy_print</code> supports the <code>sep</code> and <code>end</code> keyword arguments.  Other names that can be used to call <code>easy_print</code> include <code>Print</code>, <code>eprint</code>,   If you want to close the window, call the function <code>easy_print_close</code>.</p>
<p>You can change the size of the debug window using the <code>set_options</code> call with the <code>debug_win_size</code> parameter.</p>
<p>There is an option to tell PySimpleGUI to reroute all of your stdout and stderr output to this window.  To do so call easy_print with the parameter <code>do_not_reroute_stdout</code> set to <code>False</code>.  After calling it once with this parameter set to True, all future calls to a normal <code>print</code> will go to the debug window.</p>
<p>If you close the debug window it will re-open the next time you Print to it.  If you wish to close the window using your code, then you can call either <code>easy_print_close()</code> or <code>PrintClose()</code></p>
<h3 id="printing-to-multiline-elements">Printing To Multiline Elements</h3>
<p>Another technique for outputting information that you would normally print is to use the function <code>Multiline.print</code>.  You'll find it discussed further into this document.  The basic idea is that you can easily modify your normal <code>print</code> calls to route your printed information to your window.</p>
<hr />
<h1 id="custom-window-api-calls-your-first-window">Custom window API Calls  (Your First window)</h1>
<p>This is the FUN part of the programming of this GUI.  In order to really get the most out of the API, you should be using an IDE that supports auto complete or will show you the definition of the function.  This will make customizing go  smoother.</p>
<p>This first section on custom windows is for your typical, blocking, non-persistent window.  By this I mean, when you "show" the window, the function will not return until the user has clicked a button or closed the window with an X.</p>
<p>Two other types of windows exist.
1. Persistent window - the <code>Window.read()</code> method returns and the window continues to be visible.  This is good for applications like a chat window or a timer or anything that stays active on the screen for a while.
2. Asynchronous window - the trickiest of the lot. Great care must be exercised.  Examples are an MP3 player or status dashboard.  Async windows are updated (refreshed) on a periodic basis.  You can spot them easily as they will have a <code>timeout</code> parameter on the call to read.     <code>event, values = window.read(timeout=100)</code></p>
<p>It's both not enjoyable nor helpful to immediately jump into tweaking each and every little thing available to you.  Make some simple windows.  Use the Cookbook and the Demo Programs as a way to learn and as a "starting point".</p>
<h2 id="the-window-designer">The window Designer</h2>
<p>The good news to newcomers to GUI programming is that PySimpleGUI has a window designer.  Better yet, the window designer requires no training, no downloads, and everyone knows how to use it.</p>
<p><img alt="gui0_1" src="https://user-images.githubusercontent.com/13696193/44159598-e2257400-a085-11e8-9b02-343e72cc75c3.JPG" /></p>
<p>It's a manual process, but if you follow the instructions, it will take only a minute to do and the result will be a nice looking GUI.  The steps you'll take are:
1. Sketch your GUI on paper
2. Divide your GUI up into rows
3. Label each Element with the Element name
4. Write your Python code using the labels as pseudo-code</p>
<p>Let's take a couple of examples.</p>
<p><strong>Enter a number</strong>.... Popular beginner programs are often based on a game or logic puzzle that requires the user to enter something, like a number.  The "high-low" answer game comes to mind where you try to guess the number based on high or low tips.</p>
<p><strong>Step 1- Sketch the GUI</strong>
<img alt="gui1_1" src="https://user-images.githubusercontent.com/13696193/44160127-6a584900-a087-11e8-8fec-09099a8e16f6.JPG" /></p>
<p><strong>Step 2 - Divide into rows</strong></p>
<p><img alt="gui2_1" src="https://user-images.githubusercontent.com/13696193/44160128-6a584900-a087-11e8-9973-af866fb94c56.JPG" /></p>
<p>Step 3 - Label elements</p>
<p><img alt="gui6_1" src="https://user-images.githubusercontent.com/13696193/44160116-64626800-a087-11e8-8b57-671c0461b508.JPG" /></p>
<p>Step 4 - Write the code
The code we're writing is the layout of the GUI itself.  This tutorial only focuses on getting the window code written, not the stuff to display it, get results.</p>
<p>We have only 1 element on the first row, some text.  Rows are written as a "list of elements", so we'll need [  ] to make a list.  Here's the code for row 1</p>
<pre><code>[ sg.Text('Enter a number') ]
</code></pre>

<p>Row 2 has 1 elements, an input field.</p>
<pre><code>[ sg.Input() ]
</code></pre>

<p>Row 3 has an OK button</p>
<pre><code>[ sg.OK() ]
</code></pre>

<p>Now that we've got the 3 rows defined, they are put into a list that represents the entire window.</p>
<pre><code>layout = [ [sg.Text('Enter a Number')],
           [sg.Input()],
           [sg.OK()] ]
</code></pre>

<p>Finally we can put it all together into a program that will display our window.</p>
<pre><code class="python">import PySimpleGUI as sg

layout = [[sg.Text('Enter a Number')],
          [sg.Input()],
          [sg.OK()] ]

window = sg.Window('Enter a number example', layout)

event, values = window.read()

window.close()

sg.Popup(event, values[0])
</code></pre>

<p>Your call to <code>read</code> will normally return a dictionary, but will "look like a list" in how you access it.  The first input field will be entry 0, the next one is 1, etc..  Later you'll learn about the <code>key</code> parameter which allows you to use your own values to identify elements instead of them being numbered for you.</p>
<h3 id="example-2-get-a-filename">Example 2 - Get a filename</h3>
<p>Let's say you've got a utility you've written that operates on some input file and you're ready to use a GUI to enter than filename rather than the command line.  Follow the same steps as the previous example - draw your window on paper, break it up into rows, label the elements.</p>
<p><img alt="gui4_1" src="https://user-images.githubusercontent.com/13696193/44160132-6a584900-a087-11e8-862f-7d791a67ee5d.JPG" />
<img alt="gui5_1" src="https://user-images.githubusercontent.com/13696193/44160133-6af0df80-a087-11e8-9dec-bb4d4c59393d.JPG" /></p>
<p>Writing the code for this one is just as straightforward.  There is one tricky thing, that browse for a file button.  Thankfully PySimpleGUI takes care of associating it with the input field next to it.  As a result, the code looks almost exactly like the window on the paper.</p>
<pre><code class="python">import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Filename')],
            [sg.Input(), sg.FileBrowse()],
            [sg.OK(), sg.Cancel()] ]

window = sg.Window('Get filename example', layout)
event, values = window.read()
window.close()

sg.Popup(event, values[0])
</code></pre>

<p>Read on for detailed instructions on the calls that show the window and return your results.</p>
<h1 id="copy-these-design-patterns">Copy these design patterns!</h1>
<p>All of your PySimpleGUI programs will utilize one of these 2 design patterns depending on the type of window you're implementing.</p>
<p>Beginning in release 4.19.0 the constant WIN_CLOSED replaced using <code>None</code> as the event signaling that a window was closed.</p>
<h2 id="pattern-1-a-one-shot-window-read-a-window-one-time-then-close-it">Pattern 1 A - "One-shot Window" - Read a window one time then close it</h2>
<p>This will be the most common pattern you'll follow if you are not using an "event loop" (not reading the window multiple times).  The window is read and closed.</p>
<p>The input fields in your window will be returned to you as a dictionary (syntactically it looks just like a list lookup)</p>
<pre><code class="python">import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('SHA-1 and SHA-256 Hashes for the file')],
                 [sg.InputText(), sg.FileBrowse()],
                 [sg.Submit(), sg.Cancel()]]

window = sg.Window('SHA-1 &amp; 256 Hash', layout)

event, values = window.read()
window.close()

source_filename = values[0]     # the first input element is values[0]
</code></pre>

<h2 id="pattern-1-b-one-shot-window-read-a-window-one-time-then-close-it-compact-format">Pattern 1 B - "One-shot Window" - Read a window one time then close it (compact format)</h2>
<p>Same as Pattern 1, but done in a highly compact way.  This example uses the <code>close</code> parameter in <code>window.read</code> to automatically close the window as part of the read operation (new in version 4.16.0).  This enables you to write a single line of code that will create, display, gather input and close a window.  It's really powerful stuff!</p>
<pre><code class="python">import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

event, values  = sg.Window('SHA-1 &amp; 256 Hash', [[sg.Text('SHA-1 and SHA-256 Hashes for the file')],
                        [sg.InputText(), sg.FileBrowse()],
                        [sg.Submit(), sg.Cancel()]]).read(close=True)

source_filename = values[0]     # the first input element is values[0]
</code></pre>

<h2 id="pattern-2-a-persistent-window-multiple-reads-using-an-event-loop">Pattern 2 A - Persistent window (multiple reads using an event loop)</h2>
<p>Some of the more advanced programs operate with the window remaining visible on the screen.  Input values are collected, but rather than closing the window, it is kept visible acting as a way to both output information to the user and gather input data.</p>
<p>This code will present a window and will print values until the user clicks the exit button or closes window using an X.</p>
<pre><code class="python">import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Persistent window')],
          [sg.Input()],
          [sg.Button('Read'), sg.Exit()]]

window = sg.Window('Window that stays open', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    print(event, values)

window.close()
</code></pre>

<h2 id="pattern-2-b-persistent-window-multiple-reads-using-an-event-loop-updates-data-in-window">Pattern 2 B - Persistent window (multiple reads using an event loop + updates data in window)</h2>
<p>This is a slightly more complex, but maybe more realistic version that reads input from the user and displays that input as text in the window.  Your program is likely to be doing both of those activities (input and output) so this will give you a big jump-start.</p>
<p>Do not worry yet what all of these statements mean.   Just copy it so you can begin to play with it, make some changes.  Experiment to see how thing work.</p>
<p>This example introduces the concept of "keys".  Keys are super important in PySimpleGUI as they enable you to identify and work with Elements using names you want to use.  Keys can be (almost) ANYTHING, except <code>None</code> or a List (a tuple is fine).  To access an input element's data that is read in the example below, you will use <code>values['-IN-']</code> instead of <code>values[0]</code> like before.  </p>
<pre><code class="python">import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(12,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # change the &quot;output&quot; element to be the value of &quot;input&quot; element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()
</code></pre>

<h3 id="qt-designer">Qt Designer</h3>
<p>There actually is a PySimpleGUI Window Designer that uses Qt's window designer.  It's outside the scope of this document however.  You'll find the project here: https://github.com/nngogol/PySimpleGUIDesigner</p>
<p>I hope to start using it more soon.  </p>
<h2 id="how-gui-programming-in-python-should-look-at-least-for-beginners">How GUI Programming in Python Should Look?  At least for beginners ?</h2>
<p>While one goal was making it simple to create a GUI another just as important goal was to do it in a Pythonic manner. Whether it achieved these goals is debatable, but it was an attempt just the same.</p>
<p>The key to custom windows in PySimpleGUI is to view windows as ROWS of GUI  Elements.  Each row is specified as a list of these Elements.  Put the rows together and you've got a window.  This means the GUI is defined as a series of Lists, a Pythonic way of looking at things.</p>
<h3 id="lets-dissect-this-little-program">Let's dissect this little program</h3>
<pre><code class="python">import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Rename files or folders')],
      [sg.Text('Source for Folders', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
      [sg.Text('Source for Files ', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
      [sg.Submit(), sg.Cancel()]]

window = sg.Window('Rename Files or Folders', layout)

event, values = window.read()
window.close()
folder_path, file_path = values[0], values[1]       # get the data from the values dictionary
print(folder_path, file_path)
</code></pre>

<h3 id="themes">Themes</h3>
<p><img alt="image" src="https://user-images.githubusercontent.com/46163555/70470775-cd01ff00-1a99-11ea-8b9c-8b33c8880c99.png" /></p>
<p>The first line of code after the import is a call to <code>theme</code>.  </p>
<p>Until Dec 2019 the way a "theme" was specific in PySimpleGUI was to call <code>change_look_and_feel</code>.  That call has been replaced by the more simple function <code>theme</code>.  </p>
<h3 id="window-contents-the-layout">Window contents (The Layout)</h3>
<p>Let's agree the window has 4 rows.</p>
<p>The first row only has <strong>text</strong> that reads <code>Rename files or folders</code></p>
<p>The second row has 3 elements in it.  First the <strong>text</strong> <code>Source for Folders</code>, then an <strong>input</strong> field, then a <strong>browse</strong> button.</p>
<p>Now let's look at how those 2 rows and the other two row from Python code:</p>
<pre><code class="python">layout = [[sg.Text('Rename files or folders')],
          [sg.Text('Source for Folders', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
          [sg.Text('Source for Files ', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
          [sg.Submit(), sg.Cancel()]]
</code></pre>

<p>See how the source code mirrors the layout?  You simply make lists for each row, then submit that table to PySimpleGUI to show and get values from.</p>
<p>And what about those return values?  Most people simply want to show a window, get the input values and do something with them.  So why break up the code into button callbacks, etc., when I simply want my window's input values to be given to me.</p>
<p>For return values the window is scanned from top to bottom, left to right.  Each field that's an input field will occupy a spot in the return values.</p>
<p>In our example window, there are 2 fields, so the return values from this window will be a dictionary with 2 values in it.  Remember, if you do not specify a <code>key</code> when creating an element, one will be created for you.  They are ints starting with 0.  In this example, we have 2 input elements.  They will be addressable as values[0] and values[1]</p>
<h3 id="reading-the-windows-values-also-displays-the-window">"Reading" the window's values (also displays the window)</h3>
<pre><code class="python">event, values = window.read()
folder_path, file_path = values[0], values[1]
</code></pre>

<p>In one statement we both show the window and read the user's inputs.  In the next line of code the <em>dictionary</em> of return values is split into individual variables <code>folder_path</code> and <code>file_path</code>.</p>
<p>Isn't this what a Python programmer looking for a GUI wants? Something easy to work with to get the values and move on to the rest of the program, where the real action is taking place.  Why write pages of GUI code when the same layout can be achieved with PySimpleGUI in 3 or 4 lines of code.  4 lines or 40?  Most would choose 4.</p>
<h2 id="return-values">Return values</h2>
<p>There are 2 return values from a call to <code>Window.read()</code>, an <code>event</code> that caused the <code>Read</code> to return and <code>values</code> a list or dictionary of values.  If there are no elements with keys in the layout, then it will be a list.  However, some elements, like some buttons, have a key automatically added to them.  <strong>It's best to use keys on all of your input type elements.</strong></p>
<h3 id="two-return-values">Two Return Values</h3>
<p>All Window Read calls return 2 values.  By convention a read statement is written:</p>
<pre><code class="python">event, values = window.read()
</code></pre>

<p>You don't HAVE to write your reads in this way. You can name your variables however you want.  But if you want to code them in a way that other programmers using PySimpleGUI are used to, then use this statement.</p>
<h2 id="events">Events</h2>
<p>The first parameter <code>event</code> describes <strong>why</strong> the read completed.  Events are one of these:</p>
<p>For all Windows:</p>
<ul>
<li>Button click</li>
<li>Window closed using X</li>
</ul>
<p>For Windows that have specifically enabled these.  Please see the appropriate section in this document to learn about how to enable these and what the event return values are.</p>
<ul>
<li>Keyboard key press</li>
<li>Mouse wheel up/down</li>
<li>Menu item selected</li>
<li>An Element Changed (slider, spinner, etc.)</li>
<li>A list item was clicked</li>
<li>Return key was pressed in input element</li>
<li>Timeout waiting for event</li>
<li>Text was clicked</li>
<li>Combobox item chosen</li>
<li>Table row selected</li>
<li>etc.</li>
</ul>
<p><strong><em>Most</em></strong> of the time the event will be a button click or the window was closed.  The other Element-specific kinds of events happen when you set <code>enable_events=True</code> when you create the Element.</p>
<h3 id="window-closed-event">Window closed event</h3>
<p>Another convention to follow is the check for windows being closed with an X.  <em>This is an critically important event to catch</em>.  If you don't check for this and you attempt to use the window, your program will crash, or silently consume 100% of your CPU.  Please check for closed window and exit your program gracefully.  Your users will like you for it.  </p>
<p>Close your windows when you're done with them even though exiting the program will also close them.  tkinter can generate an error/warning sometimes if you don't close the window.  For other ports, such as PySimpleGUIWeb, not closing the Window will potentially cause your program to continue to run in the background.</p>
<p>To check for a closed window use this line of code:</p>
<pre><code class="python">if event == sg.WIN_CLOSED:
</code></pre>

<p>Prior to release 4.19.0 you'll find code that checks for <code>None</code> instead of <code>WIN_CLOSED</code>.  These are in fact the same as <code>WIN_CLOSED</code> is <code>None</code>.</p>
<p>Putting it all together we end up with an "event loop" that looks something like this:</p>
<pre><code class="python">while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
window.close()
</code></pre>

<p>You will very often see the examples and demo programs write this check as:</p>
<pre><code class="python">    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
</code></pre>

<p>The keyword <code>in</code> means to check the list of things to see if the <code>event</code> is in that list (or tuple)</p>
<p>This if statement is the same as:</p>
<pre><code class="python">    if event == sg.WIN_CLOSED or event == 'Exit':
        break
</code></pre>

<p>Instead of <code>'Exit'</code> use the name/key of the button you want to exit the window (Cancel, Quit, etc.)</p>
<h3 id="button-click-events">Button Click Events</h3>
<p>By default buttons will always return a click event, or in the case of realtime buttons, a button down event.  You don't have to do anything to enable button clicks.  To disable the events, disable the button using its Update method.</p>
<p>You can enable an additional "Button Modified" event by setting <code>enable_events=True</code> in the Button call.  These events are triggered when something 'writes' to a button, <strong><em>usually</em></strong> it's because the button is listed as a "target" in another button.</p>
<p>The button value from a Read call will be one of 2 values:
1. The Button's text     - Default
2. The Button's key      - If a key is specified</p>
<p>If a button has a key set when it was created, then that key will be returned, regardless of what text is shown on the button.  If no key is set, then the button text is returned.  If no button was clicked, but the window returned anyway, the event value is the key that caused the event to be generated.  For example, if <code>enable_events</code> is set on an <code>Input</code> Element and someone types a character into that <code>Input</code> box, then the event will be the key of the input box.</p>
<h3 id="none-is-returned-when-the-user-clicks-the-x-to-close-a-window"><strong>None is returned when the user clicks the X to close a window.</strong></h3>
<p>If your window has an event loop where it is read over and over, remember to give your user an "out".  You should <strong><em>always check for a None value</em></strong> and it's a good practice to provide an Exit button of some kind. Thus design patterns often resemble this Event Loop:</p>
<pre><code class="python">while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
</code></pre>

<p>Actually, the more "Pythonic version" is used in most Demo Programs and examples.   They do  <strong>exactly</strong> the same thing.</p>
<pre><code class="python">while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Quit'):
        break
</code></pre>

<h3 id="element-events">Element Events</h3>
<p>Some elements are capable of generating events when something happens to them.  For example, when a slider is moved, or list item clicked on or table row clicked on.  These events are not enabled by default.  To enable events for an Element, set the parameter <code>enable_events=True</code>.  This is the same as the older <code>click_submits</code> parameter.  You will find the <code>click_submits</code> parameter still in the function definition.  You can continue to use it. They are the same setting.  An 'or' of the two values is used.  In the future, click_submits will be removed so please migrate your code to using <code>enable_events</code>.</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>events</th>
</tr>
</thead>
<tbody>
<tr>
<td>InputText</td>
<td>any change</td>
</tr>
<tr>
<td>Combo</td>
<td>item chosen</td>
</tr>
<tr>
<td>Listbox</td>
<td>selection changed</td>
</tr>
<tr>
<td>Radio</td>
<td>selection changed</td>
</tr>
<tr>
<td>Checkbox</td>
<td>selection changed</td>
</tr>
<tr>
<td>Spinner</td>
<td>new item selected</td>
</tr>
<tr>
<td>Multiline</td>
<td>any change</td>
</tr>
<tr>
<td>Text</td>
<td>clicked</td>
</tr>
<tr>
<td>Status Bar</td>
<td>clicked</td>
</tr>
<tr>
<td>Graph</td>
<td>clicked</td>
</tr>
<tr>
<td>Graph</td>
<td>dragged</td>
</tr>
<tr>
<td>Graph</td>
<td>drag ended (mouse up)</td>
</tr>
<tr>
<td>TabGroup</td>
<td>tab clicked</td>
</tr>
<tr>
<td>Slider</td>
<td>slider moved</td>
</tr>
<tr>
<td>Table</td>
<td>row selected</td>
</tr>
<tr>
<td>Tree</td>
<td>node selected</td>
</tr>
<tr>
<td>ButtonMenu</td>
<td>menu item chosen</td>
</tr>
<tr>
<td>Right click menu</td>
<td>menu item chosen</td>
</tr>
</tbody>
</table>
<h3 id="other-events">Other Events</h3>
<h4 id="menubar-menu-item-chosen-for-menubar-menus-and-buttonmenu-menus">Menubar menu item chosen for MenuBar menus and ButtonMenu menus</h4>
<p>You will receive the key for the MenuBar and ButtonMenu.  Use that key to read the value in the return values dictionary.  The value shown will be the full text plus key for the menu item chosen.  Remember that you can put keys onto menu items.  You will get the text and the key together as you defined it in the menu
definition.</p>
<h4 id="right-click-menu-item-chosen">Right Click menu item chosen</h4>
<p>Unlike menu bar and button menus, you will directly receive the menu item text and its key value.  You will not do a dictionary lookup to get the value.  It is the event code returned from WindowRead().</p>
<h4 id="windows-keyboard-mouse-scroll-wheel">Windows - keyboard, mouse scroll wheel</h4>
<p>Windows are capable of returning keyboard events.  These are returned as either a single character or a string if it's a special key.  Experiment is all I can say. The mouse scroll wheel events are also strings.  Put a print in your code to see what's returned.</p>
<h4 id="timeouts">Timeouts</h4>
<p>If you set a timeout parameter in your read, then the system TIMEOUT_KEY will be returned.  If you specified your own timeout key in the Read call then that value will be what's returned instead.</p>
<h3 id="the-values-variable-return-values-as-a-list">The <code>values</code> Variable - Return values as a list</h3>
<p>The second parameter from a Read call is either a list or a dictionary of the input fields on the Window.</p>
<p>By default return values are a list of values, one entry for each input field, but for all but the simplest of windows the return values will be a dictionary.  This is because you are likely to use a 'key' in your layout.  When you do, it forces the return values to be a dictionary.</p>
<p>Each of the Elements that are Input Elements will have a value in the list of return values.  If you know for sure that the values will be returned as a list, then you could get clever and unpack directly into variables.</p>
<p>event, (filename, folder1, folder2, should_overwrite) = sg.Window('My title', window_rows).read()</p>
<p>Or, more commonly, you can unpack the return results separately.  This is the preferred method because it works for <strong>both</strong> list and dictionary return values.</p>
<pre><code class="python">event, values = sg.Window('My title', window_rows).read()
event, value_list = window.read()
value1 = value_list[0]
value2 = value_list[1]
     ...
</code></pre>

<p>However, this method isn't good when you have a lot of input fields.  If you insert a new element into your window then you will have to shuffle your unpacks down, modifying each of the statements to reference <code>value_list[x]</code>.</p>
<p>The more common method is to request your values be returned as a dictionary by placing keys on the "important" elements (those that you wish to get values from and want to interact with)</p>
<h3 id="values-variable-return-values-as-a-dictionary"><code>values</code> Variable - Return values as a dictionary</h3>
<p>For those of you that have not encountered a Python dictionary, don't freak out!  Just copy and paste the sample code and modify it. Follow this design pattern and you'll be fine.  And you might learn something along the way.</p>
<p>For windows longer than 3 or 4 fields you will want to use a dictionary to help you organize your return values. In almost all (if not all) of the demo programs you'll find the return values being passed as a dictionary.  It is not a difficult concept to grasp, the syntax is easy to understand, and it makes for very readable code.</p>
<p>The most common window read statement you'll encounter looks something like this:</p>
<p><code>window = sg.Window("My title", layout).read()</code></p>
<p>To use a dictionary, you will need to:
* Mark each input element you wish to be in the dictionary with the keyword <code>key</code>.</p>
<p>If <strong>any</strong> element in the window has a <code>key</code>, then <strong>all</strong> of the return values are returned via a dictionary.  If some elements do not have a key, then they are numbered starting at zero.</p>
<p>Let's take a look at your first dictionary-based window.</p>
<pre><code class="python">import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [
            [sg.Text('Please enter your Name, Address, Phone')],
            [sg.Text('Name', size=(15, 1)), sg.InputText('1', key='-NAME-')],
            [sg.Text('Address', size=(15, 1)), sg.InputText('2', key='-ADDRESS-')],
            [sg.Text('Phone', size=(15, 1)), sg.InputText('3', key='-PHONE-')],
            [sg.Submit(), sg.Cancel()]
            ]

window = sg.Window('Simple data entry window', layout)
event, values = window.read()
window.close()

sg.Popup(event, values, values['-NAME-'], values['-ADDRESS-'], values['-PHONE-'])
</code></pre>

<p>To get the value of an input field, you use whatever value used as the <code>key</code> value as the index value.  Thus to get the value of the name field, it is written as</p>
<pre><code>values['-NAME-']
</code></pre>
<p>Think of the variable values in the same way as you would a list, however, instead of using 0,1,2, to reference each item in the list, use the values of the key.  The Name field in the window above is referenced by <code>values['-NAME-']</code>.</p>
<p>You will find the key field used quite heavily in most PySimpleGUI windows unless the window is very simple.</p>
<p>One convention you'll see in many of the demo programs is keys being named in all caps with an underscores at the beginning and the end.  You don't HAVE to do this... your key value may look like this:
<code>key = '-NAME-'</code></p>
<p>The reason for this naming convention is that when you are scanning the code, these key values jump out at you.   You instantly know it's a key.  Try scanning the code above and see if those keys pop out.
<code>key = '-NAME-'</code></p>
<h2 id="the-event-loop-callback-functions">The Event Loop / Callback Functions</h2>
<p>All GUIs have one thing in common, an "event loop".  Usually the GUI framework runs the event loop for you, but sometimes you want greater control and will run your own event loop.  You often hear the term event loop when discussing embedded systems or on a Raspberry Pi.</p>
<p>With PySimpleGUI if your window will remain open following button clicks, then your code will have an event loop. If your program shows a single "one-shot"  window, collects the data and then has no other GUI interaction, then you don't need an event loop.</p>
<p>There's nothing mysterious about event loops... they are loops where you take care of.... wait for it..... <em>events</em>.  Events are things like button clicks, key strokes, mouse scroll-wheel up/down.</p>
<p>This little program has a typical PySimpleGUI Event Loop.</p>
<p>The anatomy of a PySimpleGUI event loop is as follows, <em>generally speaking</em>.
* The actual "loop" part is a <code>while True</code> loop
* "Read" the event and any input values the window has
* Check to see if window was closed or user wishes to exit
* A series of <code>if event ....</code> statements</p>
<p>Here is a complete, short program to demonstrate each of these concepts.</p>
<pre><code class="python">import PySimpleGUI as sg

sg.ChangeLookAndFeel('GreenTan')

# ------ Menu Definition ------ #
menu_def = [['&amp;File', ['&amp;Open', '&amp;Save', 'E&amp;xit', 'Properties']],
            ['&amp;Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&amp;Help', '&amp;About...'], ]

# ------ Column Definition ------ #
column1 = [[sg.Text('Column 1', background_color='lightblue', justification='center', size=(10, 1))],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('(Almost) All widgets in one Window!', size=(30, 1), justification='center', font=(&quot;Helvetica&quot;, 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Here is some text.... and a place to enter text')],
    [sg.InputText('This is my text')],
    [sg.Frame(layout=[
    [sg.Checkbox('Checkbox', size=(10,1)),  sg.Checkbox('My second checkbox!', default=True)],
    [sg.Radio('My first Radio!     ', &quot;RADIO1&quot;, default=True, size=(10,1)), sg.Radio('My second Radio!', &quot;RADIO1&quot;)]], title='Options',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
    [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
     sg.Multiline(default_text='A second multi-line', size=(35, 3))],
    [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 1)),
     sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
    [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],
    [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
     sg.Frame('Labelled Group',[[
     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25, tick_interval=25),
     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
     sg.Column(column1, background_color='lightblue')]])],
    [sg.Text('_' * 80)],
    [sg.Text('Choose A Folder', size=(35, 1))],
    [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
     sg.InputText('Default Folder'), sg.FolderBrowse()],
    [sg.Submit(tooltip='Click to submit this form'), sg.Cancel()]]

window = sg.Window('Everything bagel', layout, default_element_size=(40, 1), grab_anywhere=False)
event, values = window.read()
window.close()

sg.Popup('Title',
         'The results of the window.',
         'The button clicked was &quot;{}&quot;'.format(event),
         'The values are', values)

</code></pre>

<p>This is a complex window with quite a bit of custom sizing to make things line up well.  This is code you only have to write once.  When looking at the code, remember that what you're seeing is a list of lists.  Each row contains a list of Graphical Elements that are used to create the window.  If you see a pair of square brackets [ ] then you know you're reading one of the rows.  Each row of your GUI will be one of these lists.</p>
<p>This window may look "ugly" to you which is because no effort has been made to make it look nice. It's purely functional. There are 30 Elements in the window.  THIRTY Elements. Considering what it does, it's miraculous or in the least incredibly impressive.  Why?  Because in less than 50 lines of code that window was created, shown, collected the results and showed the results in another window.</p>
<p>50 lines.  It'll take you 50 lines of tkinter or Qt code to get the first 3 elements of the window written, if you can even do that.  </p>
<p>No, let's be clear here... this window will take a massive amount of code using the conventional Python GUI packages.  It's a fact and if you care to prove me wrong, then by ALL means PLEASE do it.  Please write this window using tkinter, Qt, or WxPython and send the code!</p>
<p>Note this window even has a menubar across the top, something easy to miss.</p>
<p><img alt="image" src="https://user-images.githubusercontent.com/13696193/62234730-4295ea00-b399-11e9-9281-5defb91886f6.png" /></p>
<p>Clicking the Submit button caused the window call to return.  The call to Popup resulted in this window.</p>
<p><img alt="image" src="https://user-images.githubusercontent.com/13696193/62234737-47f33480-b399-11e9-8a2c-087cc49868cd.png" /></p>
<p><strong><code>Note, event values can be None</code>*<em>.  The value for <code>event</code> will be the text that is displayed on the button element when it was created or the key for the button.  If the user closed the window using the "X" in the upper right corner of the window, then <code>event</code> will be <code>None</code>.   It is </em></strong>vitally<strong><em> </em></strong>important*** that your code contain the proper checks for None. </p>
<p>For "persistent windows",  <strong>always give your users a way out of the window</strong>.  Otherwise you'll end up  with windows that never properly close.  It's literally 2 lines of code that you'll find in every Demo Program.  While you're at it, make sure a <code>window.close()</code> call is after your event loop so that your window closes for sure.</p>
<p>You can see in the results Popup window that the values returned are a dictionary.  Each input field in the window generates one item in the return values list.  Input fields often return a <code>string</code>. Check Boxes and Radio Buttons return <code>bool</code>.  Sliders return float or perhaps int depending on how you configured it or which port you're using.</p>
<p>If your window has no keys and it has no buttons that are "browse" type of buttons, then it will return values to you as a list instead of a dictionary.  If possible PySimpleGUI tries to return the values as a list to keep things simple.</p>
<p>Note in the list of return values in this example, many of the keys are numbers.  That's because no keys were specified on any of the elements (although one was automatically made for you).  If you don't specify a key for your element, then a number will be sequentially assigned.  For elements that you don't plan on modifying or reading values from, like a Text Element, you can skip adding keys.  For other elements, you'll likely want to add keys so that you can easily access the values and perform operations on them.</p>
<h3 id="operations-that-take-a-long-time">Operations That Take a "Long Time"</h3>
<p>If you're a Windows user you've seen windows show in their title bar "Not Responding" which is soon followed by a Windows popup stating that "Your program has stopped responding".  Well, you too can make that message and popup appear if you so wish!  All you need to do is execute an operation that takes "too long" (i.e. a few seconds) inside your event loop.</p>
<p>You have a couple of options for dealing this with.  If your operation can be broken up into smaller parts, then you can call <code>Window.Refresh()</code> occasionally to avoid this message.  If you're running a loop for example, drop that call in with your other work.  This will keep the GUI happy and Window's won't complain.</p>
<p>If, on the other hand, your operation is not under your control or you are unable to add <code>Refresh</code> calls, then the next option available to you is to move your long operations into a thread.</p>
<p>There are a couple of demo programs available for you to see how to do this.  You basically put your work into a thread.  When the thread is completed, it tells the GUI by sending a message through a queue.  The event loop will run with a timer set to a value that represents how "responsive" you want your GUI to be to the work completing.  </p>
<p>These 2 demo programs are called</p>
<pre><code class="python">Demo_Threaded_Work.py - Best documented.  Single thread used for long task
Demo_Multithreaded_Long_Tasks.py - Similar to above, but with less fancy GUI. Allows you to set amount of time
</code></pre>

<p>These 2 particular demos have a LOT of comments showing you where to add your code, etc..  The amount of code to do this is actually quite small and you don't need to understand the mechanisms used if you simply follow the demo that's been prepared for you.</p>
<h3 id="multithreaded-programs">Multithreaded Programs</h3>
<p>While on the topic of multiple threads, another demo was prepared that shows how you can run multiple threads in your program that all communicate with the event loop in order to display something in the GUI window.  Recall that for PySimpleGUI (at least the tkinter port) you cannot make PySimpleGUI calls in threads other than the main program thread.</p>
<p>The key to these threaded programs is communication from the threads to your event loop.  The mechanism chosen for these demonstrations uses the Python built-in <code>queue</code> module.  The event loop polls these queues to see if something has been sent over from one of the threads to be displayed.</p>
<p>You'll find the demo that shows multiple threads communicating with a single GUI is called:</p>
<pre><code class="python">Demo_Multithreaded_Queued.py
</code></pre>

<p>Once again a <strong>warning</strong> is in order for plain PySimpleGUI (tkinter based) - your GUI must never run as anything but the main program thread and no threads can directly call PySimpleGUI calls.</p>
<hr />
<h1 id="building-custom-windows">Building Custom Windows</h1>
<p>You will find it <strong><em>much easier</em></strong> to write code using PySimpleGUI if you use an IDE such as <strong><em>PyCharm</em></strong>.  The features that show you documentation about the API call you are making will help you determine which settings you want to change, if any.  In PyCharm, two commands are particularly helpful.</p>
<pre><code>Control-Q (when cursor is on function name) brings up a box with the function definition
Control-P (when cursor inside function call "()") shows a list of parameters and their default values
</code></pre>
<h2 id="synchronous-asynchronous-windows">Synchronous / Asynchronous Windows</h2>
<p>The most common use of PySimpleGUI is to display and collect information from the user.  The most straightforward way to do this is using a "blocking" GUI call.  Execution is "blocked" while waiting for the user to close the GUI window/dialog box.</p>
<p>You've already seen a number of examples above that use blocking windows.  You'll know it blocks if the <code>Read</code> call has no timeout parameter.</p>
<p>A blocking Read (one that waits until an event happens) look like this:</p>
<pre><code class="python">event, values = window.read()
</code></pre>

<p>A non-blocking / Async Read call looks like this:</p>
<pre><code class="python">event, values = window.read(timeout=100)
</code></pre>

<p>You can learn more about these async / non-blocking windows toward the end of this document.</p>
<h1 id="themes-automatic-coloring-of-your-windows">Themes - Automatic Coloring of Your Windows</h1>
<p>In Dec 2019 the function <code>change_look_and_feel</code> was replaced by <code>theme</code>.  The concept remains the same, but a new group of function calls makes it a lot easier to manage colors and other settings.</p>
<p>By default the PySimpleGUI color theme is now <code>Dark Blue 3</code>.  Gone are the "system default" gray colors.  If you want your window to be devoid of all colors so that the system chooses the colors (gray) for you, then set the theme to 'SystemDefault1' or <code>Default1</code>.</p>
<p>There are 130 themes available.  You can preview these themes by calling <code>theme_previewer()</code> which will create a LARGE window displaying all of the color themes available.</p>
<p>As of this writing, these are your available themes.</p>
<p><img alt="SNAG-0620" src="https://user-images.githubusercontent.com/46163555/71361827-2a01b880-2562-11ea-9af8-2c264c02c3e8.jpg" /></p>
<h2 id="default-is-dark-blue-3">Default is <code>Dark Blue 3</code></h2>
<p><img alt="image" src="https://user-images.githubusercontent.com/46163555/71362356-cd070200-2563-11ea-9455-9315b9423d7e.png" /></p>
<p>In Dec 2019 the default for all PySimpleGUI windows changed from the system gray with blue buttons to a more complete theme using a grayish blue with white text.  Previously users were nagged into choosing  color theme other than gray.  Now it's done for you instead of nagging you.</p>
<p>If you're struggling with this color theme, then add a call to <code>theme</code> to change it.</p>
<h2 id="theme-name-formula">Theme Name Formula</h2>
<p>Themes names that you specify can be "fuzzy".  The text does not have to match exactly what you see printed.  For example "Dark Blue 3" and "DarkBlue3" and "dark blue 3" all work.</p>
<p>One way to quickly determine the best setting for your window is to simply display your window using a lot of different themes.  Add the line of code to set the theme - <code>theme('Dark Green 1')</code>, run your code, see if you like it, if not, change the theme string to <code>'Dark Green 2'</code> and try again.  Repeat until you find something you like.</p>
<p>The "Formula" for the string is:</p>
<p><code>Dark Color #</code></p>
<p>or</p>
<p><code>Light Color #</code></p>
<p>Color can be Blue, Green, Black, Gray, Purple, Brown, Teal, Red.   The # is optional or can be from 1 to XX.  Some colors have a lot of choices.  There are 13 "Light Brown" choices for example.</p>
<h3 id="system-default-no-colors">"System" Default - No Colors</h3>
<p>If you're bent on having no colors at all in your window, then choose <code>Default 1</code> or <code>System Default 1</code>.</p>
<p>If you want the original PySimpleGUI color scheme of a blue button and everything else gray then you can get that with the theme <code>Default</code> or <code>System Default</code>.</p>
<h2 id="theme-functions">Theme Functions</h2>
<p>The basic theme function call is <code>theme(theme_name)</code>.  This sets the theme.  Calling without a parameter, <code>theme()</code> will return the name of the current theme.</p>
<p>If you want to get or modify any of the theme settings, you can do it with these functions that you will find detailed information about in the function definitions section at the bottom of the document.  Each will return the current value if no parameter is used.</p>
<pre><code class="python">theme_background_color
theme_border_width
theme_button_color
theme_element_background_color
theme_element_text_color
theme_input_background_color
theme_input_text_color
theme_progress_bar_border_width
theme_progress_bar_color
theme_slider_border_width
theme_slider_color
theme_text_color
</code></pre>

<p>These will help you get a list of available choices.</p>
<pre><code class="python">theme_list
theme_previewer
</code></pre>

<h1 id="window-object-beginning-a-window">Window Object - Beginning a window</h1>
<p>The first step is to create the window object using the desired window customizations.  </p>
<p>Note - There is no direct support for "<strong>modal windows</strong>" in PySimpleGUI.  All windows are accessible at all times unless you manually change the windows' settings.</p>
<p><strong>IMPORTANT</strong> - Many of the <code>Window</code> methods require you to either call <code>Window.read</code> or <code>Window.Finalize</code> (or set <code>finalize=True</code> in your <code>Window</code> call) before you call the method. This is because these 2 calls are what actually creates the window using the underlying GUI Framework.  Prior to one of those calls, the methods are likely to crash as they will not yet have their underlying widgets created.</p>
<h3 id="window-location">Window Location</h3>
<p>PySimpleGUI computes the exact center of your window and centers the window on the screen.  If you want to locate your window elsewhere, such as the system default of (0,0), if you have 2 ways of doing this. The first is when the window is created.  Use the <code>location</code> parameter to set where the window.  The second way of doing this is to use the <code>SetOptions</code> call which will set the default window location for all windows in the future.</p>
<h4 id="multiple-monitors-and-linux">Multiple Monitors and Linux</h4>
<p>The auto-centering (default) location for your PySimpleGUI window may not be correct if you have multiple monitors on a Linux system.  On Windows multiple monitors appear to work ok as the primary monitor the tkinter utilizes and reports on.  </p>
<p>Linux users with multiple monitors that have a problem when running with the default location will need to specify the location the window should be placed when creating the window by setting the <code>location</code> parameter.</p>
<h3 id="window-size">Window Size</h3>
<p>You can get your window's size by access the <code>Size</code> property.  The window has to be Read once or Finalized in order for the value to be correct. Note that it's a property, not a call.</p>
<p><code>my_windows_size = window.Size</code></p>
<p>To finalize your window:</p>
<pre><code class="python">window = Window('My Title', layout, finalize=True)
</code></pre>

<h3 id="element-sizes">Element Sizes</h3>
<p>There are multiple ways to set the size of Elements.  They are:</p>
<ol>
<li>The global default size - change using <code>SetOptions</code> function</li>
<li>At the Window level - change using the parameter <code>default_element_size</code> in your call to <code>Window</code></li>
<li>At the Element level - each element has a <code>size</code> parameter</li>
</ol>
<p>Element sizes are measured in characters (there are exceptions).  A Text Element with  <code>size = (20,1)</code> has a size of 20 characters wide by 1 character tall.</p>
<p>The default Element size for PySimpleGUI is <code>(45,1)</code>.</p>
<p>There are a couple of widgets where one of the size values is in pixels rather than characters.  This is true for Progress Meters and Sliders.  The second parameter is the 'height' in pixels.</p>
<h3 id="no-titlebar">No Titlebar</h3>
<p>Should you wish to create cool looking windows that are clean with no windows titlebar, use the no_titlebar option when creating the window.</p>
<p>Be sure an provide your user an "exit" button or they will not be able to close the window!  When no titlebar is enabled, there will be no icon on your taskbar for the window.  Without an exit button you will need to kill via taskmanager... not fun.</p>
<p>Windows with no titlebar rely on the grab anywhere option to be enabled or else you will be unable to move the window.</p>
<p>Windows without a titlebar can be used to easily create a floating launcher.</p>
<p>Linux users!  Note that this setting has side effects for some of the other Elements.  Multi-line input doesn't work at all, for example  So, use with caution.</p>
<p><img alt="floating launcher" src="https://user-images.githubusercontent.com/13696193/45258246-71bafb80-b382-11e8-9f5e-79421e6c00bb.jpg" /></p>
<h3 id="grab-anywhere">Grab Anywhere</h3>
<p>This is a feature unique to PySimpleGUI.</p>
<p>Note - there is a warning message printed out if the user closes a non-blocking window using a button with grab_anywhere enabled.  There is no harm in these messages, but it may be distressing to the user.    Should you wish to enable for a non-blocking window, simply get grab_anywhere = True when you create the window.</p>
<h3 id="always-on-top">Always on top</h3>
<p>To keep a window on top of all other windows on the screen, set keep_on_top = True when the window is created.  This feature makes for floating toolbars that are very helpful and always visible on your desktop.</p>
<h3 id="focus">Focus</h3>
<p>PySimpleGUI will set a default focus location for you.  This generally means the first input field.  You can set the focus to a particular element.  If you are going to set the focus yourself, then you should turn off the automatic focus by setting <code>use_default_focus=False</code> in your Window call.</p>
<h3 id="ttk-buttons">TTK Buttons</h3>
<p>Beginning in release 4.7.0 PySimpleGUI supports both "normal" tk Buttons and ttk Buttons.  This change was needed so that Mac users can use colors on their buttons.  There is a bug that causes tk Buttons to not show text when you attempt to change the button color.  Note that this problem goes away if you install Python from the official Python.org site rather than using Homebrew.  A number of users have switched and are quite happy since even tk Buttons work on the Mac after the switch.</p>
<p>By default Mac users will get ttk Buttons when a Button Element is used.  All other platforms will get a normal tk Button.  There are ways to override this behavior.  One is by using the parameter <code>use_ttk_buttons</code> when you create your window.  If set to True, all buttons will be ttk Buttons in the window.  If set to False, all buttons will be normal tk Buttons.  If not set then the platform or the Button Element determines which is used.</p>
<p>If a system-wide setting is desired, then the default can be set using <code>set_options</code>.  This will affect all windows such as popups and the debug window.</p>
<h3 id="ttk-themes">TTK Themes</h3>
<p>tkinter has a number of "Themes" that can be used with ttk widgets.  In PySimpleGUI these widgets include - Table, Tree, Combobox, Button, ProgressBar, Tabs &amp; TabGroups.  Some elements have a 'theme' parameter but these are no longer used and should be ignored.  The initial release of PySimpleGUI attempted to mix themes in a single window but since have learned this is not possible so instead it is set at the Window or the system level.</p>
<p>If a system-wide setting is desired, then the default can be set using <code>set_options</code>. This will affect all windows such as popups and the debug window.</p>
<p>The ttk theme choices depend on the platform. Linux has a shorter number of selections than Windows.  These are the Windows choices:
'default', 'winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative'</p>
<p>There are constants defined to help you with code completion to determine what your choices are.  Theme constants start with <code>THEME_</code>.  For example, the "clam" theme is <code>THEME_CLAM</code></p>
<p>You're urged to experiment with this setting to determine which you like the most.  They change the ttk-based elements in subtle but still significant ways.</p>
<h2 id="closing-windows">Closing Windows</h2>
<p>When you are completely done with a window, you should close it and then delete it so that the resources, in particular the tkinter resources, are properly cleaned up.</p>
<p>If you wish to do this in 1 line of code, here's your line:</p>
<pre><code class="python">window.close(); del window
</code></pre>

<p>The delete helps with a problem multi-threaded application encounter where tkinter complains that it is being called from the wrong thread (not the program's main thread)</p>
<h2 id="window-methods-that-complete-formation-of-window">Window Methods That Complete Formation of Window</h2>
<p>After you have completed making your layout, stored in a variable called <code>layout</code> in these examples, you will create your window.</p>
<p>The creation part of a window involves 3 steps.</p>
<ol>
<li>Create a <code>Window</code> object</li>
<li>Adding your Layout to the window</li>
<li>Optional - Finalize if want to make changes prior to <code>Read</code> call</li>
</ol>
<p>Over time the PySimpleGUI code has continued to compact, compress, so that as little code as possible will need to be written by the programmer.</p>
<h3 id="the-individual-calls">The Individual Calls</h3>
<p>This is the "long form" as each method is called individually.</p>
<pre><code class="python">window = sg.Window('My Title')
window.layout(layout)
window.finalize()
</code></pre>

<h3 id="chaining-the-calls-the-old-method">Chaining The Calls (the old method)</h3>
<p>The next level  of compression that was done was to chain the calls together into a single line of code.</p>
<pre><code class="python">window = sg.Window('My Title').Layout(layout).finalize()
</code></pre>

<h3 id="using-parameters-instead-of-calls-new-preferred-method">Using Parameters Instead of Calls (New Preferred Method)</h3>
<p>Here's a novel concept, instead of using chaining, something that's foreign to beginners, use parameters to the <code>Window</code> call.  And that is exactly what's happened as of 4.2 of the PySimpleGUI port.</p>
<pre><code class="python">window = sg.Window('My Title', layout, finalize=True)
</code></pre>

<p>Rather than pushing the work onto the user of doing the layout and finalization calls, let the Window initialization code do it for you. Yea, it sounds totally obvious now, but it didn't a few months ago.</p>
<p>This capability has been added to all 4 PySimpleGUI ports but none are on PyPI just yet as there is some runtime required first to make sure nothing truly bad is going to happen.</p>
<p>Call to set the window layout.  Must be called prior to <code>Read</code>.  Most likely "chained" in line with the Window creation.</p>
<pre><code class="python">window = sg.Window('My window title', layout)
</code></pre>

<h4 id="finalize-or-window-parameter-finalizetrue"><code>finalize()</code> or <code>Window</code> parameter <code>finalize=True</code></h4>
<p>Call to force a window to go through the final stages of initialization.  This will cause the tkinter resources to be allocated so that they can then be modified.  This also causes your window to appear.  If you do not want your window to appear when Finalize is called, then set the Alpha to 0 in your window's creation parameters.</p>
<p>If you want to call an element's <code>Update</code> method or call a <code>Graph</code> element's drawing primitives, you <strong><em>must</em></strong> either call <code>Read</code> or <code>Finalize</code> prior to making those calls.</p>
<h4 id="readtimeoutnone-timeout_keytimeout_key">read(timeout=None, timeout_key=TIMEOUT_KEY)</h4>
<p>Read the Window's input values and button clicks in a blocking-fashion</p>
<p>Returns event, values.  Adding a timeout can be achieved by setting timeout=<em>number of milliseconds</em> before the Read times out after which a "timeout event" is returned.  The value of timeout_key will be returned as the event.   If you do not specify a timeout key, then the value <code>TIMEOUT_KEY</code> will be returned.</p>
<p>If you set the timeout = 0, then the Read will immediately return rather than waiting for input or for a timeout.  It's a truly non-blocking "read" of the window.</p>
<h1 id="layouts">Layouts</h1>
<p>While at this point in the documentation you've not been shown very much about each Element available, you should read this section carefully as you can use the techniques you learn in here to build better, shorter, and easier to understand PySimpleGUI code.</p>
<p>If it feels like this layout section is too much too soon, then come back to this section after you're learned about each Element.  <strong>Whatever order you find the least confusing is the best.</strong></p>
<p>While you've not learned about Elements yet, it makes sense for this section to be up front so that you'll have learned how to use the elements prior to learning how each element works.  At this point in your PySimpleGUI education, it is better for you to grasp time efficient ways of working with Elements than what each Element does.  By learning now how to assemble Elements now, you'll have a good model to put the elements you learn into.</p>
<p>There are <em>several</em> aspects of PySimpleGUI that make it more "Pythonic" than other Python GUI SDKs.  One of the areas that is unique to PySimpleGUI is how a window's "layout" is defined, specified or built.  A window's "layout" is simply a list of lists of elements.  As you've already learned, these lists combine to form a complete window.  This method of defining a window is super-powerful because lists are core to the Python language as a whole and thus are very easy to create and manipulate.  </p>
<p>Think about that for a moment and compare/contrast with Qt, tkinter, etc..  With PySimpleGUI the location of your element in a matrix determines where that Element is shown in the window.  It's so <strong><em>simple</em></strong> and that makes it incredibly powerful.  Want to switch a row in your GUI that has text with the one below it that has an input element?  No problem, swap the lines of code and you're done.</p>
<p>Layouts were designed to be visual. The idea is for you to be able to envision how a window will look by simply looking at the layout in the code.  The CODE itself matches what is drawn on the screen.  PySimpleGUI is a cross between straight Python code and a visual GUI designer.</p>
<p>In the process of creating your window, you can manipulate these lists of elements without having an impact on the elements or on your window.  Until you perform a "layout" of the list, they are nothing more than lists containing objects (they just happen to be your window's elements).</p>
<p>Many times your window definition / layout will be a static, straightforward to create.  </p>
<p>However, window layouts are not limited to being one of these statically defined list of Elements.</p>
<h1 id="generated-layouts-for-sure-want-to-read-if-you-have-5-repeating-elementsrows">Generated Layouts (For sure want to read if you have &gt; 5 repeating elements/rows)</h1>
<p>There are 5 specific techniques of generating layouts discussed in this section. They can be used alone or in combination with each other.</p>
<ol>
<li>Layout + Layout concatenation <code>[[A]] + [[B]] = [[A], [B]]</code></li>
<li>Element Addition on Same Row  <code>[[A] + [B]] = [[A, B]]</code></li>
<li>List Comprehension to generate a row <code>[A for x in range(10)] = [A,A,A,A,A...]</code></li>
<li>List Comprehension to generate multiple rows <code>[[A] for x in range(10)] = [[A],[A],...]</code></li>
<li>User Defined Elements / Compound Elements</li>
</ol>
<h2 id="example-list-comprehension-to-concatenate-multiple-rows-to-do-list-example">Example - List Comprehension To Concatenate Multiple Rows - "To Do" List Example</h2>
<p>Let's create a little layout that will be used to make a to-do list using PySimpleGUI.</p>
<h3 id="brute-force">Brute Force</h3>
<pre><code class="python">import PySimpleGUI as sg

layout = [
            [sg.Text('1. '), sg.In(key=1)],
            [sg.Text('2. '), sg.In(key=2)],
            [sg.Text('3. '), sg.In(key=3)],
            [sg.Text('4. '), sg.In(key=4)],
            [sg.Text('5. '), sg.In(key=5)],
            [sg.Button('Save'), sg.Button('Exit')]
         ]

window = sg.Window('To Do List Example', layout)
event, values = window.read()
</code></pre>

<p>The output from this script was this window:</p>
<p><img alt="SNAG-0451" src="https://user-images.githubusercontent.com/46163555/63563849-90cd8180-c530-11e9-80d7-4954b11deebd.jpg" /></p>
<p>Take a moment and look at the code and the window that's generated.  Are you able to look at the layout and envision the Window on the screen?</p>
<h3 id="build-by-concatenating-rows">Build By Concatenating Rows</h3>
<p>The brute force method works great on a list that's 5 items long, but what if your todo list had 40 items on it. THEN what?  Well, that's when we turn to a "generated" layout, a layout that is generated by your code.  Replace the layout= stuff from the previous example with this definition of the layout.</p>
<pre><code class="python">import PySimpleGUI as sg

layout = []
for i in range(1,6):
    layout += [sg.Text(f'{i}. '), sg.In(key=i)],
layout += [[sg.Button('Save'), sg.Button('Exit')]]

window = sg.Window('To Do List Example', layout)
event, values = window.read()
</code></pre>

<p>It produces the exact same window of course.  That's progress.... went from writing out every row of the GUI to generating every row. If we want 48 items as suggested, change the range(1,6) to range(1,48).  Each time through the list another row is added onto the layout.</p>
<h3 id="create-several-rows-using-list-comprehension">Create Several Rows Using List Comprehension</h3>
<p>BUT, we're not done yet!</p>
<p>This is <strong>Python*<em>, we're using lists to build something up, so we should be looking at </em></strong><em>list comprehensions</em>***.  Let's change the <code>for</code> loop into a list comprehension.  Recall that our <code>for</code> loop was used to concatenate 6 rows into a layout.</p>
<pre><code class="python">layout =  [[sg.Text(f'{i}. '), sg.In(key=i)] for i in range(1,6)] 
</code></pre>

<p>Here we've moved the <code>for</code> loop to inside of the list definition (a list comprehension)</p>
<h3 id="concatenating-multiple-rows">Concatenating Multiple Rows</h3>
<p>We have our rows built using the list comprehension, now we just need the buttons.  They can be easily "tacked onto the end" by simple addition.</p>
<pre><code class="python">layout =  [[sg.Text(f'{i}. '), sg.In(key=i)] for i in range(1,6)] 
layout += [[sg.Button('Save'), sg.Button('Exit')]]
</code></pre>

<p>Anytime you have 2 layouts, you can concatenate them by simple addition.  Make sure your layout is a "list of lists" layout.  In the above example, we know the first line is a generated layout of the input rows.  The last line adds onto the layout another layout... note the format being [ [ ] ].</p>
<p>This button definition is an entire layout, making it possible to add to our list comprehension</p>
<p><code>[[sg.Button('Save'), sg.Button('Exit')]]</code></p>
<p>It's quite readable code.  The 2 layouts line up visually quite well.</p>
<p>But let's not stop there with compressing the code.  How about removing that += and instead change the layout into a single line with just a <code>+</code> between the two sets of row.</p>
<p>Doing this concatenation on one line, we end up with this single statement that creates the <strong>entire layout</strong> for the GUI:</p>
<pre><code class="python">layout =  [[sg.Text(f'{i}. '), sg.In(key=i)] for i in range(1,6)] + [[sg.Button('Save'), sg.Button('Exit')]]
</code></pre>

<h3 id="final-to-do-list-program">Final "To Do List" Program</h3>
<p>And here we have our final program... all <strong>4</strong> lines.</p>
<pre><code class="python">import PySimpleGUI as sg

layout  = [[sg.Text(f'{i}. '), sg.In(key=i)] for i in range(1,6)] + [[sg.Button('Save'), sg.Button('Exit')]]

window = sg.Window('To Do List Example', layout)

event, values = window.read()
</code></pre>

<p>If you really wanted to crunch things down, you can make it a 2 line program (an import and 1 line of code) by moving the layout into the call to <code>Window</code></p>
<pre><code class="python">import PySimpleGUI as sg

event, values = sg.Window('To Do List Example', layout=[[sg.Text(f'{i}. '), sg.In(key=i)] for i in range(1,6)] + [[sg.Button('Save'), sg.Button('Exit')]]).read()
</code></pre>

<h2 id="example-list-comprehension-to-build-rows-table-simulation-grid-of-inputs">Example - List Comprehension to Build Rows - Table Simulation - Grid of Inputs</h2>
<p>In this example we're building a "table" that is 4 wide by 10 high using <code>Input</code> elements </p>
<p>The end results we're seeking is something like this:</p>
<pre><code>HEADER 1    HEADER 2    HEADER 3    HEADER 4
INPUT       INPUT       INPUT       INPUT
INPUT       INPUT       INPUT       INPUT
INPUT       INPUT       INPUT       INPUT
INPUT       INPUT       INPUT       INPUT
INPUT       INPUT       INPUT       INPUT
INPUT       INPUT       INPUT       INPUT
INPUT       INPUT       INPUT       INPUT
INPUT       INPUT       INPUT       INPUT
INPUT       INPUT       INPUT       INPUT
INPUT       INPUT       INPUT       INPUT
</code></pre>

<p>Once the code is completed, here is how the result will appear:</p>
<p><img alt="image" src="https://user-images.githubusercontent.com/46163555/63626328-b4480900-c5d0-11e9-9c81-52e3b0516bde.png" /></p>
<p>We're going to be building each row using a list comprehension and we'll build the table by concatenating rows using another list comprehension.  That's a list comprehension that goes across and another list comprehension that goes down the layout, adding one row after another.</p>
<h3 id="building-the-header">Building the Header</h3>
<p>First let's build the header.  There are 2 concepts to notice here:</p>
<pre><code class="python">import PySimpleGUI as sg

headings = ['HEADER 1', 'HEADER 2', 'HEADER 3','HEADER 4']  # the text of the headings
header =  [[sg.Text('  ')] + [sg.Text(h, size=(14,1)) for h in headings]]  # build header layout
</code></pre>

<p>There are 2 things in this code to note
1. The list comprehension that makes the heading elements
2. The spaces added onto the front</p>
<p>Let's start with the headers themselves.</p>
<p>This is the code that makes a row of Text Elements containing the text for the headers.  The result is a list of Text Elements, a row.</p>
<pre><code class="python">[sg.Text(h, size=(14,1)) for h in headings]
</code></pre>

<p>Then we add on a few spaces to shift the headers over so they are centered over their columns.  We do this by simply adding a <code>Text</code> Element onto the front of that list of headings.</p>
<pre><code class="python">header =  [[sg.Text('  ')] + [sg.Text(h, size=(14,1)) for h in headings]]
</code></pre>

<p>This <code>header</code> variable is a layout with 1 row that has a bunch of <code>Text</code> elements with the headings.</p>
<h3 id="building-the-input-elements">Building the Input Elements</h3>
<p>The <code>Input</code> elements are arranged in a grid.  To do this we will be using a double list comprehension.  One will build the row the other will add the rows together to make the grid.  Here's the line of code that does that:</p>
<pre><code class="python">input_rows = [[sg.Input(size=(15,1), pad=(0,0)) for col in range(4)] for row in range(10)]
</code></pre>

<p>This portion of the statement makes a single row of 4 <code>Input</code> Elements</p>
<pre><code class="python">[sg.Input(size=(15,1), pad=(0,0)) for col in range(4)]
</code></pre>

<p>Next we take that list of <code>Input</code> Elements and make as many of them as there are rows, 10 in this case.  We're again using Python's awesome list comprehensions to add these rows together.</p>
<pre><code class="python">input_rows = [[sg.Input(size=(15,1), pad=(0,0)) for col in range(4)] for row in range(10)]
</code></pre>

<p>The first part should look familiar since it was just discussed as being what builds a single row.  To make the matrix, we simply take that single row and create 10 of them, each being a list.</p>
<h3 id="putting-it-all-together">Putting it all together</h3>
<p>Here is our final program that uses simple addition to add the headers onto the top of the input matrix.  To make it more attractive, the color theme is set to 'Dark Brown 1'.</p>
<pre><code class="python">import PySimpleGUI as sg

sg.theme('Dark Brown 1')

headings = ['HEADER 1', 'HEADER 2', 'HEADER 3','HEADER 4']
header =  [[sg.Text('  ')] + [sg.Text(h, size=(14,1)) for h in headings]]

input_rows = [[sg.Input(size=(15,1), pad=(0,0)) for col in range(4)] for row in range(10)]

layout = header + input_rows

window = sg.Window('Table Simulation', layout, font='Courier 12')
event, values = window.read()
</code></pre>

<p><img alt="image" src="https://user-images.githubusercontent.com/46163555/70472374-f7a18700-1a9c-11ea-9cd1-27d386cd9066.png" /></p>
<h2 id="user-defined-elements-compound-elements">User Defined Elements / Compound Elements</h2>
<p>"User Defined Elements" and "Compound Elements" are one or more PySimpleGUI Elements that are wrapped in a function definition. In a layout, they have the appearance of being a custom elements of some type.</p>
<p>User Defined Elements are particularly useful when you set a lot of parameters on an element that you use over and over in your layout.</p>
<h3 id="example-a-grid-of-buttons-for-calculator-app">Example - A Grid of Buttons for Calculator App</h3>
<p>Let's say you're making a calculator application with buttons that have these settings:</p>
<ul>
<li>font = Helvetica 20</li>
<li>size = 5,1</li>
<li>button color = white on blue</li>
</ul>
<p>The code for <strong>one</strong> of these buttons is:</p>
<pre><code class="python">sg.Button('1', button_color=('white', 'blue'), size=(5, 1), font=(&quot;Helvetica&quot;, 20))
</code></pre>

<p>If you have 6 buttons across and 5 down, your layout will have 30 of these lines of text.</p>
<p>One row of these buttons could be written:</p>
<pre><code class="python">    [sg.Button('1', button_color=('white', 'blue'), size=(5, 1), font=(&quot;Helvetica&quot;, 20)),
     sg.Button('2', button_color=('white', 'blue'), size=(5, 1), font=(&quot;Helvetica&quot;, 20)),
     sg.Button('3', button_color=('white', 'blue'), size=(5, 1), font=(&quot;Helvetica&quot;, 20)),
     sg.Button('log', button_color=('white', 'blue'), size=(5, 1), font=(&quot;Helvetica&quot;, 20)),
     sg.Button('ln', button_color=('white', 'blue'), size=(5, 1), font=(&quot;Helvetica&quot;, 20)),
     sg.Button('-', button_color=('white', 'blue'), size=(5, 1), font=(&quot;Helvetica&quot;, 20))],
</code></pre>

<p>By using User Defined Elements, you can significantly shorten your layouts.  Let's call our element <code>CBtn</code>.  It would be written like this:</p>
<pre><code class="python">def CBtn(button_text):
    return sg.Button(button_text, button_color=('white', 'blue'), size=(5, 1), font=(&quot;Helvetica&quot;, 20))
</code></pre>

<p>Using your new <code>CBtn</code> Element, you could rewrite the row of buttons above as:</p>
<pre><code class="python">[CBtn('1'), CBtn('2'), CBtn('3'), CBtn('log'), CBtn('ln'), CBtn('-')],
</code></pre>

<p>See the tremendous amount of code you do not have to write!  USE this construct any time you find yourself copying an element many times.  </p>
<p>But let's not stop there.  </p>
<p>Since we've been discussing list comprehensions, let's use them to create this row.  The way to do that is to make a list of the symbols that go across the row make a loop that steps through that list.  The result is a list that looks like this:</p>
<pre><code class="python">[CBtn(t) for t in ('1','2','3', 'log', 'ln', '-')],
</code></pre>

<p>That code produces the same list as this one we created by hand:</p>
<pre><code class="python">[CBtn('1'), CBtn('2'), CBtn('3'), CBtn('log'), CBtn('ln'), CBtn('-')],
</code></pre>

<h3 id="compound-elements">Compound Elements</h3>
<p>Just like a <code>Button</code> can be returned from a User Defined Element, so can multiple Elements.</p>
<p>Going back to the To-Do List example we did earlier, we could have defined a User Defined Element that represented a To-Do Item and this time we're adding a checkbox. A single line from this list will be:</p>
<ul>
<li>The item # (a <code>Text</code> Element)</li>
<li>A <code>Checkbox</code> Element to indicate completed</li>
<li>An <code>Input</code> Element to type in what to do</li>
</ul>
<p>The definition of our User Element is this <code>ToDoItem</code> function.  It is a single User Element that is a combination of 3 PySimpleGUI Elements.</p>
<pre><code class="python">def ToDoItem(num):
    return [sg.Text(f'{num}. '), sg.CBox(''), sg.In()]
</code></pre>

<p>This makes creating a list of 5 to-do items downright trivial when combined with the list comprehension techniques we learned earlier.  Here is the code required to create 5 entries in our to-do list.</p>
<pre><code class="python">layout = [ToDoItem(x) for x in range(1,6)]
</code></pre>

<p>We can then literally add on the buttons</p>
<pre><code class="python">layout = [ToDoItem(x) for x in range(1,6)] + [[sg.Button('Save'), sg.Button('Exit')]]
</code></pre>

<p>And here is our final program</p>
<pre><code class="python">import PySimpleGUI as sg

def ToDoItem(num):
    return [sg.Text(f'{num}. '), sg.CBox(''), sg.In()]

layout = [ToDoItem(x) for x in range(1,6)] + [[sg.Button('Save'), sg.Button('Exit')]]

window = sg.Window('To Do List Example', layout)
event, values = window.read()
</code></pre>

<p>And the window it creates looks like this:</p>
<p><img alt="image" src="https://user-images.githubusercontent.com/46163555/63628682-cda28280-c5db-11e9-92a4-44ec2cb6ccf9.png" /></p>
<hr />
<h1 id="elements">Elements</h1>
<p>You will find information on Elements and all other classes and functions are located near the end of this manual.  They are in 1 large section of the readme, in alphabetical order for easy lookups.  This section's discussion of Elements is meant to teach you how they work.  The other section has detailed call signatures and parameter definitions.</p>
<p>"Elements" are the building blocks used to create windows.  Some GUI APIs use the term "Widget" to describe these graphic elements.</p>
<ul>
<li>Text</li>
<li>Single Line Input</li>
<li>Buttons including these types:<ul>
<li>File Browse</li>
<li>Folder Browse</li>
<li>Calendar picker</li>
<li>Date Chooser</li>
<li>Read window</li>
<li>Close window ("Button" &amp; all shortcut buttons)</li>
<li>Realtime</li>
</ul>
</li>
<li>Checkboxes</li>
<li>Radio Buttons</li>
<li>Listbox</li>
<li>Slider</li>
<li>Multi-line Text Input/Output</li>
<li>Multi-line Text Output (not on tkinter version)</li>
<li>Scroll-able Output</li>
<li>Vertical Separator</li>
<li>Progress Bar</li>
<li>Option Menu</li>
<li>Menu</li>
<li>ButtonMenu</li>
<li>Frame</li>
<li>Column</li>
<li>Graph</li>
<li>Image</li>
<li>Table</li>
<li>Tree</li>
<li>Tab, TabGroup</li>
<li>StatusBar</li>
<li>Pane</li>
<li>Stretch (Qt only)</li>
<li>Sizer (plain PySimpleGUI only)</li>
</ul>
<h2 id="keys">Keys</h2>
<p><strong><em>Keys are a super important concept to understand in PySimpleGUI.</em></strong> </p>
<p>If you are going to do anything beyond the basic stuff with your GUI, then you need to understand keys.</p>
<p>You can think of a "key" as a "name" for an element. Or an "identifier".  It's a way for you to identify and talk about an element with the PySimpleGUI library.  It's the exact same kind of key as a dictionary key.  They must be unique to a window.</p>
<p>Keys are specified when the Element is created using the <code>key</code> parameter.</p>
<p>Keys are used in these ways:
* Specified when creating the element
* Returned as events. If an element causes an event, its key will be used
* In the <code>values</code> dictionary that is returned from <code>window.read()</code>
* To make updates (changes), to an element that's in the window</p>
<p>After you put a key in an element's definition, the values returned from <code>window.read</code> will use that key to tell you the value.  For example, if you have an input element in your layout:</p>
<p><code>Input(key='mykey')</code></p>
<p>And your read looks like this: <code>event, values = Read()</code></p>
<p>Then to get the input value from the read it would be: <code>values['mykey']</code></p>
<p>You also use the same key if you want to call Update on an element.  Please see the section Updating Elements to understand that usage.  To get find an element object given the element's key, you can call the window method <code>find_element</code> (also written <code>FindElement</code>, <code>element</code>), or you can use the more common lookup mechanism:</p>
<pre><code class="python">window['key']
</code></pre>

<p>While you'll often see keys written as strings in examples in this document, know that keys can be <strong><em>ANYTHING</em></strong>.  </p>
<p>Let's say you have a window with a grid of input elements.  You could use their row and column location as a key (a tuple)</p>
<p><code>key=(row, col)</code></p>
<p>Then when you read the <code>values</code> variable that's returned to you from calling <code>Window.read()</code>, the key in the <code>values</code> variable will be whatever you used to create the element. In this case you would read the values as:
<code>values[(row, col)]</code></p>
<p>Most of the time they are simple text strings.  In the Demo Programs, keys are written with this convention:
<code>_KEY_NAME_</code> (underscore at beginning and end with all caps letters) or the most recent convention is to use a dash at the beginning and end (e.g. <code>'-KEY_NAME-'</code>).  You don't have to follow the convention, but it's not a bad one to follow as other users are used to seeing this format and it's easy to spot when element keys are being used.</p>
<p>If you have an element object, to find its key, access the member variable <code>.Key</code> for the element.  This assumes you've got the element in a variable already. </p>
<pre><code class="python">text_elem = sg.Text('', key='-TEXT-')

the_key = text_elem.Key
</code></pre>

<h3 id="default-keys">Default Keys</h3>
<p>If you fail to place a key on an Element, then one will be created for you automatically.  </p>
<p>For <code>Buttons</code>, the text on the button is that button's key. <code>Text</code> elements will default to the text's string (for when events are enabled and the text is clicked) </p>
<p>If the element is one of the input elements (one that will cause an generate an entry in the return values dictionary) and you fail to specify one, then a number will be assigned to it beginning with the number 0.  The effect will be as if the values are represented as a list even if a dictionary is used.</p>
<h3 id="menu-keys">Menu Keys</h3>
<p>Menu items can have keys associated with them as well.  See the section on Menus for more information about these special keys. They aren't the same as Element keys.  Like all elements, Menu Element have one of these Element keys.  The individual menu item keys are different.</p>
<h3 id="write_only_key-modifier"><code>WRITE_ONLY_KEY</code> Modifier</h3>
<p>Sometimes you have input elements (e.g. <code>Multiline</code>) that you are using as an output.  The contents of these elements may get very long.  You don't need to "read" these elements and doing so will potentially needlessly return a lot of data.</p>
<p>To tell PySimpleGUI that you do not want an element to return a value when <code>Window.read</code> is called, add the string <code>WRITE_ONLY_KEY</code> to your key name.</p>
<p>If your <code>Multiline</code> element was defined like this originally:</p>
<pre><code class="python">sg.Multiline(size=(40,8), key='-MLINE-')
</code></pre>

<p>Then to turn off return values for that element, the <code>Multiline</code> element would be written like this:</p>
<pre><code class="python">sg.Multiline(size=(40,8), key='-MLINE-' + sg.WRITE_ONLY_KEY)
</code></pre>

<h2 id="common-element-parameters">Common Element Parameters</h2>
<p>Some parameters that you  will see on almost all Element creation calls include:</p>
<ul>
<li>key   -  Used with window[key], events, and in return value dictionary</li>
<li>tooltip   - Hover your mouse over the element and you'll get a popup with this text</li>
<li>size  - (width, height) - usually measured in characters-wide, rows-high.  Sometimes they mean pixels</li>
<li>font - specifies the font family, size, etc.</li>
<li>colors - Color name or #RRGGBB string</li>
<li>pad - Amount of padding to put around element</li>
<li>enable_events - Turns on the element specific events</li>
<li>visible - Make elements appear and disappear</li>
</ul>
<h4 id="tooltip">Tooltip</h4>
<p>Tooltips are text boxes that popup next to an element if you hold your mouse over the top of it.  If you want to be extra kind to your window's user, then you can create tooltips for them by setting the parameter <code>tooltip</code> to some text string.  You will need to supply your own line breaks / text wrapping.  If you don't want to manually add them, then take a look at the standard library package <code>textwrap</code>.</p>
<p>Tooltips are one of those "polish" items that really dress-up a GUI and show's a level of sophistication.  Go ahead, impress people, throw some tooltips into your GUI.  You can change the color of the background of the tooltip on the tkinter version of PySimpleGUI by setting <code>TOOLTIP_BACKGROUND_COLOR</code> to the color string of your choice.  The default value for the color is:</p>
<p><code>TOOLTIP_BACKGROUND_COLOR = "#ffffe0"</code></p>
<h4 id="size">Size</h4>
<p>Info on setting default element sizes is discussed in the Window section above.</p>
<p>Specifies the amount of room reserved for the Element.  For elements that are character based, such a Text, it is (# characters, # rows).  Sometimes it is a pixel measurement such as the Image element.  And sometimes a mix like on the Slider element (characters long by pixels wide).  </p>
<p>Some elements, Text and Button, have an auto-size setting that is <code>on</code> by default. It will size the element based on the contents.  The result is that buttons and text fields will be the size of the string creating them.  You can turn it off.  For example, for Buttons, the effect will be that all buttons will be the same size in that window.</p>
<h4 id="element-sizes-non-tkinter-ports-qt-wxpython-web">Element Sizes - Non-tkinter Ports (Qt, WxPython, Web)</h4>
<p>In non-tkinter ports you can set the specific element sizes in 2 ways.  One is to use the normal <code>size</code> parameter like you're used to using.  This will be in characters and rows.</p>
<p>The other way is to use a new parameter, <code>size_px</code>.  This parameter allows you to specify the size directly in pixels.  A setting of <code>size_px=(300,200)</code> will create an Element that is 300 x 200 pixels.</p>
<p>Additionally, you can also indicate pixels using the <code>size</code> parameter, <strong>if the size exceeds the threshold for conversion.</strong>  What does that mean?  It means if your width is &gt; 20 (<code>DEFAULT_PIXEL_TO_CHARS_CUTOFF</code>), then it is assumed you're talking pixels, not characters.  However, some of the "normally large" Elements have a cutoff value of 100.  These include, for example, the <code>Multline</code> and <code>Output</code> elements.</p>
<p>If you're curious about the math used to do the character to pixels conversion, it's quite crude, but functional.  The conversion is completed with the help of this variable:</p>
<p><code>DEFAULT_PIXELS_TO_CHARS_SCALING = (10,26)</code></p>
<p>The conversion simply takes your <code>size[0]</code> and multiplies by 10 and your <code>size[1]</code> and multiplies it by 26.</p>
<h4 id="colors">Colors</h4>
<p>A string representing color.  Anytime colors are involved, you can specify the tkinter color name such as 'lightblue' or an RGB hex value '#RRGGBB'.  For buttons, the color parameter is a tuple (text color, background color)</p>
<p>Anytime colors are written as a tuple in PySimpleGUI, the way to figure out which color is the background is to replace the "," with the word "on".  ('white', 'red') specifies a button that is "white on red".  Works anywhere there's a color tuple.</p>
<h4 id="pad">Pad</h4>
<p>The amount of room around the element in pixels. The default value is (5,3) which means leave 5 pixels on each side of the x-axis and 3 pixels on each side of the y-axis.  You can change this on a global basis using a call to SetOptions, or on an element basis.</p>
<p>If you want more pixels on one side than the other, then you can split the number into 2 number.  If you want 200 pixels on the left side, and 3 pixels on the right, the pad would be ((200,3), 3).  In this example, only the x-axis is split.</p>
<h4 id="font">Font</h4>
<p>Specifies the font family, size, and style.  Font families on Windows include:
* Arial
* Courier
* Comic,
* Fixedsys
* Times
* Verdana
* Helvetica (the default I think)</p>
<p>The fonts will vary from system to system, however, Tk 8.0 automatically maps Courier, Helvetica and Times to their corresponding native family names on all platforms.  Also, font families cannot cause a font specification to fail on Tk 8.0 and greater.</p>
<p>If you wish to leave the font family set to the default, you can put anything not a font name as the family.  The PySimpleGUI Demo programs and documentation use the family 'Any' to demonstrate this fact..  You could use "default" if that's more clear to you.</p>
<p>There are 2 formats that can be used to specify a font... a string, and a tuple
Tuple - (family, size, styles)
String - "Family Size Styles"</p>
<p>To specify an underlined, Helvetica font with a size of 15 the values:
('Helvetica', 15, 'underline italics')
'Helvetica 15 underline italics'</p>
<h4 id="key">Key</h4>
<p>See the section above that has full information about keys.</p>
<h4 id="visible">Visible</h4>
<p>Beginning in version 3.17 you can create Elements that are initially invisible that you can later make visible.</p>
<p>To create an invisible Element, place the element in the layout like you normally would and add the parameter </p>
<p><code>visible=False</code>.</p>
<p>Later when you want to make that Element visible you simply call the Element's <code>Update</code> method and pass in the parameter <code>visible=True</code></p>
<p>This feature works best on Qt, but does work on the tkinter version as well.  The visible parameter can also be used with the Column and Frame "container" Elements.</p>
<p>Note - Tkinter elements behave differently than Qt elements in how they arrange themselves when going from invisible to visible.</p>
<p>tkinter elements tend to STACK themselves.  </p>
<p>One workaround is to place the element in a Column with other elements on its row.  This will hold the place of the row it is to be placed on.  It will move the element to the end of the row however.  </p>
<p>If you want to not only make the element invisible, on tkinter you can call `Element.</p>
<p>Qt elements tend to hold their place really well and the window resizes itself nicely.  It is more precise and less clunky.</p>
<h2 id="shortcut-functions-multiple-function-names">Shortcut Functions / Multiple Function Names</h2>
<p>Perhaps not the best idea, but one that's done none the less is the naming of methods and functions.  Some of the more "Heavily Travelled Elements" (and methods/functions) have "shortcuts".  </p>
<p>In other words, I am lazy and don't like to type. The result is multiple ways to do exactly the same thing.  Typically, the Demo Programs and other examples use the full name, or at least a longer name.  Thankfully PyCharm will show you the same documentation regardless which you use.</p>
<p>This enables you to code much quicker once you are used to using the SDK.  The Text Element, for example, has 3 different names <code>Text</code>, <code>Txt</code> or<code>T</code>.  InputText can also be written <code>Input</code> or <code>In</code> .  </p>
<p>The shortcuts aren't limited to Elements.  The <code>Window</code> method <code>Window.FindElement</code> can be written as <code>Window.Element</code> because it's such a commonly used function.  BUT, even that has now been shortened to <code>window[key]</code></p>
<p>It's an ongoing thing.  If you don't stay up to date and one of the newer shortcuts is used, you'll need to simply rename that shortcut in the code.  For examples Replace sg.T with sg.Text if your version doesn't have sg.T in it.</p>
<h2 id="text-element-t-txt-text">Text Element | <code>T == Txt == Text</code></h2>
<p>Basic Element. It displays text.</p>
<pre><code class="python">layout = [
            [sg.Text('This is what a Text Element looks like')],
         ]
</code></pre>

<p><img alt="simple text" src="https://user-images.githubusercontent.com/13696193/44959877-e9d97b00-aec3-11e8-9d24-b4405ee4a148.jpg" /></p>
<p>When creating a Text Element that you will later update, make sure you reserve enough characters for the new text.  When a Text Element is created without a size parameter, it is created to exactly fit the characters provided. </p>
<p>With proportional spaced fonts (normally the default) the pixel size of one set of characters will differ from the pixel size of a different set of characters even though the set is of the same number of characters.  In other words, not all letters use the same number of pixels.  Look at the text you're reading right now and you will see this.  An "i" takes up a less space then an "A".</p>
<hr />
<h2 id="windowfindelementkey-shortened-to-windowkey"><code>Window.FindElement(key)</code> shortened to <code>Window[key]</code></h2>
<p>There's been a fantastic leap forward in making PySimpleGUI code more compact.  </p>
<p>Instead of writing:</p>
<pre><code class="python">window.FindElement(key).update(new_value)
 ```

You can now write it as:

```python
window[key].update(new_value)
 ```

This change has been released to PyPI for PySimpleGUI

MANY Thanks is owed to the nngogol that suggested and showed me how to do this.  It's an incredible find as have been many of his suggestions.

## `Element.update()` -&gt;  `Element()` shortcut

This has to be one of the strangest syntactical constructs I've ever written.  

It is best used in combination with `FindElement` (see prior section on how to shortcut `FindElement`).  

Normally to change an element, you &quot;find&quot; it, then call its `update` method.  The code usually looks like this, as you saw in the previous section:

```python
window[key].update(new_value)
</code></pre>

<p>The code can be further compressed by removing the <code>.update</code> characters, resulting in this very compact looking call:</p>
<pre><code class="python">window[key](new_value)
</code></pre>

<p>Yes, that's a valid statement in Python.</p>
<p>What's happening is that the element itself is being called.   You can also writing it like this:</p>
<pre><code class="python">elem = sg.Text('Some text', key='-TEXT-')
elem('new text value')
</code></pre>

<p>Side note - you can also call your <code>window</code> variable directly.  If you "call" it it will actually call <code>Window.read</code>.</p>
<pre><code class="python">window = sg.Window(....)
event, values = window()

# is the same as
window = sg.Window(....)
event, values = window.read()
</code></pre>

<p>It is confusing looking however so when used, it might be a good idea to write a comment at the end of the statement to help out the poor beginner programmer coming along behind you.</p>
<p>Because it's such a foreign construct that someone with 1 week of Python classes will not recognize, the demos will continue to use the <code>.update</code> method.  </p>
<p>It does not have to be used in conjuction with <code>FindElement</code>.  The call works on any previously made Element.  Sometimes elements are created, stored into a variable and then that variable is used in the layout.  For example.</p>
<pre><code class="python">graph_element = sg.Graph(...... lots of parms ......)

layout = [[graph_element]]
.
.
.
graph_element(background_color='blue')      # this calls Graph.update for the previously defined element
</code></pre>

<p>Hopefully this isn't too confusing.  Note that the methods these shortcuts replace will not be removed.  You can continue to use the old constructs without changes.</p>
<hr />
<h3 id="fonts">Fonts</h3>
<p>Already discussed in the common parameters section.  Either string or a tuple.</p>
<h3 id="color-in-pysimplegui-are-in-one-of-two-formats-color-name-or-rgb-value">Color in PySimpleGUI are in one of two formats - color name or RGB value.</h3>
<p>Individual colors are specified using either the color names as defined in tkinter or an RGB string of this format:</p>
<pre><code>"#RRGGBB"        or          "darkblue"
</code></pre>
<h3 id="auto_size_text"><code>auto_size_text</code></h3>
<p>A <code>True</code> value for <code>auto_size_text</code>, when placed on Text Elements, indicates that the width of the Element should be shrunk do the width of the text.   The default setting is True.  You need to remember this when you create <code>Text</code> elements that you are using for output.  </p>
<p><code>Text(key='-TXTOUT-)</code> will create a <code>Text</code> Element that has 0 length.  Notice that for Text elements with an empty string, no string value needs to be indicated.  The default value for strings is <code>''</code> for Text Elements.  If you try to output a string that's 5 characters, it won't be shown in the window because there isn't enough room.  The remedy is to manually set the size to what you expect to output</p>
<p><code>Text(size=(15,1), key='-TXTOUT-)</code> creates a <code>Text</code> Element that can hold 15 characters.</p>
<h3 id="chortcut-functions">Chortcut functions</h3>
<p>The shorthand functions for <code>Text</code> are <code>Txt</code> and <code>T</code></p>
<h3 id="events-enable_events">Events <code>enable_events</code></h3>
<p>If you set the parameter <code>enable_events</code> then you will get an event if the user clicks on the Text.</p>
<h2 id="multiline-element">Multiline Element</h2>
<p>This Element doubles as both an input and output Element.</p>
<pre><code class="python">layout = [[sg.Multiline('This is what a Multi-line Text Element looks like', size=(45,5))]]
</code></pre>

<p><img alt="multiline" src="https://user-images.githubusercontent.com/13696193/44959853-b139a180-aec3-11e8-972f-f52188510c88.jpg" /></p>
<p>This element has been expanded upon quite a bit over time.  Two of the more exciting additions have been</p>
<ul>
<li>Ability to output unique text and background colors on a per-character basis</li>
<li>The <code>print</code> method that allows you to easily reroute your normally printed output to a multiline element instead</li>
</ul>
<p>The <code>Multiline.print()</code> call is made using the same element-lookup technique you're used to using to call <code>update</code>.  One of these lookups generally appear:</p>
<pre><code class="python">window['-MULTILINE KEY-']
</code></pre>

<p>To change one of your normal prints to output to your multiline element, you simply add the above lookup expression to the front of your print statement.</p>
<pre><code class="python">print('My variables are', a, b, c)       # a normal print statement

window['-MULTILINE KEY-'].print('My variables are', a, b, c)     # Routed to your multiline element
</code></pre>

<p>It gets even better though.... you can add color to your prints</p>
<pre><code class="python"># Outputs red text on a yellow background
window['-MULTILINE KEY-'].print('My variables are', a, b, c, text_color='red', background_color='yellow')

</code></pre>

<h3 id="redefine-print">Redefine print</h3>
<p>Another way to use this print capability is to redefine the <code>print</code> statement itself.  This will allow you to leave your code entirely as is.  By adding this line of code your entire program will output all printed information to a multiline element.</p>
<pre><code class="python">print = lambda *args, **kwargs: window['-MULTILINE KEY-'].print(*args, **kwargs)
</code></pre>

<h2 id="text-input-element-inputtext-input-in">Text Input Element  | <code>InputText == Input == In</code></h2>
<pre><code class="python">layout = [[sg.InputText('Default text')]]
</code></pre>

<p><img alt="inputtext 2" src="https://user-images.githubusercontent.com/13696193/44959861-b5fe5580-aec3-11e8-8040-53ec241b5079.jpg" /></p>
<hr />
<h4 id="note-about-the-do_not_clear-parameter">Note about the <code>do_not_clear</code> parameter</h4>
<p>This used to really trip people up, but don't think so anymore.  The <code>do_not_clear</code> parameter is initialized when creating the InputText Element.  If set to False, then the input field's contents will be erased after every <code>Window.read()</code> call.  Use this setting for when your window is an "Input Form" type of window where you want all of the fields to be erased and start over again every time.</p>
<h2 id="combo-element-combo-inputcombo-dropdown-drop">Combo Element | <code>Combo == InputCombo == DropDown == Drop</code></h2>
<p>Also known as a drop-down list.  Only required parameter is the list of choices.  The return value is a string matching what's visible on the GUI.</p>
<pre><code class="python">layout = [[sg.Combo(['choice 1', 'choice 2'])]]
</code></pre>

<p><img alt="combobox" src="https://user-images.githubusercontent.com/13696193/44959860-b565bf00-aec3-11e8-82fe-dbe41252458b.jpg" /></p>
<h2 id="listbox-element">Listbox Element</h2>
<p>The standard listbox like you'll find in most GUIs.  Note that the return values from this element will be a <strong><em>list of results, not a single result</em></strong>. This is because the user can select more than 1 item from the list (if you set the right mode).</p>
<pre><code class="python">layout = [[sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6))]]
</code></pre>

<p><img alt="listbox 2" src="https://user-images.githubusercontent.com/13696193/44959859-b4cd2880-aec3-11e8-881c-1e369d5c6337.jpg" /></p>
<hr />
<p>ListBoxes can cause a window to return from a Read call.  If the flag <code>enable_events</code> is set, then when a user makes a selection, the Read immediately returns.</p>
<p>Another way ListBoxes can cause Reads to return is if the flag bind_return_key is set.  If True, then if the user presses the return key while an entry is selected, then the Read returns.  Also, if this flag is set, if the user double-clicks an entry it will return from the Read.</p>
<h2 id="slider-element">Slider Element</h2>
<p>Sliders have a couple of slider-specific settings as well as appearance settings. Examples include the <code>orientation</code> and <code>range</code> settings.</p>
<pre><code class="python">layout = [[sg.Slider(range=(1,500),
         default_value=222,
         size=(20,15),
         orientation='horizontal',
         font=('Helvetica', 12))]]
</code></pre>

<p><img alt="slider" src="https://user-images.githubusercontent.com/13696193/44959858-b4349200-aec3-11e8-9e25-c0fcf025d19e.jpg" /></p>
<h3 id="qt-sliders">Qt Sliders</h3>
<p>There is an important difference between Qt and tkinter sliders.  On Qt, the slider values must be integer, not float.  If you want your slider to go from 0.1 to 1.0, then make your slider go from 1 to 10 and divide by 10.  It's an easy math thing to do and not a big deal.  Just deal with it.... you're writing software after all.  Presumably you know how to do these things.  ;-)</p>
<h2 id="radio-button-element">Radio Button Element</h2>
<p>Creates one radio button that is assigned to a group of radio buttons.  Only 1 of the buttons in the group can be selected at any one time.</p>
<pre><code class="python">layout =  [
    [sg.Radio('My first Radio!', &quot;RADIO1&quot;, default=True),
    sg.Radio('My second radio!', &quot;RADIO1&quot;)]
]
</code></pre>

<p><img alt="radio" src="https://user-images.githubusercontent.com/13696193/44959857-b4349200-aec3-11e8-8e2d-e6a49ffbd0b6.jpg" /></p>
<h2 id="checkbox-element-cbox-cb-check">Checkbox Element | <code>CBox == CB == Check</code></h2>
<p>Checkbox elements are like Radio Button elements.  They return a bool indicating whether or not they are checked.</p>
<pre><code class="python">layout =  [[sg.Checkbox('My first Checkbox!', default=True), sg.Checkbox('My second Checkbox!')]]
</code></pre>

<p><img alt="checkbox" src="https://user-images.githubusercontent.com/13696193/44959906-6f5d2b00-aec4-11e8-9c8a-962c787f0286.jpg" /></p>
<h2 id="spin-element">Spin Element</h2>
<p>An up/down spinner control.  The valid values are passed in as a list.</p>
<pre><code class="python">layout =  [[sg.Spin([i for i in range(1,11)], initial_value=1), sg.Text('Volume level')]]
</code></pre>

<p><img alt="spinner" src="https://user-images.githubusercontent.com/13696193/44959855-b1d23800-aec3-11e8-9f51-afb2109879da.jpg" /></p>
<h2 id="image-element">Image Element</h2>
<p>Images can be placed in your window provide they are in PNG, GIF, PPM/PGM format.  JPGs cannot be shown because tkinter does not naively support JPGs.  You can use the Python Imaging Library (PIL) package  to convert your image to PNG prior to calling PySimpleGUI if your images are in JPG format.</p>
<pre><code class="python">layout = [
            [sg.Image(r'C:\PySimpleGUI\Logos\PySimpleGUI_Logo_320.png')],
         ]
</code></pre>

<p><img alt="image" src="https://user-images.githubusercontent.com/13696193/61885709-4e326e00-aecc-11e9-8695-7193df2831ec.png" /></p>
<p>You can specify an animated GIF as an image and can animate the GIF by calling <code>UpdateAnimation</code>.  Exciting stuff!</p>
<p><img alt="loading animation" src="https://user-images.githubusercontent.com/13696193/51280871-d2041e80-19ae-11e9-8757-802eb95352ed.gif" /></p>
<p>You can call the method without setting the <code>time_between_frames</code> value and it will show a frame and immediately move on to the next frame.  This enables you to do the inter-frame timing.</p>
<h2 id="button-element">Button Element</h2>
<p>Buttons are the most important element of all!  They cause the majority of the action to happen.  After all, it's a button press that will get you out of a window, whether it be Submit or Cancel, one way or another a button is involved in all windows.  The only exception is to this is when the user closes the window using the "X" in the upper corner which means no button was involved.</p>
<p>The Types of buttons include:
* Folder Browse
* File Browse
* Files Browse
* File SaveAs
* File Save
* Close window  (normal button)
* Read window
* Realtime
* Calendar Chooser
* Color Chooser</p>
<p>Close window - Normal buttons like Submit, Cancel, Yes, No, do NOT close the window... they used to.  Now to close a window you need to use a CloseButton / CButton.</p>
<p>Folder Browse - When clicked a folder browse dialog box is opened.  The results of the Folder Browse dialog box are written into one of the input fields of the window.</p>
<p>File Browse - Same as the Folder Browse except rather than choosing a folder, a single file is chosen.</p>
<p>Calendar Chooser - Opens a graphical calendar to select a date.</p>
<p>Color Chooser - Opens a color chooser dialog</p>
<p>Read window - This is a window button that will read a snapshot of all of the input fields, but does not close the window after it's clicked.</p>
<p>Realtime - This is another async window button.  Normal button clicks occur after a button's click is released.  Realtime buttons report a click the entire time the button is held down.</p>
<p>Most programs will use a combination of shortcut button calls (Submit, Cancel, etc.), normal Buttons which leave the windows open and CloseButtons that close the window when clicked.</p>
<p>Sometimes there are multiple names for the same function.  This is simply to make the job of the programmer quicker and easier.  Or they are old names that are no longer used but kept around so that existing programs don't break.</p>
<p>The 4 primary windows of PySimpleGUI buttons and their names are:</p>
<ol>
<li><code>Button</code>= <code>ReadButton</code> = <code>RButton</code> = <code>ReadFormButton</code> (Use <code>Button</code>, others are old methods)</li>
<li><code>CloseButton</code> = <code>CButton</code></li>
<li><code>RealtimeButton</code></li>
<li><code>DummyButton</code></li>
</ol>
<p>You will find the long-form names in the older programs. ReadButton for example.</p>
<p>In Oct 2018, the definition of Button changed.  Previously Button would CLOSE the window when clicked.  It has been changed so the Button calls will leave the window open in exactly the same way as a ReadButton.  They are the same calls now.   To enables windows to be closed using buttons, a new button was added... <code>CloseButton</code> or <code>CButton</code>.</p>
<p>Your PySimpleGUI program is most likely going to contain only <code>Button</code> calls. The others are generally not found in user code.</p>
<p>The most basic Button element call to use is <code>Button</code></p>
<pre><code class="python">layout =  [[sg.Button('Ok'), sg.Button('Cancel')]]
</code></pre>

<p><img alt="ok cancel 3" src="https://user-images.githubusercontent.com/13696193/44959927-aa5f5e80-aec4-11e8-86e1-5dc0b3a2b803.jpg" /></p>
<p>You will rarely see these 2 buttons in particular written this way.  Recall that PySimpleGUI is focused on YOU (which generally directly means.... less typing).  As a result, the code for the above window is normally written using shortcuts found in the next section.</p>
<p>You will typically see this instead of calls to <code>Button</code>:</p>
<pre><code class="python">layout =  [[sg.Ok(), sg.Cancel()]]
</code></pre>

<p>In reality <code>Button</code> is in fact being called on your behalf.  Behind the scenes, <code>sg.Ok</code> and <code>sg.Cancel</code> call <code>Button</code> with the text set to <code>Ok</code> and <code>Cancel</code> and returning the results that then go into the layout.  If you were to print the layout it will look identical to the first layout shown that has <code>Button</code> shown specifically in the layout.</p>
<h3 id="ttk-buttons-macs">TTK Buttons &amp; Macs</h3>
<p>In 2019 support for ttk Buttons was added.  This gets around the problem of not being able to change button colors on a Mac.  There are a number of places you can control whether or not ttk buttons are used, be it on MAc or other platform.</p>
<p>TTK Buttons and TK Buttons operate slightly differently.  Button highlighting is one different.  How images and text are displayed at the same time is another.  You've got options now that weren't there previously.  It's nice to see that Mac users can finally use the color themes.</p>
<h3 id="button-element-shortcuts">Button Element Shortcuts</h3>
<p>These Pre-made buttons are some of the most important elements of all because they are used so much.  They all basically do the same thing, <strong>set the button text to match the function name and set the parameters to commonly used values</strong>. If you find yourself needing to create a custom button often because it's not on this list, please post a request on GitHub. . They include:</p>
<ul>
<li>OK</li>
<li>Ok</li>
<li>Submit</li>
<li>Cancel</li>
<li>Yes</li>
<li>No</li>
<li>Exit</li>
<li>Quit</li>
<li>Help</li>
<li>Save</li>
<li>SaveAs</li>
<li>Open</li>
</ul>
<h3 id="chooser-buttons">"Chooser" Buttons</h3>
<p>These buttons are used to show dialog boxes that choose something like a filename, date, color, etc.. that are filled into an <code>InputText</code> Element (or some other "target".... see below regarding targets)</p>
<ul>
<li>CalendarButton</li>
<li>ColorChooserButton</li>
<li>FileBrowse</li>
<li>FilesBrowse</li>
<li>FileSaveAs</li>
<li>FolderBrowse</li>
</ul>
<p><strong>IMPORT NOTE ABOUT SHORTCUT BUTTONS</strong>
Prior to release 3.11.0, these buttons closed the window.  Starting with 3.11 they will not close the window.  They act like RButtons (return the button text and do not close the window)</p>
<p>If you are having trouble with these buttons closing your window, please check your installed version of PySimpleGUI by typing <code>pip list</code> at a command prompt.  Prior to 3.11 these buttons close your window.</p>
<p>Using older versions, if you want a Submit() button that does not close the window, then you would instead use RButton('Submit').   Using the new version, if you want a Submit button that closes the window like the sold Submit() call did, you would write that as <code>CloseButton('Submit')</code> or <code>CButton('Submit')</code></p>
<h3 id="button-targets">Button targets</h3>
<p>The <code>FileBrowse</code>, <code>FolderBrowse</code>, <code>FileSaveAs</code> , <code>FilesSaveAs</code>, <code>CalendarButton</code>, <code>ColorChooserButton</code> buttons all fill-in values into another element located on the window.  The target can be a Text Element or an InputText Element or the button itself.  The location of the element is specified by the <code>target</code> variable in the function call.</p>
<p>The Target comes in two forms.
1. Key
2. (row, column)</p>
<p>Targets that are specified using a key will find its target element by using the target's key value.  This is the "preferred" method.</p>
<p>If the Target is specified using (row, column) then it utilizes a grid system.  The rows in your GUI are numbered starting with 0. The target can be specified as a hard coded grid item or it can be relative to the button.</p>
<p>The (row, col) targeting can only target elements that are in the same "container".  Containers are the Window, Column and Frame Elements.  A File Browse button located inside of a Column is unable to target elements outside of that Column.</p>
<p>The default value for <code>target</code> is <code>(ThisRow, -1)</code>.   <code>ThisRow</code> is a special value that tells the GUI to use the same row as the button.  The Y-value of -1 means the field one value to the left of the button.  For a File or Folder Browse button, the field that it fills are generally to the left of the button is most cases.    (ThisRow, -1) means the Element to the left of the button, on the same row.</p>
<p>If a value of <code>(None, None)</code> is chosen for the target, then the button itself will hold the information.  Later the button can be queried for the  value by using the button's key.</p>
<p>Let's examine this window as an example:</p>
<p><img alt="file browse" src="https://user-images.githubusercontent.com/13696193/44959944-d1b62b80-aec4-11e8-8a68-9d79d37b2c81.jpg" /></p>
<p>The <code>InputText</code> element is located at (1,0)... row 1, column 0.  The <code>Browse</code> button is located at position (2,0).  The Target for the button could be any of these values:</p>
<pre><code>Target = (1,0)
Target = (-1,0)
</code></pre>
<p>The code for the entire window could be:</p>
<pre><code class="python">layout = [[sg.T('Source Folder')],
              [sg.In()],
              [sg.FolderBrowse(target=(-1, 0)), sg.OK()]]
</code></pre>

<p>or if using keys, then the code would be:</p>
<pre><code class="python">layout = [[sg.T('Source Folder')],
              [sg.In(key='input')],
              [sg.FolderBrowse(target='input'), sg.OK()]]
</code></pre>

<p>See how much easier the key method is?</p>
<h4 id="invisible-targets">Invisible Targets</h4>
<p>One very handy trick is to make your target invisible.  This will remove the ability to edit the chosen value like you normally would be able to with an Input Element.  It's a way of making things look cleaner, less cluttered too perhaps.</p>
<h3 id="save-open-buttons">Save &amp; Open Buttons</h3>
<p>There are 4 different types of File/Folder open dialog box available.  If you are looking for a file to open, the <code>FileBrowse</code> is what you want. If you want to save a file, <code>SaveAs</code> is the button. If you want to get a folder name, then <code>FolderBrowse</code> is the button to use. To open several files at once, use the <code>FilesBrowse</code> button.  It will create a list of files that are separated by ';'</p>
<p><img alt="open" src="https://user-images.githubusercontent.com/13696193/45243804-2b529780-b2c3-11e8-90dc-6c9061db2a1e.jpg" /></p>
<p><img alt="folder" src="https://user-images.githubusercontent.com/13696193/45243805-2b529780-b2c3-11e8-95ee-fec3c0b11319.jpg" /></p>
<p><img alt="saveas" src="https://user-images.githubusercontent.com/13696193/45243807-2beb2e00-b2c3-11e8-8549-ba71cdc05951.jpg" /></p>
<h3 id="calendar-buttons">Calendar Buttons</h3>
<p>These buttons pop up a calendar chooser window.  The chosen date is returned as a string.</p>
<p><img alt="calendar" src="https://user-images.githubusercontent.com/13696193/45243374-99965a80-b2c1-11e8-8311-49777835ca40.jpg" /></p>
<h3 id="color-chooser-buttons">Color Chooser Buttons</h3>
<p>These buttons pop up a standard color chooser window.  The result is returned as a tuple.  One of the returned values is an RGB hex representation.</p>
<p><img alt="color" src="https://user-images.githubusercontent.com/13696193/45243375-99965a80-b2c1-11e8-9779-b71bed85fab6.jpg" /></p>
<h3 id="custom-buttons">Custom Buttons</h3>
<p>Not all buttons are created equal.  A button that closes a window is different that a button that returns from the window without closing it.  If you want to define your own button, you will generally do this with the Button Element <code>Button</code>, which closes the window when clicked.</p>
<pre><code class="python">layout =  [[sg.Button('My Button')]]
</code></pre>

<p><img alt="button" src="https://user-images.githubusercontent.com/13696193/44959862-b696ec00-aec3-11e8-9e88-4b9af0338a03.jpg" /></p>
<p>All buttons can have their text changed by changing the <code>button_text</code> parameter in the button call.  It is this text that is returned when a window is read.  This text will be what tells you which button was clicked.  However, you can also use keys on your buttons so that they will be unique.  If only the text were used, you would never be able to have 2 buttons in the same window with the same text.</p>
<pre><code class="python">layout =  [[sg.Button('My Button', key='_BUTTON_KEY_')]]
</code></pre>

<p>With this layout, the event that is returned from a <code>Window.read()</code> call when the button is clicked will be "<code>_BUTTON_KEY_</code>"</p>
<h3 id="button-images">Button Images</h3>
<p>Now this is an exciting feature not found in many simplified packages.... images on buttons!  You can make a pretty spiffy user interface with the help of a few button images.</p>
<p>This is one of the quickest and easiest ways to transform tkinter from a "1990s looking GUI" into a "modern GUI".  If you don't like the default buttons, then simply bring your own button images and use those instead.</p>
<p>Your button images need to be in PNG or GIF format.  When you make a button with an image, set the button background to the same color as the background.  You can get the theme's background color by calling <code>theme_background_color()</code></p>
<p><code>TRANSPARENT_BUTTON</code> - <strong>Important</strong> - This is a legacy value that is misleading.  It is currently defined as this constant value:</p>
<pre><code class="python">TRANSPARENT_BUTTON = ('#F0F0F0', '#F0F0F0')  
</code></pre>

<p>As you can see it is simply a tuple of 2 gray colors.  The effect is that the button text and the button background color to a specific shade of gray.  Way back in time, before you could change the background colors and all windows were gray, this value worked. But now that your button can be on any background color, you'll want to set the buttons color to match the background so that your button blends with the background color.</p>
<pre><code class="python">sg.Button('Restart Song', button_color=(sg.theme_background_color(), sg.theme_background_color()),
               image_filename=image_restart, image_size=(50, 50), image_subsample=2, border_width=0)
</code></pre>

<p>There are several parameters in <code>Button</code> elements that are used for button images.</p>
<pre><code>image_filename - Filename of image. Can be a relative path
image_data - A Base64 image
image_size - Size of image in pixels
image_subsample - Amount to divide the size by.  2 means your image will be 1/2 the size.  3 means 1/3
</code></pre>

<p>Here's an example window made with button images.</p>
<p><img alt="media file player" src="https://user-images.githubusercontent.com/13696193/43161977-9ee7cace-8f57-11e8-8ff8-3ea24b69dab9.jpg" /></p>
<p>You'll find the source code in the file Demo Media Player.  Here is what the button calls look like to create media player window</p>
<p>```python
sg.Button('Pause', button_color=(sg.theme_background_color(), sg.theme_background_color()),
              image_filename=image_pause,
              image_size=(50, 50),
              image_subsample=2,
              border_width=0)</p>
<pre><code>
Experimentation is sometimes required for these concepts to really sink in and they can vary depending on the underlying GUI framework. 

Button Images do work so play with them.  You can use PIL to change the size of your images before passing to PySimpleGUI.

### Realtime Buttons

Normally buttons are considered &quot;clicked&quot; when the mouse button is let UP after a downward click on the button.  What about times when you need to read the raw up/down button values.  A classic example for this is a robotic remote control.  Building a remote control using a GUI is easy enough.  One button for each of the directions is a start.  Perhaps something like this:

![robot remote](https://user-images.githubusercontent.com/13696193/44959958-ff9b7000-aec4-11e8-99ea-7450926409be.jpg)

This window has 2 button types.  There's the normal &quot;Read Button&quot; (Quit) and 4 &quot;Realtime Buttons&quot;.

Here is the code to make, show and get results from this window:

```python
import PySimpleGUI as sg

gui_rows = [[sg.Text('Robotics Remote Control')],
            [sg.T(' '  * 10), sg.RealtimeButton('Forward')],
            [sg.RealtimeButton('Left'), sg.T(' '  * 15), sg.RealtimeButton('Right')],
            [sg.T(' '  * 10), sg.RealtimeButton('Reverse')],
            [sg.T('')],
            [sg.Quit(button_color=('black', 'orange'))]
            ]

window = sg.Window('Robotics Remote Control', gui_rows)

#
# Some place later in your code...
# You need to perform a Read or Refresh call on your window every now and then or
# else it will apprear as if the program has locked up.
#
# your program's main loop
while (True):
    # This is the code that reads and updates your window
    event, values = window.read(timeout=50)
    print(event)
    if event in ('Quit', None):
        break

window.close()  # Don't forget to close your window!
</code></pre>

<p>This loop will read button values and print them.  When one of the Realtime buttons is clicked, the call to <code>window.read</code> will  return a button name matching the name on the button that was depressed or the key if there was a key assigned to the button.  It will continue to return values as long as the button remains depressed.  Once released, the Read will return timeout events until a button is again clicked.</p>
<p><strong>File Types</strong>
The <code>FileBrowse</code> &amp; <code>SaveAs</code> buttons have an additional setting named <code>file_types</code>.  This variable is used to filter the files shown in the file dialog box.  The default value for this setting is</p>
<pre><code>FileTypes=(("ALL Files", "*.*"),)
</code></pre>
<p>This code produces a window where the Browse button only shows files of type .TXT</p>
<pre><code>layout =  [[sg.In() ,sg.FileBrowse(file_types=(("Text Files", "*.txt"),))]]
</code></pre>
<p>NOTE - Mac users will not be able to use the file_types parameter.  tkinter has a bug on Macs that will crash the program is a file_type is attempted so that feature had to be removed.  Sorry about that!</p>
<p><strong><em>The ENTER key</em></strong>
       The ENTER key is an important part of data entry for windows.  There's a long  tradition of the enter key being used to quickly submit windows.  PySimpleGUI implements this by tying the ENTER key to the first button that closes or reads a window.</p>
<p>The Enter Key can be "bound" to a particular button so that when the key is pressed, it causes the window to return as if the button was clicked.  This is done using the <code>bind_return_key</code> parameter in the button calls.
If there are more than 1 button on a window, the FIRST button that is of type Close window or Read window is used.  First is determined by scanning the window, top to bottom and left to right.</p>
<h2 id="buttonmenu-element">ButtonMenu Element</h2>
<p>The ButtonMenu element produces a unique kind of effect.  It's a button, that when clicked, shows you a menu.   It's like clicking one of the top-level menu items on a MenuBar.  As a result, the menu definition take the format of a single  menu entry from  a normal menu definition.  A normal menu definition is  a list of lists.  This definition is one of those lists.</p>
<pre><code class="python"> ['Menu', ['&amp;Pause Graph', 'Menu item::optional_key']]
</code></pre>

<p>The very first string normally specifies what is shown on the menu bar.  In this case, the value is <strong>not used</strong>.  You set the text for the button using a different parameter, the <code>button_text</code> parm.</p>
<p>One use of this element is to make a "fake menu bar" that has a colored background.  Normal menu bars cannot have their background color changed.  Not so with ButtonMenus.</p>
<p><img alt="buttonmenu" src="https://user-images.githubusercontent.com/13696193/50387000-bc0d8180-06c0-11e9-8d17-3b22ed665e78.gif" /></p>
<p>Return values for ButtonMenus are sent via the return values dictionary.  If a selection is made, then an event is generated that will equal the ButtonMenu's key value.  Use that key value to look up the value selected by the user.  This is the same mechanism as the Menu Bar Element, but differs from the pop-up (right click) menu.</p>
<h2 id="verticalseparator-element">VerticalSeparator Element</h2>
<p>This element has limited usefulness and is being included more for completeness than anything else.  It will draw a line between elements.</p>
<p>It works best when placed between columns or elements that span multiple rows.  If on a "normal" row with elements that are only 1 row high, then it will only span that one row.</p>
<pre><code class="python">VerticalSeparator(pad=None)
</code></pre>

<p><img alt="snag-0129" src="https://user-images.githubusercontent.com/13696193/47376041-a92a0100-d6bf-11e8-8f5b-0c0df56cf0f3.jpg" /></p>
<h2 id="horizontalseparator-element">HorizontalSeparator Element</h2>
<p>In PySimpleGUI, the tkinter port, there is no <code>HorizontalSeparator</code> Element.  One will be added as a "stub" so that code is portable.  It will likely do nothing just like the <code>Stretch</code> Element.</p>
<p>An easy way to get a horizontal line in PySimpleGUI is to use a <code>Text</code> Element that contains a line of underscores</p>
<pre><code class="python">sg.Text('_'*30)             # make a horizontal line stretching 30 characters
</code></pre>

<h2 id="progressbar-element">ProgressBar Element</h2>
<p>The <code>ProgressBar</code> element is used to build custom Progress Bar windows.  It is HIGHLY recommended that you use OneLineProgressMeter that provides a complete progress meter solution for you.  Progress Meters are not easy to work with because the windows have to be non-blocking and they are tricky to debug.</p>
<p>The <strong>easiest</strong> way to get progress meters into your code is to use the <code>OneLineProgressMeter</code> API.  This consists of a pair of functions, <code>OneLineProgressMeter</code> and <code>OneLineProgressMeterCancel</code>.  You can easily cancel any progress meter by calling it with the current value = max value.  This will mark the meter as expired and close the window.
You've already seen OneLineProgressMeter calls presented earlier in this readme.</p>
<pre><code class="python">sg.OneLineProgressMeter('My Meter', i+1, 1000,  'key', 'Optional message')
</code></pre>

<p>The return value for <code>OneLineProgressMeter</code> is:
<code>True</code> if meter updated correctly
<code>False</code> if user clicked the Cancel button, closed the window, or vale reached the max value.</p>
<h4 id="progress-meter-in-your-window">Progress Meter in Your window</h4>
<p>Another way of using a Progress Meter with PySimpleGUI is to build a custom window with a <code>ProgressBar</code> Element in the window.  You will need to run your window as a non-blocking window.  When you are ready to update your progress bar, you call the <code>UpdateBar</code> method for the <code>ProgressBar</code> element itself.</p>
<pre><code class="python">import PySimpleGUI as sg

# layout the window
layout = [[sg.Text('A custom progress meter')],
          [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar')],
          [sg.Cancel()]]

# create the window`
window = sg.Window('Custom Progress Meter', layout)
progress_bar = window['progressbar']
# loop that would normally do something useful
for i in range(1000):
    # check to see if the cancel button was clicked and exit loop if clicked
    event, values = window.read(timeout=10)
    if event == 'Cancel'  or event == sg.WIN_CLOSED:
        break
  # update bar with loop value +1 so that bar eventually reaches the maximum
    progress_bar.UpdateBar(i + 1)
# done with loop... need to destroy the window as it's still open
window.close()
</code></pre>

<p><img alt="progress custom" src="https://user-images.githubusercontent.com/13696193/45243969-c3508100-b2c3-11e8-82bc-927d0307e093.jpg" /></p>
<h2 id="output-element">Output Element</h2>
<p>The Output Element is a re-direction of Stdout.</p>
<p>If you are looking for a way to quickly add the ability to show scrolling text within your window, then adding an <code>Output</code> Element is about as quick and easy as it gets.</p>
<p><strong>Anything "printed" will be displayed in this element.</strong>  This is the "trivial" way to show scrolling text in your window.  It's as easy as dropping an Output Element into your window and then calling print as much as you want.  The user will see a scrolling area of text inside their window.</p>
<p><strong><em>IMPORTANT</em></strong>  You will NOT see what you <code>print</code> until you call either <code>window.read</code> or <code>window.Refresh</code>.  If you want to immediately see what was printed, call <code>window.Refresh()</code> immediately after your print statement.</p>
<pre><code class="python">Output(size=(80,20))
</code></pre>

<p><img alt="output" src="https://user-images.githubusercontent.com/13696193/44959863-b72f8280-aec3-11e8-8caa-7bc743149953.jpg" /></p>
<hr />
<p>Here's a complete solution for a chat-window using an Output Element.  To display data that's received, you would to simply "print" it and it will show up in the output area.  You'll find this technique used in several Demo Programs including the HowDoI application.</p>
<pre><code class="python">import PySimpleGUI as sg

def ChatBot():
    layout = [[(sg.Text('This is where standard out is being routed', size=[40, 1]))],
              [sg.Output(size=(80, 20))],
              [sg.Multiline(size=(70, 5), enter_submits=True),
               sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
               sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

    window = sg.Window('Chat Window', layout, default_element_size=(30, 2))

    # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
    while True:
        event, value = window.read()
        if event == 'SEND':
            print(value)
        else:
            break
    window.close()
ChatBot()
</code></pre>

<h2 id="column-element-frame-tab-container-elements">Column Element &amp; Frame, Tab "Container" Elements</h2>
<p>Columns and Frames and Tabs are all "Container Elements" and behave similarly.  This section focuses on Columns but can be applied elsewhere.</p>
<p>Starting in version 2.9 you'll be able to do more complex layouts by using the Column Element.  Think of a Column as a window within a window.  And, yes, you can have a Column within a Column if you want.</p>
<p>Columns are specified, like all "container elements", in exactly the same way as a window, as a list of lists.</p>
<p>Columns are needed when you want to specify more than 1 element in a single row.  </p>
<p>For example, this layout has a single slider element that spans several rows followed by 7 <code>Text</code> and <code>Input</code> elements on the same row.</p>
<p><img alt="column" src="https://user-images.githubusercontent.com/13696193/44959988-66b92480-aec5-11e8-9c26-316ed24a68c0.jpg" /></p>
<p>Without a Column Element you can't create a layout like this.  But with it, you should be able to closely match any layout created using tkinter only.</p>
<pre><code class="python">
import PySimpleGUI as sg

# Demo of how columns work
# window has on row 1 a vertical slider followed by a COLUMN with 7 rows
# Prior to the Column element, this layout was not possible
# Columns layouts look identical to window layouts, they are a list of lists of elements.

window = sg.Window('Columns')                                   # blank window

# Column layout
col = [[sg.Text('col Row 1')],
       [sg.Text('col Row 2'), sg.Input('col input 1')],
       [sg.Text('col Row 3'), sg.Input('col input 2')],
       [sg.Text('col Row 4'), sg.Input('col input 3')],
       [sg.Text('col Row 5'), sg.Input('col input 4')],
       [sg.Text('col Row 6'), sg.Input('col input 5')],
       [sg.Text('col Row 7'), sg.Input('col input 6')]]

layout = [[sg.Slider(range=(1,100), default_value=10, orientation='v', size=(8,20)), sg.Column(col)],
          [sg.In('Last input')],
          [sg.OK()]]

# Display the window and get values

window = sg.Window('Compact 1-line window with column', layout)
event, values = window.read()
window.close()

sg.Popup(event, values, line_width=200)

</code></pre>

<h3 id="column-frame-tab-window-element_justification">Column, Frame, Tab, Window element_justification</h3>
<p>Beginning in Release 4.3 you can set the justification for any container element.  This is done through the <code>element_justification</code> parameter.  This will greatly help anyone that wants to center all of their content in a window.  Previously it was difficult to do these kinds of layouts, if not impossible.</p>
<p>justify the <code>Column</code> element's row by setting the <code>Column</code>'s <code>justification</code> parameter.</p>
<p>You can also justify the entire contents within a <code>Column</code> by using the Column's <code>element_justification</code> parameter.</p>
<p>With these parameter's it is possible to create windows that have their contents centered.  Previously this was very difficult to do.</p>
<p>This is currently only available in the primary PySimpleGUI port.</p>
<p>They can also be used to justify a group of elements in a particular way.</p>
<p>Placing <code>Column</code> elements inside <code>Columns</code> elements make it possible to create a multitude of </p>
<h2 id="sizer-element">Sizer Element</h2>
<p>New in 4.3 is the <code>Sizer</code> Element.  This element is used to help create a container of a particular size.  It can be placed inside of these PySimpleGUI items:</p>
<ul>
<li>Column</li>
<li>Frame</li>
<li>Tab</li>
<li>Window</li>
</ul>
<p>The implementation of a <code>Sizer</code> is quite simple.  It returns an empty <code>Column</code> element that has a pad value set to the values passed into the <code>Sizer</code>.  Thus isn't not a class but rather a "Shortcut function" similar to the pre-defined Buttons.</p>
<p>This feature is only available in the tkinter port of PySimpleGUI at the moment.  A cross port is needed.</p>
<hr />
<h2 id="frame-element-labelled-frames-frames-with-a-title">Frame Element (Labelled Frames, Frames with a title)</h2>
<p>Frames work exactly the same way as Columns.  You create layout that is then used to initialize the Frame.  Like a Column element, it's a "Container Element" that holds one or more elements inside.</p>
<p><img alt="frame element" src="https://user-images.githubusercontent.com/13696193/45889173-c2245700-bd8d-11e8-8f73-1e5f1be3ddb1.jpg" /></p>
<p>Notice how the Frame layout looks identical to a window layout. A window works exactly the same way as a Column and a Frame.  They all are "container elements" - elements that contain other elements.</p>
<p><em>These container Elements can be nested as deep as you want.</em> That's a pretty spiffy feature, right?  Took a lot of work so be appreciative.  Recursive code isn't trivial.</p>
<p>This code creates a window with a Frame and 2 buttons.</p>
<pre><code class="python">frame_layout = [
                  [sg.T('Text inside of a frame')],
                  [sg.CB('Check 1'), sg.CB('Check 2')],
               ]
layout = [
          [sg.Frame('My Frame Title', frame_layout, font='Any 12', title_color='blue')],
          [sg.Submit(), sg.Cancel()]
         ]

window = sg.Window('Frame with buttons', layout, font=(&quot;Helvetica&quot;, 12))
</code></pre>

<h2 id="canvas-element">Canvas Element</h2>
<p>In my opinion, the tkinter Canvas Widget is the most powerful of the tkinter widget.  While I try my best to completely isolate the user from anything that is tkinter related, the Canvas Element is the one exception.  It enables integration with a number of other packages, often with spectacular results.</p>
<p>However, there's another way to get that power and that's through the Graph Element, an even MORE powerful Element as it uses a Canvas that you can directly access if needed.  The Graph Element has a large number of drawing methods that the Canvas Element does not have.  Plus, if you need to, you can access the Graph Element's "Canvas" through a member variable.</p>
<h3 id="matplotlib-pyplot-integration">Matplotlib, Pyplot Integration</h3>
<p><strong>NOTE - The newest version of Matplotlib (3.1.0) no longer works with this technique. </strong> You must install 3.0.3 in order to use the Demo Matplotlib programs provided in the Demo Programs section.</p>
<p>One such integration is with Matplotlib and Pyplot.  There is a Demo program written that you can use as a design pattern to get an understanding of how to use the Canvas Widget once you get it.</p>
<pre><code>def Canvas(canvas - a tkinter canvasf if you created one. Normally not set
         background_color - canvas color
         size - size in pixels
         pad - element padding for packing
         key - key used to lookup element
         tooltip - tooltip text)
</code></pre>
<p>The order of operations to obtain a tkinter Canvas Widget is:</p>
<pre><code class="python">
    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
    # define the window layout
    layout = [[sg.Text('Plot test')],
              [sg.Canvas(size=(figure_w, figure_h), key='canvas')],
              [sg.OK(pad=((figure_w / 2, 0), 3), size=(4, 2))]]

    # create the window and show it without the plot
    window = sg.Window('Demo Application - Embedding Matplotlib In PySimpleGUI', layout).Finalize()

    # add the plot to the window
    fig_photo = draw_figure(window['canvas'].TKCanvas, fig)

    # show it all again and get buttons
    event, values = window.read()
</code></pre>

<p>To get a tkinter Canvas Widget from PySimpleGUI, follow these steps:
* Add Canvas Element to your window
* Layout your window
* Call <code>window.Finalize()</code> - this is a critical step you must not forget
* Find the Canvas Element by looking up using key
* Your Canvas Widget Object will be the found_element.TKCanvas
* Draw on your canvas to your heart's content
* Call <code>window.read()</code> - Nothing will appear on your canvas until you call Read</p>
<p>See <code>Demo_Matplotlib.py</code> for a Recipe you can copy.</p>
<h3 id="methods-properties">Methods &amp; Properties</h3>
<p>TKCanvas - not a method but a property. Returns the tkinter Canvas Widget</p>
<h2 id="graph-element">Graph Element</h2>
<p>All you math fans will enjoy this Element... and all you non-math fans will enjoy it even more.</p>
<p>I've found nothing to be less fun than dealing with a graphic's coordinate system from a GUI Framework.  It's always upside down from what I want.  (0,0) is in the upper left hand corner.... sometimes... or was it in the lower left?  In short, it's a <strong>pain in the ass</strong>.</p>
<p>How about the ability to get your own location of (0,0) and then using those coordinates instead of what tkinter provides?  This results in a very powerful capability - working in your own units, and then displaying them in an area defined in pixels.</p>
<p>If you've ever been frustrated with where (0,0) is located on some surface you draw on, then fear not, your frustration ends right here.  You get to draw using whatever coordinate system you want.  Place (0,0) anywhere you want, including not anywhere on your Graph.  You could define a Graph that's all negative numbers between -2.1 and -3.5 in the X axis and -3 to -8.2 in the Y axis</p>
<p>There are 3 values you'll need to supply the Graph Element.  They are:</p>
<ul>
<li>Size of the canvas in pixels</li>
<li>The lower left (x,y) coordinate of your coordinate system</li>
<li>The upper right (x,y) coordinate of your coordinate system</li>
</ul>
<p>After you supply those values you can scribble all of over your graph by creating Graph Figures.  Graph Figures are created, and a Figure ID is obtained by calling:</p>
<ul>
<li>DrawCircle</li>
<li>DrawLine</li>
<li>DrawPoint</li>
<li>DrawRectangle</li>
<li>DrawOval</li>
<li>DrawImage</li>
</ul>
<p>You can move your figures around on the canvas by supplying the Figure ID the <strong>x,y delta</strong> to move.  It does not move to an absolute position, but rather an offset from where the figure is now.  (Use Relocate to move to a specific location)</p>
<pre><code>graph.MoveFigure(my_circle, 10, 10)
</code></pre>
<p>You'll also use this ID to delete individual figures you've drawn:</p>
<pre><code class="python">graph.DeleteFigure(my_circle)
</code></pre>

<h3 id="mouse-events-inside-graph-elements">Mouse Events Inside Graph Elements</h3>
<p>If you have enabled events for your Graph Element, then you can receive mouse click events.  If you additionally enable <code>drag_submits</code> in  your creation of the Graph Element, then you will also get events when you "DRAG" inside of a window.  A "Drag" is defined as a left button down and then the mouse is moved.  </p>
<p>When a drag event happens, the event will be the Graph Element's key.  The <code>value</code> returned in the values dictionary is a tuple of the (x,y) location of the mouse currently.</p>
<p>This means you'll get a "stream" of events.  If the mouse moves, you'll get at LEAST 1 and likely a lot more than 1 event.</p>
<h3 id="mouse-up-event-for-drags">Mouse Up Event for Drags</h3>
<p>When you've got <code>drag_submits</code> enabled, there's a sticky situation that arises.... what happens when you're done dragging and you've let go of the mouse button?  How is the "Mouse Up" event relayed back to your code.</p>
<p>The "Mouse Up" will generate an event to you with the value:  <code>Graph_key</code> + <code>'+UP'</code>.  Thus, if your Graph Element has a key of <code>'_GRAPH_'</code>, then the event you will receive when the mouse button is released is:   <code>'_GRAPH_+UP'</code></p>
<p>Yea, it's a little weird, but it works.  It's SIMPLE too.  I recommend using the <code>.startswith</code> and <code>.endswith</code> built-ins when dealing with these kinds of string values.</p>
<p>Here is an example of the <code>events</code> and the <code>values dictionary</code> that was generated by clicking and dragging inside of a Graph Element with the key == 'graph':</p>
<pre><code>graph {'graph': (159, 256)}
graph {'graph': (157, 256)}
graph {'graph': (157, 256)}
graph {'graph': (157, 254)}
graph {'graph': (157, 254)}
graph {'graph': (154, 254)}
graph {'graph': (154, 254)}
graph+UP {'graph': (154, 254)}
</code></pre>

<h2 id="table-element">Table Element</h2>
<p>Table and Tree Elements are of the most complex in PySimpleGUI.  They have a lot of options and a lot of unusual characteristics.</p>
<h3 id="windowread-return-values-from-table-element"><code>window.read()</code> return values from Table Element</h3>
<p>The values returned from a <code>Window.read</code> call for the Table Element are a list of row numbers that are currently highlighted.</p>
<h3 id="the-qt-tableget-call">The Qt <code>Table.Get()</code> call</h3>
<p>New in <strong>PySimpleGUIQt</strong> is the addition of the <code>Table</code> method <code>Get</code>.  This method returns the table that is currently being shown in the GUI.  This method was required in order to obtain any edits the user may have made to the table.</p>
<p>For the tkinter port, it will return the same values that was passed in when the table was created because tkinter Tables cannot be modified by the user (please file an Issue if you know a way).</p>
<h3 id="known-table-visualization-problem">Known <code>Table</code> visualization problem....</h3>
<p>There has been an elusive problem where clicking on or near the table's header caused tkinter to go crazy and resize the columns continuously as you moved the mouse.</p>
<p>This problem has existed since the first release of the <code>Table</code> element.  It was fixed in release 4.3.</p>
<h3 id="known-table-colors-in-python-373-374-38">Known table colors in Python 3.7.3, 3.7.4, 3.8, ?</h3>
<p>The tkinter that's been released in the past several releases of Python has a bug.  Table colors of all types are not working, at all.  The background of the rows never change.  If that's important to you, you'll need to <strong>downgrade</strong> your Python version.  3.6 works really well with PySimpleGUI and tkinter.</p>
<h3 id="empty-tables">Empty Tables</h3>
<p>If you wish to start your table as being an empty one, you will need to specify an empty table.  This list comprehension will create an empty table with 15 rows and 6 columns.</p>
<pre><code class="python">data = [['' for row in range(15)]for col in range(6)]
</code></pre>

<h3 id="events-from-tables">Events from Tables</h3>
<p>There are two ways to get events generated from Table Element.<br />
<code>change_submits</code> event generated as soon as a row is clicked on
<code>bind_return_key</code> event generate when a row is double clicked or the return key is press while on a row.</p>
<h2 id="tree-element">Tree Element</h2>
<p>The Tree Element and Table Element are close cousins.   Many of the parameters found in the Table Element apply to Tree Elements.  In particular the heading information, column widths, etc..</p>
<p>Unlike Tables there is no standard format for trees.  Thus the data structure passed to the Tree Element must be constructed.  This is done using the TreeData class.  The process is as follows:</p>
<ul>
<li>Get a TreeData Object</li>
<li>"Insert" data into the tree</li>
<li>Pass the filled in TreeData object to Tree Element</li>
</ul>
<h4 id="treedata-format">TreeData format</h4>
<pre><code class="python">def TreeData()
def Insert(self, parent, key, text, values, icon=None)
</code></pre>

<p>To "insert" data into the tree the TreeData method Insert is called.</p>
<pre><code class="python">Insert(parent_key, key, display_text, values)
</code></pre>

<p>To indicate insertion at the head of the tree, use a parent key of "".  So, every top-level node in the tree will have a parent node = ""</p>
<p>This code creates a TreeData object and populates with 3 values</p>
<pre><code class="python">treedata = sg.TreeData()

treedata.Insert(&quot;&quot;, '_A_', 'A', [1,2,3])
treedata.Insert(&quot;&quot;, '_B_', 'B', [4,5,6])
treedata.Insert(&quot;_A_&quot;, '_A1_', 'A1', ['can','be','anything'])
</code></pre>

<p>Note that you <strong><em>can</em></strong> use the same values for display_text and keys.  The only thing you have to watch for is that you cannot repeat keys.</p>
<p>When Reading a window the Table Element will return a list of rows that are selected by the user.  The list will be empty is no rows are selected.</p>
<h4 id="icons-on-tree-entries">Icons on Tree Entries</h4>
<p>If you wish to show an icon next to a tree item, then you specify the icon in the call to <code>Insert</code>.  You pass in a filename or a Base64 bytes string using the optional <code>icon</code> parameter.</p>
<p>Here is the result of showing an icon with a tree entry.</p>
<p><img alt="image" src="https://user-images.githubusercontent.com/13696193/51087270-2b561e80-171f-11e9-8260-6142ea9b1137.png" /></p>
<h2 id="tab-and-tab-group-elements">Tab and Tab Group Elements</h2>
<p>Tabs are another of PySimpleGUI "Container Elements".  It is capable of "containing" a layout just as a window contains a layout.  Other container elements include the <code>Column</code> and <code>Frame</code> elements.</p>
<p>Just like windows and the other container elements, the <code>Tab</code> Element has a layout consisting of any desired combination of Elements in any desired layouts.  You can have Tabs inside of Tabs inside of Columns inside of Windows, etc..</p>
<p><code>Tab</code> layouts look exactly like Window layouts, that is they are <strong>a list of lists of Elements</strong>.</p>
<p><em>How you place a Tab element into a window is different than all other elements.</em>  You cannot place a Tab directly into a Window's layout.  </p>
<p>Also, tabs cannot be made invisible at this time.  They have a visibility parameter but calling update will not change it.</p>
<p>Tabs are contained in TabGroups.  They are <strong>not</strong> placed into other layouts.  To get a Tab into your window, first place the <code>Tab</code> Element into a <code>TabGroup</code> Element and then place the <code>TabGroup</code> Element into the Window layout.</p>
<p>Let's look at this Window as an example:</p>
<p><img alt="tabbed 1" src="https://user-images.githubusercontent.com/13696193/45992808-b10f6a80-c059-11e8-9746-ac71afd4d3d6.jpg" /></p>
<p>View of second tab:</p>
<p><img alt="tabbed 2" src="https://user-images.githubusercontent.com/13696193/45992809-b10f6a80-c059-11e8-94e6-3bf543c9b0bd.jpg" /></p>
<pre><code class="python">tab1_layout =  [[sg.T('This is inside tab 1')]]

tab2_layout = [[sg.T('This is inside tab 2')],
               [sg.In(key='in')]]

</code></pre>

<p>The layout for the entire window looks like this:</p>
<pre><code class="python">layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]])],
              [sg.Button('Read')]]
</code></pre>

<p>The Window layout has the TabGroup and within the tab Group are the two Tab elements.</p>
<p>One important thing to notice about all of these container Elements and Windows layouts... they all take a "list of lists" as the layout.  They all have a layout that looks like this <code>[[   ]]</code></p>
<p>You will want to keep this <code>[[ ]]</code> construct in your head a you're debugging your tabbed windows.  It's easy to overlook one or two necessary ['s</p>
<p>As mentioned earlier, the old-style Tabs were limited to being at the Window-level only.  In other words, the tabs were equal in size to the entire window.  This is not the case with the "new-style" tabs.  This is why you're not going to be upset when you discover your old code no longer works with the new PySimpleGUI release.  It'll be worth the few moments it'll take to convert your code.</p>
<p>Check out what's possible with the NEW Tabs!</p>
<p><img alt="tabs tabs tabs" src="https://user-images.githubusercontent.com/13696193/45993438-fd0fde80-c05c-11e8-9ed0-742f14d3070f.jpg" /></p>
<p>Check out Tabs 7 and 8.  We've got a Window with a Column containing Tabs 5 and 6.  On Tab 6 are... Tabs 7 and 8.</p>
<p>As of Release 3.8.0, not all of <em>options</em> shown in the API definitions of the Tab and TabGroup Elements are working. They are there as placeholders.</p>
<p>First we have the Tab layout definitions. They mirror what you see in the screen shots.  Tab 1 has 1 Text Element in it.  Tab 2 has a Text and an Input Element.</p>
<h3 id="reading-tab-groups">Reading Tab Groups</h3>
<p>Tab Groups now return a value when a Read returns.  They return which tab is currently selected.  There is also a <code>enable_events</code> parameter that can be set that causes a Read to return if a Tab in that group is selected / changed.  The key or title belonging to the Tab that was switched to will be returned as the value</p>
<p>x## Pane Element</p>
<p>New in version 3.20 is the Pane Element, a super-cool tkinter feature.  You won't find this one in PySimpleGUIQt, only PySimpleGUI.   It's difficult to describe one of these things.  Think of them as "Tabs without labels" that you can slide.</p>
<p><img alt="pane3" src="https://user-images.githubusercontent.com/13696193/50035040-fcd50e80-ffcd-11e8-939c-df8ab8d64712.gif" /></p>
<p><strong><em>Each "Pane" of a Pane Element must be a Column Element</em></strong>.  The parameter <code>pane_list</code> is a list of Column Elements.</p>
<p>Calls can get a little hairy looking if you try to declare everything in-line as you can see in this example.</p>
<pre><code class="python">sg.Pane([col5, sg.Column([[sg.Pane([col1, col2, col4], handle_size=15, orientation='v',  background_color=None, show_handle=True, visible=True, key='_PANE_', border_width=0,  relief=sg.RELIEF_GROOVE),]]),col3 ], orientation='h', background_color=None, size=(160,160), relief=sg.RELIEF_RAISED, border_width=0)
</code></pre>

<p>Combing these with <em>visibility</em> make for an interesting interface with entire panes being hidden from view until neded by the user.  It's one way of producing "dynamic" windows.</p>
<h2 id="colors_1">Colors</h2>
<p>Starting in version 2.5 you can change the background colors for the window and the Elements.</p>
<p>Your windows can go from this:</p>
<p><img alt="snap0155" src="https://user-images.githubusercontent.com/13696193/43273879-a9fdc10a-90cb-11e8-8c20-4f6a244ebe2f.jpg" /></p>
<p>to this... with one function call...</p>
<p><img alt="snap0156" src="https://user-images.githubusercontent.com/13696193/43273880-aa1955e6-90cb-11e8-94b6-673ecdb2698c.jpg" /></p>
<p>While you can do it on an element by element or window level basis, the easier way is to use either the <code>theme</code> calls or <code>set_options</code>.  These calls will set colors for all window that are created.</p>
<p>Be aware that once you change these options they are changed for the rest of your program's execution.  All of your windows will have that Theme, until you change it to something else.</p>
<p>This call sets a number of the different color options.</p>
<pre><code class="python">SetOptions(background_color='#9FB8AD',
       text_element_background_color='#9FB8AD',
       element_background_color='#9FB8AD',
       scrollbar_color=None,
       input_elements_background_color='#F7F3EC',
       progress_meter_color = ('green', 'blue')
       button_color=('white','#475841'))
</code></pre>

<h1 id="systemtray">SystemTray</h1>
<p>In addition to running normal windows, it's now also possible to have an icon down in the system tray that you can read to get menu events.  There is a new SystemTray object that is used much like a Window object.  You first get one, then you perform Reads in order to get events.</p>
<h2 id="tkinter-version">Tkinter version</h2>
<p>While only PySimpleGUIQt and PySimpleGUIWx offer a true "system tray" feature, there is a simulated system tray feature that became available in 2020 for the tkinter version of PySimpleGUI.  All of the same objects and method calls are the same and the effect is very similar to what you see with the Wx and Qt versions.  The icon is placed in the bottom right corner of the window.  Setting the location of it has not yet been exposed, but you can drag it to another location on your screen.</p>
<p>The idea of supporting Wx, Qt, and tkinter with the exact same source code is very appealing and is one of the reasons a tkinter version was developed.  You can switch frameworks by simply changing your import statement to any of those 3 ports.</p>
<p>The balloons shown for the tkinter version is different than the message balloons shown by real system tray icons.  Instead a nice semi-transparent window is shown.  This window will fade in / out and is the same design as the one found in the <a href="https://github.com/PySimpleGUI/ptoaster">ptoaster package</a>.</p>
<h2 id="systemtray-object">SystemTray Object</h2>
<p>Here is the definition of the SystemTray object.</p>
<pre><code class="python">SystemTray(menu=None, filename=None, data=None, data_base64=None, tooltip=None,  metadata=None):
        '''
 SystemTray - create an icon in the system tray
 :param menu: Menu definition
 :param filename: filename for icon
 :param data: in-ram image for icon
 :param data_base64: basee-64 data for icon
 :param tooltip: tooltip string 
 :param metadata: (Any) User metadata that can be set to ANYTHING
'''
</code></pre>

<p>You'll notice that there are 3 different ways to specify the icon image.  The base-64 parameter allows you to define a variable in your .py code that is the encoded image so that you do not need any additional files.  Very handy feature.</p>
<h2 id="system-tray-design-pattern">System Tray Design Pattern</h2>
<p>Here is a design pattern you can use to get a jump-start.</p>
<p>This program will create a system tray icon and perform a blocking Read.  If the item "Open" is chosen from the system tray, then a popup is shown.</p>
<p>The same code can be executed on any of the Desktop versions of PySimpleGUI (tkinter, Qt, WxPython)</p>
<pre><code class="python">import PySimpleGUIQt as sg
# import PySimpleGUIWx as sg
# import PySimpleGUI as sg

menu_def = ['BLANK', ['&amp;Open', '---', '&amp;Save', ['1', '2', ['a', 'b']], '&amp;Properties', 'E&amp;xit']]

tray = sg.SystemTray(menu=menu_def, filename=r'default_icon.ico')

while True:  # The event loop
    menu_item = tray.read()
    print(menu_item)
    if menu_item == 'Exit':
        break
    elif menu_item == 'Open':
        sg.popup('Menu item chosen', menu_item)

</code></pre>

<p>The design pattern creates an icon that will display this menu:
<img alt="snag-0293" src="https://user-images.githubusercontent.com/13696193/49057441-8bbfe980-f1cd-11e8-93e7-1aeda9ccd173.jpg" /></p>
<h3 id="icons-for-system-trays">Icons for System Trays</h3>
<p>System Tray Icons are in PNG &amp; GIF format when running on PySimpleGUI (tkinter version).  PNG, GIF, and ICO formats will work for the Wx and Qt ports.</p>
<p>When specifying "icons", you can use 3 different formats.
* <code>filename</code>- filename
* <code>data_base64</code> - base64 byte string
* '<code>data</code> - in-ram bitmap or other "raw" image</p>
<p>You will find 3 parameters used to specify these 3 options on both the initialize statement and on the Update method.</p>
<p>For testing you may find using the built-in PySimpleGUI icon is a good place to start to make sure you've got everything coded correctly before bringing in outside image assets. It'll tell you quickly if you've got a problem with your icon file.  To run using the default icon, use something like this to create the System Tray:</p>
<pre><code class="python">tray = sg.SystemTray(menu=menu_def, data_base64=sg.DEFAULT_BASE64_ICON)
</code></pre>

<h2 id="menu-definition">Menu Definition</h2>
<pre><code class="python">menu_def = ['BLANK', ['&amp;Open', '&amp;Save', ['1', '2', ['a', 'b']], '!&amp;Properties', 'E&amp;xit']]
</code></pre>

<p>A menu is defined using a list.  A "Menu entry" is a string that specifies:
* text shown
* keyboard shortcut
* key</p>
<p>See section on Menu Keys for more information on using keys with menus.</p>
<p>An entry without a key and keyboard shortcut is a simple string
<code>'Menu Item'</code></p>
<p>If you want to make the "M" be a keyboard shortcut, place an <code>&amp;</code> in front of the letter that is the shortcut.
<code>'&amp;Menu Item'</code></p>
<p>You can add "keys" to make menu items unique or as another way of identifying a menu item than the text shown.  The key is added to the text portion by placing <code>::</code> after the text.</p>
<p><code>'Menu Item::key'</code></p>
<p>The first entry can be ignored.<code>'BLANK</code>' was chosen for this example. It's this way because normally you would specify these menus under some heading on a menu-bar.  But here there is no heading so it's filled in with any value you want.</p>
<p><strong>Separators</strong>
If you want a separator between 2 items, add the entry <code>'---'</code> and it will add a separator item at that place in your menu.</p>
<p><strong>Disabled menu entries</strong></p>
<p>If you want to disable a menu entry, place a <code>!</code> before the menu entry</p>
<h2 id="systemtray-methods">SystemTray Methods</h2>
<h3 id="read-read-the-context-menu-or-check-for-events">Read - Read the context menu or check for events</h3>
<pre><code class="python">def Read(timeout=None)
    '''
 Reads the context menu
 :param timeout: Optional.  Any value other than None indicates a non-blocking read
 :return:   String representing meny item chosen. None if nothing read.
    '''
</code></pre>

<p>The <code>timeout</code> parameter specifies how long to wait for an event to take place.  If nothing happens within the timeout period, then a "timeout event" is returned.  These types of reads make it possible to run asynchronously.  To run non-blocked, specify <code>timeout=0</code>on the Read call.</p>
<p>Read returns the menu text, complete with key, for the menu item chosen.  If you specified <code>Open::key</code> as the menu entry, and the user clicked on <code>Open</code>, then you will receive the string <code>Open::key</code> upon completion of the Read.</p>
<h4 id="read-special-return-values">Read special return values</h4>
<p>In addition to Menu Items, the Read call can return several special values.    They include:</p>
<p>EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED - Tray icon was double clicked
EVENT_SYSTEM_TRAY_ICON_ACTIVATED - Tray icon was single clicked
EVENT_SYSTEM_TRAY_MESSAGE_CLICKED - a message balloon was clicked
TIMEOUT_KEY is returned if no events are available if the timeout value is set in the Read call</p>
<h3 id="hide">Hide</h3>
<p>Hides the icon.  Note that no message balloons are shown while an icon is hidden.</p>
<pre><code class="python">def Hide()
</code></pre>

<h3 id="close">Close</h3>
<p>Does the same thing as hide</p>
<pre><code class="python">def Close()
</code></pre>

<h3 id="unhide">UnHide</h3>
<p>Shows a previously hidden icon</p>
<pre><code class="python">def UnHide()
</code></pre>

<h3 id="showmessage">ShowMessage</h3>
<p>Shows a balloon above the icon in the system tray area.  You can specify your own icon to be shown in the balloon, or you can set <code>messageicon</code> to one of the preset values.</p>
<p>This message has a custom icon.</p>
<p><img alt="snag-0286" src="https://user-images.githubusercontent.com/13696193/49057459-a85c2180-f1cd-11e8-9a66-aa331d7e034c.jpg" /></p>
<p>The preset <code>messageicon</code> values are:</p>
<pre><code>SYSTEM_TRAY_MESSAGE_ICON_INFORMATION
SYSTEM_TRAY_MESSAGE_ICON_WARNING
SYSTEM_TRAY_MESSAGE_ICON_CRITICAL
SYSTEM_TRAY_MESSAGE_ICON_NOICON
</code></pre>
<pre><code class="python">ShowMessage(title, message, filename=None, data=None, data_base64=None, messageicon=None, time=10000):
'''
 Shows a balloon above icon in system tray
 :param title:  Title shown in balloon
 :param message: Message to be displayed
 :param filename: Optional icon filename
 :param data: Optional in-ram icon
 :param data_base64: Optional base64 icon
 :param time: How long to display message in milliseconds  :return:
 '''
</code></pre>

<p>Note, on windows it may be necessary to make a registry change to enable message balloons to be seen.  To fix this, you must create the DWORD you see in this screenshot.</p>
<p><img alt="snag-0285" src="https://user-images.githubusercontent.com/13696193/49056144-6381bc00-f1c8-11e8-9f44-199394823369.jpg" /></p>
<h3 id="update">Update</h3>
<p>You can update any of these items within a SystemTray object
* Menu definition
* Icon
* Tooltip</p>
<p>Change them all or just 1.</p>
<h3 id="notify-class-method">Notify Class Method</h3>
<p>In addition to being able to show messages via the system tray, the tkinter port has the added capability of being able to display the system tray messages without having a system tray object defined.  You can simply show a notification window.  This perhaps removes the need for using the ptoaster package?</p>
<p>The method is a "class method" which means you can call it directly without first creating an instanciation of the object.  To show a notification window, call <code>SystemTray.notify</code>.</p>
<p>This line of code</p>
<pre><code class="python">sg.SystemTray.notify('Notification Title', 'This is the notification message')
</code></pre>

<p>Will show this window, fading it in and out:</p>
<p><img alt="image" src="https://user-images.githubusercontent.com/46163555/74970862-2321e580-53ed-11ea-99ba-1581a05575f0.png" /></p>
<p>This is a blocking call so expect it to take a few seconds if you're fading the window in and out.  There are options to control the fade, how long things are displayed, the alpha channel, etc..  See the call signature at the end of this document.</p>
<h1 id="global-settings">Global Settings</h1>
<p>There are multiple ways to customize PySimpleGUI.  The call with the most granularity (allows access to specific and precise settings).  The <code>ChangeLookAndFeel</code> call is in reality a single call to <code>SetOptions</code> where it changes 13 different settings.  </p>
<p><strong>Mac Users</strong> - You can't call <code>ChangeLookAndFeel</code> but you can call <code>SetOptions</code> with any sets of values you want.  Nothing is being blocked or filtered.</p>
<p><strong>These settings apply to all windows that are created in the future.</strong></p>
<p><code>SetOptions</code>.  The  options and Element options will take precedence over these settings.  Settings can be thought of as levels of settings with the window-level being the highest and the Element-level the lowest.  Thus the levels are:</p>
<ul>
<li>Global</li>
<li>Window</li>
<li>Element</li>
</ul>
<p>Each lower level overrides the settings of the higher level.  Once settings have been changed, they remain changed for the duration of the program (unless changed again).</p>
<h1 id="persistent-windows-window-stays-open-after-button-click">Persistent windows (Window stays open after button click)</h1>
<p>Early versions of PySimpleGUI did not have a concept of "persisent window". Once a user clicked a button, the window would close.  After some time, the functionality was expanded so that windows remained open by default.</p>
<h2 id="input-fields-that-auto-clear">Input Fields that Auto-clear</h2>
<p>Note that <code>InputText</code> and <code>MultiLine</code> Elements can be <strong>cleared</strong> when performing a <code>read</code>.  If you want your input field to be cleared after a <code>window.read</code> then you can set the <code>do_not_clear</code> parameter to False when creating those elements. The clear is turned on and off on an element by element basis.</p>
<p>The reasoning behind this is that Persistent Windows are often "forms".  When "submitting" a form you want to have all of the fields left blank so the next entry of data will start with a fresh window.  Also, when implementing a "Chat Window" type of interface, after each read / send of the chat data, you want the input field cleared.  Think of it as a Texting application.  Would you want to have to clear your previous text if you want to send a second text?</p>
<h2 id="basic-persistent-window-design-pattern">Basic Persistent Window Design Pattern</h2>
<p>The design pattern for Persistent Windows was already shown to you earlier in the document... here it is for your convenience.</p>
<pre><code class="python">import PySimpleGUI as sg

layout = [[sg.Text('Persistent window')],
          [sg.Input()],
          [sg.Button('Read'), sg.Exit()]]

window = sg.Window('Window that stays open', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

window.close()
</code></pre>

<h2 id="readtimeout-t-timeout_keytimeout_key-closefalse">Read(timeout = t, timeout_key=TIMEOUT_KEY, close=False)</h2>
<p>Read with a timeout is a very good thing for your GUIs to use in a non-blocking read situation.  If your device can wait for a little while, then use this kind of read.  The longer you're able to add to the timeout value, the less CPU time you'll be taking.  </p>
<p>The idea to wait for some number of milliseconds before returning.  It's a trivial way to make a window that runs on a periodic basis.</p>
<p>One way of thinking of reads with timeouts:</p>
<blockquote>
<p>During the timeout time, you are "yielding" the processor to do other tasks.</p>
</blockquote>
<p>But it gets better than just being a good citizen....<strong>your GUI will be more responsive than if you used a non-blocking read</strong></p>
<p>Let's say you had a device that you want to "poll" every 100ms.   The "easy way out" and the only way out until recently was this:</p>
<pre><code class="python"># YOU SHOULD NOT DO THIS....
while True:             # Event Loop
    event, values = window.ReadNonBlocking()   # DO NOT USE THIS CALL ANYMORE
    read_my_hardware() # process my device here
    time.sleep(.1)     # sleep 1/10 second  DO NOT PUT SLEEPS IN YOUR EVENT LOOP!
</code></pre>

<p>This program will quickly test for user input, then deal with the hardware.  Then it'll sleep for 100ms, while your gui is non-responsive, then it'll check in with your GUI again.  </p>
<p>The better way using PySimpleGUI... using the Read Timeout mechanism, the sleep goes away.</p>
<pre><code class="python"># This is the right way to poll for hardware
while True:             # Event Loop
    event, values = window.read(timeout = 100)
    read_my_hardware() # process my device here
</code></pre>

<p>This event loop will run every 100 ms.  You're making a <code>read</code> call, so anything that the use does will return back to you immediately, and you're waiting up to 100ms for the user to do something.  If the user doesn't do anything, then the read will timeout and execution will return to the program.</p>
<h2 id="sgtimeout_key">sg.TIMEOUT_KEY</h2>
<p>If you're using a read with a timeout value, then an event value of None signifies that the window was closed, just like a normal <code>window.read</code>.  That leaves the question of what it is set to when not other events are happening.  This value will be the value of <code>TIMEOUT_KEY</code>.  If you did not specify a timeout_key value in your call to read, then it will be set to a default value of:
<code>TIMEOUT_KEY = __timeout__</code></p>
<p>If you wanted to test for "no event" in your loop, it would be written like this:</p>
<pre><code class="python">while True:
    event, value = window.read(timeout=10)
    if event == sg.WIN_CLOSED:
        break # the use has closed the window
    if event == sg.TIMEOUT_KEY:
        print(&quot;Nothing happened&quot;)
</code></pre>

<p>Use async windows sparingly.  It's possible to have a window that appears to be async, but it is not.  <strong>Please</strong> try to find other methods before going to async windows.  The reason for this plea is that async windows poll tkinter over and over.  If you do not have a timeout in your Read and you've got nothing else your program will block on, then you will eat up 100% of the CPU time. It's important to be a good citizen.   Don't chew up CPU cycles needlessly.  Sometimes your mouse wants to move ya know?</p>
<h3 id="readtimeout0"><code>read(timeout=0)</code></h3>
<p>You may find some PySimpleGUI programs that set the timeout value to zero.  This is a very dangerous thing to do.  If you do not pend on something else in your event loop, then your program will consume 100% of your CPU.  Remember that today's CPUs are multi-cored.  You may see only 7% of your CPU is busy when you're running with timeout of 0.  This is because task manager is reporting a system-wide CPU usage.  The single core your program is running on is likely at 100%.</p>
<p>A true non-blocking (timeout=0) read is generally reserved as a "last resort".  Too many times people use non-blocking reads when a blocking read will do just fine or a read with a timeout would work.</p>
<p>It's valid to use a timeout value of zero if you're in need of every bit of CPU horsepower in your application.  Maybe your loop is doing something super-CPU intensive and you can't afford for the GUI to use any CPU time. This is the kind of situation where a timeout of zero is appropriate.  </p>
<p>Be a good computing citizen.  Run with a non-zero timeout so that other programs on your CPU will have time to run.</p>
<h3 id="small-timeout-values-under-10ms">Small Timeout Values (under 10ms)</h3>
<p><strong><em>Do Not</em></strong> use a timeout of less than 10ms.  Otherwise you will simply thrash, spending your time trying to do some GUI stuff, only to be interruped by a timeout timer before it can get anything done.  The results are potentially disasterous.</p>
<p>There is a hybrid approach... a read with a timeout.   You'll score much higher points on the impressive meter if you're able to use a lot less CPU time by using this type of read.</p>
<p>The most legit time to use a non-blocking window is when you're working directly with hardware.  Maybe you're driving a serial bus.  If you look at the Event Loop in the Demo_OpenCV_Webcam.py program, you'll see that the read is a non-blocking read.  However, there is a place in the event loop where blocking occurs.   The point in the loop where you will block is the call to read frames from the webcam.  When a frame is available you want to quickly deliver it to the output device, so you don't want your GUI blocking.  You want the read from the hardware to block.</p>
<p>Another example can be found in the demo for controlling a robot on a Raspberry Pi.  In that application you want to read the direction buttons, forward, backward, etc., and immediately take action.  If you are using RealtimeButtons, your only option at the moment is to use non-blocking windows.  You have to set the timeout to zero if you want the buttons to be real-time responsive.</p>
<p>However, with these buttons, adding a sleep to your event loop will at least give other processes time to execute.  It will, however, starve your GUI. The entire time you're sleeping, your GUI isn't executing.</p>
<h3 id="periodically-callingread">Periodically Calling<code>Read</code></h3>
<p>Let's say you do end up using non-blocking reads... then you've got some housekeeping to do.  It's up to you to periodically "refresh" the visible GUI.  The longer you wait between updates to your GUI the more sluggish your windows will feel.  It is up to you to make these calls or your GUI will freeze.</p>
<p>There are 2 methods of interacting with non-blocking windows.
1. Read the window just as you would a normal window
2. "Refresh" the window's values without reading the window. It's a quick operation meant to show the user the latest values</p>
<p>With asynchronous windows the window is shown, user input is read, but your code keeps right on chugging.  YOUR responsibility is to call <code>PySimpleGUI.read</code> on a periodic basis.  Several times a second or more will produce a reasonably snappy GUI.</p>
<p>## Exiting (Closing) a Persistent Window</p>
<p>If your window has a special button that closes the window, then PySimpleGUI will automatically close the window for you.  If all of your buttons are normal <code>Button</code> elements, then it'll be up to you to close the window when done.</p>
<p>To close a window, call the <code>close</code> method.</p>
<pre><code class="python">window.close()
</code></pre>

<p>Beginning in version 4.16.0 you can use a <code>close</code> parameter in the <code>window.read</code> call to indicate that the window should be closed before returning from the read.  This capability to an excellent way to make a single line Window to quickly get information.</p>
<p>This single line of code will display a window, get the user's input, close the window, and return the values as an event and a values dictionary.</p>
<pre><code class="python">event, values = sg.Window('Login Window',
                  [[sg.T('Enter your Login ID'), sg.In(key='-ID-')],
                  [sg.B('OK'), sg.B('Cancel') ]]).read(close=True)

login_id = values['-ID-']
</code></pre>

<p>You can also make a custom popup quite easily:</p>
<pre><code class="python">long_string = '123456789 '* 40

event, values = sg.Window('This is my customn popup',
                  [[sg.Text(long_string, size=(40,None))],
                  [sg.B('OK'), sg.B('Cancel') ]]).read(close=True)
</code></pre>

<p>Notice the height parameter of size is <code>None</code> in this case.  For the tkinter port of PySimpleGUI this will cause the number of rows to "fit" the contents of the string to be displayed.</p>
<h2 id="persistent-window-example-running-timer-that-updates">Persistent Window Example - Running timer that updates</h2>
<p>See the sample code on the GitHub named Demo Media Player for another example of Async windows.  We're going to make a window and update one of the elements of that window every .01 seconds.    Here's the entire code to do that.</p>
<pre><code class="python">import PySimpleGUI as sg
import time

# ----------------  Create Form  ----------------
sg.ChangeLookAndFeel('Black')
sg.SetOptions(element_padding=(0, 0))

layout = [[sg.Text('')],
         [sg.Text(size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
         [sg.Button('Pause', key='button', button_color=('white', '#001480')),
          sg.Button('Reset', button_color=('white', '#007339'), key='Reset'),
          sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]]

window = sg.Window('Running Timer', layout, no_titlebar=True, auto_size_buttons=False, keep_on_top=True, grab_anywhere=True)

# ----------------  main loop  ----------------
current_time = 0
paused = False
start_time = int(round(time.time() * 100))
while (True):
    # --------- Read and update window --------
    event, values = window.read(timeout=10)
    current_time = int(round(time.time() * 100)) - start_time
    # --------- Display timer in window --------
    window['text'].update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
                                                                  (current_time // 100) % 60,
                                                                  current_time % 100))
</code></pre>

<p>Previously this program was implemented using a sleep in the loop to control the clock tick.  This version uses the new timeout parameter.  The result is a window that reacts quicker then the one with the sleep and the accuracy is just as good.</p>
<h2 id="instead-of-a-non-blocking-read-use-enable_events-true-or-return_keyboard_events-true">Instead of a Non-blocking Read --- Use <code>enable_events = True</code> or <code>return_keyboard_events = True</code></h2>
<p>Any time you are thinking "I want an X Element to cause a Y Element to do something", then you want to use the <code>enable_events</code> option.</p>
<p><strong><em>Instead of polling, try options that cause the window to return to you.</em></strong>  By using non-blocking windows, you are <em>polling</em>.  You can indeed create your application by polling.  It will work.  But you're going to be maxing out your processor and may even take longer to react to an event than if you used another technique.</p>
<p><strong>Examples</strong></p>
<p>One example is you have an input field that changes as you press buttons on an on-screen keypad.</p>
<p><img alt="keypad 3" src="https://user-images.githubusercontent.com/13696193/45260275-a2198e80-b3b0-11e8-85fe-a4ce6484510f.jpg" /></p>
<h1 id="updating-elements-changing-elements-values-in-an-active-window">Updating Elements (changing element's values in an active window)</h1>
<p>If you want to change an Element's settings in your window after the window has been created, then you will call the Element's Update method.</p>
<p><strong>NOTE</strong> a window <strong>must be Read or Finalized</strong> before any Update calls can be made.  Also, not all settings available to you when you created the Element are available to you via its <code>update</code> method.</p>
<p>Here is an example of updating a Text Element</p>
<pre><code class="python">import PySimpleGUI as sg

layout = [ [sg.Text('My layout', key='-TEXT-')],
           [sg.Button('Read')]]

window = sg.Window('My new window', layout)

while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    window['-TEXT-'].update('My new text value')
</code></pre>

<p>Notice the placement of the Update call.  If you wanted to Update the Text Element <em>prior</em> to the Read call, outside of the event loop, then you must call Finalize on the window first.</p>
<p>In this example, the Update is done prior the Read.  Because of this, the Finalize call is added to the Window creation.</p>
<pre><code class="python">import PySimpleGUI as sg

layout = [ [sg.Text('My layout', key='-TEXT-')],
           [sg.Button('Read')]]

window = sg.Window('My new window', layout, finalize=True)

window['-TEXT-'].update('My new text value')

while True:             # Event Loop
  event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
</code></pre>

<p>Persistent windows remain open and thus continue to interact with the user after the Read has returned.  Often the program wishes to communicate results (output information) or change an Element's values (such as populating a List Element).</p>
<p>You can use Update to do things like:
* Have one Element (appear to) make a change to another Element
* Disable a button, slider, input field, etc.
* Change a button's text
* Change an Element's text or background color
* Add text to a scrolling output window
* Change the choices in a list
* etc.</p>
<p>The way this is done is via an Update method that is available for nearly all of the Elements.  Here is an example of a program that uses a persistent window that is updated.</p>
<p><img alt="snap0272" src="https://user-images.githubusercontent.com/13696193/45260249-ec4e4000-b3af-11e8-853b-9b29d0bf7797.jpg" /></p>
<p>In some programs these updates happen in response to another Element.  This program takes a Spinner and a Slider's input values and uses them to resize a Text Element.  The Spinner and Slider are on the left, the Text element being changed is on the right.</p>
<pre><code class="python"># Testing async window, see if can have a slider
# that adjusts the size of text displayed

import PySimpleGUI as sg
fontSize = 12
layout = [[sg.Spin([sz for sz in range(6, 172)], font=('Helvetica 20'), initial_value=fontSize, change_submits=True, key='spin'),
           sg.Slider(range=(6,172), orientation='h', size=(10,20),
           change_submits=True, key='slider', font=('Helvetica 20')),
           sg.Text(&quot;Aa&quot;, size=(2, 1), font=&quot;Helvetica &quot;  + str(fontSize), key='text')]]

sz = fontSize
window = sg.Window(&quot;Font size selector&quot;, layout, grab_anywhere=False)
# Event Loop
while True:
    event, values= window.read()
    if event == sg.WIN_CLOSED:
        break
    sz_spin = int(values['spin'])
    sz_slider = int(values['slider'])
    sz = sz_spin if sz_spin != fontSize else sz_slider
    if sz != fontSize:
        fontSize = sz
        font = &quot;Helvetica &quot;  + str(fontSize)
        window['text'].update(font=font)
        window['slider'].update(sz)
        window['spin'].update(sz)

print(&quot;Done.&quot;)
</code></pre>

<p>Inside the event loop we read the value of the Spinner and the Slider using those Elements' keys.
For example, <code>values['slider']</code> is the value of the Slider Element.</p>
<p>This program changes all 3 elements if either the Slider or the Spinner changes.  This is done with these statements:</p>
<pre><code class="python">window['text'].update(font=font)
window['slider'].update(sz)
window['spin'].update(sz)
</code></pre>

<p>Remember this design pattern because you will use it OFTEN if you use persistent windows.</p>
<p>It works as follows.  The expresion <code>window[key]</code> returns the Element object represented by the provided <code>key</code>.  This element is then updated by calling it's <code>update</code> method.  This is another example of Python's "chaining" feature. We could write this code using the long-form:</p>
<pre><code>text_element = window['text']
text_element.update(font=font)
</code></pre>
<p>The takeaway from this exercise is that keys are key in PySimpleGUI's design.  They are used to both read the values of the window and also to identify elements.  As already mentioned, they are used in a wide variety of places.</p>
<h3 id="locating-elements-findelement-element-elem">Locating Elements (FindElement == Element == Elem == [ ])</h3>
<p>The Window method call that's used to find an element is:
<code>FindElement</code>
or the shortened version
<code>Element</code>
or even shorter (version 4.1+)
<code>Elem</code></p>
<p>And now it's finally shortened down to:
window[key]</p>
<p>You'll find the pattern - <code>window.Element(key)</code> in older code.  All of code after about 4.0 uses the shortened <code>window[key]</code> notation.</p>
<h3 id="progressbar-progress-meters">ProgressBar / Progress Meters</h3>
<p>Note that to change a progress meter's progress, you call <code>update_bar</code>, not <code>update</code>.  A change to this is being considered for a future release.</p>
<h1 id="keyboard-mouse-capture">Keyboard &amp; Mouse Capture</h1>
<p>NOTE - keyboard capture is currently formatted uniquely among the ports. For basic letters and numbers there is no great differences, but when you start adding Shift and Control or special keyus, they all behave slightly differently.  Your best bet is to simply print what is being returned to you to determine what the format for the particular port is.</p>
<p>Beginning in version 2.10 you can capture keyboard key presses and mouse scroll-wheel events.   Keyboard keys can be used, for example, to detect the page-up and page-down keys for a PDF viewer.  To use this feature, there's a boolean setting in the Window call <code>return_keyboard_events</code> that is set to True in order to get keys returned along with buttons.</p>
<p>Keys and scroll-wheel events are returned in exactly the same way as buttons.</p>
<p>For scroll-wheel events, if the mouse is scrolled up, then the <code>button</code> text will be <code>MouseWheel:Up</code>.   For downward scrolling, the text returned is <code>MouseWheel:Down</code></p>
<p>Keyboard keys return 2 types of key events. For "normal" keys (a,b,c, etc.), a single character is returned that represents that key.  Modifier and special keys are returned as a string with 2 parts:</p>
<pre><code>Key Sym:Key Code
</code></pre>
<p>Key Sym is a string such as 'Control_L'.  The Key Code is a numeric representation of that key.  The left control key, when pressed will return the value 'Control_L:17'</p>
<pre><code class="python">import PySimpleGUI as sg

# Recipe for getting keys, one at a time as they are released
# If want to use the space bar, then be sure and disable the &quot;default focus&quot;

text_elem = sg.Text(size=(18, 1))

layout = [[sg.Text(&quot;Press a key or scroll mouse&quot;)],
          [text_elem],
          [sg.Button(&quot;OK&quot;)]]

window = sg.Window(&quot;Keyboard Test&quot;, layout,  return_keyboard_events=True, use_default_focus=False)

# ---===--- Loop taking in user input --- #
while True:
    event, value = window.read()

    if event == &quot;OK&quot; or event == sg.WIN_CLOSED:
        print(event, &quot;exiting&quot;)
        break
    text_elem.update(event)
</code></pre>

<p>You want to turn off the default focus so that there no buttons that will be selected should you press the spacebar.</p>
<h1 id="menus">Menus</h1>
<h2 id="menubar">MenuBar</h2>
<p>Beginning in version 3.01 you can add a MenuBar to your window.  You specify the menus in much the same way as you do window layouts, with lists.  Menu selections are returned as events and as of 3.17, also as in the values dictionary.  The value returned will be the entire menu entry, including the key if you specified one.</p>
<pre><code class="python">    menu_def = [['File', ['Open', 'Save', 'Exit',]],
                ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
                ['Help', 'About...'],]
</code></pre>

<p><img alt="menu" src="https://user-images.githubusercontent.com/13696193/45306723-56b7cb00-b4eb-11e8-8cbd-faef0c90f8b4.jpg" /></p>
<p>Note the placement of ',' and of [].  It's tricky to get the nested menus correct that implement cascading menus.  See how paste has Special and Normal as a list after it.  This means that Paste has a cascading menu with items Special and Normal.</p>
<h2 id="methods">Methods</h2>
<hr />
<p>To add a menu to a Window place the <code>Menu</code> or <code>MenuBar</code> element into your layout.</p>
<pre><code>layout = [[sg.Menu(menu_def)]]
</code></pre>
<p>It doesn't really matter where you place the Menu Element in your layout as it will always be located at the top of the window.</p>
<p>When the user selects an item, it's returns as the event (along with the menu item's key if one was specified in the menu definition)</p>
<h2 id="buttonmenus">ButtonMenus</h2>
<p>Button menus were introduced in version 3.21, having been previously released in PySimpleGUIQt.  They work exactly the same and are source code compatible between PySimpleGUI and PySimpleGUIQt.  These types of menus take a single menu entry where a Menu Bar takes a list of menu entries.</p>
<p><strong>Return values for ButtonMenus are different than Menu Bars.</strong></p>
<p>You will get back the ButtonMenu's KEY as the event.  To get the actual item selected, you will look it up in the values dictionary.  This can be done with the expression <code>values[event]</code></p>
<h2 id="right-click-menus">Right Click Menus</h2>
<p>Right Click Menus were introduced in version 3.21.  Almost every element has a right_click_menu parameter and there is a window-level setting for rich click menu that will attach a right click menu to all elements in the window.</p>
<p>The menu definition is the same as the button menu definition, a single menu entry.</p>
<pre><code class="python">right_click_menu = ['&amp;Right', ['Right', '!&amp;Click', '&amp;Menu', 'E&amp;xit', 'Properties']]
</code></pre>

<p>The first string in a right click menu and a button menu is <strong><em>ignored</em></strong>.  It is not used.  Normally you would put the string that is shown on the menu bar in that location.</p>
<p><strong>Return values for right click menus are the same as MenuBars.</strong>  The value chosen is returned as the event.</p>
<h2 id="menu-shortcut-keys">Menu Shortcut keys</h2>
<p>You have used ALT-key in other Windows programs to navigate menus.  For example Alt-F+X exits the program.  The Alt-F pulls down the File menu.  The X selects the entry marked Exit.</p>
<p>The good news is that PySimpleGUI allows you to create the same kind of menus!  Your program can play with the big-boys.  And, it's trivial to do.</p>
<p>All that's required is for your to add an "&amp;" in front of the letter you want to appear with an underscore.  When you hold the Alt key down you will see the menu with underlines that you marked.</p>
<p>One other little bit of polish you can add are separators in your list.  To add a line in your list of menu choices, create a menu entry that looks like this: <code>'---'</code></p>
<p>This is an example Menu with underlines and a separator.</p>
<pre><code># ------ Menu Definition ------ #
menu_def = [['&amp;File', ['&amp;Open', '&amp;Save', '---', 'Properties', 'E&amp;xit'  ]],
            ['&amp;Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
            ['&amp;Help', '&amp;About...'],]
</code></pre>

<p>And this is the spiffy menu it produced:
  <img alt="menus with shortcuts" src="https://user-images.githubusercontent.com/13696193/46251674-f5b74f00-c427-11e8-95c6-547adc59041b.jpg" /></p>
<h2 id="disabled-menu-entries">Disabled Menu Entries</h2>
<p>If you want one of your menu items to be disabled, then place a '!' in front of the menu entry.  To disable the Paste menu entry in the previous examples, the entry would be:
<code>['!&amp;Edit', ['Paste', ['Special', 'Normal',], 'Undo'],]</code></p>
<p>If your want to change the disabled menu item flag / character from '!' to something else, change the variable <code>MENU_DISABLED_CHARACTER</code></p>
<h2 id="keys-for-menus">Keys for Menus</h2>
<p>Beginning in version 3.17 you can add a <code>key</code> to your menu entries.  The <code>key</code> value will be removed prior to be inserted into the menu.  When you receive Menu events, the entire menu entry, including the <code>key</code> is returned.  A key is indicated by adding <code>::</code> after a menu entry, followed by the key.</p>
<p>To add the <code>key</code> <code>_MY_KEY_</code> to the Special menu entry, the code would be:</p>
<p><code>['&amp;Edit', ['Paste', ['Special::_MY_KEY_', 'Normal',], 'Undo'],]</code></p>
<p>If you want to change the characters that indicate a key follows from '::' to something else, change the variable <code>MENU_KEY_SEPARATOR</code></p>
<h2 id="the-menu-definitions">The Menu Definitions</h2>
<p>Having read through the Menu section, you may have noticed that the right click menu and the button menu have a format that is a little odd as there is a part of it that is not utilized (the first very string).  Perhaps the words "Not Used" should be in the examples.... But, there's a reason to retain words there that make sense.</p>
<p>The reason for this is an architectural one, but it also has a convienence for the user.  You can put the individual menu items (button and right click) into a list and you'll have a menu bar definition.</p>
<p>This would work to make a menu bar from a series of these individual menu defintions:</p>
<pre><code class="python">menu_bar = [right_click_menu_1, right_click_menu_2, button_menu_def ]
</code></pre>

<p>And, of course, the direction works the opposite too.  You can take a Menu Bar definition and pull out an individual menu item to create a right click or button menu. </p>
<h1 id="running-multiple-windows">Running Multiple Windows</h1>
<p>This is where PySimpleGUI continues to be simple, but the problem space just went into the realm of "Complex".</p>
<p>If you wish to run multiple windows in your event loop, then there are 2 methods for doing this.</p>
<ol>
<li>First window does not remain active while second window is visible</li>
<li>First window remains active while second window is visible</li>
</ol>
<p>You will find the 2 design matters in 2 demo programs in the Demo Program area of the GitHub (http://www.PySimpleGUI.com)</p>
<p><strong><em>Critically important</em></strong>
When creating a new window you must use a "fresh" layout every time.  You cannot reuse a layout from a previous window.  As a result you will see the layout for window 2 being defined inside of the larger event loop.</p>
<p>If you have a window layout that you used with a window and you've closed the window, you cannot use the specific elements that were in that window.  You must RE-CREATE your <code>layout</code> variable every time you create a new window.  Read that phrase again....  You must RE-CREATE your <code>layout</code> variable every time you create a new window.  That means you should have a statemenat that begins with <code>layout =</code>.  Sorry to be stuck on this point, but so many people seem to have trouble following this simple instruction.</p>
<h2 id="the-golden-rule-of-window-layouts">THE GOLDEN RULE OF WINDOW LAYOUTS</h2>
<p><strong><em>Thou shalt not re-use a windows's layout.... ever!</em></strong></p>
<p>Or more explicitly put....</p>
<blockquote>
<p>If you are calling <code>Window</code> then you should define your window layout in the statement just prior to the <code>Window</code> call.</p>
</blockquote>
<h2 id="demo-programs-for-multiple-windows">Demo Programs For Multiple Windows</h2>
<p>There are several "Demo Programs" that will help you run multiple windows.  Please download these programs and FOLLOW the example they have created for you.</p>
<p>Here is <strong><em>some</em></strong> of the code patterns you'll find when looking through the demo programs.</p>
<h2 id="multi-window-design-pattern-1-both-windows-active">Multi-Window Design Pattern 1 - both windows active</h2>
<pre><code class="python">import PySimpleGUI as sg

# Design pattern 2 - First window remains active

layout = [[ sg.Text('Window 1'),],
          [sg.Input(do_not_clear=True)],
          [sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Button('Launch 2'), sg.Button('Exit')]]

win1 = sg.Window('Window 1', layout)

win2_active = False
while True:
    ev1, vals1 = win1.read(timeout=100)
    win1['-OUTPUT-'].update(vals1[0])
    if ev1 is None or ev1 == 'Exit':
        break

     if not win2_active and ev1 == 'Launch 2':
        win2_active = True
        layout2 = [[sg.Text('Window 2')],
                   [sg.Button('Exit')]]

        win2 = sg.Window('Window 2', layout2)

    if win2_active:
        ev2, vals2 = win2.read(timeout=100)
        if ev2 is None or ev2 == 'Exit':
            win2_active  = False
            win2.close()
</code></pre>

<h2 id="multi-window-design-pattern-2-only-1-active-window">Multi-Window Design Pattern 2 - only 1 active window</h2>
<pre><code class="python">import PySimpleGUIQt as sg

# Design pattern 1 - First window does not remain active

layout = [[ sg.Text('Window 1'),],
          [sg.Input(do_not_clear=True)],
          [sg.Text(size=(15,1),  key='-OUTPUT-')],
          [sg.Button('Launch 2')]]

win1 = sg.Window('Window 1', layout)
win2_active=False
while True:
    ev1, vals1 = win1.read(timeout=100)
    if ev1 is None:
        break
    win1.FindElement('-OUTPUT-').update(vals1[0])

    if ev1 == 'Launch 2'  and not win2_active:
        win2_active = True
        win1.Hide()
        layout2 = [[sg.Text('Window 2')],       # note must create a layout from scratch every time. No reuse
                   [sg.Button('Exit')]]

        win2 = sg.Window('Window 2', layout2)
        while True:
            ev2, vals2 = win2.read()
            if ev2 is None or ev2 == 'Exit':
                win2.close()
                win2_active = False
                win1.UnHide()
                break
</code></pre>

<hr />
<h1 id="the-pysimplegui-debugger">The PySimpleGUI Debugger</h1>
<p>Listen up if you are
* advanced programmers debugging some really hairy stuff
* programmers from another era that like to debug this way
* those that want to have "x-ray vision" into their code
* asked to use debugger to gather information
* running on a platform that lacks ANY debugger
* debugging a problem that happens only outside of a debugger environment
* finding yourself saying "but it works when running PyCharm"</p>
<p>Starting on June 1, 2019, a built-in version of the debugger <code>imwatchingyou</code> has been shipping in every copy of PySimpleGUI.  It's been largely downplayed to gauge whether or not the added code and the added feature and the use of a couple of keys, would mess up any users.  Over 30,000 users have installed PySimpleGUI since then and there's not be a single Issue filed nor comment/complaint made, so seems safe enough to normal users... so far....</p>
<p>So far no one has reported anything at all about the debugger.  The assumption is that it is quietly lying dormant, waiting for you to press the <code>BREAK</code> or <code>CONTROL</code> + <code>BREAK</code> keys.  It's odd no one has accidently done this and freaked out, logging an Issue.</p>
<p>The plain PySimpleGUI module has a debugger builtin.  For the other ports, please use the package <code>imwatchingyou</code>.</p>
<h2 id="what-is-it-why-use-it-what-the-heck-i-already-have-an-ide">What is it?  Why use it?  What the heck?  I already have an IDE.</h2>
<p>This debugger provides you with something unique to most typical Python developers, the ability to "see" and interact with your code, <strong>while it is running</strong>.  You can change variable values while your code continues to run.</p>
<p>Print statements are cool, but perhaps you're tired of seeing a printout of <code>event</code> and <code>values</code>:</p>
<pre><code>Push Me {0: 'Input here'}
Push Me {0: 'Input here'}
Push Me {0: 'Input here'}
</code></pre>

<p>And would prefer to see this window updating continuously in the upper right corner of your display:</p>
<p><img alt="image" src="https://user-images.githubusercontent.com/13696193/62793751-54197900-baa0-11e9-9a98-f780259062b1.png" /></p>
<p>Notice how easy it is, using this window alone, to get the location that your PySimpleGUI package is coming from <strong><em>for sure</em></strong>, no guessing.  Expect this window to be in your debugging future as it'll get asked for from time to time.</p>
<h2 id="preparing-to-run-the-debugger">Preparing To Run the Debugger</h2>
<p>If your program is running with blocking <code>Read</code> calls, then you will want to add a timeout to your reads.  This is because the debugger gets it's cycles by stealing a little bit of time from these async calls... but only when you have one of these debugger windows open so no bitching about wasted CPU time as there is none.</p>
<p>Your event loop will be modified from this blocking:</p>
<pre><code class="python">while True:
    event, values = window.read()
</code></pre>

<p>To this non-blocking:</p>
<pre><code class="python">while True:
    event, values = window.read(timeout=200)
    if event == sg.TIMEOUT_KEY:
        continue
</code></pre>

<p>These 3 lines will in no way change how your application looks and performs.  You can do this to any PySimpleGUI app that uses a blocking read and you'll not notice a difference.  The reason this is a NOP (No-operation) is that when a timeout happens, the envent will be set to <code>sg.TIMEOUT_KEY</code>.  If a timeout is returned as the event, the code simply ignores it and restarts the loop by executing a <code>continue</code> statement.</p>
<p>This timeout value of 200 means that your debugger GUI will be updated 5 times a second if nothing is happening.  If this adds too much "drag" to your application, you can make the timeout larger.  Try using 500 or 1000 instead of 100.</p>
<h3 id="what-happens-if-you-dont-add-a-timeout">What happens if you don't add a timeout</h3>
<p>Let's say you're in a situation where a very intermettent bug has just happened and the debugger would really help you, but you don't have a timeout on your <code>windows.read()</code> call.  It's OK.  Recall that the way the debugger gets its "cycles" is to borrow from your <code>Read</code> calls.  What you need to do is alternate between using the debugger and then generating another pass through your event loop.</p>
<p>Maybe it's an OK button that will cause your loop to execute again (without exiting).  If so, you can use it to help move the debugger along.  </p>
<p>Yes, this is a major pain in the ass, but it's not THAT bad and compared to nothing in a time of crisis and this is potentially your "savior tool" that's going to save your ass, pressing that OK button a few times is going to look like nothing to you.  You just want to dump out the value of a variable that holds an instance of your class!</p>
<h2 id="a-sample-program-for-us-to-use">A Sample Program For Us To Use</h2>
<p>Now that you understand how to add the debugger to your program, let's make a simple little program that you can use to follow these examples:</p>
<pre><code class="python">import PySimpleGUI as sg

window = sg.Window('Testing the Debugger', [[sg.Text('Debugger Tester'), sg.In('Input here'), sg.B('Push Me')]])

while True:
    event, values = window.read(timeout=500)
    if event == sg.TIMEOUT_KEY:
        continue
    if event == sg.WIN_CLOSED:
        break
    print(event, values)
window.close()
</code></pre>

<h2 id="debugger-windows">Debugger Windows</h2>
<h3 id="popout-debugger-window">"Popout Debugger Window"</h3>
<p>There are 2 debugger windows. One is called the "Popout" debugger window.  The Popout window displays as many currently in-scope local variables as possible.  This window is not interactive.  It is meant to be a frequently updated "dashboard" or "snapshot" of your variables.</p>
<p>One "variable" shown in the popout window that is an often asked for piece of information when debugging Issues and that variable is <code>sg</code> (or whatever you named the PySimpleGUI pacakge when you did your import). The assumption is that your import is <code>import PySimpleGUI as sg</code>.  If your import is different, then you'll see a different variable.  The point is that it's shown here.</p>
<p>Exiting this window is done via the little red X, <strong>or using the rickt-click menu</strong> which is also used as one way to launch the Main Debugger Window</p>
<h4 id="ways-of-launching-the-popout-window">Ways of Launching the Popout Window</h4>
<p>There are 3 ways of opening the Popout window.</p>
<ol>
<li>Press the <code>BREAK</code> key on your keyboard.</li>
<li>Call the function <code>show_debugger_popout_window(location=(x,y))</code></li>
<li>Add <code>Debug()</code> button to your layout - adds a little purple and yellow PySimpleGUI logo to your window</li>
</ol>
<h4 id="when-you-are-asked-for-the-location-of-your-pysimplegui-package-or-pysimpleguipy-file-do-this">When you are asked for the "Location of your PySimpleGUI package or PySimpleGUI.py file" do this</h4>
<p>If you wish to use the debugger to find the location of THIS running program's PySimpleGUI package / the PySimpleGUI.py file, then all you need to do is:
* Press the <code>BREAK</code> key on your keyboard. 
    * This is sometimes labelled as the <code>Cancel</code> key
    * May also have <code>Pause</code> printed on key
    * On some US keyboards, it is located next to <code>Scroll Lock</code> and/or above <code>PageUp</code> key
* This will open a window located in the upper right corner of your screen that looks something like this:
<img alt="image" src="https://user-images.githubusercontent.com/13696193/62793751-54197900-baa0-11e9-9a98-f780259062b1.png" />
* The information you are seeking is shown next to the <code>sg</code> in the window
You don't need to modify your program to get this info using this technique.</p>
<p>If your variable's value is too long and doesn't fit, then you'lll need to collect this information using the "Main Debugger Window"</p>
<h4 id="whats-not-listed-in-the-popout-debugger-window">What's NOT Listed In The Popout Debugger Window</h4>
<p>The Popup window is a "Snapshot" of your local variables at the time the window was opened. This means <strong>any variables that did not exist at the time the Popout was created will not be shown</strong>.   This window does <strong>NOT</strong> expand in size by adding new variables.  Maybe in the future.</p>
<h3 id="the-main-debugger-window">The "Main Debugger Window"</h3>
<p>Now we're talking serious Python debugging!</p>
<p>Ever wish you had a <code>repl&gt;&gt;&gt;</code> prompt that you could run while your program is running.  Well, that's pretty much what you're getting with the PySimpleGUI debugger Main Window!  Cool, huh?  If you're not impressed, go get a cup of coffee and walk off that distraction in your head before carring on because we're in to some seriously cool shit here....</p>
<p>You'll find that this window has 2 tabs, one is labelled <code>Variables</code> and the other is labelled <code>REPL &amp; Watches</code></p>
<h4 id="ways-of-opening-the-main-debugger-window">Ways of Opening the Main Debugger Window</h4>
<p>There are 3 ways to open the Main Debugger Window</p>
<ol>
<li>Press <code>Control</code> + <code>Break</code> on your PC keyboard</li>
<li>From the Popout Debug Window, right click and choose <code>Debugger</code> from the right click menu</li>
<li>From your code call <code>show_debugger_window(location=(x,y))</code></li>
</ol>
<h4 id="the-variables-tab-of-main-debugger-window">The "Variables" Tab of Main Debugger Window</h4>
<p><img alt="SNAG-0440" src="https://user-images.githubusercontent.com/13696193/62797391-a01ceb80-baa9-11e9-845d-3cd02ca0dbcc.jpg" /></p>
<p>Notice the the "frame" surrounding this window is labelled "Auto Watches" in blue.  Like the Popup window, this debugger window also "Watches" variables, which means continuously updates them as often as you call <code>Window.read</code>.</p>
<p>The maximum number of "watches" you can have any any one time is 9.</p>
<h5 id="choosing-variables-to-watch">Choosing variables to watch</h5>
<p>You can simply click "Show All Variable" button and the list of watched variables will be automatically populard by the first 9 variables it finds.  Or you can click the "Choose Variables to Auto Watch" button where you can individually choose what variables, <strong>and expressions</strong> you wish to display.</p>
<p><img alt="SNAG-0442" src="https://user-images.githubusercontent.com/13696193/62797520-e96d3b00-baa9-11e9-8ba0-794e479b6fc5.jpg" /></p>
<p>In this window we're checking checkboxes to display these variables:</p>
<p><code>event</code>, <code>sg</code>, <code>values</code>, <code>window</code>, <code>__file__</code></p>
<p><img alt="SNAG-0443" src="https://user-images.githubusercontent.com/13696193/62797518-e8d4a480-baa9-11e9-8575-5256dcf6b5ab.jpg" /></p>
<p>Additionally, you can see at the bottom of the window a "Custom Watch" has been defined.  This can be any experession you want.  Let's say you have a window with a LOT of values.  Rather than looking through the <code>values</code> variable and finding the entry with the key you are looking for, the values variable's entry for a specific key is displayed.</p>
<p>In this example the Custom Watch entered was <code>values[0]</code>.  After clicking on the "OK" button, indicating the variables are chosen that we wish to watch, this is the Main window that is shown:</p>
<p><img alt="SNAG-0444" src="https://user-images.githubusercontent.com/13696193/62797514-e8d4a480-baa9-11e9-9a86-cfe99342dedb.jpg" /></p>
<p>We can see the variables we checked as well as the defined expression <code>values[0]</code>.  If you leave this window open, these values with continuously be updated, on the fly, every time we call the line in our example code <code>window.read(timeout=500)</code>.  This means that the Main Debugger Window and these variables we defined will be updated every 500 milliseconds.</p>
<h4 id="the-repl-watches-tab">The REPL &amp; Watches Tab</h4>
<p><img alt="SNAG-0441" src="https://user-images.githubusercontent.com/13696193/62797507-e7a37780-baa9-11e9-93c4-6ff0c8acb11d.jpg" /></p>
<p>This tab is provided to you as a way to interact with your running program on a real-time basis.  </p>
<p>If you want to quickly look at the values of variables, nearly ANY variables, then type the information into one of the 3 spaces provided to "Watch" either variables or experessions.  In this example, the variable window was typed into the first slow.  </p>
<p><strong><em>Immediately</em></strong> after typing the character 'w', the information to the right was displayed.  No button needs to be clicked.  You merely neeed to type in a valid experession and it will be displayed to you.... and it will be displayed on an on-going, constantly-refreshing-basis.</p>
<p><img alt="SNAG-0447" src="https://user-images.githubusercontent.com/13696193/62797393-a0b58200-baa9-11e9-8016-1cadca4d97e7.jpg" /></p>
<p>If the area to the right of the input field is too small, then you can click on the "Detail" button and you will be shown a popup, scrolled window with all of the information displayed as if it were printed.  </p>
<p>I'm sure you've had the lovely experience of printing an object.  When clicking the "Detail" button next to the <code>window</code> variable being shown, this window is shown:</p>
<p><img alt="SNAG-0449" src="https://user-images.githubusercontent.com/13696193/62801423-b0d25f00-bab3-11e9-829a-aebb429521cd.jpg" /></p>
<p>Oh, Python, -sigh-.  I just want to see my <code>window</code> object printed.  </p>
<h4 id="obj-button-to-the-rescue"><code>Obj</code> Button to the Rescue!</h4>
<p>PySimpleGUI has a fun and very useful function that is discussed in the docs named <code>ObjToString</code> which takes an object and converts it's <strong>contents</strong> it into a nicely formatted string.  This function is used to create the text output when you click the <code>Obj</code> button.  The result is this instead of the tiny window shown previously:</p>
<p><img alt="SNAG-0446" src="https://user-images.githubusercontent.com/13696193/62797508-e7a37780-baa9-11e9-96bf-b2c066e72d78.jpg" /></p>
<h2 id="the-repl-prompt">The REPL Prompt</h2>
<p>While not <strong>really</strong> a Python REPL prompt, this window's <code>REPL &gt;&gt;&gt;</code> prompt is meant to act as much like one as possible.  Here you can enter experessions and code too.</p>
<p>The uses for this prompt are so numerous and diverse that listing them all won't be attempted. </p>
<h3 id="your-xray-and-endoscope-into-your-program">Your "XRay" and "Endoscope" into Your Program</h3>
<p>Think of this prompt as a way to get specific diagnostics information about your <strong><em>running</em></strong> program.  It cannot be stressed enough that the power and the usefullness of this tool is in its ability to diagnose a running program, after you've already started it running. </p>
<h3 id="execute-code">Execute Code</h3>
<p>In addition to displaying information, getting paths to packages, finding version information, you can execute code from the PySimpleGUI Debugger's <code>REPL &gt;&gt;&gt;</code> prompt.  You can type in any expression as well as any <strong>executable statement</strong>.</p>
<p>For example, want to see what <code>PopupError</code> looks like while you're running your program.  From the REPL prompt, type:
<code>sg.PopupError('This is an error popup')</code></p>
<p>The result is that you are shown a popup window with the text you supplied.</p>
<h3 id="know-answers-to-questions-about-your-program">KNOW Answers to Questions About Your Program</h3>
<p>Using this runtime tool, you can be confident in the data you collect.  Right?  </p>
<p><strong><em>There's no better way to find what version of a package that your program is using than to ask your program.</em></strong>  This is so true.  Think about it.  Rather than go into PyCharm, look at your project's "Virtual Environment", follow some path to get to a window that lists packages installed for that project, get the verstion and your're done, right?  Well, maybe.  But are you CERTAIN your program is using THAT version of the package in question?</p>
<p>SO MUCH time has been wasted in the past  when people KNEW, for sure, what version they were running. Or, they had NO CLUE what version, or no clue to find out.  There's nothing wrong with not knowing how to do something.  We ALL start there.  Geeez..</p>
<p>A real world example.....</p>
<h2 id="how-to-use-the-debugger-to-find-the-version-number-of-a-package">How To Use the Debugger to Find The Version Number of a Package</h2>
<p>Let's pull together everything we've learned to now and use the debugger to solve a problem that happens often and sometimes it's not at all obvious how to find the answer.</p>
<p>We're using <strong><em>Matplotlib</em></strong> and want to find the "Version".</p>
<p>For this example, the little 12-line program in the section "A Sample Program For Us To Use" is being used.</p>
<p>That program does not import <code>matplotlib</code>.  We have a couple of choices, we can change the code, we can can import the package from the debugger.  Let's use the debgger.</p>
<p>Pull up the Main Debugger Window by pressing <code>CONTROL+BREAK</code> keys.  Then click the "REPL * Watches" tab.  At the <code>&gt;&gt;&gt;</code> prompt we'll first import the package by typing:
<code>import matplotlib as m</code></p>
<p>The result returned from Python calls that don't return anything is the value None.  You will see the command you entered in the output area followed by "None", indicating success.</p>
<p>finally, type:
<code>m.__version__</code></p>
<p>The entire set of operations is shown in this window:</p>
<p><img alt="SNAG-0448" src="https://user-images.githubusercontent.com/13696193/62797392-a0b58200-baa9-11e9-97f4-9ef74cbb86f7.jpg" /></p>
<p>By convention you'll find many modules have a variable <code>__version__</code> that has the package's version number.  PySimpleGUI has one.  As you can see matplotlib has one.  The <code>requests</code> module has this variable.</p>
<p>For maximum compatibility, PySimpleGUI not only uses <code>__version__</code>, but also has the version contained in another variable <code>version</code> which has the version number because in some situations the <code>__version__</code> is not available but the <code>version</code> variable is avaiable.</p>
<p><strong>It is recommended that you use the variable <code>version</code> to get the PySimpleGUI version</strong> as it's so far been the most successful method.</p>
<p>tkinter, however does NOT.... of course.... follow this convention.  No, to get the tkinter version, you need to look at the variable:
<code>TkVersion</code></p>
<p>Here's the output from the REPL in the debugger showing the tkinter version:</p>
<pre><code>&gt;&gt;&gt; import tkinter as t
None
&gt;&gt;&gt; t.TkVersion
8.6
&gt;&gt;&gt; t.__version__
Exception module 'tkinter' has no attribute '__version__'
</code></pre>

<hr />
<h1 id="extending-pysimplegui">Extending PySimpleGUI</h1>
<p>PySimpleGUI doesn't and can't provide every single setting available in the underlying GUI framework.  Not all tkinter options are available for a <code>Text</code> Element.  Same with PySimpleGUIQt and the other ports.  </p>
<p>There are a few of reasons for this.</p>
<ol>
<li>Time &amp; resource limits - The size of the PySimpleGUI development team is extremely small</li>
<li>PySimpleGUI provides a "Unified API".  This means the code is, in theory, portable across all of the PySimpleGUI ports without chaning the user's code (except for the import)</li>
<li>PySimpleGUI is meant, by design, to be simple and cover 80% of the GUI problems.</li>
</ol>
<p>However, PySimpleGUI programs are <strong><em>not</em></strong> dead ends!!  Writing PySimpleGUI code and then getting to a point where you really really feel like you need to extend the Listbox to include the ability to change the "Selected" color.  Maybe that's super-critical to your project.  And maybe you find out late that the base PySimpleGUI code doesn't expose that tkinter capability.  Fear not!  The road does continue!!</p>
<h2 id="widget-access">Widget Access</h2>
<p>Most of the user extensions / enhancements are at the "Element" level.  You want some Element to do a trick that you cannot do using the existing PySimpleGUI APIs.  It's just not possible.  What to do?  </p>
<p>What you need is access to the underlying GUI framework's "Widget".  The good news is that you HAVE that access ready and waiting for you, for all of the ports of PySimpleGUI, not just the tkinter one.</p>
<h3 id="elementwidget-is-the-gui-widget"><code>Element.Widget</code> is The GUI Widget</h3>
<p>The class variable <code>Widget</code> contains the tkinter, Qt, WxPython, or Remi widget.  With that variable you can modify that widget directly.  </p>
<p><strong><em>You must first <code>Read</code> or <code>Finalize</code> the window before accessing the <code>Widget</code> class variable</em></strong></p>
<p>The reason for the Finalize requirement is that until a Window is Read or is Finalized it is not actually created and populated with GUI Widgets.  The GUI Widgets are created when you do these 2 operations.</p>
<p>Side note - You can stop using the <code>.Finalize()</code> call added onto your window creation and instead use the <code>finalize</code> parameter in the <code>Window</code> call.</p>
<p>OLD WAY:</p>
<pre><code class="python">window = sg.Window('Window Title', layout).Finalize()

</code></pre>

<p>THE NEW WAY:</p>
<pre><code class="python">window = sg.Window('Window Title', layout, finalize=True)

</code></pre>

<p>It's cleaner and less confusing for beginners who aren't necessarily trained in how chaining calls work.  Py<strong>Simple</strong>GUI.</p>
<h3 id="example-use-of-elementwidget">Example Use of <code>Element.Widget</code></h3>
<p>So far there have been 2 uses of this capability.  One already mentioned is adding a new capability.  The other way it's been used has been to fix a bug or make a workaround for a quirky behavior.</p>
<p>A recent Issue posted was that focus was always being set on a button in a tab when you switch tabs in tkinter.  The user didn't want this to happen as it was putting an ugly black line around their nicely made graphical button.</p>
<p>There is no current way in PySimpleGUI to "disable focus" on an Element.  That's essentially what was needed, the ability to tell tkinter that this widget should never get focus.  </p>
<p>There is a way to tell tkinter that a widget should not get focus.  The downside is that if you use your tab key to navigate, that element will never get focus.  So, it's not only blocking focus for this automatic problem, but blocking it for all uses.  Of course you can still click on the button.</p>
<p>The way through for this user was to modify the tkinter widget directly and tell it not to get focus.  This was done in a single line of code:</p>
<pre><code class="python">window[button_key].Widget.config(takefocus=0)
</code></pre>

<p>The absolute beauty to this solution is that tkinter does NOT need to be imported into the user's program for this statement to run.  Python already know what kind of object <code>.Widget</code> is and can thus show you the various methods and class variables for that object.  Most all tkinter options are strings so you don't need to import tkinter to get any enums.</p>
<h3 id="finding-your-elements-widget-type">Finding Your Element's Widget Type</h3>
<p>Of course, in order to call the methods or access the object's class variables, you need to know the type of the underlying Widget being used.  This document could list them all, but the downside is the widget could change types (not a good thing for people using the .Widget already!).  It also saves space and time in getting this documentation published and available to you.</p>
<p>So, here's the way to get your element's widget's type:</p>
<pre><code class="python">    print(type(window[your_element_key].Widget))
</code></pre>

<p>In the case of the button example above, what is printed is:</p>
<p><code>&lt;class 'tkinter.Button'&gt;</code></p>
<p>I don't think that could be any clearer.  Your job at this point is to look at the tkinter documentation to see what the methods are for the tkinter <code>Button</code> widget.</p>
<h2 id="window-level-access">Window Level Access</h2>
<p>For this one you'll need some specific variables for the time being as there is no <code>Window</code> class variable that holds the window's representation in the GUI library being used.</p>
<p>For tkinter, at the moment, the window's root object is this:</p>
<pre><code class="python">sg.Window.TKroot
</code></pre>

<p>The type will vary in PySimpleGUI.  It will either be:
<code>tkinter.Tk()</code>
<code>tkinter.Toplevel()</code></p>
<p>Either way you'll access it using the same <code>Window</code> variable <code>sg.Window.TKroot</code></p>
<p>Watch this space in the future for the more standardized variable name for this object.  It may be something like <code>Window.Widget</code> as the Elements use or something like <code>Window.GUIWindow</code>.</p>
<h2 id="binding-tkiner-events">Binding tkiner "events"</h2>
<p>If you wish to receive events directly from tkinter, but do it in a PySimpleGUI way, then you can do that and get those events returned to you via your standard <code>Window.read()</code> call.  </p>
<p>Both the Elements and Window objects have a method called <code>bind</code>.  You specify 2 parameters to this function.  One is the string that is used to tell tkinter what events to bind.  The other is a "key modifier" for Elements and a "key" for Windows.</p>
<p>The <code>key_modifier</code> in the <code>Element.bind</code> call is something that is added to your key. If your key is a string, then this modifier will be appended to your key and the event will be a single string.</p>
<p>If your element's key is not a string, then a tuple will be returned as the event
(your_key, key_modifier)</p>
<p>This will enable you to continue to use your weird, non-string keys. Just be aware that you'll be getting back a tuple instead of your key in these situations.</p>
<p>The best example of when this can happen is in a Minesweeper game where each button is already a tuple of the (x,y) position of the button. Normal left clicks will return (x,y). A right click that was generated as a result of bind call will be ((x,y), key_modifier).</p>
<p>It'll be tricky for the user to parse these events, but it's assumed you're an advanced user if you're using this capability and are also using non-string keys.</p>
<p>There are 2 member variables that have also been added as shown in the documentation for the bind methods. This added variable contains the tkinter specific event information. In other words, the 'event' that tkinter normally sends back when a callback happens.</p>
<p>Here is sample code that shows how to make these calls.</p>
<p>Three events are being bound.</p>
<ol>
<li>Any button clicks in the window will return an event "Window Click" from window.read()</li>
<li>Right clicking the "Go" buttons will return an event "Go+RIGHT CLICK+" from window.read()</li>
<li>When the Input Element receives focus, an event "-IN-+FOCUS+" will be returned from window.read()</li>
</ol>
<pre><code class="python">import PySimpleGUI as sg

sg.theme('Dark Green 2')

layout = [  [sg.Text('My Window')],
            [sg.Input(key='-IN-'), sg.Text(size=(15,1), key='-OUT-')],
            [sg.Button('Go'), sg.Button('Exit')]
              ]

window = sg.Window('Window Title', layout, finalize=True)

window['-IN-'].bind(&quot;&lt;FocusIn&gt;&quot;, '+FOCUS+')
window.bind(&quot;&lt;Button-1&gt;&quot;, 'Window Click')
window['Go'].bind(&quot;&lt;Button-3&gt;&quot;, '+RIGHT CLICK+')

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

window.close(); del window
</code></pre>

<h2 id="there-is-no-way-to-unbind-and-event-at-this-time-sorry-didnt-think-of-it-before-releasing">There is no way to "unbind" and event at this time.  (sorry, didn't think of it before releasing)</h2>
<hr />
<hr />
<h1 id="demo-programs-applications">"Demo Programs" Applications</h1>
<p>There are too many to list!!</p>
<p>There are over 170 sample programs to give you a jump start.</p>
<p>These programs are an integral part of the overall PySimpleGUI documentation and learning system.  They will give you a headstart in a way you can learn from and understand.  They also show you integration techiques to other packages that have been figured out for you.</p>
<p>You will find Demo Programs located in a subfolder named "Demo Programs" under the top level and each of the PySimpleGUI ports on GitHub.</p>
<p>Demo programs for plain PySimpleGUI (tkinter)
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/DemoPrograms</p>
<p>Demo programs for PySimpleGUIQt:
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIQt/Demo%20Programs</p>
<p>Demo programs for PySimpleGUIWx:
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWx/Demo%20Programs</p>
<p>Demo programs for PySimpleGUIWeb:
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWeb/Demo%20Programs</p>
<p>There are not many programs under each of the port's folders because the main Demo Programs should run on all of the other platforms with minimal changes (often only the import statement changes).</p>
<p>You will also find a lot of demos running on Trinket
http://Trinket.PySimpleGUI.org</p>
<h2 id="packages-used-in-demos">Packages Used In Demos</h2>
<p>While the core PySimpleGUI code  does not utilize any 3rd party packages, some of the demos do.  They add a GUI to a few popular packages.  These packages include:
  * <a href="https://github.com/gunthercox/ChatterBot">Chatterbot</a>
  * <a href="https://github.com/olemb/mido">Mido</a>
  * <a href="https://matplotlib.org/">Matplotlib</a>
  * <a href="https://github.com/rk700/PyMuPDF">PyMuPDF</a>
  * OpenCV
  * pymunk
  * psutil
  * pygame
  * Forecastio</p>
<h1 id="creating-a-windows-exe-file">Creating a Windows .EXE File</h1>
<p>It's possible to create a single .EXE file that can be distributed to Windows users. There is no requirement to install the Python interpreter on the PC you wish to run it on. Everything it needs is in the one EXE file, assuming you're running a somewhat up to date version of Windows.</p>
<p>Installation of the packages, you'll need to install PySimpleGUI and PyInstaller (you need to install only once)</p>
<pre><code class="bash">pip install PySimpleGUI
pip install PyInstaller

</code></pre>

<p>To create your EXE file from your program that uses PySimpleGUI,  <code>my_program.py</code>, enter this command in your Windows command prompt:</p>
<pre><code class="bash">pyinstaller -wF my_program.py

</code></pre>

<p>You will be left with a single file,  <code>my_program.exe</code>, located in a folder named  <code>dist</code>  under the folder where you executed the  <code>pyinstaller</code>  command.</p>
<p>That's all... Run your  <code>my_program.exe</code>  file on the Windows machine of your choosing.</p>
<blockquote>
<p>"It's just that easy."</p>
</blockquote>
<p>(famous last words that screw up just about anything being referenced)</p>
<p>Your EXE file should run without creating a "shell window". Only the GUI window should show up on your taskbar.</p>
<p>If you get a crash with something like:</p>
<pre><code class="python">ValueError: script '.......\src\tkinter' not found
</code></pre>

<p>Then try adding <strong><code>--hidden-import tkinter</code></strong> to your command</p>
<h1 id="creating-a-mac-app-file">Creating a Mac App File</h1>
<p>There are reports that PyInstaller can be used to create App files.  It's not been officially tested.</p>
<p>Run this command on your Mac</p>
<blockquote>
<p>pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' your_program.py</p>
</blockquote>
<p>This info was located on Reddit with the source traced back to:
https://github.com/pyinstaller/pyinstaller/issues/1350</p>
<h1 id="debug-output">Debug Output</h1>
<p>Be sure and check out the EasyPrint (Print) function described in the high-level API section.  Leave your code the way it is, route your stdout and stderror to a scrolling window.</p>
<p>For a fun time, add these lines to the top of your script</p>
<pre><code class="python">    import PySimpleGUI as sg
    print = sg.Print
</code></pre>

<p>This will turn all of your print statements into prints that display in a window on your screen rather than to the terminal.</p>
<h1 id="look-and-feel">Look and Feel</h1>
<p>You can change defaults and colors of a large number of things in PySimpleGUI quite easily.</p>
<h2 id="changlelookandfeel"><code>ChangleLookAndFeel</code></h2>
<p>Want a quick way of making your windows look a LOT better?  Try calling <code>ChangeLookAndFeel</code>.  It will, in a single call, set various color values to widgets, background, text, etc.</p>
<p>Or dial in the look and feel (and a whole lot more) that you like with the <code>SetOptions</code> function.  You can change all of the defaults in one function call.  One line of code to customize the entire GUI.</p>
<pre><code class="python">    sg.ChangeLookAndFeel('GreenTan')
</code></pre>

<p>Valid look and feel values are currently:</p>
<pre><code class="python">SystemDefault
Reddit
Topanga
GreenTan
Dark
LightGreen
Dark2
Black
Tan
TanBlue
DarkTanBlue
DarkAmber
DarkBlue
Reds
Green
BluePurple
Purple
BlueMono
GreenMono
BrownBlue
BrightColors
NeutralBlue
Kayak
SandyBeach
TealMono
</code></pre>

<p>The way this call actually works is that it calls <code>SetOptions</code> with a LOT of color settings.  Here is the actual call that's made.  As you can see lots of stuff is defined for you.</p>
<pre><code class="python">SetOptions(background_color=colors['BACKGROUND'],
            text_element_background_color=colors['BACKGROUND'],
            element_background_color=colors['BACKGROUND'],
            text_color=colors['TEXT'],
            input_elements_background_color=colors['INPUT'],
            button_color=colors['BUTTON'],
            progress_meter_color=colors['PROGRESS'],
            border_width=colors['BORDER'],
            slider_border_width=colors['SLIDER_DEPTH'],
            progress_meter_border_depth=colors['PROGRESS_DEPTH'],
            scrollbar_color=(colors['SCROLL']),
            element_text_color=colors['TEXT'],
            input_text_color=colors['TEXT_INPUT'])
</code></pre>

<p>To see the latest list of color choices you can call <code>ListOfLookAndFeelValues()</code></p>
<p>You can also combine the <code>ChangeLookAndFeel</code> function with the <code>SetOptions</code> function to quickly modify one of the canned color schemes.  Maybe you like the colors but was more depth to your bezels.  You can dial in exactly what you want.</p>
<p><strong>ObjToString</strong>
Ever wanted to easily display an objects contents easily?  Use ObjToString to get a nicely formatted recursive walk of your objects.
This statement:</p>
<pre><code>print(sg.ObjToSting(x))
</code></pre>
<p>And this was the output</p>
<pre><code>&lt;class '__main__.X'&gt;
    abc = abc
    attr12 = 12
    c = &lt;class '__main__.C'&gt;
        b = &lt;class '__main__.B'&gt;
            a = &lt;class '__main__.A'&gt;
                attr1 = 1
                attr2 = 2
                attr3 = three
            attr10 = 10
            attrx = x
</code></pre>
<p>You'll quickly wonder how you ever coded without it.</p>
<hr />
<h1 id="known-issues">Known Issues</h1>
<p>Well, there are a few quirks, and problems of course.  Check the <a href="https://github.com/PySimpleGUI/PySimpleGUI/issues">GitHub Issues database</a> for a list of them.</p>
<p>As previously mentioned <strong>this is where you should post all problems and enhancements.</strong></p>
<p>Random crashes have been rare.  The code is stable and hasn't been "quirky" nor have there been many "emergency" releases.</p>
<h2 id="macs-tkinter">MACS &amp; tkinter</h2>
<p>Macs and PySimpleGUI did not play well together up until Nov 2019 and the release of ttk buttons.  Prior to that buttons had to be white.  Now the Mac can use any color for buttons and they work great.  Images on buttons work as well.</p>
<p>The problems were the normal tk.Button was not working correctly on the Mac.  You couldn't set the button color.  If you tried it appeared as if the text was missing.</p>
<p>Users have recently reported the ability to install Python 3.7 from the Python.org website and not use the Homebrew version.  This resolved all of the button color problems. </p>
<p>Regardless of where you get your Python / tkinter, Macs can now enjoy using all of the look and feel color themes that Windows and Linux users are able to achieve.</p>
<p>Many PySimpleGUI users have switched from PySimpleGUI to PySimpleGUIQt due to the button problems.  IF you're one of them, <strong><em>you should consider switching back</em></strong>.  One reason to return to PySimpleGUI is that features tend to get implemented on PySimpleGUI (tkinter version) and then later on the  other ports.  There are a number of other reasons to give tkinter another try.</p>
<h2 id="multiple-threads">Multiple threads</h2>
<p>Consider this is a <strong><em>stern warning</em></strong></p>
<h3 id="do-not-attempt-to-call-pysimplegui-from-multiple-threads-at-least-the-tkinter-based-port-because-tkinter-is-not-threadsafe-and-has-known-issues-with-multiple-threads"><strong>Do not attempt</strong> to call <code>PySimpleGUI</code> from multiple threads! At least the <code>tkinter</code> based port because tkinter is not threadsafe and has known issues with multiple threads</h3>
<p>Tkinter also wants to be the MAIN thread in your code.  So, if you have to run multiple threads, make sure the GUI is the main thread.</p>
<p>Other than that, feel free to use threads with PySimpleGUI on all of the ports.  You'll find a good example for how to run "long running tasks" in your event loop by looking at the demo program: <code>Demo_Multithreaded_Long_Tasks.py</code>.  There are several examples of using threads with PySimpleGUI.</p>
<p>Be sure and <strong>delete</strong> your windows after you close them if you are running with multiple threads.  There is a chance another thread's garbage collect will attempt to delete the window when not in the mainthread which will cause tkinter to crash.</p>
<h3 id="the-dreaded-tcl_asyncdelete-async-handler-deleted-by-the-wrong-thread-error">The dreaded "Tcl_AsyncDelete: async handler deleted by the wrong thread" error</h3>
<p>This crash has plagued and mystified tkinter users for some time now.  It happens when the user is running multiple threads in their application.  Even if the user doesn't make any calls that are into tkinter, this problem can still cause your program to crash.</p>
<p>I'm thrilled to say there's a solution and it's easy to implement.  If you're getting this error, then here is what is causing it.</p>
<p>When you close a window and delete the layout, the tkinter widgets that were in use in the window are no longer needed.  Python marks them to be handled by the "Garbage Collector".  They're deleted but not quite gone from memory.  Then, later, while your thread is running, the Python Garbage Collect algorithm decides it's time to run garbage collect.  When it tells tkinter to free up the memory, the tkinter code looks to see what context it is running under.  It sees that it's a thread, not the main thread, and generates this exception.  </p>
<p>The way around this is actually quite easy.</p>
<p>When you are finished with a window, be sure to:</p>
<ul>
<li>Close the Window</li>
<li>Set the <code>layout</code> variable to None</li>
<li>Set the <code>window</code> variable to None</li>
<li>Trigger Python's Garbage Collect to run immediately</li>
</ul>
<p>The sequence looks like this in code:</p>
<pre><code class="python">    import gc

    # Do all your windows stuff... make a layout... show your window... then when time to exit
    window.close()
    layout = None
    window = None
    gc.collect()
</code></pre>

<p>This will ensure that the tkinter widgets are all deleted in the context of the main-thread and another thread won't accidently run the Garbage Collect</p>
<h1 id="contributing-to-pysimplegui">Contributing to PySimpleGUI</h1>
<h3 id="open-source-license-but-private-development">Open Source License, but Private Development</h3>
<p>PySimpleGUI is different than most projects on GitHub.  It is licensed using the "Open Source License" LGPL3.  However, the coding and development of the project is not "open source".</p>
<p>This project does not accept user submitted code.</p>
<h4 id="write-applications-use-pysimplegui-write-tutorials-teach-others">Write Applications, Use PySimpleGUI, Write Tutorials, Teach Others</h4>
<p>These are a few of the ways you can directly contribute to PySimpleGUI.  Using the package to make cool stuff and helping others learn how to use it to make cool stuff and a big help to PySimpleGUI.   <strong>Everyone</strong> learns from seeing other people's implementations.  It's through user's creating applications that new problems and needs are discovered.  These have had a profound and positive impact on the project in the past.</p>
<h4 id="pull-requests">Pull Requests</h4>
<p>Pull requests are <em>not being accepted</em> for the project.  This includes sending code changes via other means than "pull requests".  Plainly put, core code you send will not be used.</p>
<h4 id="bug-fixes">Bug Fixes</h4>
<p>If you file an Issue for a bug, have located the bug, and found a fix in 10 lines of code or less.... and you wish to share your fix with the community, then feel free to include it with the filed Issue.  If it's longer than 10 lines and wish to discuss it, then send an email to <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="f59d909985b5a58ca69c98859990b2a0bcdb9a8792db">[email&#160;protected]</a></p>
<h2 id="thank-you">Thank You</h2>
<p>The support from the user community has been amazing.  Your passion for creating PySimpleGUI applications is infectious.  Every "thank you" is noticed and appreciated!  Your passion for wanting to see PySimpleGUI improve is neither ignored nor unappreciated.</p>
<p>It's understood that this way of development of a Python package is unorthodox.  You may find it frustrating and slow, but hope you can respect the decision for it to operate in this manner and be supportive.</p>
<h2 id="github-repos">GitHub Repos</h2>
<p>If you've created a GitHub for your project that uses PySimpleGUI then please post screenshots in in the "User's Screenshots" Issue on the PySimpleGUI GitHub.  Say a little something about it and I'll also add it to the announcements. People <em>love</em> success stories and showing your GUI's screen visually communicates your success. </p>
<h2 id="versions">Versions</h2>
<table>
<thead>
<tr>
<th>Version</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>1.0.9</td>
<td>July 10, 2018 - Initial Release</td>
</tr>
<tr>
<td>1.0.21</td>
<td>July 13, 2018 - Readme updates</td>
</tr>
<tr>
<td>2.0.0</td>
<td>July 16, 2018 - ALL optional parameters renamed from CamelCase to all_lower_case</td>
</tr>
<tr>
<td>2.1.1</td>
<td>July 18, 2018 - Global settings exposed, fixes</td>
</tr>
<tr>
<td>2.2.0</td>
<td>July 20, 2018 - Image Elements, Print output</td>
</tr>
<tr>
<td>2.3.0</td>
<td>July 23, 2018 - Changed form.Read return codes, Slider Elements, Listbox element. Renamed some methods but left legacy calls in place for now.</td>
</tr>
<tr>
<td>2.4.0</td>
<td>July 24, 2018 - Button images. Fixes so can run on Raspberry Pi</td>
</tr>
<tr>
<td>2.5.0</td>
<td>July 26, 2018 - Colors. Listbox scrollbar. tkinter Progress Bar instead of homegrown.</td>
</tr>
<tr>
<td>2.6.0</td>
<td>July 27, 2018 - auto_size_button setting.  License changed to LGPL 3+</td>
</tr>
<tr>
<td>2.7.0</td>
<td>July 30, 2018 - realtime buttons, window_location default setting</td>
</tr>
<tr>
<td>2.8.0</td>
<td>Aug 9, 2018 - New None default option for Checkbox element, text color option for all elements, return values as a dictionary, setting focus, binding return key</td>
</tr>
<tr>
<td>2.9.0</td>
<td>Aug 16,2018 - Screen flash fix, <code>do_not_clear</code> input field option, <code>autosize_text</code> defaults to <code>True</code> now, return values as ordered dict, removed text target from progress bar, rework of return values and initial return values, removed legacy Form.Refresh() method (replaced by Form.ReadNonBlockingForm()), COLUMN elements!!, colored text defaults</td>
</tr>
<tr>
<td>2.10.0</td>
<td>Aug 25, 2018 - Keyboard &amp; Mouse features (Return individual keys as if buttons, return mouse scroll-wheel as button, bind return-key to button, control over keyboard focus), SaveAs Button, Update &amp; Get methods for InputText, Update for Listbox, Update &amp; Get for Checkbox, Get for Multiline, Color options for Text Element Update, Progess bar Update can change max value, Update for Button to change text &amp; colors, Update for Image Element, Update for Slider, Form level text justification, Turn off default focus, scroll bar for Listboxes, Images can be from filename or from in-RAM, Update for Image).  Fixes - text wrapping in buttons, msg box, removed slider borders entirely and others</td>
</tr>
<tr>
<td>2.11.0</td>
<td>Aug 29, 2018 - Lots of little changes that are needed for the demo programs to work. Buttons have their own default element size, fix for Mac default button color, padding support for all elements, option to immediately return if list box gets selected, FilesBrowse button, Canvas Element, Frame Element, Slider resolution option, Form.Refresh method, better text wrapping, 'SystemDefault' look and feel settin</td>
</tr>
<tr>
<td>2.20.0</td>
<td>Sept 4, 2018 - Some sizable features this time around of interest to advanced users.  Renaming of the MsgBox functions to Popup. Renaming GetFile, etc, to PopupGetFile. High-level windowing capabilities start with Popup, PopupNoWait/PopupNonblocking, PopupNoButtons, default icon, change_submits option for Listbox/Combobox/Slider/Spin/, New OptionMenu element, updating elements after shown, system defaul color option for progress bars, new button type (Dummy Button) that only closes a window, SCROLLABLE Columns!! (yea, playing in the Big League now), LayoutAndShow function removed, form.Fill - bulk updates to forms, FindElement - find element based on key value (ALL elements have keys now), no longer use grid packing for row elements (a potentially huge change), scrolled text box sizing changed, new look and feel themes (Dark, Dark2, Black, Tan, TanBlue, DarkTanBlue, DarkAmber, DarkBlue, Reds, Green)</td>
</tr>
<tr>
<td>2.30.0</td>
<td>Sept 6, 2018 - Calendar Chooser (button), borderless windows, load/save form to disk</td>
</tr>
<tr>
<td>3.0.0</td>
<td>Sept 7, 2018 - The "fix for poor choice of 2.x numbers" release. Color Chooser (button), "grab anywhere" windows are on by default, disable combo boxes, Input Element text justification (last part needed for 'tables'), Image Element changes to support OpenCV?, PopupGetFile and PopupGetFolder have better no_window option</td>
</tr>
<tr>
<td>3.01.01</td>
<td>Sept 10, 2018 - Menus! (sort of a big deal)</td>
</tr>
<tr>
<td>3.01.02</td>
<td>Step 11, 2018 - All Element.Update functions have a <code>disabled</code> parameter so they can be disabled.  Renamed some parameters in Update function (sorry if I broke your code), fix for bug in Image.Update. Wasn't setting size correctly, changed grab_anywhere logic again,added grab anywhere option to PupupGetText (assumes disabled)</td>
</tr>
<tr>
<td>3.02.00</td>
<td>Sept 14, 2018 - New Table Element (Beta release), MsgBox removed entirely, font setting for InputText Element, <strong>packing change</strong> risky change that allows some Elements to be resized,removed command parameter from Menu Element, new function names for ReadNonBlocking (Finalize, PreRead), change to text element autosizing and wrapping (yet again), lots of parameter additions to Popup functions (colors, etc).</td>
</tr>
<tr>
<td>3.03.00</td>
<td>New feature - One Line Progress Meters, new display_row_numbers for Table Element, fixed bug in EasyProgresssMeters (function will soon go away), OneLine and Easy progress meters set to grab anywhere but can be turned off.</td>
</tr>
<tr>
<td>03,04.00</td>
<td>Sept 18, 2018 - New features - Graph Element, Frame Element, more settings exposed to Popup calls.  See notes below for more.</td>
</tr>
<tr>
<td>03.04.01</td>
<td>Sept 18, 2018 - See release notes</td>
</tr>
<tr>
<td>03.05.00</td>
<td>Sept 20, 2018 - See release notes</td>
</tr>
<tr>
<td>03.05.01</td>
<td>Sept 22, 2018 - See release notes</td>
</tr>
<tr>
<td>03.05.02</td>
<td>Sept 23, 2018 - See release notes</td>
</tr>
<tr>
<td>03.06.00</td>
<td>Sept 23, 2018 - Goodbye FlexForm, hello Window</td>
</tr>
<tr>
<td>03.08.00</td>
<td>Sept 25, 2018 - Tab and TabGroup Elements\</td>
</tr>
<tr>
<td>01.00.00 for 2.7</td>
<td>Sept 25, 2018 - First release for 2.7</td>
</tr>
<tr>
<td>03.08.04</td>
<td>Sept 30, 2018 - See release notes</td>
</tr>
<tr>
<td>03.09.00</td>
<td>Oct 1, 2018</td>
</tr>
<tr>
<td>2.7 01.01.00</td>
<td>Oct 1, 2018</td>
</tr>
<tr>
<td>2.7 01.01.02</td>
<td>Oct 8, 2018</td>
</tr>
<tr>
<td>03.09.01</td>
<td>Oct 8, 2018</td>
</tr>
<tr>
<td>3.9.3 &amp; 1.1.3</td>
<td>Oct 11, 2018</td>
</tr>
<tr>
<td>3.9.4 &amp; 1.1.4</td>
<td>Oct 16, 2018</td>
</tr>
<tr>
<td>3.10.1 &amp; 1.2.1</td>
<td>Oct 20, 2018</td>
</tr>
<tr>
<td>3.10.3 &amp; 1.2.3</td>
<td>Oct 23, 2018</td>
</tr>
<tr>
<td>3.11.0 &amp; 1.11.0</td>
<td>Oct 28, 2018</td>
</tr>
<tr>
<td>3.12.0 &amp; 1.12.0</td>
<td>Oct 28, 2018</td>
</tr>
<tr>
<td>3.13.0 &amp; 1.13.0</td>
<td>Oct 29, 2018</td>
</tr>
<tr>
<td>3.14.0 &amp; 1.14.0</td>
<td>Nov 2, 2018</td>
</tr>
<tr>
<td>3.15.0 &amp; 1.15.0</td>
<td>Nov 20, 2018</td>
</tr>
<tr>
<td>3.16.0 &amp; 1.16.0</td>
<td>Nov 26, 2018</td>
</tr>
<tr>
<td>3.17.0 &amp; 1.17.0</td>
<td>Dec 1, 2018</td>
</tr>
</tbody>
</table>
<h2 id="release-notes">Release Notes</h2>
<p>2.3 - Sliders, Listbox's and Image elements (oh my!)</p>
<p>If using Progress Meters, avoid cancelling them when you have another window open.  It could lead to future windows being blank. It's being worked on.</p>
<p>New debug printing capability.  <code>sg.Print</code></p>
<p>2.5 Discovered issue with scroll bar on <code>Output</code> elements.  The bar will match size of ROW not the size of the element.  Normally you never notice this due to where on a form the <code>Output</code> element goes.</p>
<p>Listboxes are still without scrollwheels. The mouse can drag to see more items.  The mouse scrollwheel will also scroll the list and will <code>page up</code> and <code>page down</code> keys.</p>
<p>2.7 Is the "feature complete" release. Pretty much all features are done and in the code</p>
<p>2.8 More text color controls.  The caller has more control over things like the focus and what buttons should be clicked when enter key is pressed. Return values as a dictionary! (NICE addition)</p>
<p>2.9 COLUMNS!  This is the biggest feature and had the biggest impact on the code base.  It was a difficult feature to add, but it was worth it.  Can now make even more layouts. Almost any layout is possible with this addition.</p>
<p>.................. insert releases 2.9 to 2.30 .................</p>
<p>3.0 We've come a long way baby!  Time for a major revision bump.  One reason is that the numbers started to confuse people  the latest release was 2.30, but some people read it as 2.3 and thought it went backwards.  I kinda messed up the 2.x series of numbers, so why not start with a clean slate.  A lot has happened anyway so it's well earned.</p>
<p>One change that will set PySimpleGUI apart is the parlor trick of being able to move the window by clicking on it anywhere.  This is turned on by default.  It's not a common way to interact with windows.  Normally you have to move using the titlebar.  Not so with PySimpleGUI.  Now you can drag using any part of the window.  You will want to turn off for windows with sliders.  This feature is enabled in the Window call.</p>
<p>Related to the Grab Anywhere feature is the no_titlebar option, again found in the call to Window.  Your window will be a spiffy, borderless window.  It's a really interesting effect.  Slight problem is that you do not have an icon on the taskbar with these types of windows, so if you don't supply a button to close the window, there's no way to close it other than task manager.</p>
<p>3.0.2 Still making changes to Update methods with many more ahead in the future.  Continue to mess with grab anywhere option.  Needed to disable in more places such as the PopupGetText function.  Any time these is text input on a form, you generally want to turn off the grab anywhere feature.</p>
<h4 id="320">3.2.0</h4>
<p>Biggest change was the addition of the Table Element.  Trying to make changes so that form resizing is a possibility but unknown if will work in the long run.  Removed all MsgBox, Get* functions and replaced with Popup functions.  Popups had multiple new parameters added to change the look and feel of a popup.</p>
<h4 id="330">3.3.0</h4>
<p>OneLineProgressMeter function added which gives you not only a one-line solution to progress meters, but it also gives you the ability to have more than 1 running at the same time, something not possible with the EasyProgressMeterCall</p>
<h4 id="340">3.4.0</h4>
<ul>
<li>Frame - New Element - a labelled frame for grouping elements. Similar
   to Column</li>
<li>Graph (like a Canvas element except uses the caller's
   coordinate system rather than tkinter's).</li>
<li>initial_folder - sets starting folder for browsing type buttons (browse for file/folder).</li>
<li>Buttons return  key value rather than button text <strong>If</strong> a <code>key</code> is specified,
*
   OneLineProgressMeter!  Replaced EasyProgressMeter (sorry folks that's
   the way progress works sometimes)</li>
<li>Popup - changed ALL of the Popup calls to   provide many more customization settings<ul>
<li>Popup</li>
<li>PopupGetFolder</li>
<li>PopupGetFile</li>
<li>PopupGetText</li>
<li>Popup</li>
<li>PopupNoButtons</li>
<li>PopupNonBlocking</li>
<li>PopupNoTitlebar</li>
<li>PopupAutoClose</li>
<li>PopupCancel</li>
<li>PopupOK</li>
<li>PopupOKCancel</li>
<li>PopupYesNo</li>
</ul>
</li>
</ul>
<h4 id="341">3.4.1</h4>
<ul>
<li>Button.GetText - Button class method.  Returns the current text being shown on a button.</li>
<li>Menu - Tearoff option. Determines if menus should allow them to be torn off</li>
<li>Help - Shorcut button. Like Submit, cancel, etc</li>
<li>ReadButton - shortcut for ReadFormButton</li>
</ul>
<h4 id="350">3.5.0</h4>
<ul>
<li>Tool Tips for all elements</li>
<li>Clickable text</li>
<li>Text Element relief setting</li>
<li>Keys as targets for buttons</li>
<li>New names for buttons:</li>
<li>Button = SimpleButton</li>
<li>RButton = ReadButton = ReadFormButton</li>
<li>Double clickable list entries</li>
<li>Auto sizing table widths works now</li>
<li>Feature DELETED - Scaling. Removed from all elements</li>
</ul>
<h4 id="351">3.5.1</h4>
<ul>
<li>Bug fix for broken PySimpleGUI if Python version &lt; 3.6 (sorry!)</li>
<li>LOTS of Readme changes</li>
</ul>
<h4 id="352">3.5.2</h4>
<ul>
<li>Made <code>Finalize()</code> in a way that it can be chained</li>
<li>Fixed bug in return values from Frame Element contents</li>
</ul>
<h4 id="360">3.6.0</h4>
<ul>
<li>Renamed FlexForm to Window</li>
<li>Removed LookAndFeel capability from Mac platform.</li>
</ul>
<h4 id="380">3.8.0</h4>
<ul>
<li>Tab and TabGroup Elements - awesome new capabilities</li>
</ul>
<h4 id="100-python-27">1.0.0 Python 2.7</h4>
<p>It's official.  There is a 2.7 version of PySimpleGUI!</p>
<h4 id="382">3.8.2</h4>
<ul>
<li>Exposed <code>TKOut</code> in Output Element</li>
<li><code>DrawText</code> added to Graph Elements</li>
<li>Removed <code>Window.UpdateElements</code></li>
<li><code>Window.grab_anywere</code> defaults to False</li>
</ul>
<h4 id="383">3.8.3</h4>
<ul>
<li>Listbox, Slider, Combobox, Checkbox,  Spin, Tab Group - if change_submits is set, will return the Element's key rather than ''</li>
<li>Added change_submits capability to Checkbox, Tab Group</li>
<li>Combobox - Can set value to an Index into the Values table rather than the Value itself</li>
<li>Warnings added to Drawing routines for Graph element (rather than crashing)</li>
<li>Window - can "force top level" window to be used rather than a normal window.  Means that instead of calling Tk to get a window, will call TopLevel to get the window</li>
<li>Window Disable / Enable - Disables events (button clicks, etc) for a Window.  Use this when you open a second window and want to disable the first window from doing anything. This will simulate a 'dialog box'</li>
<li>Tab Group returns a value with Window is Read.  Return value is the string of the selected tab</li>
<li>Turned off grab_anywhere for Popups</li>
<li>New parameter, default_extension, for PopupGetFile</li>
<li>Keyboard shortcuts for menu items. Can hold ALT key to select items in men</li>
<li>Removed old-style Tabs - Risky change because it hit fundamental window packing and creation. Will also break any old code using this style tab (sorry folks this is how progress happens)</li>
</ul>
<h4 id="386">3.8.6</h4>
<ul>
<li>Fix for Menus.</li>
<li>Fixed table colors. Now they work</li>
<li>Fixed returning keys for tabs</li>
<li>Window Hide / UnHide methods</li>
<li>Changed all Popups to remove context manager</li>
<li>Error checking for Graphing objects and for Element Updates</li>
</ul>
<h3 id="390-110">3.9.0 &amp; 1.1.0</h3>
<ul>
<li>The FIRST UNIFIED version of the code!</li>
<li>Python 2.7 got a TON of features . Look back to 1.0 release for the list</li>
<li>Tab locations - Can place Tabs on top, bottom, left, right now instead of only the top</li>
</ul>
<h3 id="391-112">3.9.1 &amp; 1.1.2</h3>
<ul>
<li>Tab features</li>
<li>Themes</li>
<li>Enable / Disable</li>
<li>Tab text colors</li>
<li>Selected tab color</li>
<li>New GetListValues method for Listbox</li>
<li>Can now have multiple progress bars in 1 window</li>
<li>Fix for closing debug-output window with other windows open</li>
<li>Topanga Look and Feel setting</li>
<li>User can create new look and feel settings / can access the look and feel table</li>
<li>New PopupQuick call. Shows a non-blocking popup window with auto-close</li>
<li>Tree Element partially done (don't use despite it showing up)</li>
</ul>
<h3 id="393-113">3.9.3 &amp; 1.1.3</h3>
<ul>
<li>Disabled setting when creating element for:</li>
<li>Input</li>
<li>Combo</li>
<li>Option Menu</li>
<li>Listbox</li>
<li>Radio</li>
<li>Checkbox</li>
<li>Spinner</li>
<li>Multiline</li>
<li>Buttons</li>
<li>Slider</li>
<li>Doc strings on all Elements updated</li>
<li>Buttons can take image data as well as image files</li>
<li>Button Update can change images</li>
<li>Images can have background color</li>
<li>Table element new num_rows parameter</li>
<li>Table Element new alternating_row_color parameter</li>
<li>Tree Element</li>
<li>Window Disappear / Reappear methods</li>
<li>Popup buttons resized to same size</li>
<li>Exposed look and feel table</li>
</ul>
<h3 id="394-114">3.9.4 &amp; 1.1.4</h3>
<ul>
<li>Parameter order change for Button.Update so that new button ext is at front</li>
<li>New Graph.DrawArc method</li>
<li>Slider tick interval parameter for labeling sliders</li>
<li>Menu tearoff now disabled by default</li>
<li>Tree Data printing simplified and made prettier</li>
<li>Window resizable parameter.  Defaults to not resizable</li>
<li>Button images can have text over them now</li>
<li>BUG fix in listbox double-click.  First bug fix in months</li>
<li>New Look And Feel capability.  List predefined settings using ListOfLookAndFeelValues</li>
</ul>
<h3 id="3101-121">3.10.1 &amp; 1.2.1</h3>
<ul>
<li>Combobox new readonly parameter in init and Update</li>
<li>Better default sizes for Slider</li>
<li>Read of Tables now returns which rows are selected (big damned deal feature)</li>
<li>PARTIAL support of Table.Update with new values (use at your own peril)</li>
<li>Alpha channel setting for Windows</li>
<li>Timeout setting for Window.Read (big damned deal feature)</li>
<li>Icon can be base64 image now in SetIcon call</li>
<li>Window.FindElementWithFocus call</li>
<li>Window.Move allows moving window anywhere on screen</li>
<li>Window.Minimize will minimize to taskbar</li>
<li>Button background color can be set to system default (i.e. not changed)</li>
</ul>
<h3 id="3102-122">3.10.2 &amp; 1.2.2</h3>
<p>Emergency patch release... going out same day as previous release
* The timeout timer for the new Read with timer wasn't being properly shut down
* The Image.Update method appears to not have been written correctly.  It didn't handle base64 images like the other elements that deal with images (buttons)</p>
<h3 id="3103-123">3.10.3 &amp; 1.2.3</h3>
<ul>
<li>New element - Vertical Separator</li>
<li>New parameter for InputText - change_submits. If True will cause Read to return when a button fills in the InputText element</li>
<li>Read with timeout = 0 is same as read non blocking and is the new preferred method</li>
<li>Will return event == None if window closed</li>
<li>New Close method will close all window types</li>
<li>Scrollbars for Tables automatically added (no need for a Column Element)</li>
<li>Table Update method complete</li>
<li>Turned off expand when packing row frame... was accidentally turned on (primary reason for this release)</li>
<li>Try added to Image Update so won't crash if bad image passed in</li>
</ul>
<h3 id="3110-1110">3.11.0 &amp; 1.11.0</h3>
<ul>
<li>Syncing up the second digit of the releases so that they stay in sync better.  the 2.7 release is built literally from the 3.x code so they really are the same</li>
<li>Reworked Read call... significantly.</li>
<li>Realtime buttons work with timeouts or blocking read</li>
<li>Removed default value parm on Buttons and Button Updates</li>
<li>New Tree Element parm show_expanded. Causes Tree to be shown as fully expanded</li>
<li>Tree Element now returns which rows are selected when Read</li>
<li>New Window method BringToFront</li>
<li>Shortcut buttons no longer close windows!</li>
<li>Added CloseButton, CButton that closes the windows</li>
</ul>
<h3 id="3120-1120">3.12.0 &amp; 1.12.0</h3>
<ul>
<li>Changed Button to be the same as ReadButton which means it will no longer close the window</li>
<li>All shortcut buttons no longer close the window</li>
<li>Updating a table clears selected rows information in return values</li>
<li>Progress meter uses new CloseButton</li>
<li>Popups use new CloseButton</li>
</ul>
<h3 id="3130-1130">3.13.0 &amp; 1.13.0</h3>
<ul>
<li>Improved multiple window handling of Popups when the X is used to close</li>
<li>Change submits added for:</li>
<li>Multiline</li>
<li>Input Text</li>
<li>Table</li>
<li>Tree</li>
<li>Option to close calendar chooser when date selected</li>
<li>Update for Tree Element</li>
<li>Scroll bars for Trees</li>
</ul>
<h3 id="3140-1140">3.14.0 &amp; 1.14.0</h3>
<ul>
<li>More windowing changes...<ul>
<li>using a hidden root windowing (Tk())</li>
<li>all children are Toplevel() windows</li>
</ul>
</li>
<li>Read only setting for:<ul>
<li>Input Text</li>
<li>Multiline</li>
</ul>
</li>
<li>Font setting for InputCombo, Multiline</li>
<li>change_submits setting for Radio Element</li>
<li>SetFocus for multiline, input elements</li>
<li>Default mon, day, year for calendar chooser button</li>
<li>Tree element update, added ability to change a single key</li>
<li>Message parm removed from ReadNonBlocking</li>
<li>Fix for closing windows using X</li>
<li>CurrentLocation method for Windows</li>
<li>Debug Window options<ul>
<li>location</li>
<li>font</li>
<li>no_button</li>
<li>no_titlebar</li>
<li>grab_anywhere</li>
<li>keep_on_top</li>
</ul>
</li>
<li>New Print / EasyPrint options<ul>
<li>location</li>
<li>font</li>
<li>no_button</li>
<li>no_titlebar</li>
<li>grab_anywhere</li>
<li>keep_on_top</li>
</ul>
</li>
<li>New popup, PopupQuickMessage</li>
<li>PopupGetFolder, PopupGetFile new initial_folder parm</li>
</ul>
<h3 id="3150-1150">3.15.0 &amp; 1.15.0</h3>
<ul>
<li>Error checking for InputText.Get method</li>
<li>Text color, background color added to multiline element.Update</li>
<li>Update method for Output Element - gives ability to clear the output</li>
<li>Graph Element - Read returns values if new flages set<ul>
<li>Change submits, drag submits</li>
<li>Returns x,y coordinates</li>
</ul>
</li>
<li>Column element new parm vertical_scroll_only</li>
<li>Table element new parm - bind return key - returns if return or double click</li>
<li>New Window parms - size, disable_close</li>
<li>"Better" multiwindow capabilities</li>
<li>Window.Size property</li>
<li>Popups - new title parm, custom_text<ul>
<li>title sets the window title</li>
<li>custom_text - single string or tuple string sets text on button(s)</li>
</ul>
</li>
</ul>
<h3 id="3160-1160">3.16.0 &amp; 1.16.0</h3>
<ul>
<li>Bug fix in PopupScrolled</li>
<li>New <code>Element</code> shortcut function for <code>FindElement</code></li>
<li>Dummy Stretch Element made for backwards compatibility with Qt</li>
<li>Timer function prints in milliseconds now, was seconds</li>
</ul>
<h3 id="3170-1170-2-dec-2018">3.17.0 &amp;1.17.0 2-Dec-2018</h3>
<p>3.17.0 2-Dec-2017
* Tooltip offset now programmable.  Set variable DEFAULT_TOOLTIP_OFFSET.  Defaults to (20,-20)
* Tooltips are always on top now
* Disable menu items
* Menu items can have keys
* StatusBar Element (preparing for a real status bar in Qt)
* enable_events parameter added to ALL Elements capable of generating events
* InputText.Update select parameter will select the input text
* Listbox.Update - set_to_index parameter will select a single items
* Menus can be updated!
* Menus have an entry in the return values
* LayoutAndRead depricated
* Multi-window support continues (X detection)
* PopupScrolled now has a location parameter
* row_height parameter to Table Element
* Stretch Element (DUMMY) so that can be source code compatible with Qt
* ButtonMenu Element (DUMMY) so can be source code compat with Qt.  Will implement eventually</p>
<h2 id="3180-11-dec-2018">3.18.0  11-Dec-2018</h2>
<p>NOTE - <strong>Menus are broken</strong> on version 2.7.  Don't know how long they've been this way.  Please get off legacy Python if that's what you're running.</p>
<ul>
<li>Default progress bar length changed to shorter</li>
<li>Master window and tracking of num open windows moved from global to Window class variable</li>
<li>Element visibility setting (when created and when Updating element)</li>
<li>Input text visiblity</li>
<li>Combo visiblity</li>
<li>Combo replaces InputCombo as the primary class name</li>
<li>Option menu visibility</li>
<li>Listbox visiblity</li>
<li>Listbox new SetFocus method</li>
<li>Radio visibility</li>
<li>Checkbox visibility</li>
<li>Spin visiblity</li>
<li>Spin new Get method returns current value</li>
<li>Multiline visiblity</li>
<li>Text visibility</li>
<li>StatusBar visiblity</li>
<li>Output visibility</li>
<li>Button visibility</li>
<li>Button SetFocus</li>
<li>ProgressBar - New Update method (used only for visibility)</li>
<li>Image - clickable images!  enable_events parameter</li>
<li>Image visibility</li>
<li>Canvas visibility</li>
<li>Graph visibility</li>
<li>Graph - new DrawImage capability (finally)</li>
<li>Frame visibility</li>
<li>Tab visibility (may not be fully functional)</li>
<li>TabGroup visibility</li>
<li>Slider visibility</li>
<li>Slider - new disable_number_display parameter</li>
<li>Column visibilty</li>
<li>Menu visibility - Not functional</li>
<li>Table visibility</li>
<li>Table - new num_rows parm for Update - changes number of visible rows</li>
<li>Tree visiblity</li>
<li>Window - New element_padding parameter will get padding for entire window</li>
<li>OneLineProgressMeter - Completely REPLACED the implementation</li>
<li>OneLineProgressMeter - can get reason for the cancellation (cancel button versus X)</li>
<li>EasyProgressMeter - completely removed. Use OneLineProgressMeter instead</li>
<li>Debug window, EasyPrint, Print - debug window will re-open if printed to after being closed</li>
<li>SetOptions - can change the error button color</li>
<li>Much bigger window created when running PySimpleGUI.py by itself.  Meant to help with regression testing</li>
</ul>
<h2 id="3192-13-dec-2018">3.19.2  13-Dec-2018</h2>
<ul>
<li>Warning for Mac's when trying to change button color</li>
<li>New parms for Button.Update - image_size and image_subsample</li>
<li>Buttons - remove highlight when border depth == 0</li>
<li>OneLineProgressMeter - better layout implementation</li>
</ul>
<h2 id="3200-1200-18-dec-2018">3.20.0 &amp; 1.20.0 18-Dec-2018</h2>
<ul>
<li>New Pane Element</li>
<li>Graph.DeleteFigure method</li>
<li>disable_minimize - New parameter for Window</li>
<li>Fix for 2.7 menus</li>
<li>Debug Window no longer re-routes stdout by default</li>
<li>Can re-route by specifying in Print / EasyPrint call</li>
<li>New non-blocking for PopupScrolled</li>
<li>Can set title for PopupScrolled window</li>
</ul>
<h2 id="3210-1210-28-dec-2018">3.21.0 &amp; 1.21.0 28-Dec-2018</h2>
<ul>
<li>ButtonMenu Element</li>
<li>Embedded base64 default icon</li>
<li>Input Text Right click menu</li>
<li>Disabled Input Text are now 'readonly' instead of disabled</li>
<li>Listbox right click menu</li>
<li>Multiline right click menu</li>
<li>Text right click menu</li>
<li>Output right click menu</li>
<li>Image right click menu</li>
<li>Canvas right click menu</li>
<li>Graph right click menu</li>
<li>Frame right click menu</li>
<li>Tab, tabgroup right click menu (unsure if works correctly)</li>
<li>Column right click menu</li>
<li>Table right click menu</li>
<li>Tree right click menu</li>
<li>Window level right click menu</li>
<li>Window icon can be filename or bytes (Base64 string)</li>
<li>Window.Maximize method</li>
<li>Attempted to use Styles better with Combobox</li>
<li>Fixed bug blocking setting bar colors in OneLineProgressMeter</li>
</ul>
<h1 id="3220-pysimplegui-1220-pysimplegui27">3.22.0 PySimpleGUI / 1.22.0 PySimpleGUI27</h1>
<ul>
<li>Added type hints to some portions of the code</li>
<li>Output element can be made invisible</li>
<li>Image sizing and subsample for Button images</li>
<li>Invisibility for ButtonMenusup</li>
<li>Attempt at specifying size of Column elements (limited success)</li>
<li>Table Element</li>
<li>New row_colors parameter</li>
<li>New vertical_scroll_only parameter - NOTE - will have to disable to get horizontal scrollbars</li>
<li>Tree Element</li>
<li>New row_height parameter</li>
<li>New feature - Icons for tree entries using filename or Base64 images</li>
<li>Fix for bug sending back continuous mouse events</li>
<li>New parameter silence_on_error for FindElement / Element calls</li>
<li>Slider returns float now</li>
<li>Fix for Menus when using Python 2.7</li>
<li>Combobox Styling (again)</li>
</ul>
<h1 id="320-pysimplegui-1230-pysimplegui27-16-jan-2019">3.2.0 PySimpleGUI /  1.23.0 PySimpleGUI27 16-Jan-2019</h1>
<ul>
<li>Animated GIFs!</li>
<li>Calendar Chooser stays on top of other windows</li>
<li>Fixed bug of no column headings for Tables</li>
<li>Tables now use the font parameter</li>
</ul>
<h1 id="3240-1240-16-jan-2019">3.24.0 1.24.0 16-Jan-2019</h1>
<ul>
<li>PopupAnimated - A popup call for showing "loading" type of windows</li>
</ul>
<h1 id="325-125-20-feb-2019">3.25 &amp; 1.25 20-Feb-2019</h1>
<ul>
<li>Comments :-)</li>
<li>Convert Text to string right away</li>
<li>Caught exceptions when main program shut down with X</li>
<li>Caught exceptions in all of the graphics primitives</li>
<li>Added parameter exportselection=False to Listbox so can use multiple listboxes</li>
<li>OneLineProgressMeter - Can now change the text on every call if desired</li>
</ul>
<h2 id="3270-pysimplegui-31-mar-2019">3.27.0 PySimpleGUI  31-Mar-2019</h2>
<p>Mixup.... 3.26 changes don't appear to have been correctly released so releasing in 3.27 now</p>
<ul>
<li>do_not_clear now defaults to TRUE!!!</li>
<li>Input Element</li>
<li>Multiline Element</li>
<li>Enable Radio Buttons to be in different containers</li>
<li>Ability to modify Autoscroll setting in Multiline.Update call</li>
<li>PopupGetFolder, PopupGetFile, PopupGetText - title defaults to message if none provided</li>
<li>PopupAnimated - image_source can be a filename or bytes (base64)</li>
<li>Option Menu can now have values updated</li>
</ul>
<h2 id="3280-11-apr-2019-pysimplegui">3.28.0 11-Apr-2019 PySimpleGUI</h2>
<ul>
<li>NEW Window Parameter - layout - second parameter. Can pass in layout directly now!</li>
<li>New shortcuts<ul>
<li>I = InputText</li>
<li>B = Btn = Butt = Button</li>
</ul>
</li>
<li>Convert button text to string when creating buttons</li>
<li>Buttons are returned now as well as input fields when searching for element with focus</li>
</ul>
<h2 id="329-22-apr-2019">3.29 22-Apr-2019</h2>
<ul>
<li>New method for <code>Graph</code> - <code>RelocateFigure</code></li>
<li>Output Element no longer accepts focus</li>
</ul>
<h2 id="3320-pysimplegui-24-may-2019">3.32.0 PySimpleGUI 24-May-2019</h2>
<ul>
<li>Rework of ALLL Tooltips. Was always displaying at uttuper left part of element. Not displays closer to where mouse entered or edited</li>
<li>New Element.Widget base class variable. Brings tkinter into the newer architecture of user accessibility to underlying GUI Frameworks' widgets</li>
<li>New SetTooltip Element method. Means all Elements gain this method. Can set the tooltip on the fly now for all elements</li>
<li>Include scroll bar when making visible / invisible Listbox Elements</li>
<li>New Radio Element method - <code>Radio.ResetGroup()</code> sets all elements in the Radio Group to False* Added borderwidth to Multiline Element</li>
<li><code>Button.Click()</code> - new method - Generates a button click even as if a user clicked a button (at the tkinter level)</li>
<li>Made a Graph.Images dictionary to keep track of images being used in a graph.  When graph is deleted, all of the accociated images should be deleted too.'</li>
<li>Added <code>Graph.SetFocus()</code> to give a Graph Element the focus just as you can input elements</li>
<li>Table new parameter - <code>hide_vertical_scroll</code> if True will hide the table's vertical bars</li>
<li>Window - new parameter - <code>transparent_color</code>. Causes a single color to become completely transparent such that you see through the window, you can click through the window. Its like tineows never was there.</li>
<li>The new <code>Window.AllKeysDict = {}</code> has been adopted by all PySimpleGUI ports.  It's a new method of automatically creating missing keys, storing and retrieving keys in general for a window.</li>
<li>Changed how <code>window.Maximize</code> is implemented previously used the '-fullscreen' attribute.  Now uses the 'zoomed' state</li>
<li>Window gets a new <code>Normal()</code> method to return from Maximize state.  Sets root.state('normal')</li>
<li>Window.Close() now closes the special <code>Window.hidden_master_root</code> window when the "last" window is closed</li>
<li><code>Window.SetTransparentColor</code> method added.  Same effect as if window was created with parameter set</li>
<li>An Element's Widget stored in <code>.Widget</code> attribute</li>
<li>Making ComboBox's ID unique by using it's Key</li>
<li>Changed Multiline to be sunken and have a border depth setting now</li>
<li>Removed a second canvas that was being used for Graph element.</li>
<li>Changed how no titlebar is implemented running on Linux versus Windows. -type splash now used for Linux</li>
<li>PopupScrolled - Added back using CloseButton to close the window</li>
<li>Fixed PopupGetFolder to use correct PySimpleGUI program constructs (keys)</li>
<li>PopupGetText populated values carrectly using the value variable, used keys</li>
<li>PopupAnimated finally gets a completely transparent background</li>
</ul>
<h2 id="3330-and-133-pysimplegui-25-may-2019">3.33.0 and 1.33 PySimpleGUI 25-May-2019</h2>
<ul>
<li>Emergency fix due to debugger.  Old bug was that Image Element was not testing for COLOR_SYSTEM_DEFAULT correctly.</li>
</ul>
<h2 id="3340-pysimplegui-1340-pysimplegui27-25-may-2019">3.34.0 PySimpleGUI &amp; 1.34.0 PySimpleGUI27 25-May-2019</h2>
<p>pip rhw  w cenf
* Fixed Window.Maximize and Window.Normal - needed special code for Linux
* Check for DEFAULT_SCROLLBAR_COLOR not being the COLOR_SYSTEM_DEFAULT (crashed)</p>
<h2 id="335-pysimplegui-135-pysimplegui27-27-may-2019">3.35 PySimpleGUI &amp; 1.35 PySimpleGUI27 27-May-2019</h2>
<ul>
<li>Bug fix - when setting default for Checkbox it was also disabling the element!</li>
</ul>
<h2 id="336-pysimplegui-136-pysimplegui27-29-may-2019">3.36 PySimpleGUI &amp; 1.36 PySimpleGUI27 29-May-2019</h2>
<p>A combination of user requests, and needs of new <code>imwatchingyou</code> debugger</p>
<ul>
<li>New Debugger Icon for future built-in debugger</li>
<li>Fixed bug in FindBoundReturnKey - needed to also check Panes</li>
<li>NEW Window functions to turn on/off the Grab Anywhere feature<ul>
<li><code>Window.GrabAnyWhereOn()</code></li>
<li><code>Window.GrabAnyWhereOff()</code></li>
</ul>
</li>
<li>New "Debugger" button that's built-in like other buttons.  It's a TINY button with a logo. For future use when a debugger is built into PySimpleGUI itself (SOON!)</li>
<li>Change Text Element Wrap Length calculation.  Went fromn +40 pixels to +10 pixels in formula</li>
<li>PopupGetFile has new parameter - <code>multiple_files</code>. If True then allows selection of multiple files</li>
</ul>
<h2 id="337-pysimplegui-137-pysimplegui27-1-june-2019">3.37 PySimpleGUI &amp; 1.37 PySimpleGUI27 1-June-2019</h2>
<ul>
<li>The built-in debugger is HERE - might not WORK exactly yet, but a lot of code went into te PySimpleGUI.py file for this.  At the moment, the <code>imwatchingyou</code> package is THE way to use a PySimpleGUI debugger. But soon enough you won't need that project in order to debug your program.</li>
<li>Some strange code reformatting snuck in.  There are 351 differences between this and previous release.  I'm not sure what happened but am looking at every change by hand.</li>
<li>New Calendar Button features<ul>
<li>locale, format - new parameters to TKCalendar call</li>
<li>Use custom icon for window if one has been set</li>
<li>New parameters to CalendarButton - <code>locale</code>, <code>format</code></li>
</ul>
</li>
<li>The bulk of the built-in PySimpleGUI debugger has been added but is not yet "officially supported".  Try pressing "break" or "ctrl+break" on your keyboard.<ul>
<li>New bindings for break / pause button and debugger</li>
<li>New Debug button will launch debugger.</li>
<li>New parameter <code>debugger_enabled</code> added to Window call.  Default is <strong>enabled</strong>.</li>
<li>Your progam's call to Read is all that's needed to refresh debugger</li>
<li>New <code>Window</code> methods to control debugger access<ul>
<li><code>EnableDebugger</code> - turns on HOTKEYS to debugger</li>
<li><code>DisableDebugger</code> - turns off HOTKEYS to debugger</li>
</ul>
</li>
</ul>
</li>
<li>Restored wrap len for Text elements back from +10 to +40 pixels</li>
<li><code>PopupGetFolder</code>, <code>PopupGetFile</code> - fixed so that the "hidden" master window stays hidden (a Linux problem)</li>
<li>Added support for Multiple Files to <code>PopupGetFiles</code> when no_window option has been set.</li>
</ul>
<h2 id="338-pysimplegui-138-pysimplegui27">3.38 PySimpleGUI, 1.38 PySimpleGUI27</h2>
<ul>
<li>Multiline - now has a "read only" state if created as "Disabled"</li>
<li>Multiline - If window is created as resizable, then Multiline Elements will now expand when the window is enlarged, a feature long asked for.</li>
<li>Output Element expands in the Y Direction</li>
<li>"Expandable Rows" option added to PackFormIntoFrame allowing future elements to also expand</li>
<li>Error Element - silence_on_error option</li>
<li>Text Element wrapping - FINALLY got it right?  No more "Fudge factor" added</li>
<li>PopupScrolled - Windows are now resizable</li>
<li>Option to "launch built-in debugger" from the test harness</li>
<li>Rememeber that the Debugger is still in this code!  It may or may not be operational as it's one version back from the latest release of the <code>imwatchingyou</code> debugger code. This code needs to be integrated back in</li>
</ul>
<h2 id="339-pysimplegui-139-pysimplegui27-13-june-2019">3.39 PySimpleGUI &amp; 1.39 PySimpleGUI27 13-June-2019</h2>
<ul>
<li>Ported the imwatchingyou debugger code into PySimpleGUI code<ul>
<li>Replaced old debugger built-in code with the newer imwatchingyou version</li>
<li>Required removing all of the 'sg.' before PySimpleGUI calls since not importing</li>
<li>Dynamically create the debugger object when first call to <code>refresh</code> or <code>show</code> is made</li>
</ul>
</li>
<li>Started the procecss of renaming Class Methods that are private to start with _</li>
<li>Needed for the automatic documentation generation that's being worked on</li>
<li>Fixed crash when clicking the Debug button</li>
<li>Fixed bug in DeleteFigure. Needed to delete image separately</li>
<li>Added more type hints</li>
<li>New <code>TabGroup</code> method <code>SelectTab(index)</code> selects a <code>Tab</code> within a <code>TabGroup</code></li>
<li>New <code>Table.Update</code> parameter - <code>select_rows</code>. List of rows to select (0 is first)</li>
<li>Error checking in <code>Window.Layout</code> provides error "hints" to the user<ul>
<li>Looks for badly placed ']'</li>
<li>Looks for functions missing '()'</li>
<li>Pops up a window warning user instead of crashing</li>
<li>May have to revisit if the popups start getting in the way</li>
</ul>
</li>
<li>New implementations of <code>Window.Disable()</code> and <code>Window.Enable()</code><ul>
<li>Previously did not work correctly at all</li>
<li>Now using the "-disabled" attribute</li>
</ul>
</li>
<li>Allow Comboboxes to have empty starting values<ul>
<li>Was crashing</li>
<li>Enables application to fill these in later</li>
</ul>
</li>
</ul>
<h1 id="400-pysimplegui-200-pysimplegui27-19-june-2019">4.0.0 PySimpleGUI &amp; 2.0.0 PySimpleGUI27   19-June-2019</h1>
<ul>
<li>DOC STRINGS DOCS STRINGS DOC STRINGS!<ul>
<li>Your IDE is about to become very happy</li>
<li>All Elements have actual documentation in the call signature</li>
<li>The Readme and ReadTheDocs will be generated going forward using the CODE</li>
<li>HUGE Thanks for @nngogol for both copying &amp; adding all those strings, but also for making an entire document creation system.</li>
</ul>
</li>
<li>New <strong>version</strong> string for PySimpleGUI.py</li>
<li>New parameter to ALL <code>SetFocus</code> calls.    <ul>
<li>def SetFocus(self, force=False)</li>
<li>If force is True, then a call to <code>focus_force</code> is made instead of <code>focus_set</code></li>
</ul>
</li>
<li>Get - New Radio Button Method.  Returns True is the Radio Button is set</li>
<li>Rename of Debugger class to _Debugger so IDEs don't get confused</li>
<li>User read access to last Button Color set now available via property <code>Button.ButtonColor</code></li>
<li>Rename of a number of callback handlers to start with _</li>
<li>Fix for memory leak in Read call. Every call to read lost a little memory due to root.protocol calls</li>
<li>Listbox.Update - New parameter - scroll_to_index - scroll view so that index is shown at the top</li>
<li>First PyPI release to use new documentation!</li>
</ul>
<h2 id="pysimplegui-41-anniversary-release-4-aug-2019">PySimpleGUI 4.1 Anniversary Release!  4-Aug-2019</h2>
<p>NEVER has there been this long of a lag, sorry to all users!
Long time coming.  Docstrings continue to be a focus.</p>
<ul>
<li>Version can be found using PySimpleGUI.version</li>
<li>New bit of licensing info at the top of the file</li>
<li>Types used in the doc strings. Also type hints in some comments. Because also running on 2.7 can't use full typing</li>
<li>Added using of Warnings. Just getting started using this mechanism. May be great, maybe not. We'll see with this change</li>
<li>Added TOOLTIP_BACKGROUND_COLOR which can be changed (it's tkinter only setting however so undertand this!)</li>
<li>Graph.DrawText.  Ability to set <code>text_location</code> when drawing text onto a Graph Element.  Determines what part of the text will be located at the point you provide when you draw the text.   Choices are:<ul>
<li>TEXT_LOCATION_TOP</li>
<li>TEXT_LOCATION_BOTTOM</li>
<li>TEXT_LOCATION_LEFT</li>
<li>TEXT_LOCATION_RIGHT</li>
<li>TEXT_LOCATION_TOP_LEFT</li>
<li>TEXT_LOCATION_TOP_RIGHT</li>
<li>TEXT_LOCATION_BOTTOM_LEFT</li>
<li>TEXT_LOCATION_BOTTOM_RIGT</li>
<li>TEXT_LOCATION_CENTER</li>
</ul>
</li>
<li>Flag ENABLE_TK_WINDOWS = False.  If True, all windows will be made using only tk.Tk()</li>
<li>SetFocus available for all elements now due to it being added to base class. May NOT work on all elements however</li>
<li>Added Combo.GetSElectedItemsIndexes() - returns a list of all currently selected items</li>
<li>Fixed Listbox.Update - set_to_index changed to be an int, list or tuple</li>
<li>Added parent parameter to call to tkinter's askopenfilename, directory, filenames.  Not sure why the root wasn't passed in before</li>
<li>Button.Update - also sets the activebackground to the button's background color</li>
<li>Graph - New parameter when creating. <code>float_values</code>.  If True, then you're indicating that your coordinate system is float not int based</li>
<li>Graph.Update - made background color optional parm so that visible only can be set</li>
<li>Frame.Layout returns self now for chaining</li>
<li>TabGroup.Layout returns self now for chaining</li>
<li>Column.Layout returns self now for chaining</li>
<li>Menu.Update menu_definition is now optional to allow for changing visibility only</li>
<li>Added inivisiblity support for menu bars</li>
<li>Table.Update supports setting alternating row color and row_colors (list of rows and the color to set)</li>
<li>Set window.TimeoutKey to TIMEOUT_KEY initially</li>
<li>Window - check for types for title (should be string) and layout (should be list) and warns user if not correct</li>
<li>Window - renamed some methods by adding _ in front (like Show) as they are NOT user callable</li>
<li>Another shortcut! Elem = Element = FindElement</li>
<li>SaveToDisk - will not write buttons to file.  Fixed problems due to buttons having keys</li>
<li>Remapped Windowl.CloseNonBlockingForm, Window.CloseNonBlocking to be Window.CloseNonBlocking</li>
<li>Fix for returning values from a combo list. Wasn't handling current value not in list of provided values</li>
<li>Spin - Returns an actual value from list provided when Spin was created or updated</li>
<li>Chaneged FillFormWithValues to use the new internal AllKeysDict dictionary</li>
<li>Added try when creating combo. Problem happens when window is created twice.  Prior window had already created the style</li>
<li>Added list of table (tree) ids to the Table element</li>
<li>Enabled autoclose to use fractions of a second</li>
<li>Added a try around one of the destroys because it could fail if user aborted</li>
<li>Popup - Icon is no longer set to default by default</li>
<li>Fix for debugger trying to execute a REPL comand.  The exec is only avilable in Python 3</li>
<li>main() will display the version number in big letters when program is running</li>
</ul>
<h3 id="42-pysimplegui-22-for-pysimplegui27-18-aug-2019">4.2 PySimpleGUI  2.2 for PySimpleGUI27  18 - Aug 2019</h3>
<p>The cool lookup release!  No more need for FindElement. You can continue to use FindElement.
However, your code will look weird and ancient.  ;-)  (i.e. readable)
MORE Docstring and main doc updates!</p>
<ul>
<li>Finally 2.7 gets an upgrade and with it doc strings.  It however doesn't get a full-version bump like main PySimpleGUI as this may be its last release.</li>
<li>New <code>window[key] == window.FindElement(key)</code></li>
<li>New Update calling method. Can directly call an Element and it will call its Update method<ul>
<li><code>window[key](value=new_value)    ==     window.FindElement(key).Update(value=new_value)</code></li>
</ul>
</li>
<li>Made Tearoff part of element so anything can be a menu in theory</li>
<li>Removed a bunch of <code>__del__</code> calls. Hoping it doesn't bite me in memory leaks</li>
<li>Combo.Get method added</li>
<li>Combo.GetSelectedItemsIndexes removed</li>
<li>New Graph methods SendFigureToBack, BringFigureToFront</li>
<li>Butten release changed for better Graph Dragging<ul>
<li>Now returns key+"Up" for the event</li>
<li>Also returns the x,y coords in the values</li>
</ul>
</li>
<li>Tab.Select method added</li>
<li>TabGroup.Get method added - returns key of currently selected Tab</li>
<li>Window finalize parameter added - Will call finalize if a layout is also included.  No more need for Finalize!!</li>
<li>Quiet, steady change to PEP8 user interface started<ul>
<li>Now available are Window methods - read, layout, finalize, find_element, element, close</li>
<li>Should provide 100% PEP with these alone for most PySimpleGUI programs</li>
</ul>
</li>
<li>Added finding focus across ALL elements by using the .Widget member variable</li>
<li>Fixed sizing Columns!  NOW they will finally be the size specified</li>
<li>Fixed not using the initialdir paramter in PopupGetFile if the no_window option is set</li>
</ul>
<h2 id="43-pysimplegui-release-22-aug-2019">4.3 PySimpleGUI Release 22-Aug-2019</h2>
<p>PEP8 PEP8 PEP8
Layout controls!  Can finally center stuff
Some rather impactful changes this time
Let's hope it doesn't all blow up in our faces!</p>
<ul>
<li>PEP8 interfaces added for Class methods &amp; functions<ul>
<li>Finally a PEP8 compliant interface for PySimpleGUI!!</li>
<li>The "old CamelCase" are still in place and will be for quite some time</li>
<li>Can mix and match at will if you want, but suggest picking one and sticking with it</li>
<li>All docs and demo programs will need to be changed</li>
</ul>
</li>
<li>Internally saving parent row frame for layout checks</li>
<li>Warnings on all Update calls - checks if Window.Read or Window.Finalize has been called</li>
<li>Warning if a layout is attempted to be used twice<ul>
<li>Shows an "Error Popup" to get the user's attention for sure</li>
</ul>
</li>
<li>Removed all element-specific SetFocus methods and made it available to ALL elements</li>
<li>Listbox - no_scrollbar parameter added. If True then no scrollbar will be shown</li>
<li>NEW finalize bool parameter added to Window. Removes need to "chain" .Finalize() call.</li>
<li>NEW element_justification parameter for Column, Frame, Tab Elements and Window<ul>
<li>Valid values are 'left', 'right', 'center'. Only first letter checked so can use 'l', 'c','r'</li>
<li>Default = 'left'</li>
<li>Result is that all Elements INSIDE of this container will be justified as specified</li>
<li>Works well with new Sizer Elements</li>
</ul>
</li>
<li>NEW justification parameter for Column elements.  <ul>
<li>Justifies Column AND the row it's on to this setting (left, right, center)</li>
<li>Enables individual rows to be justified in addition to the entire window</li>
</ul>
</li>
<li>NEW Sizer Element<ul>
<li>Has width and height parameters.  Can set one or both</li>
<li>Causes the element it is contained within to expand according to width and height of Sizer Element</li>
<li>Helps greatly with centering.  Frames will shrink to fit the contents for example. Use Sizer to pad out to right size</li>
</ul>
</li>
<li>Added Window.visibility_changed to match the PySimpleGUIQt call</li>
<li>Fixed Debugger so that popout window shows any newly added locals</li>
</ul>
<h2 id="44-pysimplegui-release-5-sep-2019">4.4 PySimpleGUI Release 5-Sep-2019</h2>
<ul>
<li>window() - "Calling" your Window object will perform a Read call</li>
<li>InputText - move cursor to end following Update</li>
<li>Shortcuts - trying to get a manageable and stable set of Normal, Short, Super-short<ul>
<li>DD - DropDown (Combo)</li>
<li>LB, LBox - Listbox</li>
<li>R, Rad - Radio</li>
<li>ML, MLine - Multiline</li>
<li>BMenu - ButtonMenu</li>
<li>PBar, Prog - ProgressBar</li>
<li>Col - Column</li>
</ul>
</li>
<li>Listbox - new method GetIndexes returns currently selected items as a list of indexes</li>
<li>Output - new method Get returns the contents of the output element</li>
<li>Button - For Macs don't don't allow setting button color. Previously only warned</li>
<li>ButtonMenu - new Click method will click the button just like a normal Button's Click method</li>
<li>Column scrolling finally works correctly with mousewheel. Shift+Mouse Scroll will scroll horizontally</li>
<li>Table - Get method is a dummy version a Get because Qt port got a real Get method</li>
<li>Table - Will add numerical column headers if Column Headsing is set to None when creating Table Element</li>
<li>Table - FIXED the columns crazily resizing themselves bug!!</li>
<li>Table - Can resize individual columns now</li>
<li>Tree - was not returning Keys but instead the string representation of the key</li>
<li>SetIcon will set to default base64 icon if there's an error loading icon</li>
<li>Fix for duplicate key error. Was attempting to add a "unique key counter" onto end of keys if duplicate, but needed to turn into string first</li>
<li>Columns<ul>
<li>No longer expand nor fill</li>
<li>Sizing works for both scrolled and normal</li>
</ul>
</li>
<li>Setting focus - fixed bug when have tabs, columns, frames that have elements that can get the focus. Setting focus on top-level window</li>
<li>InputText elements will now cause rows to expand due to X direction expansion</li>
<li>Frame - Trying to set the size but doesn't seem to be setting it correctly</li>
<li>Tabs will now expand &amp; fill now (I hope this is OK!!!)</li>
</ul>
<h2 id="45-pysimplegui-release-04-nov-2019">4.5 PySimpleGUI Release 04-Nov-2019</h2>
<ul>
<li>Metadata!<ul>
<li>All elements have a NEW metadata parameter that you can set to anything and access with Element.metadata</li>
<li>Windows can have metadata too</li>
</ul>
</li>
<li>Window.finalize() - changed internally to do a fully window.read with timeout=1 so that it will complete all initializations correctly</li>
<li>Removed typing import</li>
<li>ButtonReboundCallback - Used with tkinter's Widget.bind method. Use this as a "target" for your bind and you'll get the event back via window.read()</li>
<li>NEW Element methods that will work on a variety of elements:<ul>
<li>set_size - sets width, height. Can set one or both</li>
<li>get_size - returns width, heigh of Element (underlying Widget), usually in PIXELS</li>
<li>hide_row - hides the entire row that an element occupies</li>
<li>unhide_row - makes visible the entire row that an element occupies</li>
<li>expand - causes element to expand to fill available space in X or Y or both directions</li>
</ul>
</li>
<li>InputText Element - Update got new parameters: text_color=None, background_color=None, move_cursor_to='end'</li>
<li>RadioButton - fix in Update. Was causing problems with loading a window from disk</li>
<li>Text Element - new border width parameter that is used when there's a relief set for the text element</li>
<li>Output Element - special expand method like the one for all other elements</li>
<li>Frame element - Can change the text for the frame using Update method</li>
<li>Slider element - can change range. Previously had to change value to change the range</li>
<li>Scrollable frame / column - change to how mousewheel scrolls.  Was causing all things to scroll when scrolling a single column<ul>
<li>NOTE - may have a bad side effect for scrolling tables with a mouse wheel</li>
</ul>
</li>
<li>Fix for icon setting when creating window.  Wasn't defaulting to correct icon</li>
<li>Window.get_screen_size() returns the screen width and height.  Does not have to be a window that's created already as this is a class method</li>
<li>Window.GetScreenDimensions - will return size even if the window has been destroyed by using get_screen_size</li>
<li>Now deleting window read timers every time done with them</li>
<li>Combo no longer defaults to first entry</li>
<li>New Material1 and Material2 look and feel color schemes</li>
<li>change_look_and_feel has new "force" parameter.  Set to True to force colors when using a Mac</li>
<li>Fix in popup_get_files when 0 length of filename</li>
<li>Fix in Window.SetIcon - properly sets icon using file with Linux now. Was always defaulting</li>
</ul>
<h2 id="46-pysimplegui-16-nov-2019">4.6 PySimpleGUI 16-Nov-2019</h2>
<ul>
<li>Themes!!!</li>
<li>Added a LOT of Look and Feel themes. Total &lt; 100 now</li>
<li>Doctring comments for some missing functions</li>
<li>PEP8 bindings for button_rebound_collback, set_tooltip, set_focus</li>
<li>Spin Element Update - shortened code</li>
<li>Allow tk.PhotoImage objeft to be passed into Image.update as the data</li>
<li>DrawRectangle - added line_width parameter. Defaults to 1</li>
<li>Fix for Slider - was only setting the trough color if the background color was being set_focus</li>
<li>Added a deiconify call to Window.Normal so it can be used to restore a window that has been minimized.  Not working on Linux</li>
<li>Combo - Fix for not allowing a "0" to be specified as the default</li>
<li>Table - Saving the Frame that contains a table in the member variable table_frame.  This will enable the frame to be changed to expandable in the future so that the table can be resized as a window expands.</li>
<li>LOTS AND LOTS of Look and Feel themes!!!!</li>
<li>Added SystemDefaultForReal to look and feel that will prodce 100% not styled windows</li>
<li>Changed the "gray" strings in look and feel table into RGB strtings (e.g. gray25 = #404040). No all graphics subsystems</li>
<li>Removed Mac restriction from Look and Feel setting changes.  All color settings are changed EXCEPT for the button color now on a Mac</li>
<li>"Fuzzy Logic" Look and Feel Theme Selection - No longer have to memorize every character and get the case right. Now can get "close enough" and it'll working</li>
<li>New function - preview_all_look_and_feel_themes.  Causes a window to be shown that shows all of the currently available look and feel themes</li>
<li>Removed use of CloseButton in popup get file, folder, text.  Was causing problems where input fields stopped working.  See bug on GitHub</li>
</ul>
<h2 id="470-pysimplegui-26-nov-2019">4.7.0 PySimpleGUI 26-Nov-2019</h2>
<p>TTK WIDGETS!  Welcome back Mac Users!</p>
<ul>
<li>Significant progress on using ttk widgets properly</li>
<li>Added ttk buttons - MACS can use colored buttons again!!  (Big damned deal)</li>
<li>The existing ttk based Elements are now correctly being colored and styled</li>
<li>Ability to set the ttk theme for individual windows or system-wide, but no longer on a single Element basis</li>
<li>Ability to use ttk buttons on a selective basis for non-Mac systems</li>
<li>port variable == 'PySimpleGUI' so that your code can determine which PySimpleGUI is running</li>
<li>InputText new parameter - use_readonly_for_dsiable defaults to True enables user to switch between a true disable and readonly setting when disabling</li>
<li>Rework of progress bar's ttk style name</li>
<li>Button - new parameter use_ttk_buttons - True = force use, False = force not used, None = let PySimpleGUI determine use</li>
<li>Macs are forced to use ttk buttons EXCEPT when an image is added to the button</li>
<li>TabGroup - can no longer set ttk theme directly</li>
<li>Window new parameters<ul>
<li>ttk_theme - sets the theme for the entire window</li>
<li>use_ttk_buttons - sets ttk button use policy for the entire window</li>
</ul>
</li>
<li>More Window layout error checking - checks that rows are iterables (a list). If not, an error popup is shown to help user find error</li>
<li>Fixed progessbars not getting a key auto assigned to theme</li>
<li>New Window method - send_to_back (SendToBack) - sends the window to the bottom of stack of all windows</li>
<li>Fixed normal tk button text - was left justifying instead of centering</li>
<li>Fixed table colors - wasn't setting correctly due to bad ttk styling</li>
<li>Fixed tree ccolors - wasn't setting correctly due to bad ttk styling</li>
<li>TabGroups now function correction with colors including currently selected tab color and background color of non-tab area (next to the tabs)</li>
<li>New set_options parameters<ul>
<li>use_ttk_buttons - sets system-wide policy for using ttk buttons. Needed for things like popups to work with ttk buttons</li>
<li>ttk_theme - sets system-wide tth theme</li>
<li>progress_meter_style parameter no longer used and generates a warning</li>
</ul>
</li>
<li>list_of_look_and_feel_values now sorts the list prior to returning</li>
<li>Removed Mac restriction on Button colors from look and feel calls. Now can set button colors to anything!</li>
<li>popup_scrolled new parameters - all popups need more parameters but these are for sure needed for the scrolled popup<ul>
<li>background_color</li>
<li>text_color</li>
<li>no_titlebar</li>
<li>grab_anywhere</li>
<li>keep_on_top</li>
<li>font</li>
</ul>
</li>
<li>Test harness changes to help test new ttk stuff (want to shrink this window in the future so will fit on Trinket, Pi, etc </li>
</ul>
<h2 id="480-pysimplegui-4-dec-2019">4.8.0 PySimpleGUI 4-Dec-2019</h2>
<p>Multicolored multiline text!  Often asked for feature going way back
ttk Buttons can have images
Print in color!</p>
<ul>
<li>Multiline Element got 2 new parameters to the update method<ul>
<li>text_color_for_value - color for the newly added text</li>
<li>background_color_for_value - background color of the newly added text</li>
</ul>
</li>
<li>New Print/EasyPrint parameters and capability<ul>
<li>text_color, background_color - control the text's color and background color when printing to "Debug Window"</li>
<li>Must be done only when used in mode where stdout is not re-routed (the default)</li>
<li>Wouldn't it be really nice if normal print calls had this parameter?</li>
<li>Print(event, text_color='green', background_color='white',  end='')</li>
</ul>
</li>
<li>ttk Buttons<ul>
<li>can have images. No longer forces Buttons with images to be the old tk Butons. Now you can choose either  </li>
<li>can update the button color</li>
<li>can update the button image</li>
</ul>
</li>
<li>Set warning filter so that warnings are repeated</li>
<li>New global variables:<ul>
<li>CURRENT_LOOK_AND_FEEL - The current look and feel setting in use. Starts out as "Default"</li>
<li>BROWSE_FILES_DELIMITER - Defaults to ";"  It is the string placed between entries returned from a FilesBrowse button</li>
<li>TRANSPARENT_BUTTON - Depricated - was being used incorrectly as it was a relic from the early days. It's value was a color of gray</li>
</ul>
</li>
<li>Window - gentle reminder if you don't choose a look and feel for your window. It's easy to stop them. Add a change_look_and_feel line</li>
<li>Test harness uses a debug window so don't be shocked when 2 windows appear when running PySimpleGUI by itself<ul>
<li>Prints the "Event" in Green on White text</li>
<li>Prints the "values" normally</li>
</ul>
</li>
</ul>
<h2 id="490-pysimplegui-7-dec-2019">4.9.0 PySimpleGUI 7-Dec-2019</h2>
<p>The "Finally Nailed Tabs" release</p>
<ul>
<li>Colors for Tabs!<ul>
<li>When creating TabGroup can now specify</li>
<li>Text &amp; Background color of all tabs</li>
<li>Text &amp; Background color of selected tab</li>
<li>If nothing is specified then the Look and Feel theme will be used (which turned out GREAT)</li>
</ul>
</li>
<li>Tab visibility - Can finally control individual tab's visibility using update and when creating</li>
<li>More "Look and Feel" Themes!  There's no excuse to be grey again. There are now 126 themes to choose from.  Here are the 32 new themes"
    DefaultNoMoreNagging
    DarkBlack1
    DarkBlue12
    DarkBlue13
    DarkBlue14
    DarkBlue15
    DarkBlue16
    DarkBlue17
    DarkBrown5
    DarkBrown6
    DarkGreen2
    DarkGreen3
    DarkGreen4
    DarkGreen5
    DarkGreen6
    DarkGrey4
    DarkGrey5
    DarkGrey6
    DarkGrey7
    DarkPurple6
    DarkRed2
    DarkTeal10
    DarkTeal11
    DarkTeal12
    DarkTeal9
    LightBlue6
    LightBlue7
    LightBrown12
    LightBrown13
    LightGray1
    LightGreen10
    LightGreen9
    LightGrey6</li>
<li>preview_all_look_and_feel_themes now has a columns parameter to control number of entries per rows<ul>
<li>also made each theme display smaller due to large number of themes</li>
</ul>
</li>
</ul>
<h2 id="4100-pysimplegui-9-dec-2019">4.10.0 PySimpleGUI 9-Dec-2019</h2>
<p>"Oh crap the debugger is broken!" + "Pretty Progress Bars" release</p>
<ul>
<li>Fix for built-in debugger not working<ul>
<li>Important due to upcoming educational usage</li>
<li>Has been broken since 4.5.0 when a change to Finalize was made</li>
</ul>
</li>
<li>ProgessBar element colors set using Look and Feel colors<ul>
<li>Combination of button color, input element, and input element text are used</li>
</ul>
</li>
</ul>
<h2 id="4110-pysimplegui-10-dec-2019">4.11.0 PySimpleGUI 10-Dec-2019</h2>
<p>The Element &amp; Window bindings release</p>
<ul>
<li>Element.bind - New method of all Elements<ul>
<li>Enables tkinter bindings to be added to any element</li>
<li>Will get an event returned from window.read() if the tkinter event happens</li>
</ul>
</li>
<li>Window.bind - New method for Windows, just like Elements<ul>
<li>Enables tkinter bindings to be added to Windows</li>
<li>Will get an event returned from window.read() if the tkinter event happens</li>
</ul>
</li>
<li>TabGroup fonts - can now set the font and font size for Tab text</li>
</ul>
<h2 id="4120-pysimplegui-14-dec-2019">4.12.0 PySimpleGUI 14-Dec-2019</h2>
<p>Finally no more outlines around TK Elements on Linux</p>
<ul>
<li>Fixed a long-term problem of the mysterious white border around (almost) all TK Elements on Linux</li>
<li>Ability to set the disabled button colors<ul>
<li>New Button and Button.update parameter - disabled_button_color</li>
<li>Specified as (Text Color, Background Color) just like button colors</li>
<li>For Normal / TK Buttons - can set button text color only</li>
<li>For TTK Buttons - can set both a disabled button and text color</li>
<li>Either parameter can be None to use current setting</li>
</ul>
</li>
<li>Removed use of CloseButton from Popups (still have a bug in the CloseButton code but not in popups now)</li>
<li>Combobox - removed requirement of setting disabled if want to set to readonly using update method</li>
<li>Fix for cancelling out of file/folder browse on Linux caused target to be cleared instead of just cancelling</li>
<li>Removed try block around setting button colors - if user sets a bad color, well don't do that</li>
<li>Now deleting windows after closing them for popup</li>
</ul>
<h2 id="4130-pysimplegui-18-dec-2019">4.13.0 PySimpleGUI 18-Dec-2019</h2>
<p>Table and Tree header colors, expanded Graph methods</p>
<ul>
<li>Element.expand new parameter - expand_row. If true then row will expand along with the widgets. Provides better resizing control</li>
<li>Using math.floor now instead of an int cast in Graph Element's unit conversions</li>
<li>Graph.draw_point - now using caller's graph units for specifying point size</li>
<li>Graph.draw_circle - converted radius size from user's graph units.</li>
<li>Graph.draw_circle - added line_width parameter</li>
<li>Graph.draw_oval - added line_width parameter</li>
<li>Graph.get_figures_at_location - new method for getting a list of figures at a particular point</li>
<li>Graph.get_bounding_box - returns bounding box for a previously drawn figure</li>
<li>Table and Tree Elements<ul>
<li>3 new element creation parameters<ul>
<li>header_text_color - color of the text for the column headings</li>
<li>header_background_color - color of the background of column headings</li>
<li>header_font - font family, style , size for the column headings</li>
</ul>
</li>
<li>Defaults to using the current look and feel setting<ul>
<li>Uses similar algorithm as Tabs - Input Text background and text colors are used</li>
</ul>
</li>
</ul>
</li>
<li>Spin element - fixed bug that showed "None" if default value is "None"</li>
<li>Test Harness sets incorrect look and feel on purpose so a random one is chosen</li>
</ul>
<h2 id="4140-pysimplegui-23-dec-2019">4.14.0 PySimpleGUI 23-Dec-2019</h2>
<p>THEMES!</p>
<ul>
<li>theme is replacing change_look_and_feel. The old calls will still be usable however</li>
<li>LOTS of new theme functions.  Search for "theme_" to find them in this documentation.  There's a section discussing themes too</li>
<li>"Dark Blue 3" is the default theme now.  All windows will be colored using this theme unless the user sets another one</li>
<li>Removed the code that forced Macs to use gray</li>
<li>New element.set_cursor - can now set a cursor for any of the elements.  Pass in a cursor string and cursor will appear when mouse over widget</li>
<li>Combo - enable setting to any value, not just those in the list</li>
<li>Combo - changed how initial value is set</li>
<li>Can change the font on tabs by setting font parameter in TabGroup</li>
<li>Table heading font now defaults correctly</li>
<li>Tree heading font now defaults correctly</li>
<li>Renamed DebugWin to _DebugWin to discourage use</li>
</ul>
<h2 id="4150-pysimplegui-08-jan-2020">4.15.0 PySimpleGUI 08-Jan-2020</h2>
<p>Dynamic Window Layouts!  Extend your layouts with <code>Window.extend_layout</code>
Lots of fixes</p>
<ul>
<li>Window.extend_layout</li>
<li>Graph.change_coordinates - realtime change of coordinate systems for the Graph element</li>
<li>theme_text_element_background_color - new function to expose this setting</li>
<li>Radio &amp; Checkbox colors changed to be ligher/darker than background</li>
<li>Progress bar - allow updates of value &gt; max value</li>
<li>Output element does deletes now so that cleanup works. Can use in multiple windows as a result</li>
<li>DrawArc (draw_arc) - New width / line width parameter</li>
<li>RGB does more error checking, converts types</li>
<li>More descriptive errors for find element  </li>
<li>popup_error used interally now sets keep on top</li>
<li>Element Re-use wording changed so that it's clear the element is the problem not the layout when re-use detected</li>
<li>Window.Close (Window.close) - fix for not immediately seeing the window disappear on Linux when clicking "X"</li>
<li>Window.BringToFront (bring_to_front) - on Windows needed to use topmost to bring window to front insteade of lift</li>
<li>Multiline Scrollbar - removed the scrollbar color. It doesn't work on Windows so keeping consistent</li>
<li>Changed how Debug Windows are created.  Uses finalize now instead of the read non-blocking</li>
<li>Fix for Debug Window being closed by X causing main window to also close</li>
<li>Changed all "black" and "white" in the Look and Feel table to #000000 and #FFFFFF</li>
<li>Added new color processing functions for internal use (hsl and hsv related)</li>
<li>popup - extended the automatic wrapping capabilities to messages containing \n</li>
<li>Test harness uses a nicer colors for event, value print outs.</li>
<li>_timeit decorator for timing functions</li>
</ul>
<h2 id="4151-pysimplegui-09-jan-2020">4.15.1 PySimpleGUI 09-Jan-2020</h2>
<p>Quick patch to remove change to popup</p>
<h2 id="4152-pysimplegui-15-jan-2020">4.15.2 PySimpleGUI 15-Jan-2020</h2>
<p>Quick patch to remove f-string for 3.5 compat.</p>
<h2 id="4160-pysimplegui-20-feb-2020">4.16.0 PySimpleGUI 20-Feb-2020</h2>
<p>The "LONG time coming" release.  System Tray, Read with close + loads more changes
Note - there is a known problem with the built-in debugger created when the new read with close was added</p>
<ul>
<li>System Tray - Simulates the System Tray feature currently in PySimpleGUIWx and PySimpleGUIQt. All calls are the same. The icon is located just above the system tray (bottom right corner)</li>
<li>Window.read - NEW close parameter will close the window for you after the read completes. Can make a single line window using this</li>
<li>Window.element_list - Returns a list of all elements in the window</li>
<li>Element.unbind - can remove a previously created binding</li>
<li>Element.set_size - retries using "length" if "height" setting fails</li>
<li>Listbox.update - select_mode parameter added</li>
<li>Listbox.update - no longer selects the first entry when all values are changed</li>
<li>Listbox.get - new. use to get the current values.  Will be the same as the read return dictionary</li>
<li>Checkbox.update - added ability to change background and text colors.  Uses the same combuted checkbox background color (may remove)</li>
<li>Multiline.update - fix for when no value is specified</li>
<li>Multiline - Check for None when creating. Ignores None rather than converting to string</li>
<li>Text.update - added changing value to string. Assumed caller was passing in string previously.</li>
<li>Text Element - justification can be specified with a single character. l=left, r=right, c=center. Previously had to fully spell out</li>
<li>Input Element - justification can be specified with a single character. l=left, r=right, c=center. Previously had to fully spell out</li>
<li>StatusBar Element - justification can be specified with a single character. l=left, r=right, c=center. Previously had to fully spell out</li>
<li>Image Element - can specify no image when creating.  Previously gave a warning and required filename = '' to indicate nothing set</li>
<li>Table Element - justification can be specified as an "l" or "r" instead of full word left/right</li>
<li>Tree Element - justification can be specified as an "l" or "r" instead of full word left/right</li>
<li>Graph.draw_point - changed to using 1/2 the size rather than size. Set width = 0 so no outline will be drawn</li>
<li>Graph.draw_polygon - new drawing method!  Can now draw polygons that fill</li>
<li>Layout error checking and reporting added for - Frame, Tab, TabGroup, Column, Window</li>
<li>Menu - Ability to set the font for the menu items</li>
<li>Debug window - fix for problem closing using the "Quit" button</li>
<li>print_to_element - print-like call that can be used to output to a Multiline element as if it is an Output element</li>
</ul>
<h2 id="4170-pysimplegui-24-mar-2020">4.17.0 PySimpleGUI 24-Mar-2020</h2>
<p>The "it's been a minute" release
Improved DocStrings and documentation!
Upgrade utility
"Printing" directly to Multiline</p>
<ul>
<li>New upgrade utility to upgrade your installed package using GitHub version<ul>
<li>Can invoke from command line. Run      <code>python -m PySimpleGUI.PySimpleGUI upgrade</code></li>
<li>The test harness GUI has an upgrade button</li>
</ul>
</li>
<li>Multiline.print - Add multiline element to the front of any print statement.  Also supports color output</li>
<li>Debug informmation like path and version displayed in test harness GUI</li>
<li>Added back the TRANSPARENT_BUTTON variable until can find a better way to deprecate</li>
<li>All elements were losing padding when made invisible. Fixed</li>
<li>Image.update - fixed crash due to not checking for type before getting size</li>
<li>Image.update_animation_no_buffering - playback GIF animations of any length</li>
<li>Graph element - Fixed divide by zero error in convert function</li>
<li>TabGroup will now autonumber keys if none specified</li>
<li>Measuring strings more accurately during layout<ul>
<li>Using specific font for measurement</li>
<li>Used to compute TTK button height</li>
<li>Used to compute Slider length</li>
<li>Used to compute header widths in Tables, Trees</li>
<li>Used to compute column widths in Tables, Trees</li>
<li>Used to compute row heights in Tables</li>
</ul>
</li>
<li>Removed padx from row frames.  Was using window's margins. Now padx &amp; pady = 0. Was causing too every Column element to have extra padding</li>
<li>Added no_titlebar to one line progress meter</li>
<li>popup_notify - Creates a "notification window" that is like the System Tray Message window</li>
<li>shell_with_animation - launch a shell command that runs while an animated GIF is shown</li>
<li>Fixed problem with debugger not working after the recent close parameter addition to Window.read</li>
</ul>
<h2 id="4180-pysimplegui-26-mar-2020">4.18.0 PySimpleGUI 26-Mar-2020</h2>
<p>An "Oh F**k" Release - Table column sizes were bad</p>
<ul>
<li>Fixed bug in Table Element's column size computation</li>
<li>popup_animated has new title parameter</li>
<li>Checkbox - update can change the text</li>
</ul>
<h2 id="4181-pysimplegui-12-apr-2020">4.18.1 PySimpleGUI 12-Apr-2020</h2>
<p>Emergency patch - f-string managed to get into the code resulting crashes on 3.5 systems (Pi's for example) </p>
<h2 id="4182-pysimplegui-12-apr-2020">4.18.2 PySimpleGUI 12-Apr-2020</h2>
<p>The Epic Fail release.... import error on 3.5 for subprocess.</p>
<h2 id="4190-pysimplegui-5-may-2020">4.19.0 PySimpleGUI 5-May-2020</h2>
<p>New Date Chooser
Scrollable columns with mousewheel!! (oh please work right!)
WINDOW_CLOSE &amp; WIN_CLOSE events
Long list of stuff!</p>
<ul>
<li>Imported from typing again to get correct docstrings</li>
<li>Print and MLine.Print fixed sep char handling </li>
<li>New parameter to Muliline.print(autoscroll parameter)</li>
<li>New autoscroll parameter added to _print_to_element</li>
<li>popup_get_date </li>
<li>Complete reworking on Calendar Chooser Button<ul>
<li>Has a LOT more paramteter</li>
<li>Can set location!</li>
</ul>
</li>
<li>icon parm popup_animated </li>
<li>popup button size (6,1) for all popups</li>
<li>NEW CALENDAR chooser integrated </li>
<li>Graph.draw_lines - new method to allow for multiline lines that may not be a full polygon</li>
<li>System Tray fixed the docstrings</li>
<li>color chooser set parent window (needed for icon?)</li>
<li>scrollable column scrollwheel fixed </li>
<li>fixed TabGroup border width (wasn't getting set properly at all)</li>
<li>EXPERIMENTAL Scrollable Columns </li>
<li>Fixed Debug Printing to work like a normal "print"</li>
<li>Fixed _print_to_element to work like a normal "print"</li>
<li>Fixed light green 1 theme definition - Text color wasn't being set</li>
<li>fix for install from GitHub </li>
<li>fix for Column scrolling with comboboxes </li>
<li>Added Text.get </li>
<li>Spin.update fix </li>
<li>import typing again </li>
<li>fixes for Pi </li>
<li>test for valid ttk_theme names </li>
<li>fix for Text.get docstring </li>
<li>added tuples to some docstrings </li>
<li>added code for better tag handling for Multiline elements (fixes a potential memory leak... thanks Ruud)</li>
<li>WIN_CLOSE &amp; WINDOW_CLOSED constants added.  Both are None</li>
<li>EVENT_TIMEOUT and TIMEOUT_EVENT constants added to both be the same as TIMEOUT_KEY</li>
<li>Some changes in test harness that tested recent changes (may still need shortening for trinket or others)</li>
<li>Changed the misleading TRANSPARENT_BUTTON constant with an attempt using themes calls</li>
</ul>
<h3 id="upcoming">Upcoming</h3>
<p>There will always be overlapping work as the ports will never actually be "complete" as there's always something new that can be built.  However there's a definition for the base functionality for PySimpleGUI.  This is what is being strived for with the currnt ports that are underway.</p>
<p>The current road ahead is to complete these ports - Qt (very close), Web (pretty close), Wx (not all that close).</p>
<p>PySimpleGUIDroid is in the works....</p>
<p>In addition to the ports there is ongoing work with educators that want to bring PySimpleGUI into their classrooms.  Some projects have already started with teachers.  One effort is to examine a number of books that teach Python to kids and convert the exercises to use PySimpleGUI instead of tkinter or command line.  Another educational effort is in integrating with Circuit Python.  It's unclear exactly how PySimpleGUI will fit into the picture.  A board from Adafruit is arriving soon which should help solidify what's possible.</p>
<h2 id="code-condition">Code Condition</h2>
<pre><code>Make it run
Make it right
Make it fast
</code></pre>
<p>It's a recipe for success if done right.  PySimpleGUI has completed the "Make it run" phase.  It's far from "right" in many ways.  These are being worked on.  The module has historically been particularly poor for PEP8 compliance.  It was a learning exercise that turned into a somewhat complete GUI solution for lightweight problems.</p>
<p>While the internals to PySimpleGUI are a tad sketchy, the public interfaces into the SDK are more strictly defined and comply with PEP8 naming conventions.  A set of "PEP8 Bindings" was released in summar 2019 to ensure the enternally facing interfaces all adhere to PEP8 names.</p>
<p>Please log bugs and suggestions <strong>only on the PySimpleGUI GitHub</strong>!  It will only make the code stronger and better in the end, a good thing for us all, right?  Logging them elsewhere doesn't enable the core developer and other PySimpleGUI users to help.  To make matters worse, you may get bad advice from other sites because there are simply not many PySimpleGUI experts, yet.</p>
<h2 id="design">Design</h2>
<p>A moment about the design-spirit of <code>PySimpleGUI</code>.  From the beginning, this package was meant to take advantage of Python's capabilities with the goal of programming ease.</p>
<p><strong>Single File</strong>
While not the best programming practice, the implementation resulted in a single file solution.  Only one file is needed, PySimpleGUI.py.  You can post this file, email it, and easily import it using one statement.</p>
<p><strong>Functions as objects</strong>
In Python, functions behave just like object. When you're placing a Text Element into your form, you may be sometimes calling a function and other times declaring an object.  If you use the word Text, then you're getting an object.  If you're using <code>Txt</code>, then you're calling a function that returns a <code>Text</code> object.</p>
<p><strong>Lists</strong>
It seemed quite natural to use Python's powerful list constructs when possible.  The form is specified as a series of lists.  Each "row" of the GUI is represented as a list of Elements. </p>
<p><strong>Dictionaries</strong>
Want to view your form's results as a dictionary instead of a list... no problem, just use the <code>key</code> keyword on your elements.  For complex forms with a lot of values that need to be changed frequently, this is by far the best way of consuming the results.</p>
<p>You can also look up elements using their keys.  This is an excellent way to update elements in reaction to another element.  Call <code>form.FindElement(key)</code> to get the Element.</p>
<p><strong>Named / Optional Parameters</strong>
This is a language feature that is featured <strong>heavily</strong>  in all of the API calls, both functions and classes.  Elements are configured, in-place, by setting one or more optional parameters.  For example, a Text element's color is chosen by setting the optional <code>text_color</code> parameter.</p>
<p><strong>tkinter*<em>
tkinter is the "official" GUI that Python supports.  It runs on Windows, Linux, and Mac.  It was chosen as the first target GUI framework due to its </em></strong>ubiquity***.  Nearly all Python installations, with the exception of Ubuntu Linux, come pre-loaded with tkinter.   It is the "simplest" of the GUI frameworks to get up an running (among Qt, WxPython, Kivy, etc).</p>
<p>From the start of the PSG project, tkinter was not meant to be the only underlying GUI framework for PySimpleGUI.  It is merely a starting point.  All journeys begin with one step forward and choosing tkinter was the first of many steps for PySimpleGUI.  Now there are 4 ports up and running - tkinter, WxPython, Qt and Remi (web support)</p>
<h2 id="author-owner">Author &amp; Owner</h2>
<p>The PySimpleGUI Organization</p>
<p>This documentation as well as all PySimpleGUI code is Copyright 2018, 2019, 2020 by PySimpleGUI.org</p>
<p>Send correspondence to <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="b5e5cce6dcd8c5d9d0f2e0fcf5e5cce6dcd8c5d9d0f2e0fc9bd6dad8">[email&#160;protected]</a></p>
<h2 id="license">License</h2>
<p>GNU Lesser General Public License (LGPL 3) +</p>
<h2 id="acknowledgments">Acknowledgments</h2>
<p>There are a number of people that have been key contributors to this project both directly and indirectly.  Paid professional help has been deployed a number of critical times in the project's history.  This happens in the life of software development from time to time.</p>
<p>If you've helped, I sure hope that you feel like you've been properly thanked.  That you have been recognized.  If not, then say something.... drop an email to <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="4c2f2321212922383f0c1c351f25213c20290b190562233e2b62">[email&#160;protected]</a> </p>
<h2 id="support_1">Support</h2>
<p>In response to a number of email contacts from individuals and corporations that are using PySimpleGUI that wanted to financially support the project a "Support" Button was added to the GitHub site.  This support button is connected with a PayPal account.  If you wish to help support this currently freely supplied software and free technical support, then follow this link: www.paypal.me/psgui . </p>
<p>To be clear, this is not a solicitation for your money.  No one is being directly asked to support / contribute.  The project is self-funded and there are ongoing costs just to offer the software (URLs, ReadTheDocs, etc). If you're a corporate user and find that PySimpleGUI is helping you financially, that's awesome.  If you want to help ensure PySimpleGUI has a future, you now have that option to help.  It's likely that at some point the costs will become too high for the project to continue, but until then we'll all enjoy the successes we're having.</p></div>
        </div>

        <footer class="col-md-12">
            <hr>
            <p>Documentation built with <a href="http://www.mkdocs.org/">MkDocs</a>.</p>
        </footer>
        <script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script>var base_url = '.';</script>
        <script src="./js/base.js"></script>
        <script src="./readthedocs-data.js"></script>
        <script src="https://assets.readthedocs.org/static/core/js/readthedocs-doc-embed.js"></script>
        <script src="https://assets.readthedocs.org/static/javascript/readthedocs-analytics.js"></script>
        <script src="./search/require.js"></script>
        <script src="./search/search.js"></script>

        <div class="modal" id="mkdocs_search_modal" tabindex="-1" role="dialog" aria-labelledby="Search Modal" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
                <h4 class="modal-title" id="exampleModalLabel">Search</h4>
            </div>
            <div class="modal-body">
                <p>
                    From here you can search these documents. Enter
                    your search terms below.
                </p>
                <form role="form">
                    <div class="form-group">
                        <input type="text" class="form-control" placeholder="Search..." id="mkdocs-search-query">
                    </div>
                </form>
                <div id="mkdocs-search-results"></div>
            </div>
            <div class="modal-footer">
            </div>
        </div>
    </div>
</div><div class="modal" id="mkdocs_keyboard_modal" tabindex="-1" role="dialog" aria-labelledby="Keyboard Shortcuts Modal" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
                <h4 class="modal-title" id="exampleModalLabel">Keyboard Shortcuts</h4>
            </div>
            <div class="modal-body">
              <table class="table">
                <thead>
                  <tr>
                    <th style="width: 20%;">Keys</th>
                    <th>Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><kbd>?</kbd></td>
                    <td>Open this help</td>
                  </tr>
                  <tr>
                    <td><kbd>&larr;</kbd></td>
                    <td>Previous page</td>
                  </tr>
                  <tr>
                    <td><kbd>&rarr;</kbd></td>
                    <td>Next page</td>
                  </tr>
                  <tr>
                    <td><kbd>s</kbd></td>
                    <td>Search</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="modal-footer">
            </div>
        </div>
    </div>
</div>


    </body>
</html>

<!--
MkDocs version : 0.17.3
Build Date UTC : 2020-05-20 00:06:06
-->
