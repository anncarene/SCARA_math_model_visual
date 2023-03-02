from typing             import Dict, Callable
from zope.interface     import Interface, Attribute

from backend.Exceptions import *

class IMainWindowActionsFactory(Interface):
    """Интерфейс, предоставляемый классом MainWindowActions"""

    def __call__(
        set_outputs:                                Callable[[Dict[str, float]], None],
        
        get_app_state:                              Callable[[], Dict],
        
        set_anim_settings_window_entry_x1_text:     Callable[[str], None],
        set_anim_settings_window_entry_y1_text:     Callable[[str], None],
        set_anim_settings_window_M1_entries_text:   Callable[[str, str], None],
        
        anim_settings_window_init:                  Callable[[], None],
        anim_settings_window_dismiss:               Callable[[], None],
        mp_anim_settings_window_dismiss:            Callable[[], None],
        
        set_a_value:                                Callable[[float], None],
        set_xy_values:                              Callable[[float, float], None],
        
        err_window_init:                            Callable[
            [
                NotNumberEntryException | ConvertingException | AnimationCalcException
            ],
            None],
        
        draw_plot_in_main_window:                   Callable[[], None],
        
        set_a_entry_text:                           Callable[[str], None],
        
        main_window_destroy:                        Callable[[], None],
        
        show_prev_path:                             Callable[[], None],
        hide_prev_path:                             Callable[[], None],
        set_prev_path_showed:                       Callable[[bool], None],

        set_mp_x_list_entry_text:                   Callable[[str], None],
        set_mp_y_list_entry_text:                   Callable[[str], None]
    ):
        pass

class IMainWindowActions(Interface):
    """Интерфейс, реализуемый классом MainWindowActions"""

    """Поля"""
    __get_app_state                             = Attribute("Функция из App, влияющая на состояние приложения")
    __set_outputs                               = Attribute("Функция из App, влияющая на состояние приложения")
    __set_anim_settings_window_entry_x1_text    = Attribute("Функция из App, влияющая на состояние приложения")
    __set_anim_settings_window_entry_y1_text    = Attribute("Функция из App, влияющая на состояние приложения")
    __set_anim_settings_window_M1_entries_text  = Attribute("Функция из App, влияющая на состояние приложения")
    __anim_settings_window_init                 = Attribute("Функция из App, влияющая на состояние приложения")
    __anim_settings_window_dismiss              = Attribute("Функция из App, влияющая на состояние приложения")
    __set_a_value                               = Attribute("Функция из App, влияющая на состояние приложения")
    __set_xy_values                             = Attribute("Функция из App, влияющая на состояние приложения")
    __err_window_init                           = Attribute("Функция из App, влияющая на состояние приложения")
    __draw_plot_in_main_window                  = Attribute("Функция из App, влияющая на состояние приложения")
    __set_a_entry_text                          = Attribute("Функция из App, влияющая на состояние приложения")
    __main_window_destroy                       = Attribute("Функция из App, влияющая на состояние приложения")
    __show_prev_path                            = Attribute("Функция из App, влияющая на состояние приложения")
    __hide_prev_path                            = Attribute("Функция из App, влияющая на состояние приложения")
    __set_prev_path_showed                      = Attribute("Функция из App, влияющая на состояние приложения")
    __set_mp_x_list_entry_text                  = Attribute("Функция из App, влияющая на состояние приложения")
    __set_mp_y_list_entry_text                  = Attribute("Функция из App, влияющая на состояние приложения")
    
    """Методы"""
    def calc_btn_click(entries: Dict[str, str]) -> None: pass
    def anim_settings_btn_click() -> None: pass
    def a_entry_key_release(text: str) -> None: pass
    def x_entry_key_release(text: str) -> None: pass
    def y_entry_key_release(text) -> None: pass
    def show_prev_path_btn_click() -> None: pass
    def destroy() -> None: pass