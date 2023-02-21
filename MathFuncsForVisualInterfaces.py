from zope.interface         import Interface
from typing                 import Tuple, Generator, List

class IMathFuncsForVisualFactory(Interface):
    """Интерфейс, предоставляемый классом MathFuncsForVisual"""
    
    def yr(
        psi:    float, 
        x:      float, 
        a:      float, 
        typeNum:int
    ) -> float:
        """"""
        
    def lin_func(
        coords: Tuple[float, float],
        t:      float
    ) -> float:
        """"""
    
    def deltaxr(
        psi:    float, 
        a:      float, 
        typeNum:int
    ) -> Tuple[float, float]:
        """"""
        
    def limits(
        psi:    float, 
        phi:    float, 
        a:      float, 
        typeNum:int
    ) -> Tuple[float, float, float, float]:
        """"""
        
    def generate_spaces(
        a:      float,
        psi:    float,
        phi:    float
    ) -> Tuple[List[List[float]], List[List[float]]]:
        """"""