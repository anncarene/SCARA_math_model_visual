from zope.interface         import Interface
from typing                 import Tuple, List

class IMathFuncsForVisualFactory(Interface):
    """Интерфейс, предоставляемый классом MathFuncsForVisual"""
    
    def yr(
        psi:    float, 
        x:      float, 
        a:      float, 
        typeNum:int
    ) -> float: pass
        
    def lin_func(
        coords: Tuple[float, float],
        t:      float
    ) -> float: pass
    
    def deltaxr(
        psi:    float, 
        a:      float, 
        typeNum:int
    ) -> Tuple[float, float]: pass
        
    def limits(
        psi:    float, 
        phi:    float, 
        a:      float, 
        typeNum:int
    ) -> Tuple[float, float, float, float]: pass
        
    def generate_spaces(
        a:      float,
        psi:    float,
        phi:    float
    ) -> Tuple[List[float], List[float]]: pass
    
    def generate_animation_frames(
        xm1:    float,
        ym1:    float,
        xm2:    float,
        ym2:    float,
        mode:   str
    ) -> List[Tuple[float, float]]: pass