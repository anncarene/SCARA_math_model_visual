from abc                import ABCMeta
import numpy            as np
from typing             import Tuple
from zope.interface     import provider

from MathFuncsForVisualInterfaces   import *
from Converting                     import *

@provider(IMathFuncsForVisualFactory)
class MathFuncsForVisual():
    """MathFuncsForVisual - абстрактный класс с расчетами функций и интервалов для визуала"""
     
    __metaclass__: ABCMeta

    @staticmethod
    def yr(
        psi: float, 
        x: float, 
        a: float, 
        typeNum: int
    ) -> float:
        """
            Описание:
            Функция y(x) в системе координат, повернутой на угол phi - pi/2
            
            Возвращает значение y в точке x
            
            Аргументы:
            
            psi - угол между плечом и OXr
            
            x - точка x в повернутой системе координат, очевидно
            
            a - плечо привода
            
            typeNum - порядковый номер ребра от I до IV в описанной мат. модели
        """
        
        derSign = 1
        if typeNum == 2 or typeNum == 3:
            derSign = -1
        
        prlx = 0
        if typeNum == 2 or typeNum == 4:
            prlx = 1
        
        return derSign * np.tan(psi) * x + prlx * 2 * a * np.sin(psi)
    
    @staticmethod
    def lin_func(
        coords: Tuple[float, float],
        t: float
    ) -> float:
        """
            Описание:
            
            Возвращает значение переменной как параметрически заданной линейной
            функции в формате x = (x2 - x1) * t + x1
            
            Аргументы:
            
            coords - кортеж координат 2 точек в формате (x1, x2)
            
            t - параметр, принимающий значение от 0 до 1
        """
        
        return (coords[1] - coords[0]) * t + coords[0]
    
    @staticmethod
    def deltaxr(
        psi: float, 
        a: float, 
        typeNum: int
    ) -> Tuple[float, float]:
        """
            Описание:
            Возвращает пару чисел - границ отрезка области определения
            y(x) в повернутой на phi - pi/2 системе координат
            
            Аргументы:
            
            psi - угол между плечом и OXr
            
            a - плечо привода
            
            typeNum - порядковый номер ребра от I до IV в описанной мат. модели
        """
        
        if typeNum <= 2:
            return 0., a * np.cos(psi)
        return -a * np.cos(psi), 0.
    
    @staticmethod
    def limits(
        psi: float, 
        phi: float, 
        a: float, 
        typeNum: float
    ) -> Tuple[float, float, float, float]:
        """
            Описание:
            
            Функция, возвращающая координаты крайних точек ребра в формате
            (x1, x2, y1, y2)
            
            Аргументы:
            
            psi - угол между плечом и OXr
            
            a - плечо привода
            
            typeNum - порядковый номер ребра от I до IV в описанной мат. модели
        """
    
        xr = MathFuncsForVisual.deltaxr(psi, a, typeNum)
        
        yr = [0., 0.]
        for i in range(len(xr)):
            yr[i] = MathFuncsForVisual.yr(psi, xr[i], a, typeNum)
        
        x = [0., 0.]
        y = [0., 0.]
        for i in range(len(xr)):
            x[i], y[i] = Converting.r_r_transfer(xr[i], yr[i], phi - (np.pi / 2))
        
        return x[0], x[1], y[0], y[1]
    
    @staticmethod
    def generate_spaces(
        a: float, 
        psi: float, 
        phi: float,
    ) -> Tuple[List[List[float]], List[List[float]]]:
        """
            Описание:
            
            Генерирует кортеж из 2 списков в формате (x_spaces, y_spaces).
            Сами списки представляют из себя множество значений соответствующей координаты
            для последующей отрисовки в качестве графика в matplotlib
            
            Аргументы:
            
            a - длина ребра
            
            psi - угол между плечом и OXr
            
            phi - угол поворота в полярной системе координат
        """
        
        x_spaces: List[List[float]] = [[], [], [], []]
        y_spaces: List[List[float]] = [[], [], [], []]
        
        for i in range(4):
            x1, x2, y1, y2 = MathFuncsForVisual.limits(psi, phi, a, i + 1)
            
            for j in range(101):
                t = j / 100.0
                x_spaces[i].append(MathFuncsForVisual.lin_func((x1, x2), t))
                y_spaces[i].append(MathFuncsForVisual.lin_func((y1, y2), t))
            
        return x_spaces, y_spaces
