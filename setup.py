from setuptools import setup,find_packages

with open("README.md", "r") as fh:
    long_descriptions = fh.read()

s = setup(
    name="rx7",
    version="2.6.0",
    license="MIT",
    description="Shortcut for most usefull functions, High API, Special Features",
    url="http://rx7.ir",
    packages=find_packages(),
    install_requires=['colored','psutil','requests','pyautogui','keyboard',
                      'mouse','pyscreeze','whois'], #'win10toast'
    python_requires = ">= 3.4",
    author="Ramin RX7",
    author_email="rawmin.rx@gmail.com",

    classifiers=['Programming Language :: Python :: 3',
                 #'Development Status :: 5 - Production/Stable',
                 ],
    long_description=long_descriptions,
    long_description_content_type="text/markdown",
    )
