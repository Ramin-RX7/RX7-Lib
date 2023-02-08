import rx7 as rx

class IO:
    
    @staticmethod
    def wait_for_input(prompt,SS:list=[]):
        answer= ''
        while not answer:
            answer = input(prompt).strip()
        return answer

    @staticmethod
    def selective_input(prompt,choices,default=None,ignore_case=False,error=True,invalid='Invalid input'):
        Choices = choices
        if type(choices) == dict:
            Choices = list(choices.keys())+list(choices.values())
        if ignore_case:
            Choices = [item.lower() for item in choices]

        while True:
            inp = input(prompt)
            inp = inp.lower() if ignore_case else inp
            if not inp  or  inp not in Choices:
                if error:
                    rx.style.print(invalid, color='red')
                else:
                    if default:
                        inp = default
                        break
            else:
                break
        if type(choices) == dict:
            try:
                inp = choices[inp]
            except KeyError:
                pass
        return inp

    @staticmethod
    def yesno_input(prompt,default=None):
        error= not bool(default)
        return io.selective_input(prompt,['y','yes','n','no'],default,error)
    
    @staticmethod
    def Input(prompt:str ='', default_value:str =''):
        '''
        Make Default Value For Your Input!  
        (THIS ONLY WORK ON WINDOWS (SORRY))
        prompt is what you want and it's input(prompt) .
        default_value is what there should be after prompt.
        E.g: 
        >>> Input('Is rx7 Library Easy to Learn?  ', 'Yes')
        Is rx7 Library Easy to Learn?  Yes
        '''

        import win32console
        _stdin = win32console.GetStdHandle(win32console.STD_INPUT_HANDLE)
        keys = []
        for c in str(default_value):
            evt = win32console.PyINPUT_RECORDType(win32console.KEY_EVENT)
            evt.Char = c
            evt.RepeatCount = 1
            evt.KeyDown = True
            keys.append(evt)
        _stdin.WriteConsoleInput(keys)
        return input(str(prompt))
    
    @staticmethod
    def getpass(prompt):
        '''
        Prompt for a password, with echo turned off.
        '''
        import getpass as Getpass
        return Getpass.getpass(prompt=prompt)
io = IO
Input   = default_input  = io.Input
getpass = password_input = io.getpass
