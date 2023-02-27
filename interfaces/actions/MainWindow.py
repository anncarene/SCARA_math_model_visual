from typing         import Dict
from zope.interface import Interface, Attribute

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

    """Методы"""
    def calc_btn_click(entries: Dict[str, str]) -> None: pass
    def anim_settings_btn_click() -> None: pass
    def a_entry_key_release(text: str) -> None: pass
    def x_entry_key_release(text: str) -> None: pass
    def y_entry_key_release(text) -> None: pass
    def show_prev_path_btn_click() -> None: pass
    def destroy() -> None: pass