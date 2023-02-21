from abc                    import ABCMeta
import numpy                as np
from typing                 import Tuple, List
from zope.interface         import provider

from ConvertingInterfaces   import *

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

@provider(IConvertingFactory)
class Converting():
    """
        Converting - абстрактный класс с математическими отображениями
        
        При некорректных входных данных функции выкидывают ConvertingException
    """
    
    __metaclass__: ABCMeta
    
    @staticmethod
    def degToRad(angleInDeg: float) -> float:
        """Принимает угол в градусах и возвращает угол в радианах"""
        
        return (np.pi / 180) * angleInDeg
    
    @staticmethod
    def radToDeg(angleInRad: float) -> float:
        """Принимает угол в радианах и возвращает угол в градусах"""
    
        return (180 / np.pi) * angleInRad
    
    @staticmethod
    def cartesianToPolar(
        x: float, 
        y: float
    ) -> Tuple[float, float]:
        """Отображение (x, y) -> (phi(rad), r)"""
        
        r = np.sqrt((x ** 2) + (y ** 2))
        
        if x > 0:
            return np.arctan(y/x), r
        if x < 0:
            return np.pi + np.arctan(y/x), r
        if x == 0. and y > 0:
            return np.pi / 2, r
        if x == 0. and y < 0:
            return 3 * np.pi / 2, r
        
        raise ConvertingException(
            "недопустимое преобразование",
            "cartesianToPolar(x: float, y: float) -> Tuple[float, float]"
        )

    @staticmethod
    def polarToCartesian(
        phi:    float, 
        r:      float
    ) -> Tuple[float, float]:
        """Отображение (phi(rad), r) -> (x, y)"""
        
        if r <= 0.:
            raise ConvertingException(
                "недопустимое преобразование: r <= 0",
                "polarToCartesian(phi: float, r: float) -> Tuple[float, float]"
            )
        
        x = r * np.cos(phi)
        y = r * np.sin(phi)
        
        return x, y
    
    @staticmethod
    def teta(r, a) -> float:
        """
            Описание:
            Возвращает угол между плечом и вертикальной осью привода (в радианах)
            
            Аргументы:
            
            r - радиус в полярной системе координат
            
            a - плечо привода
        """
        
        errors: List[str] = []
        
        if (a <= 0.):
            errors.append("a <= 0")
        if (r <= 0.):
            errors.append("r <= 0")
        if (np.absolute(r / (2 * a)) > 1.):
            errors.append("|r/(2*a)| > 1") 

        if len(errors) > 0:
            msg = ""
            
            for i in range(len(errors)):
                if len(errors) != 1:
                    if i != len(errors) - 1:
                        errors[i] += "; " 
                
                msg += errors[i]
            
            raise ConvertingException(
                msg,
                "teta(r: float, a: float) -> float"
            )
        else:
            return np.arccos(r / (2 * a))
    
    @staticmethod
    def psi(teta: float) -> float:
        """
            Описание:
            Возвращает угол между плечом и осью x
            в повернутой на phi системе координат (rad)
            
            Аргументы:
            
            teta - угол между плечом и вертикальной осью привода (rad)
        """
        
        if teta <= 0. or teta >= np.pi / 2:
            raise ConvertingException(
                "недопустимое значение teta",
                "psi(teta: float) -> float"
            )
        return (np.pi / 2) - teta
    
    @staticmethod
    def p_transfer(
        x:          float,
        y:          float,
        deltax:     float,
        deltay:     float
    ) -> Tuple[float, float]:
        """
            Прямой параллельный перенос
            
            Отображение (x, y) -> (x', y')
        """
        
        return x - deltax, y - deltay
    
    @staticmethod
    def r_p_transfer(
        x_n:        float, 
        y_n:        float, 
        deltax:     float,
        deltay:     float
        ) -> Tuple[float, float]:
        """
            Обратный параллельный перенос
            
            Отображение (x', y') -> (x, y)
        """
    
        return x_n + deltax, y_n + deltay
    
    @staticmethod
    def r_transfer(
        x:          float,
        y:          float,
        phi_r:        float
    ) -> Tuple[float, float]:
        """
            Поворот системы координат на угол phi_r по часовой стрелке
            
            Отображение (x, y) -> (xr, yr)
        """
        
        xr = x * np.cos(phi_r) + y * np.sin(phi_r)
        yr = y * np.cos(phi_r) - x * np.sin(phi_r)
        return xr, yr
    
    @staticmethod
    def r_r_transfer(
        xr:         float,
        yr:         float,
        phi_r:        float
    ) -> Tuple[float, float]:
        """
            Поворот системы координат на угол phi_r против часовой стрелки
            
            Отображение (xr, yr) -> (x, y)
        """
        
        x = xr * np.cos(phi_r) - yr * np.sin(phi_r)
        y = xr * np.sin(phi_r) + yr * np.cos(phi_r)
        return x, y