from setuptools import setup,find_packages

with open("README.md", "r") as fh:
    long_descriptions = fh.read()

s = setup(
    name = "rx7",
    version = "3.2.0",
    license = "LGPL",
    description = "Shortcut for most usefull functions, High API, Special Features",
    url = "https://github.com/Ramin-RX7/RX7-Lib",
    packages = find_packages(), # ['rx7']
    install_requires = ['colored','psutil','requests'],
       # 'pyscreeze','keyboard', 'mouse','pyautogui'
       # 'whois','win10toast' #'pywin32'
    python_requires = ">= 3.7",
    author = "Ramin RX7",
    author_email = "rawmin.rx@gmail.com",
    classifiers = ['Programming Language :: Python :: 3',
    ],
    long_description = long_descriptions,
    long_description_content_type = "text/markdown",
    )
