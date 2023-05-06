"""
Terminal title in mac: "\033]0;{}\007".format(title)

 def screen_recorder():
    from screen_recorder_sdk import screen_recorder
    #screen_recorder.enable_dev_log ()
    screen_recorder.disable_log()
    pid = 2456
    screen_recorder.init_resources(pid)
    screen_recorder.start_video_recording ('video1.mp4', 30, 8000000, True)
    _time.sleep(10)
    print('hello')
    for i in range(100):
        x= i**3
    screen_recorder.stop_video_recording ()
    screen_recorder.free_resources()

 class Error(Exception):
    '''
    This module is for creating you own Error and Exception!
     Useage:
     >>> MyError = Error(name='MyError', msg='An Error occurred')
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     MyError: An Error occurred

     Also You can raise it directly:
     >>> raise Error(name='MyError', msg='An Error occurred')
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     MyError: An Error occurred

    '''
    def __new__(cls, msg, name=''):
        Error.__name__ = name
        return super(Error, cls).__new__(cls, msg)

    def __init__(self, **kwargs):
        pass

"""