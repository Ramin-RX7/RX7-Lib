'''
This is 'System' module.  No difference between this and 'system' class.  
So I recommend to use rx.system but no difference.
'''

import socket
import os
import psutil

from typing import Union

#from .Internet import internet


def convert_bytes(num:int) -> str :
    """
    Convert num to idiomatic byte unit.
    num is the input number (bytes).
    
    >>> convert_bytes(200)
    '200.0 bytes'
    >>> convert_bytes(6000)
    '5.9 KB'
    >>> convert_bytes(80000)
    '78.1 KB'
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


class system:
    '''
    Some system actions and information.
    - Information about ram, ip, terminal, etc.
    - Some System Actions like Shutdown and Restart
    (ALL FUNCTIONS ARE STATIC METHODS)
    '''
    @staticmethod
    def accname():
        '''
        return account username you have logged in.
        '''
        return os.getlogin()
    @staticmethod
    def pid():
        '''
        Get pid number of terminal and return it.
        '''
        return os.getpid()
    '''@staticmethod
    def disk_usage(path):
        ####
        return shutil.disk_usage(path)'''
    @staticmethod
    def chdir(path):
        '''
        Change directory of terminal.
        '''
        os.chdir(path)
    @staticmethod
    def SHUT_DOWN():
        '''
        Shut down the PC. (WINDOWS)
        '''
        os.system("shutdown /s /t 1")
    @staticmethod
    def RESTART():
        '''
        Restart the PC. (WINDOWS)
        '''
        os.system("shutdown /r /t 1")
    @staticmethod
    def terminal_size() -> tuple:
        '''
        Return terminal size in tuple (columns,rows)
        '''
        size= os.get_terminal_size()
        return (size.columns,size.lines)
    @staticmethod
    def cwd():
        '''
        Return a unicode string representing the current working directory.
        '''
        return os.getcwd()
    @staticmethod
    def ip_global():
        """
        Return ip with by http://ipinfo.io/ip api.
        returns global ip as string
        """
        try:
            import requests
            new_session = requests.session()
            response = new_session.get("http://ipinfo.io/ip")
            import re
            ip_list = re.findall(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}", response.text)
            new_session.close()
            return ip_list[0]
        except:
            class ConnectionError(requests.exceptions.ConnectionError):
                def __init__(self, message): super().__init__(message)
            raise ConnectionError('No Internet Connection')
    """ip_global= internet.ip_global"""
    @staticmethod
    def ip_local():
        """
        Return local ip of computer in windows by socket module
        and in unix with hostname command in shell.
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
                import subprocess
                command = subprocess.Popen(["hostname", "-I"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE,shell=False)
                response = list(command.communicate())
                if len(response[0]) > 0:
                    return str(response[0])[2:-4]
                raise NetworkError('No Network Connection')
            raise NetworkError('No Network Connection')
        except:
            raise  
    """ip_local= internet.ip_local"""
    @staticmethod
    def ram_total(convert=True):
        """
        Return total ram of board as string
        parameter convert: flag for convert mode (using of convert_byte function)
        """
        response = list(psutil.virtual_memory())
        if convert:
            return convert_bytes(int(response[0]))
        return str(response[0])
    @staticmethod
    def ram_used(convert=True):
        """
        Return how much ram is using.
        parameter convert: flag for convert mode (convert with convert_byte function)
        """
        response = list(psutil.virtual_memory())
        if convert:
            return convert_bytes(int(response[3]))
        return str(response[3])
    @staticmethod
    def ram_free(convert=True):
        """
        Return how much ram is available.
        parameter convert: flag for convert mode (convert with convert_byte function)
        """
        response = list(psutil.virtual_memory())
        if convert:
            return convert_bytes(int(response[1]))
        return str(response[1])
    @staticmethod
    def ram_percent(ONLY_NOM=False):
        """
        Return available ram percentage as an integer if ONLY_NOM, as string with % if not ONLY_NOM
        Parameter ONLY_NOM: flag for return type and value.
        """
        response = list(psutil.virtual_memory())
        if ONLY_NOM:
            return response[2]    
        return str(response[2]) + " %"
    @staticmethod
    def boot_time():
        '''
        Return the system boot time expressed in seconds since the epoch.
        '''
        return psutil.boot_time()
    @staticmethod
    def device_name():
        return socket.gethostname()
    @staticmethod
    def ip_website(url):
        '''get IP address of Web Site'''
        return socket.gethostbyname(url)
    """ip_webs= internet.ip_website"""
    @staticmethod
    def win10_notification(title,message,icon=None, duration=5) -> None:
        '''
        (THIS ONLY WORKS FOR "WINDOWS 10")\n
        Display Notification with title, message and icon for speciefic time.
        '''
        try:
            from win10toast import ToastNotifier
            ToastNotifier().show_toast(title,message,duration=duration)
        except:
            raise ImportError('Use "pip install win10toast" to install required module')
    @staticmethod
    def cpu_count(logical=True):
        '''
        Return the number of logical CPUs in the system
         (same as os.cpu_count() in Python 3.4).
        If *logical* is False return the number of physical cores only
         (e.g. hyper thread CPUs are excluded).
        Return None if undetermined.
        '''
        return psutil.cpu_count(logical)
    @staticmethod
    def pyshell_execute_bit():
        '''to determine whether a Python shell is executing in 32bit or 64bit'''
        #return platform.architecture()[0][:2]     # SLOW
        #return ctypes.sizeof(ctypes.c_voidp)*8
        import struct
        return struct.calcsize("P") * 8
    @staticmethod
    def pids() -> list:
        '''Return a list of current running PIDs'''
        return psutil.pids()
    @staticmethod
    def cpu_percent() -> float:
        '''
        Return a float representing the current system-wide CPU utilization as a percentage.'''
        return psutil.cpu_percent()
    @staticmethod
    def pid_exists(pid) -> bool:
        return psutil.pid_exists(pid)
