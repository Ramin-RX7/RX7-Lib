'''
System actions and information.
- Information about ram, ip, terminal, etc.
- Some System Actions like change terminal dir, send notification
'''
import os as _os
import re as _re
import socket as _socket
import psutil as _psutil
import subprocess as _subprocess



def _convert_bytes(nom:int) -> str:
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if nom < 1024.0:
            return "%3.1f %s" % (nom, x)
        nom /= 1024.0


def accname() -> str:
    '''return account username you have logged in.'''
    return _os.getlogin()


def pid() -> int:
    '''Get pid number of terminal and return it.'''
    return _os.getpid()

'''
def disk_usage(path):
    return _shutil.disk_usage(path)
'''

def chdir(path:str) -> None:
    '''Change directory of terminal.'''
    _os.chdir(path)


def SHUT_DOWN():
    '''(Windows only) Shut down the PC.'''
    _os.system("shutdown /s /t 1")


def RESTART():
    '''(Windows only) Restart the PC.'''
    _os.system("shutdown /r /t 1")


def terminal_size() -> tuple:
    '''Return terminal size in tuple (columns,rows)'''
    size= _os.get_terminal_size()
    return (size.columns,size.lines)


def cwd() -> str:
    '''Return string representing the current working directory.'''
    return _os.getcwd()


def ip_global() -> str:
    """
    Return ip with by http://ipinfo.io/ip api.
    returns global ip as string
    """
    import requests as _requests
    try:
        new_session = _requests.session()
        response = new_session.get("http://ipinfo.io/ip")
        import re
        ip_list = _re.findall(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}", response.text)
        new_session.close()
        return ip_list[0]
    except:
        raise ConnectionError('No Internet Connection') from None
# ip_global= internet.ip_global


def ip_local() -> str:
    """
    Return local ip of computer in windows by `socket` module
    and in linux with hostname command in shell.
    """
    #return [l for l in ([ip for ip in _socket.gethostbyname_ex(_socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [_socket._socket.(_socket.AF_INET, _socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
    import platform
    class NetworkError(Exception):
        pass
    ip = _socket.gethostbyname(_socket.gethostname())
    if ip  and  ip not in ("127.0.1.1","127.0.0.1"):
        return ip
    elif platform.system() != "Windows":
        command = _subprocess.Popen(["hostname", "-I"],stdout=_subprocess.PIPE,stderr=_subprocess.PIPE,stdin=_subprocess.PIPE,shell=False)
        response = list(command.communicate())
        if len(response[0]) > 0:
            return str(response[0])[2:-4]
        raise NetworkError('No Network Connection')
    raise NetworkError('No Network Connection')
# ip_local= internet.ip_local


def ram_total(convert:bool=True) -> int|str:
    """
    Return total ram of board as string
    parameter convert: convert result to idiomatic byte unit (str)
    """
    response = list(_psutil.virtual_memory())
    if convert:
        return _convert_bytes(int(response[0]))
    return response[0]


def ram_used(convert:bool=True) -> int|str:
    """
    Return how much ram is using.
    parameter convert: convert result to idiomatic byte unit (str)
    """
    response = list(_psutil.virtual_memory())
    if convert:
        return _convert_bytes(int(response[3]))
    return response[3]


def ram_free(convert:bool=True) -> int|str:
    """
    Return how much ram is available.
    parameter convert: convert result to idiomatic byte unit (str)
    """
    response = list(_psutil.virtual_memory())
    if convert:
        return _convert_bytes(int(response[1]))
    return response[1]


def ram_percent(ONLY_NOM:bool=False) -> int|str:
    """Return available ram percentage as an integer"""
    response = list(_psutil.virtual_memory())
    return response[2]


def boot_time() -> str:
    '''Return the system boot time expressed in seconds since the epoch.'''
    return _psutil.boot_time()


def device_name() -> str:
    """Returns device host name"""
    return _socket.gethostname()


def win10_notification(title:str, message:str, icon=None, duration:int=5) -> None:
    '''
    (WINDOWS-10 only)
    Display Notification with title, message and icon for given seconds.
    '''
    try:
        from win10toast import ToastNotifier
        ToastNotifier().show_toast(title,message,duration=duration)
    except:
        raise ImportError('Use "pip install win10toast" to install required module')


def cpu_count(logical=True) -> int:
    '''
    Return the number of logical CPUs in the system
     (same as _os.cpu_count() in Python 3.4).
    If *logical* is False return the number of physical cores only
     (e.g. hyper thread CPUs are excluded).
    Return None if undetermined.
    '''
    return _psutil.cpu_count(logical)


def pyshell_execute_bit() -> int:
    """to determine whether a Python shell is executing in 32bit or 64bit"""
    #return platform.architecture()[0][:2]     # SLOW
    #return ctypes.sizeof(ctypes.c_voidp)*8
    import struct
    return struct.calcsize("P") * 8


def pids() -> list:
    '''Return a list of current running PIDs'''
    return _psutil.pids()


def cpu_percent() -> float:
    '''
    Return a float representing the current system-wide CPU utilization as a percentage.
    '''
    return _psutil.cpu_percent()


def pid_exists(pid:int) -> bool:
    """Detemines whether a pid exists or not"""
    return _psutil.pid_exists(pid)


def mac_address(formatted:bool=False) -> str:
    """Returns mac address of the running device"""
    import uuid
    mac = uuid.getnode()
    if formatted:
        return ':'.join(['{:02x}'.format((mac >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
    return hex(mac)


def os_name():
    """Returns OS name of the device running the code"""
    import platform
    return platform.system()
