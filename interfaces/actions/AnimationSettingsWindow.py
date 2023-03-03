from typing             import List, Tuple, Dict, Callable
from zope.interface     import Interface, Attribute

from backend.Exceptions import *

class IAnimationSettingsWindowActionsFactory(Interface):
    """Интерфейс, предоставляемый классом AnimationSettingsWindowActions"""

    def __call__(
        set_entries_state:                          Callable[[str], None],
        set_start_btns_state:                       Callable[[str], None],
        set_radio_btns_state:                       Callable[[str], None],
        
        get_app_state:                              Callable[[], Dict],
        
        set_main_window_x_entry_text:               Callable[[str], None],
        set_main_window_y_entry_text:               Callable[[str], None],
        
        start_animation:                            Callable[[List[Tuple[float, float]]], None],
        err_window_init:                            Callable[
                [
                    NotNumberEntryException | ConvertingException | AnimationCalcException
                ], 
                None
            ],
        anim_settings_window_dismiss:               Callable[[], None],
        
        set_a_value:                                Callable[[float], None],
        set_outputs:                                Callable[[Dict[str, float]], None],
        set_xy_values:                              Callable[[float, float], None],
        set_x2y2_values:                            Callable[[float, float], None],
        set_moving_mode:                            Callable[[str], None],
       
        set_anim_settings_window_M1_entries_text:   Callable[[str, str], None],
        set_anim_settings_window_entry_x2_text:     Callable[[str], None],
        set_anim_settings_window_entry_y2_text:     Callable[[str], None],
        
        set_prev_path_coords:                       Callable[[List[Tuple[float, float]]], None],
        set_show_prev_path_btn_state:               Callable[[str], None],

        set_mp_x_list:                              Callable[[List[float]], None],
        set_mp_y_list:                              Callable[[List[float]], None],
        set_mp_moving_mode_list:                    Callable[[List[int]], None],

        set_mp_x_list_entry_text:                   Callable[[str], None],
        set_mp_y_list_entry_text:                   Callable[[str], None],
        set_mp_widgets_state:                       Callable[[str], None],
        mp_anim_settings_window_init:               Callable[[], None]

    ): 
        pass

class IAnimationSettingsWindowActions(Interface):
    """Интерфейс, реализуемый классом AnimationSettingsWindowActions"""

    """Поля"""
    __set_prev_path_coords                      = Attribute("Функция из App, влияющая на состояние")
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
    
    __set_mp_x_list                             = Attribute("Функция из App, влияющая на состояние")
    __set_mp_y_list                             = Attribute("Функция из App, влияющая на состояние")
    __set_mp_moving_mode_list                   = Attribute("Функция из App, влияющая на состояние")

    __set_mp_x_list_entry_text                  = Attribute("Функция из App, влияющая на состояние")
    __set_mp_y_list_entry_text                  = Attribute("Функция из App, влияющая на состояние")
    __set_mp_widgets_state                      = Attribute("Функция из App, влияющая на состояние")
    __mp_anim_settings_window_init              = Attribute("Функция из App, влияющая на состояние")

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