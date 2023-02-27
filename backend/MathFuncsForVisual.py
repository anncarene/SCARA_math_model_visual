from abc                                    import ABCMeta
from typing                                 import Tuple, List
from zope.interface                         import provider

import numpy                                as np

from interfaces.backend.MathFuncsForVisual  import *

from backend.Converting                     import *

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
        match typeNum:
            case 1:
                return 0., a * np.cos(psi)
            case 2:
                return a * np.cos(psi), 0.
            case 3:
                return -a * np.cos(psi), 0.
            case 4:
                return 0., -a * np.cos(psi)
        
                
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
    def generate_spaces_x_y(
        psi:    float, 
        phi:    float,
        a:      float,
    ) -> Tuple[List[float], List[float]]:
        """
            Генерация списков значений для графиков положений ребер в matplotlib. Возвращает
            списки в формате (x_list, y_list)

            Аргументы:

            psi - угол между осью xr и плечом привода

            phi - угол точки M в полярной системе координат

            a - длина плеча привода
        """
        xI1, xI2, yI1, yI2 = MathFuncsForVisual.limits( 
            psi=psi, 
            phi=phi,
            a=a,
            typeNum=1
        )

        xIV1, xIV2, yIV1, yIV2 = MathFuncsForVisual.limits( 
            psi=psi, 
            phi=phi,
            a=a,
            typeNum=4
        )
        x_space = [xI1, xI2, xIV1, xIV2, xI1]
        y_space = [yI1, yI2, yIV1, yIV2, yI1]

        return x_space, y_space

    @staticmethod
    def generate_animation_frames(
        xm1:    float,
        ym1:    float,
        xm2:    float,
        ym2:    float, 
        mode:   str
    ) -> List[Tuple[float, float]]:
        """
            Генерация фреймов для анимации. Возвращает список фреймов для точки M в формате
            [(xm1, ym1), (xm2, ym2),..]

            Аргументы:

            xm1, ym1 - координаты начальной точки
            
            xm2, ym2 - координаты конечной точки

            mode - режим перемещения привода
        """

        m_frames: List[Tuple[float, float]] = []

        match mode:
            case "linear":
                for i in range(101):
                    t = i / 100.0
                    xm = MathFuncsForVisual.lin_func((xm1, xm2), t)
                    ym = MathFuncsForVisual.lin_func((ym1, ym2), t)
                    m_frames.append((xm, ym))

            case "radial":
                phi_m1, r_m1    = Converting.cartesianToPolar(xm1, ym1)
                phi_m2, r_m2    = Converting.cartesianToPolar(xm2, ym2)
                xd, yd          = Converting.polarToCartesian(phi_m1, r_m2)

                for i in range(50):
                    t = i / 50.0
                    xm = MathFuncsForVisual.lin_func((xm1, xd), t)
                    ym = MathFuncsForVisual.lin_func((ym1, yd), t)
                    m_frames.append((xm, ym))

                xr_m2, yr_m2    = Converting.r_transfer(xm2, ym2, (phi_m1 - np.pi / 2))
                phir_m2, rr_m2  = Converting.cartesianToPolar(xr_m2, yr_m2)

                sign_deltaphi   = 1
                deltaphi_abs    = 0.
                
                if xr_m2 >= 0.: 
                    sign_deltaphi = -1
                    deltaphi_abs = np.pi / 2 - (phir_m2)
                else:
                    deltaphi_abs = phir_m2 - np.pi / 2
                
                deltaphi = sign_deltaphi * deltaphi_abs

                for i in range(51):
                    phi = phi_m1 + i * (deltaphi / 50.0)
                    xm, ym = Converting.polarToCartesian(phi, r_m2)
                    m_frames.append((xm, ym))

            case "integral":
                phi_m1, r_m1    = Converting.cartesianToPolar(xm1, ym1)
                phi_m2, r_m2    = Converting.cartesianToPolar(xm2, ym2)

                xr_m2, yr_m2    = Converting.r_transfer(xm2, ym2, (phi_m1 - np.pi / 2))
                phir_m2, rr_m2  = Converting.cartesianToPolar(xr_m2, yr_m2)

                sign_deltaphi   = 1
                deltaphi_abs    = 0.
                
                if xr_m2 >= 0.: 
                    sign_deltaphi = -1
                    deltaphi_abs = np.pi / 2 - (phir_m2)
                else:
                    deltaphi_abs = phir_m2 - np.pi / 2
                
                deltaphi = sign_deltaphi * deltaphi_abs
                
                deltar = r_m2 - r_m1

                for i in range(101):
                    phi = phi_m1 + i * (deltaphi / 100.)
                    r = r_m1 + i * (deltar / 100.)
                    xm, ym = Converting.polarToCartesian(phi, r)
                    m_frames.append((xm, ym))
                
        return m_frames