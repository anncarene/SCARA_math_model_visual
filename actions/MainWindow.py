from typing                         import Callable, Dict
from zope.interface                 import implementer

from interfaces.actions.MainWindow  import *

from backend.Exceptions             import *
from backend.AdditionalFuncs        import *

@implementer(IMainWindowActions)
class MainWindowActions():
    
    def __init__(
        self,
        set_outputs:                                Callable[[Dict[str, float]], None],
        get_app_state:                              Callable[[], Dict],
        set_anim_settings_window_entry_x1_text:     Callable[[str], None],
        set_anim_settings_window_entry_y1_text:     Callable[[str], None],
        set_anim_settings_window_M1_entries_text:   Callable[[str, str], None],
        anim_settings_window_init:                  Callable[[], None],
        anim_settings_window_dismiss:               Callable[[], None],
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
        set_prev_path_showed:                       Callable[[bool], None]
    ):
        self.__set_outputs                              = set_outputs
        self.__get_app_state                            = get_app_state
        self.__set_anim_settings_window_entry_x1_text   = set_anim_settings_window_entry_x1_text
        self.__set_anim_settings_window_entry_y1_text   = set_anim_settings_window_entry_y1_text
        self.__set_anim_settings_window_M1_entries_text = set_anim_settings_window_M1_entries_text
        self.__anim_settings_window_init                = anim_settings_window_init
        self.__anim_settings_window_dismiss             = anim_settings_window_dismiss
        self.__set_a_value                              = set_a_value
        self.__set_xy_values                            = set_xy_values
        self.__err_window_init                          = err_window_init
        self.__draw_plot_in_main_window                 = draw_plot_in_main_window
        self.__set_a_entry_text                         = set_a_entry_text
        self.__main_window_destroy                      = main_window_destroy
        self.__show_prev_path                           = show_prev_path
        self.__hide_prev_path                           = hide_prev_path
        self.__set_prev_path_showed                     = set_prev_path_showed

    def calc_btn_click(self, entries: Dict[str, str]) -> None:
        try:
            AdditionalFuncs.primal_entries_validation(entries)
            
            outputs = AdditionalFuncs.calc_outputs(entries)

            self.__set_xy_values(float(entries["x"]), float(entries["y"]))
            self.__set_a_value(float(entries["a"]))
            self.__set_anim_settings_window_M1_entries_text(entries["x"], entries["y"])
            self.__set_outputs(outputs)

            self.__draw_plot_in_main_window()

        except (
            NotNumberEntryException, 
            ConvertingException
        ) as err:
            self.__err_window_init(err)

    def anim_settings_btn_click(self) -> None:
        self.__anim_settings_window_init()

    def a_entry_key_release(self, text: str) -> None:
        self.__set_a_entry_text(text)
    
    def x_entry_key_release(self, text: str) -> None:
        self.__set_anim_settings_window_entry_x1_text(text)

    def y_entry_key_release(self, text) -> None:
        self.__set_anim_settings_window_entry_y1_text(text)

    def show_prev_path_btn_click(self) -> None:
        try:
            if self.__get_app_state()["prev_path_showed"]:
                self.__hide_prev_path()
                self.__set_prev_path_showed(False)
            else:
                if len(self.__get_app_state()["prev_path_x_coords"]) == 0:
                    raise ShowingPathException("Этот привод еще не перемещался")
                self.__show_prev_path()
                self.__set_prev_path_showed(True)
        except ShowingPathException as err:
            self.__err_window_init(err)

    def destroy(self) -> None:
        if self.__get_app_state()["anim_settings_window_opened"]:
            self.__anim_settings_window_dismiss()
        self.__main_window_destroy()