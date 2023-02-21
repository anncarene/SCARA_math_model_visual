from zope.interface         import Interface, Attribute
from matplotlib.figure      import Figure
from typing                 import Dict

class IMainWindowFactory(Interface):
    """Интерфейс, предоставляемый классом MainWindow"""
    
    def calc_plot_figure(a: float, psi: float, phi: float) -> Figure:
        """"""
    
    def is_entry_valid(entry_value: str) -> bool:
        """"""
    
    def calc_outputs(entries: Dict[str, float]) -> Dict[str, float]:
        """"""            

class IMainWindow(Interface):
    """Интерфейс, реализуемый классом MainWindow"""
    
    """Поля"""
    title               = Attribute("Заголовок окна")
    geometry            = Attribute("Геометрия окна")
    
    a_label             = Attribute("Метка a=")
    a_entry             = Attribute("Поле ввода для a")
    
    x_label             = Attribute("Метка x=")
    x_entry             = Attribute("Поле ввода для x")
    
    y_label             = Attribute("Метка y=")
    y_entry             = Attribute("Поле ввода для y")
    
    r_label             = Attribute("Метка r=")
    r_value_label       = Attribute("Рассчитанное значение r")
    
    phi_label           = Attribute("Метка phi=")
    phi_value_label     = Attribute("Рассчитанное значение phi в градусах")
    
    psi_label           = Attribute("Метка psi=")
    psi_value_label     = Attribute("Рассчитанное значение psi в градусах")
    
    calc_btn            = Attribute("Кнопка, при нажатии на которую происходит расчет")
    canvas              = Attribute("Объект Canvas с визуализацией. Либо просто пустой")
    
    def drawCanvas(self, fig: Figure) -> None:
        """"""
    
    def set_outputs(self, outputs: Dict[str, float]) -> None:
        """"""
    
    def onClick(self):
        """"""