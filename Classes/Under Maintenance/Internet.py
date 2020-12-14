from bs4 import BeautifulSoup
import requests, re, socket, urllib


ReConErr = requests.exceptions.ConnectionError

class internet:
    
    @staticmethod
    def connected(website='http://x.com/'):
        '''
        Check for internet connection with trying to connect to web-site
         ( Maybe you want to know why i used http://x.com/ as default web-site
           The reason is there's no extra code to load
           (compare x.com and google.com html source code)
           And this make it a lot faster for checking.
          )
        '''
        try:
            urllib.request.urlopen(website)
            return True
        except:
            return False

    def connection_checker(func):
        def inside(*args,**kwargs):
            if not internet.connected():
                raise ConnectionError('No internet connection') from None
            return func(*args,**kwargs)
        return inside
    
    @staticmethod
    def ip_global() -> str:
        """
        Return ip with by http://ipinfo.io/ip api.
        returns global ip as string
        """
        new_session = requests.session()
        response = new_session.get("http://ipinfo.io/ip")
        ip_list = re.findall(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}", response.text)
        new_session.close()
        return ip_list[0]
    
    @staticmethod
    def ip_local() -> str:
        """
        Return local ip of computer in windows by socket module 
        and in linux with hostname command in shell.
        """
        #return [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
        '''
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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
            ip = socket.gethostbyname(socket.gethostname())
            if ip and ip != "127.0.1.1":
                return ip
            elif platform.system() != "Windows":
                command = subprocess.Popen(["hostname", "-I"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE,shell=False)
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
        check if url exists
        (NEED HTTP[S])
        '''
        try:
            request = requests.get(URL)
        except ReConErr:
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
            return socket.gethostbyname(URL)
        except socket.gaierror:
            if internet.connected():
                class NotExistsError(Exception):
                    def __init__(self):
                        return super().__init__('URL Does Not Exists')
                raise NotExistsError from None
            else:
                raise ConnectionError from None
    
    @staticmethod
    def url_links(URL) -> list:
        '''
        Get all links that are used in a specifiec url
        (All "a" tags from html source)
        ''' #html.parser
        try:
            soup= BeautifulSoup(requests.get(URL).text,features="lxml")
            LINKS= []
            for link in soup.find_all('a'):
                LINKS.append(link.get('href'))
            return LINKS
        except ReConErr:
            raise ConnectionError('No internet connection') from None
    
    @staticmethod
    def find_urls(string) -> list:
        '''
        find all urls in a string and returns list of them
         (urls should start with http[s])
        '''
        url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string) 
        return url
    
    @staticmethod
    def is_url(URL) -> bool:
        '''
        check if a string is url (WITH HTTP[S])
        '''
        search= re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', URL)
        if search and len(search.group())==len(URL):
            return True
        else:
            return False
    
    @staticmethod
    def whois(URL):
        '''
         return whois lookup of a website
         (WITHOUT HTTPS)
        '''
        try:
            import whois
            WHOIS = whois.whois(URL)
            return {i:WHOIS[i] for i in WHOIS}
        except socket.gaierror:
            raise ConnectionError('No internet connection') from None
    


