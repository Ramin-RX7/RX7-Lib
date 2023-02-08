import re as _re
import socket as _socket
import subprocess as _subprocess

import rx7 as rx
import urllib as _urllib



class Internet:
    
    @staticmethod
    def is_connected(website='http://x.com/'):
        '''
        Check for internet connection with trying to connect to web-site
         ( Maybe you want to know why i used http://x.com/ as default web-site
           The reason is there's no extra code to load
           (compare x.com and google.com html source code)
           And this make it a lot faster for checking.
          )
        '''
        try:
            _urllib.request.urlopen(website)
            return True
        except:
            return False

    def connection_checker(func):
        """Decaorator Which Checks Internet Connection before calling a function

        Parameters
        ----------
        func : Function
            function which you are going to check if 
             there is internet connection before call it
        """
        def inside(*args,**kwargs):
            if not internet.is_connected():
                raise ConnectionError('No internet connection') from None
            return func(*args,**kwargs)
        return inside
    
    '''
    @staticmethod
    def ip_global() -> str:
        """
        Return your global ip by http://ipinfo.io/ip api.
        """
        new_session = _requests.session()
        response = new_session.get("http://ipinfo.io/ip")
        ip_list = _re.findall(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}", response.text)
        new_session.close()
        return ip_list[0]
    '''
    ip_global = rx.system.ip_global

    @staticmethod
    def ip_local() -> str:
        """
        Return local ip of computer in windows by _socket. module 
        and in linux with hostname command in shell.
        """
        #return [l for l in ([ip for ip in _socket.gethostbyname_ex(_socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [_socket._socket.(_socket.AF_INET, _socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
        '''
        s = _socket._socket.(_socket.AF_INET, _socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP
        '''
        import platform
        class NetworkError(Exception):
            def __init__(self, message): super().__init__(message)
        try:
            ip = _socket.gethostbyname(_socket.gethostname())
            if ip and ip not in ("127.0.1.1","127.0.0.1"):
                return ip
            elif platform.system() != "Windows":
                command = _subprocess.Popen(["hostname", "-I"],stdout=_subprocess.PIPE,stderr=_subprocess.PIPE,stdin=_subprocess.PIPE,shell=False)
                response = list(command.communicate())
                if len(response[0]) > 0:
                    return str(response[0])[2:-4]
                raise NetworkError('No Network Connection')
            raise NetworkError('No Network Connection')
        except:
            raise
    
    @staticmethod
    def url_exists(URL) -> bool:
        '''
        check if url exists (with 'requests' module)
        (NEED HTTP[S])
        '''
        import requests as _requests
        _ReqConErr = _requests.exceptions.ConnectionError
        try:
            request = _requests.get(URL)
        except _ReqConErr:
            raise ConnectionError('No internet connection') from None
        #print(response.status_code < 400)
        if request.status_code == 200:
            return True
        else:
            return False
    
    @staticmethod
    def ip_website(URL) -> str:
        '''
        get IP address of Web Site\n
        (Without http[s])
        '''
        try:
            return _socket.gethostbyname(URL)
        except _socket.gaierror:
            if internet.is_connected():
                class NotExistsError(Exception):
                    def __init__(self):
                        super().__init__('URL Does Not Exists')
                raise NotExistsError from None
            else:
                raise ConnectionError from None
    
    @staticmethod
    def url_links(URL) -> list:
        '''
        Get all links that are used in a specifiec url
        (All "a" tags from html source)
        (Needs 'http[s]')
        ''' #html.parser
        import requests as _requests
        _ReqConErr = _requests.exceptions.ConnectionError
        try:
            from bs4 import BeautifulSoup
            soup= BeautifulSoup(_requests.get(URL).text,features="lxml")
            LINKS= []
            for link in soup.find_all('a'):
                LINKS.append(link.get('href'))
            return LINKS
        except _ReqConErr:
            raise ConnectionError('No internet connection') from None
    
    @staticmethod
    def find_urls(string) -> list:
        '''
        find all urls in a string and returns list of them
         (urls should start with http[s])
        '''
        url = _re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string) 
        return url

    @staticmethod
    def is_url(URL) -> bool:
        '''
        check if a string is url (WITH HTTP[S])
        '''
        search= _re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', URL)
        '(http[s]?://)?([Ww]{3}\.)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        if search and len(search.group())==len(URL):
            return True
        else:
            return False
    
    @staticmethod
    def open_browser(url,new_tab=True):
        import webbrowser
        if new_tab:
            webbrowser.open_new_tab(url)
        else:
            webbrowser.open(url)

    """
    @staticmethod
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
internet = Internet
