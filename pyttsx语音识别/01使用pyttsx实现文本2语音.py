import pyttsx3 as pyttsx
'''
    错误明细：ModuleNotFoundError: No module named 'pythoncom'
    解决方案：pip install pywin32
'''
engine = pyttsx.init()
engine.say('好好学习')
engine.runAndWait()
