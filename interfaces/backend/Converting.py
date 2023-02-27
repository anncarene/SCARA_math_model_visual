from zope.interface         import Interface
from typing                 import Tuple

class IConvertingFactory(Interface):
    """Интерфейс, предоставляемый классом Converting"""
    
    def degToRad(angleInDeg: float) -> float: pass
    
    def radToDeg(angleInRad: float) -> float: pass
    
    def cartesianToPolar(
        x: float, 
        y: float
    ) -> Tuple[float, float]: pass
        
    def polarToCartesian(
        phi:    float, 
        r:      float
    ) -> Tuple[float, float]: pass
        
    def teta(r, a) -> float: pass
        
    def checkEntriedData(r: float, a: float) -> None: pass

    def psi(teta: float) -> float: pass
        
    def p_transfer(
        x:      float, 
        y:      float, 
        deltax: float, 
        deltay: float
    ) -> Tuple[float, float]: pass
        
    def r_p_transfer(
        x_n:    float, 
        y_n:    float, 
        deltax: float, 
        deltay: float
    ) -> Tuple[float, float]: pass
    
    def r_transfer(
        x:      float, 
        y:      float, 
        phi_r:  float
    ) -> Tuple[float, float]: pass
        
    def r_r_transfer(
        xr:     float, 
        yr:     float, 
        phi_r:  float
    ) -> Tuple[float, float]: pass