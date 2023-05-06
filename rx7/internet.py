"""
Useful functions when working with network/internet
"""

import re as _re
import urllib.request as _urllib_request
import socket as _socket
import subprocess as _subprocess

from . import system



ip_global = system.ip_global
ip_local  = system.ip_local


def is_connected(url:str='https://www.google.com/'):
    '''Check for internet connection with trying to connect to url'''
    try:
        _urllib_request.urlopen(url)
        return True
    except:
        return False


def connection_checker(func):
    """Decaorator Which Checks Internet Connection before calling a function"""
    def inside(*args,**kwargs):
        if not is_connected():
            raise ConnectionError('No internet connection') from None
        return func(*args,**kwargs)
    return inside


def url_exists(url) -> bool:
    '''
    check if url exists (with 'requests' module)
    (Needs HTTP[S] prefix)
    '''
    import requests as _requests
    ReqConErr = _requests.exceptions.ConnectionError
    try:
        request = _requests.get(url)
    except ReqConErr:
        raise ConnectionError('No internet connection') from None
    #print(response.status_code < 400)
    if request.status_code == 200:
        return True
    else:
        return False


@connection_checker
def ip_website(URL) -> str:
    '''
    get IP address of Web Site
    (Without http[s] prefix)
    '''
    class NotExistsError(Exception):
        pass
    try:
        return _socket.gethostbyname(URL)
    except _socket.gaierror:
        raise NotExistsError from None


def url_links(URL) -> list:
    '''
    Get all links that are used in a specifiec url
    (All "a" tags from html source)
    (Needs 'http[s]' prefix)
    ''' #html.parser
    import requests as _requests
    _ReqConErr = _requests.exceptions.ConnectionError
    try:
        from bs4 import BeautifulSoup
        soup= BeautifulSoup(_requests.get(URL).text,features="lxml")
        links= []
        for link in soup.find_all('a'):
            links.append(link.get('href'))
        return links
    except _ReqConErr:
        raise ConnectionError('No internet connection') from None


def find_urls(string) -> list:
    '''
    find all urls in a string and returns list of them
     (urls should start with http[s])
    '''
    return _re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        string
    )


def is_url(url:str) -> bool:
    '''check if a string is url (requires HTTP[S] prefix)'''
    search = _re.search(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        url
    )
    # '(http[s]?://)?([Ww]{3}\.)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    if search and len(search.group()) == len(url):
        return True
    else:
        return False


def open_browser(url, new_tab=True):
    """Opens given url in default browser"""
    import webbrowser
    if new_tab:
        webbrowser.open_new_tab(url)
    else:
        webbrowser.open(url)


"""
def whois(URL):
    '''
     return whois lookup of a website
     (WITHOUT HTTPS)
    '''
    try:
        import whois
        WHO = whois.query(URL)
        WHOIS = WHO.dict
        return {i:WHOIS[i] for i in WHOIS}
    except _socket.gaierror:
        raise ConnectionError('No internet connection') from None
"""
