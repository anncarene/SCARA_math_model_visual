from typing         import List, Tuple
from zope.interface import Interface, Attribute

class IPlotPicture(Interface):
    """Интерфейс, реализуемый классом PlotPicture"""

    """Поля"""
    fig                         = Attribute("Объект Figure с графиком")
    subplt                      = Attribute("subplot для fig")
    
    arms                        = Attribute("Графики плеч привода")
    joints                      = Attribute("Сочленения")
    joint_M                     = Attribute("Сочленение в точке M")

    prev_path                   = Attribute("График последнго пройденного маршрута")
    prev_path_limit_dots        = Attribute("Крайние точки графика последнего пройденного маршрута")

    animation                   = Attribute("Объект анимации")

    __get_app_state             = Attribute("Геттер переменных состояния приложения")
    __set_plot_figure_calced    = Attribute("Функция из App, влияющая на состояние")
    __set_prev_path_showed      = Attribute("Функция из App, влияющая на состояние")
    __set_prev_path_coords      = Attribute("Функция из App, влияющая на состояние")

    """Методы"""
    def set_plot_limits(a: float) -> None: pass
    def set_joints(x_space: List[float], y_space: List[float]) -> None: pass
    def calc_arms(x_space: List[float], y_space: List[float]) -> None: pass
    def show_prev_path(self) -> None: pass
    def hide_prev_path(self) -> None: pass
    def calc_plot_figure_from_scratch(psi: float, phi: float, a: float) -> None: pass
    def update(frame: Tuple[float, float]) -> None: pass
    def animate(frames: List[Tuple[float, float]]) -> None: pass