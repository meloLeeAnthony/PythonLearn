import pyttsx3 as pyttsx
'''
    错误明细：ModuleNotFoundError: No 08-module模块 named 'pythoncom'
    解决方案：pip install pywin32
'''
engine = pyttsx.init()
engine.say('好好学习')
engine.runAndWait()
