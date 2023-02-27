from typing                             import Callable, List, Tuple
from matplotlib.figure                  import Figure
from matplotlib.axes                    import Axes
from matplotlib.lines                   import Line2D
from matplotlib.animation               import FuncAnimation
from zope.interface                     import implementer

from interfaces.components.PlotPicture  import *

from backend.MathFuncsForVisual         import *
from backend.AdditionalFuncs            import *

@implementer(IPlotPicture)
class PlotPicture():
    """
        Класс, экземпляр которого хранит данные графика. Его экземпляр
        должен быть единственным.
    """

    def __init__(
        self, 
        get_app_state:  Callable[[], Dict],
        set_plot_figure_calced: Callable[[], None],
        set_prev_path_showed: Callable[[bool], None],
        set_prev_path_coords: Callable[[List[Tuple[float, float]]], None]
    
    ):

        self.__get_app_state            = get_app_state
        self.__set_plot_figure_calced   = set_plot_figure_calced
        self.__set_prev_path_showed     = set_prev_path_showed
        self.__set_prev_path_coords     = set_prev_path_coords

        #объект Figure
        self.fig:       Figure              = None
        self.subplt:    Axes                = None
        
        #графики плеч
        self.arms:      Line2D              = None

        #сочленения
        self.joints:    Line2D              = None
        self.joint_M:   Line2D              = None

        #предыдущий путь
        self.prev_path:             Line2D  = None
        self.prev_path_limit_dots:  Line2D  = None

        #анимация
        self.animation                      = None

    def set_plot_limits(self, a: float) -> None:
        self.subplt.set_xlim(left=-2.0*a, right=2.0*a)
        self.subplt.set_ylim(bottom=-2.0*a, top=2.0*a)
    
    def set_joints(self, x_space: List[float], y_space: List[float]) -> None:
        """Отрисовка сочленений"""

        self.joints, = self.subplt.plot(
            [x_space[0], x_space[1], x_space[3]], 
            [y_space[0], y_space[1], y_space[3]], 
            linestyle='',
            marker='o',
            markerfacecolor='#5D76CB'
        )
        self.joint_M, = self.subplt.plot(
            [x_space[2]],
            [y_space[2]],
            linestyle='',
            marker='o',
            markerfacecolor='#E32636'
        )
        
    def calc_arms(self, x_space: List[float], y_space: List[float]) -> None:
        """Отрисовка положения плеч"""

        self.arms, = self.subplt.plot(
            x_space,
            y_space,
            linewidth=3.0,
            color='darkcyan'
        )
            
    def show_prev_path(self) -> None:
        """Показывает последнюю траекторию, по которой перемщался привод"""
        self.prev_path, = self.subplt.plot(
            self.__get_app_state()["prev_path_x_coords"],
            self.__get_app_state()["prev_path_y_coords"],
            linewidth=1.5,
            color="#FF0033"
        )
        self.prev_path_limit_dots, = self.subplt.plot(
            [
                self.__get_app_state()["prev_path_x_coords"][0],
                self.__get_app_state()["prev_path_x_coords"][-1]
            ],

            [
                self.__get_app_state()["prev_path_y_coords"][0],
                self.__get_app_state()["prev_path_y_coords"][-1]
            ],
            linestyle='',
            marker='o',
            markerfacecolor='#FF0033',
        )

    def hide_prev_path(self) -> None:
        """Скрывает отрисованную траекторию"""

        self.prev_path.remove()
        self.prev_path_limit_dots.remove()

    def calc_plot_figure_from_scratch(self, psi: float, phi: float, a: float) -> None:
        """
            Создает объект графика matplotlib с отрисованными функциями y{I-IV}
            
            Аргументы:
            
            a - плечо привода
            
            psi - угол между плечом привода и осью OXr
            
            phi - угол поворота в полярной системе координат
        """

        self.fig = Figure(figsize=(5, 5))
        self.subplt = self.fig.add_subplot()

        x_space, y_space = MathFuncsForVisual.generate_spaces_x_y(
            a=a, 
            psi=psi, 
            phi=phi
        )

        self.set_plot_limits(a)
        self.set_joints(x_space, y_space)
        self.calc_arms(x_space, y_space)

        self.prev_path = None

        self.subplt.grid(True)

        self.__set_plot_figure_calced()
        self.__set_prev_path_coords([])
        self.__set_prev_path_showed(False)

    def update(self, frame: Tuple[float, float]) -> None:
        """
            Функция, вызываемая при обновлении фрейма анимации
        
            Аргументы:

            frame - кортеж в формате (x, y)
        """

        x, y = frame
        a = self.__get_app_state()["a"]

        outputs = AdditionalFuncs.calc_outputs({
            "x": x,
            "y": y,
            "a": a
        })
        
        x_space, y_space = MathFuncsForVisual.generate_spaces_x_y(
            outputs["psi"],
            outputs["phi"],
            a
        )
        
        self.arms.set_xdata(x_space)
        self.arms.set_ydata(y_space)

        self.joints.set_xdata([x_space[0], x_space[1], x_space[3]])
        self.joints.set_ydata([y_space[0], y_space[1], y_space[3]])
        self.joint_M.set_xdata([x])
        self.joint_M.set_ydata([y])

        return [
            self.arms,
            self.joints,
            self.joint_M
        ]
    
    def animate(self, frames: List[Tuple[float, float]]) -> None:
        self.animation = FuncAnimation(
            fig=self.fig,
            func=self.update,
            frames=frames,
            interval=25,
            blit=True,
            repeat=False
        )