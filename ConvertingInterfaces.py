from zope.interface         import Interface
from typing                 import Tuple

class IConvertingFactory(Interface):
    """Интерфейс, предоставляемый классом Converting"""
    
    def degToRad(angleInDeg: float) -> float:
        """"""
    
    def radToDeg(angleInRad: float) -> float:
        """"""
    
    def cartesianToPolar(
        x: float, 
        y: float
    ) -> Tuple[float, float]:
        """"""
        
    def polarToCartesian(
        phi:    float, 
        r:      float
    ) -> Tuple[float, float]:
        """"""
        
    def teta(r, a) -> float:
        """"""
        
    def psi(teta: float) -> float:
        """"""
        
    def p_transfer(
        x:      float, 
        y:      float, 
        deltax: float, 
        deltay: float
    ) -> Tuple[float, float]:
        """"""
        
    def r_p_transfer(
        x_n:    float, 
        y_n:    float, 
        deltax: float, 
        deltay: float
    ) -> Tuple[float, float]:
        """"""
    
    def r_transfer(
        x:      float, 
        y:      float, 
        phi_r:    float
    ) -> Tuple[float, float]:
        """"""
        
    def r_r_transfer(
        xr:     float, 
        yr:     float, 
        phi_r:  float
    ) -> Tuple[float, float]:
        """"""