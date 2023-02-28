from typing         import List, Tuple, Dict
from zope.interface import Interface, Attribute

class IAnimationSettingsWindowActions(Interface):
    """Интерфейс, реализуемый классом AnimationSettingsWindowActions"""

    """Поля"""
    __set_show_prev_path_btn_state              = Attribute("Функция из App, влияющая на состояние")
    __set_entries_state                         = Attribute("Функция из App, влияющая на состояние")
    __set_start_btns_state                      = Attribute("Функция из App, влияющая на состояние")
    __set_radio_btns_state                      = Attribute("Функция из App, влияющая на состояние")
    __set_main_window_x_entry_text              = Attribute("Функция из App, влияющая на состояние")
    __set_main_window_y_entry_text              = Attribute("Функция из App, влияющая на состояние")
    __start_animation                           = Attribute("Функция из App, влияющая на состояние")
    __anim_settings_window_dismiss              = Attribute("Функция из App, влияющая на состояние")
    __set_a_value                               = Attribute("Функция из App, влияющая на состояние")
    __set_outputs                               = Attribute("Функция из App, влияющая на состояние")
    __set_xy_values                             = Attribute("Функция из App, влияющая на состояние")
    __set_x2y2_values                           = Attribute("Функция из App, влияющая на состояние")
    __set_anim_settings_window_M1_entries_text  = Attribute("Функция из App, влияющая на состояние")
    __set_anim_settings_window_entry_x2_text    = Attribute("Функция из App, влияющая на состояние")
    __set_anim_settings_window_entry_y2_text    = Attribute("Функция из App, влияющая на состояние")
    __set_prev_path_coords                      = Attribute("Функция из App, влияющая на состояние")

    set_moving_mode         = Attribute("Функция из App, влияющая на состояние")
    err_window_init         = Attribute("Функция из App, влияющая на состояние")
    get_app_state           = Attribute("Геттер для переменных состояния")

    """Методы"""
    def xm1_entry_key_release(text: str) -> None: pass
    def ym1_entry_key_release(text: str) -> None: pass
    def xm2_entry_key_release(text: str) -> None: pass
    def ym2_entry_key_release(text: str) -> None: pass
    def anim_start_btn_click(mode: str, entries: Dict[str, str]) -> None: pass    
    def anim_start_btn_click(mode: str, entries: Dict[str, str]) -> None: pass
    def destroy() -> None: pass
    def set_values_after_animaion(xm2: float, ym2: float) -> None: pass
    def unblock_widgets() -> None: pass