from typing             import Dict, List, Tuple
from zope.interface     import Interface, Attribute

from backend.Exceptions import *

class IApp(Interface):
    """Интерфейс, реализуемый классом App"""

    """Поля"""
    __state                 = Attribute("Объект состояния приложения")
    plot_picture            = Attribute("Объект графика")
    main_window             = Attribute("Объект главного окна")
    
    anim_settings_window    = Attribute("Объект окна с настройками анимации")
    err_window              = Attribute("Объект окна с ошибкой")
    mp_anim_settings_window = Attribute("Объект окна с расширенными настройками анимации")

    """Методы"""
    def set_entries_state(state: str) -> None: pass
    def set_start_btns_state(state: str) -> None: pass
    def set_anim_settings_btn_state(state: str) -> None: pass
    def set_radio_btns_state(state: str) -> None: pass
    def set_mp_widgets_state(state: str) -> None: pass

    def get_app_state() -> Dict: pass
    
    def set_outputs(outputs: Dict[str, float]) -> None: pass
    
    def draw_plot_in_main_window() -> None: pass
    
    def set_main_window_x_entry_text(text: str): pass
    def set_main_window_y_entry_text(text: str): pass
    def set_a_entry_text(text: str) -> None: pass
    def set_main_window_entries_text(x_entry_text: str, y_entry_text: str) -> None: pass
    
    def err_window_init(
        err: NotNumberEntryException | ConvertingException | AnimationCalcException
    ) -> None: pass
    def anim_settings_window_init() -> None: pass
    
    def set_anim_settings_window_opened(opened: bool) -> None: pass
    def set_mp_anim_settings_window_opened(opened: bool) -> None: pass
    
    def set_plot_figure_calced() -> None: pass
    def set_prev_path_showed(showed: bool) -> None: pass
    
    def anim_settings_window_dismiss() -> None: pass
    def mp_anim_settings_window_dismiss() -> None: pass
    def main_window_destroy() -> None: pass
    
    def set_anim_settings_window_entry_x1_text(text: str) -> None: pass
    def set_anim_settings_window_entry_y1_text(text: str) -> None: pass
    def set_anim_settings_window_entry_x2_text(text: str) -> None: pass
    def set_anim_settings_window_entry_y2_text(text: str) -> None: pass
    def set_anim_settings_window_M1_entries_text(x_entry_text: str, y_entry_text: str) -> None: pass
    
    def set_mp_x_list_entry_text(text: str) -> None: pass
    def set_mp_y_list_entry_text(text: str) -> None: pass
    def set_mp_moving_mode_list_entry_text(text: str) -> None: pass

    def set_a_value(a: float) -> None: pass
    def set_xy_values(x: float, y: float) -> None: pass
    def set_x2y2_values(x: float, y: float) -> None: pass
    
    def set_mp_x_list(x_list: List[float]) -> None: pass
    def set_mp_y_list(y_list: List[float]) -> None: pass
    def set_mp_moving_mode_list(moving_mode_list: List[int]) -> None: pass

    def start_animation(frames: List[Tuple[float, float]]) -> None: pass
    
    def calc_plot_figure_from_scratch(psi: float, phi: float, a: float) -> None: pass
    
    def set_moving_mode(mode: str) -> None: pass
    
    def set_prev_path_coords(frames: List[Tuple[float, float]]) -> None: pass
    
    def show_prev_path() -> None: pass
    def hide_prev_path() -> None: pass
    
    def set_show_prev_path_btn_state(state: str) -> None: pass
    