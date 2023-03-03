from zope.interface                         import implementer
from typing                                 import List, Tuple, Dict

from State                                  import *

from interfaces.App                         import *

from components.MainWindow                  import *
from components.AnimationSettingsWindow     import *
from components.MP_AnimationSttingsWindow   import *
from components.ErrWindow                   import *
from components.PlotPicture                 import *

from actions.MainWindow                     import *
from actions.MP_AnimationSettingsWindow     import *
from actions.AnimationSettingsWindow        import *

from config                                 import INTERFACE_EXCEPTIONS_MODE

from backend.InterfaceVerificator           import *
from backend.Exceptions                     import *
from backend.Converting                     import *

@InterfaceVerificator.except_if_not_implements(
    INTERFACE_EXCEPTIONS_MODE,
    IApp
)
@implementer(IApp)
class App():
    """Класс, экземпляр которого является корневым объектом приложения"""

    def __init__(self):
        
        #инициализация состояния приложения
        self.__state: State = State()
        
        #инициализация объекта графика
        self.plot_picture: PlotPicture = PlotPicture(
            get_app_state           = self.get_app_state,
            set_plot_figure_calced  = self.set_plot_figure_calced,
            set_prev_path_showed    = self.set_prev_path_showed,
            set_prev_path_coords    = self.set_prev_path_coords
        )
        
        #открытие главного окна
        self.main_window: MainWindow = MainWindow(
            #инициализация обработчика событий окна
            actions = MainWindowActions(
                set_outputs                                 = self.set_outputs,
                get_app_state                               = self.get_app_state,
                set_anim_settings_window_entry_x1_text      = self.set_anim_settings_window_entry_x1_text,
                set_anim_settings_window_entry_y1_text      = self.set_anim_settings_window_entry_y1_text,
                set_anim_settings_window_M1_entries_text    = self.set_anim_settings_window_M1_entries_text,
                anim_settings_window_init                   = self.anim_settings_window_init,
                anim_settings_window_dismiss                = self.anim_settings_window_dismiss,
                mp_anim_settings_window_dismiss             = self.mp_anim_settings_window_dismiss,
                set_a_value                                 = self.set_a_value,
                set_xy_values                               = self.set_xy_values,
                err_window_init                             = self.err_window_init,
                draw_plot_in_main_window                    = self.draw_plot_in_main_window,
                set_a_entry_text                            = self.set_a_entry_text,
                main_window_destroy                         = self.main_window_destroy,
                show_prev_path                              = self.show_prev_path,
                hide_prev_path                              = self.hide_prev_path,       
                set_prev_path_showed                        = self.set_prev_path_showed,
                set_mp_x_list_entry_text                    = self.set_mp_x_list_entry_text,
                set_mp_y_list_entry_text                    = self.set_mp_y_list_entry_text
            ),
            plot_picture = self.plot_picture
        )

        self.anim_settings_window: AnimationSettingsWindow = None
        self.mp_anim_settings_window: MP_AnimationSettingsWindow = None
        self.err_window: ErrWindow = None

    def set_entries_state(self, state: str) -> None:
        """Устанавливает state-параметр полей для ввода"""

        self.main_window.a_entry["state"]                       = [state]
        self.main_window.x_entry["state"]                       = [state]
        self.main_window.y_entry["state"]                       = [state]

        if self.__state.anim_settings_window_opened:
            self.anim_settings_window.xm1_entry["state"]        = [state]
            self.anim_settings_window.ym1_entry["state"]        = [state]
            self.anim_settings_window.xm2_entry["state"]        = [state]
            self.anim_settings_window.ym2_entry["state"]        = [state]

        self.__state.anim_settings_window_entries_state         = state

    def set_start_btns_state(self, state: str) -> None:
        """Устанавливает state-параметр кнопок старта анимации и расчета"""

        self.main_window.calcbtn["state"]                       = [state]
        if self.__state.anim_settings_window_opened:
            self.anim_settings_window.anim_start_btn["state"]   = [state]
        self.__state.anim_settings_window_start_btn_state       = state

    def set_anim_settings_btn_state(self, state: str) -> None:
        """Устанавливает state-параметр кнопки настроек анимации"""
        
        self.main_window.anim_settings_btn["state"]             = [state]
    
    def set_show_mp_settings_btn_state(self, state: str) -> None:
        """Устанавливает state-параметр кнопки расширенных настроек анимации"""
        
        if self.__state.anim_settings_window_opened:
            self.anim_settings_window.show_mp_settings_btn["state"] = [state]

    def set_radio_btns_state(self, state: str) -> None:
        """Устанавливает state-параметр радио-кнопок в окне настроек анимации"""

        if self.__state.anim_settings_window_opened:
            self.anim_settings_window.radial_mode_btn["state"]      = [state]
            self.anim_settings_window.linear_mode_btn["state"]      = [state]
            self.anim_settings_window.integral_mode_btn["state"]    = [state]
        
        self.__state.anim_settings_window_radio_btns_state          = state

    def set_mp_widgets_state(self, state: str) -> None:
        """Устанавливает state-параметр виджетов окна с расширенными настройками анимации"""

        if self.__state.mp_anim_settings_window_opened:
            self.mp_anim_settings_window.x_list_entry["state"]              = [state]
            self.mp_anim_settings_window.y_list_entry["state"]              = [state]
            self.mp_anim_settings_window.moving_mode_list_entry["state"]    = [state]
            self.mp_anim_settings_window.clear_btn["state"]                 = [state]
            self.mp_anim_settings_window.start_btn["state"]                 = [state]
        
        self.__state.mp_entries_state   = state
        self.__state.mp_btns_state      = state


    def get_app_state(self) -> Dict:
        """Геттер для переменных состояния приложения"""

        return {
            "xm1":      self.__state.xm1,
            "ym1":      self.__state.ym1,
            "xm2":      self.__state.xm2,
            "ym2":      self.__state.ym2,
            "a":        self.__state.a,
            "r":        self.__state.r,
            "phi":      self.__state.phi,
            "psi":      self.__state.psi,
            "teta":     self.__state.teta,
            "a_entry_text": self.__state.a_entry_text,
            "anim_settings_window_opened": self.__state.anim_settings_window_opened,
            "anim_settings_window_entries_state": self.__state.anim_settings_window_entries_state,
            "anim_settings_window_radio_btns_state": self.__state.anim_settings_window_radio_btns_state,
            "anim_settings_window_start_btn_state": self.__state.anim_settings_window_start_btn_state,
            "xm1_entry_text":       self.__state.xm1_entry_text,
            "ym1_entry_text":       self.__state.ym1_entry_text,
            "xm2_entry_text":       self.__state.xm2_entry_text,
            "ym2_entry_text":       self.__state.ym2_entry_text,
            "plot_figure_calced":   self.__state.plot_figure_calced,
            "moving_mode":          self.__state.moving_mode,
            "prev_path_showed":     self.__state.prev_path_showed,
            "prev_path_x_coords":   self.__state.prev_path_x_coords,
            "prev_path_y_coords":   self.__state.prev_path_y_coords,
            "mp_anim_settings_window_opened": self.__state.mp_anim_settings_window_opened,
            "mp_x_list":            self.__state.mp_x_list,
            "mp_y_list":            self.__state.mp_y_list,
            "mp_moving_mode_list":  self.__state.mp_moving_mode_list,
            "mp_x_list_entry_text": self.__state.mp_x_list_entry_text,
            "mp_y_list_entry_text": self.__state.mp_y_list_entry_text,
            "mp_moving_mode_list_entry_text": self.__state.mp_moving_mode_list_entry_text,
            "mp_entries_state":     self.__state.mp_entries_state,
            "mp_btns_state":        self.__state.mp_btns_state
        }

    def set_outputs(self, outputs: Dict[str, float]) -> None:
        """
            Задает и отображает в главном окне приложения r, teta, phi, psi

            Аргументы:

            outputs - словарь в формате {"r": float, "teta": float, "phi": float, "psi": float}
        """
        
        self.__state.r    = outputs["r"]
        self.__state.phi  = outputs["phi"]
        self.__state.psi  = outputs["psi"]
        self.__state.teta = outputs["teta"]

        self.main_window.r_value_label["text"]       = str(self.__state.r)
        self.main_window.teta_value_label["text"]    = str(Converting.radToDeg(self.__state.teta)) + " deg"
        self.main_window.phi_value_label["text"]     = str(Converting.radToDeg(self.__state.phi)) + " deg"
        self.main_window.psi_value_label["text"]     = str(Converting.radToDeg(self.__state.psi)) + " deg"

    def draw_plot_in_main_window(self) -> None:
        """Отрисовка графика с нуля на основании введенных данных"""

        self.plot_picture.calc_plot_figure_from_scratch(
            psi = self.__state.psi,
            phi = self.__state.phi,
            a   = self.__state.a
        )
        self.main_window.draw_canvas()

    def set_main_window_x_entry_text(self, text: str):
        """Задает и отображает текст для поля ввода x в главном окне"""

        self.__state.xm1_entry_text = text
        
        self.main_window.x_entry.delete(0, END)
        self.main_window.x_entry.insert(0, text)
    
    def set_main_window_y_entry_text(self, text: str):
        """Задает и отображает текст для поля ввода y в главном окне"""

        self.__state.ym1_entry_text = text
        
        self.main_window.y_entry.delete(0, END)
        self.main_window.y_entry.insert(0, text)

    def set_a_entry_text(self, text: str) -> None:
        """
            Задает переменную(!) введенного в поле ввода a текста
            в глобальном состоянии приложения
        """

        self.__state.a_entry_text = text
    
    def set_main_window_entries_text(self, x_entry_text: str, y_entry_text: str) -> None:
        """Задает и отображает в главном окне измененные x(M), y(M)"""
        
        self.set_main_window_x_entry_text(x_entry_text)
        self.set_main_window_y_entry_text(y_entry_text)

    def err_window_init(
            self, 
            err: NotNumberEntryException | ConvertingException | AnimationCalcException
        ) -> None:
        """Инициализация окна с ошибкой"""

        self.err_window = ErrWindow(str(err))

    def anim_settings_window_init(self) -> None:
        """Инициализация окна настроек анимации"""

        self.set_anim_settings_window_opened(True)
        self.set_anim_settings_btn_state("disabled")
        self.anim_settings_window = AnimationSettingsWindow(
            #инициализация обработчика событий окна
            actions = AnimationSettingsWindowActions(
                set_entries_state               = self.set_entries_state,
                set_start_btns_state            = self.set_start_btns_state,
                set_radio_btns_state            = self.set_radio_btns_state,
                get_app_state                   = self.get_app_state,
                set_main_window_x_entry_text    = self.set_main_window_x_entry_text,
                set_main_window_y_entry_text    = self.set_main_window_y_entry_text,
                start_animation                 = self.start_animation,
                err_window_init                 = self.err_window_init,
                anim_settings_window_dismiss    = self.anim_settings_window_dismiss,
                set_a_value                     = self.set_a_value,
                set_outputs                     = self.set_outputs,
                set_xy_values                   = self.set_xy_values,
                set_x2y2_values                 = self.set_x2y2_values,
                set_moving_mode                 = self.set_moving_mode,
                set_prev_path_coords            = self.set_prev_path_coords,
                set_show_prev_path_btn_state    = self.set_show_prev_path_btn_state,
                set_anim_settings_window_M1_entries_text    = self.set_anim_settings_window_M1_entries_text,
                set_anim_settings_window_entry_x2_text      = self.set_anim_settings_window_entry_x2_text,
                set_anim_settings_window_entry_y2_text      = self.set_anim_settings_window_entry_y2_text,
                set_mp_x_list_entry_text        = self.set_mp_x_list_entry_text,
                set_mp_y_list_entry_text        = self.set_mp_y_list_entry_text,
                set_mp_widgets_state            = self.set_mp_widgets_state,
                mp_anim_settings_window_init    = self.mp_anim_settings_window_init,
                set_mp_x_list                   = self.set_mp_x_list,
                set_mp_y_list                   = self.set_mp_y_list,
                set_mp_moving_mode_list         = self.set_mp_moving_mode_list
            )
        )

    def mp_anim_settings_window_init(self) -> None:
        """Инициализация окна с расширенными настройками анимации"""

        self.set_mp_anim_settings_window_opened(True)
        self.set_show_mp_settings_btn_state("disabled")
        self.mp_anim_settings_window = MP_AnimationSettingsWindow(
            #инициализация обработчика событий
            actions = MP_AnimationSettingsWindowActions(
                set_entries_state               = self.set_entries_state,
                set_start_btns_state            = self.set_start_btns_state,
                set_radio_btns_state            = self.set_radio_btns_state,
                get_app_state                   = self.get_app_state,
                set_main_window_x_entry_text    = self.set_main_window_x_entry_text,
                set_main_window_y_entry_text    = self.set_main_window_y_entry_text,
                start_animation                 = self.start_animation,
                err_window_init                 = self.err_window_init,
                set_a_value                     = self.set_a_value,
                set_outputs                     = self.set_outputs,
                set_xy_values                   = self.set_xy_values,
                set_x2y2_values                 = self.set_x2y2_values,
                set_prev_path_coords            = self.set_prev_path_coords,
                set_show_prev_path_btn_state    = self.set_show_prev_path_btn_state,
                set_anim_settings_window_M1_entries_text    = self.set_anim_settings_window_M1_entries_text,
                mp_anim_settings_window_dismiss     = self.mp_anim_settings_window_dismiss,
                set_mp_x_list                       = self.set_mp_x_list,
                set_mp_y_list                       = self.set_mp_y_list,
                set_mp_moving_mode_list             = self.set_mp_moving_mode_list,
                set_mp_x_list_entry_text            = self.set_mp_x_list_entry_text,
                set_mp_y_list_entry_text            = self.set_mp_y_list_entry_text,
                set_mp_moving_mode_list_entry_text  = self.set_mp_moving_mode_list_entry_text,
                set_mp_widgets_state                = self.set_mp_widgets_state,
            )
        )


    def set_anim_settings_window_opened(self, opened: bool) -> None:
        """
            Задает переменную глобального состояния приложения,
            обозначающую, открыто ли окно настроек анимации на
            bool-значение opened 
        """

        self.__state.anim_settings_window_opened = opened
    
    def set_mp_anim_settings_window_opened(self, opened: bool) -> None:
        """
            Задает переменную глобального состояния приложения,
            обозначающую, открыто ли окно расширенных настроек анимации, на
            bool-значение opened
        """

        self.__state.mp_anim_settings_window_opened = opened

    def set_plot_figure_calced(self) -> None:
        """
            Статично задает на True значение глобальной переменной
            состояния приложения, обозначающей, был ли график рассчитан
            хотя бы 1 раз 
        """
        
        self.__state.plot_figure_calced = True

    def set_prev_path_showed(self, showed: bool) -> None:
        """
            Задает переменную глобального состояния приложения,
            обозначающую, показан ли последний маршрут привода на графике.
            Соответствующе меняет состояние кнопок расчета и старта анимации
        """

        self.__state.prev_path_showed = showed
        if showed is True:
            self.set_start_btns_state("disabled")
            self.set_mp_widgets_state("disabled")
            self.main_window.show_prev_path_btn["text"] = "Скрыть предыдущий маршрут"
        else:
            self.set_start_btns_state("normal")
            self.set_mp_widgets_state("normal")
            self.main_window.show_prev_path_btn["text"] = "Показать предыдущий маршрут"

    def anim_settings_window_dismiss(self) -> None:
        self.set_anim_settings_window_opened(False)
        self.set_anim_settings_btn_state("normal")
        self.anim_settings_window.destroy()

    def mp_anim_settings_window_dismiss(self) -> None:
        self.set_mp_anim_settings_window_opened(False)
        self.set_show_mp_settings_btn_state("normal")
        self.mp_anim_settings_window.destroy()

    def main_window_destroy(self) -> None:
        self.main_window.destroy()
    
    def set_anim_settings_window_entry_x1_text(self, text: str) -> None:
        """
            Задает глобальную переменную состояния, хранящую в себе ввод поля
            x1 для окна настроек анимации, меняет текст в поле ввода соответствующим образом,
            усли это окно открыто
        """

        self.__state.xm1_entry_text = text
        
        if self.__state.anim_settings_window_opened:
            self.anim_settings_window.xm1_entry.delete(0, END)
            self.anim_settings_window.xm1_entry.insert(0, text)
    
    def set_anim_settings_window_entry_y1_text(self, text: str) -> None:
        """
            Задает глобальную переменную состояния, хранящую в себе ввод поля
            y1 для окна настроек анимации, меняет текст в поле ввода соответствующим образом,
            усли это окно открыто
        """

        self.__state.ym1_entry_text = text
        
        if self.__state.anim_settings_window_opened:
            self.anim_settings_window.ym1_entry.delete(0, END)
            self.anim_settings_window.ym1_entry.insert(0, text)
    
    def set_anim_settings_window_entry_x2_text(self, text: str) -> None:
        """
            Задает глобальную переменную состояния, хранящую в себе ввод поля
            x2 для окна настроек анимации, меняет текст в поле ввода соответствующим образом,
            усли это окно открыто
        """
        
        self.__state.xm2_entry_text = text
        
        if self.__state.anim_settings_window_opened:
            self.anim_settings_window.xm2_entry.delete(0, END)
            self.anim_settings_window.xm2_entry.insert(0, text)

    def set_anim_settings_window_entry_y2_text(self, text: str) -> None:
        """
            Задает глобальную переменную состояния, хранящую в себе ввод поля
            y2 для окна настроек анимации, меняет текст в поле ввода соответствующим образом,
            усли это окно открыто
        """
        
        self.__state.ym2_entry_text = text

        if self.__state.anim_settings_window_opened:
            self.anim_settings_window.ym2_entry.delete(0, END)
            self.anim_settings_window.ym2_entry.insert(0, text)

    def set_anim_settings_window_M1_entries_text(
        self, 
        x_entry_text: str,
        y_entry_text: str
    ) -> None:
        """
            Задает глобальные переменные состояния, хранящие в себе ввод полей
            x1, y1 для окна настроек анимации, меняет текст в поле ввода соответствующим образом,
            усли это окно открыто
        """

        self.set_anim_settings_window_entry_x1_text(x_entry_text)
        self.set_anim_settings_window_entry_y1_text(y_entry_text)

    def set_mp_x_list_entry_text(self, text: str) -> None:
        self.__state.mp_x_list_entry_text = text

        if self.__state.mp_anim_settings_window_opened:
            self.mp_anim_settings_window.x_list_entry.delete(0, END)
            self.mp_anim_settings_window.x_list_entry.insert(0, text)

    def set_mp_y_list_entry_text(self, text: str) -> None:
        self.__state.mp_y_list_entry_text = text

        if self.__state.mp_anim_settings_window_opened:
            self.mp_anim_settings_window.y_list_entry.delete(0, END)
            self.mp_anim_settings_window.y_list_entry.insert(0, text)

    def set_mp_moving_mode_list_entry_text(self, text: str) -> None:
        self.__state.mp_moving_mode_list_entry_text = text

        if self.__state.mp_anim_settings_window_opened:
            self.mp_anim_settings_window.moving_mode_list_entry.delete(0, END)
            self.mp_anim_settings_window.moving_mode_list_entry.insert(0, text)    

    def set_a_value(self, a: float) -> None:
        """Задает state-переменную a"""

        self.__state.a = a
 
    def set_xy_values(self, x: float, y: float) -> None:
        """Задает state-переменные xm1, ym1"""

        self.__state.xm1 = x
        self.__state.ym1 = y
    
    def set_x2y2_values(self, x: float, y: float) -> None:
        """Задает state-переменные xm2, ym2"""

        self.__state.xm2 = x
        self.__state.ym2 = y
    
    def set_mp_x_list(self, x_list: List[float]) -> None:
        self.__state.mp_x_list = x_list
    
    def set_mp_y_list(self, y_list: List[float]) -> None:
        self.__state.mp_y_list = y_list
    
    def set_mp_moving_mode_list(self, moving_mode_list: List[int]) -> None:
        self.__state.mp_moving_mode_list = moving_mode_list

    def start_animation(self, frames: List[Tuple[float, float]]) -> None:
        """
            Старт анимации

            Аргументы:

            frames - список фрееймов для точки M в формате [(x1, y1), (x2, y2),..]
        """

        self.plot_picture.animate(frames)

    def calc_plot_figure_from_scratch(self, psi: float, phi: float, a: float) -> None:
        """Расчет объекта графика с нуля"""

        self.plot_picture.calc_plot_figure_from_scratch(psi, phi, a)

    def set_moving_mode(self, mode: str) -> None:
        """Задание режима перемещений на уровне глобальной переменной состояния приложения"""
        self.__state.moving_mode = mode
    
    def set_prev_path_coords(self, frames: List[Tuple[float, float]]) -> None:
        """
            Полная очистка списков, хранящих в себе последний пройденный приводом
            маршрут и заполнение их новыми значениями

            Аргументы:

            frames - список в формате [(x1, y1), (x2, y2),..]
        """

        self.__state.prev_path_x_coords = []
        self.__state.prev_path_y_coords = []
        
        for elem in frames:
            self.__state.prev_path_x_coords.append(elem[0])
            self.__state.prev_path_y_coords.append(elem[1])
    
    def show_prev_path(self) -> None:
        self.plot_picture.show_prev_path()
    
    def hide_prev_path(self) -> None:
        self.plot_picture.hide_prev_path()
    
    def set_show_prev_path_btn_state(self, state: str) -> None:
        """Задает state-параметр кнопки для показа последнего пройденного маршрута"""

        self.main_window.show_prev_path_btn["state"] = [state]