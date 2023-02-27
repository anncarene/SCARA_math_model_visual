class NotNumberEntryException(Exception):
    """Класс исключений для некорректных вводов (если не число вдруг введут)"""
    
    def __init__(self, *args):
        self.message = None
        
        if args:
            self.message = args[0]
            
    def __str__(self):
        return self.message


class ConvertingException(Exception):
    """Класс исключений для конвертации"""
    
    def __init__(self, *args):
        """Конструктор. Синтаксис вызова: __init__(message?: str, method?: str)"""
        
        self.message = args[0]
        self.method = args[1]
            
    def __str__(self):
        res = ""
        
        if self.method:
            res += " в методе " + self.method
        if self.message:
            res += " обнаружена проблема: " + self.message
            
        return res

class AnimationCalcException(Exception):
    """Класс исключений для анимации"""

    def __init__(self, *args):
        self.message = args[0]
    
    def __str__(self):
        return self.message

class ShowingPathException(Exception):
    """Класс исключений, выбрасываемых при отсутствии предыдущего пути для отрисовки"""

    def __init__(self, *args):
        self.message = args[0]

    def __str__(self):
        return self.message