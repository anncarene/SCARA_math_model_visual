from typing                                     import Callable, Dict, List, Tuple
from zope.interface                             import implementer, provider

from interfaces.actions.AnimationSettingsWindow import *

from config                                     import INTERFACE_EXCEPTIONS_MODE

from backend.InterfaceVerificator               import *
from backend.Exceptions                         import *
from backend.MathFuncsForVisual                 import *
from backend.AdditionalFuncs                    import *

@InterfaceVerificator.except_if_not_provides(
    INTERFACE_EXCEPTIONS_MODE,
    IAnimationSettingsWindowActionsFactory
)
@InterfaceVerificator.except_if_not_implements(
    INTERFACE_EXCEPTIONS_MODE,
    IAnimationSettingsWindowActions
)
@provider(IAnimationSettingsWindowActionsFactory)
@implementer(IAnimationSettingsWindowActions)
class AnimationSettingsWindowActions():
    
    def __init__(
        self,
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
        set_mp_x_list_entry_text:                   Callable[[str], None],
        set_mp_y_list_entry_text:                   Callable[[str], None],
        set_mp_widgets_state:                       Callable[[str], None],
        mp_anim_settings_window_init:               Callable[[], None]
    ):
        self.__set_show_prev_path_btn_state             = set_show_prev_path_btn_state
        self.__set_entries_state                        = set_entries_state
        self.__set_start_btns_state                     = set_start_btns_state
        self.__set_radio_btns_state                     = set_radio_btns_state
        
        self.__set_main_window_x_entry_text             = set_main_window_x_entry_text
        self.__set_main_window_y_entry_text             = set_main_window_y_entry_text
        
        self.__start_animation                          = start_animation
        
        self.__anim_settings_window_dismiss             = anim_settings_window_dismiss
        
        self.__set_a_value                              = set_a_value
        self.__set_outputs                              = set_outputs
        self.__set_xy_values                            = set_xy_values
        self.__set_x2y2_values                          = set_x2y2_values
        
        self.__set_anim_settings_window_M1_entries_text = set_anim_settings_window_M1_entries_text
        self.__set_anim_settings_window_entry_x2_text   = set_anim_settings_window_entry_x2_text
        self.__set_anim_settings_window_entry_y2_text   = set_anim_settings_window_entry_y2_text
        
        self.__set_prev_path_coords                     = set_prev_path_coords
        
        self.__set_mp_x_list_entry_text                 = set_mp_x_list_entry_text
        self.__set_mp_y_list_entry_text                 = set_mp_y_list_entry_text
        
        self.__set_mp_widgets_state                     = set_mp_widgets_state

        self.__mp_anim_settings_window_init             = mp_anim_settings_window_init

        self.set_moving_mode                            = set_moving_mode
        self.err_window_init                            = err_window_init
        self.get_app_state                              = get_app_state

    def show_mp_settings_btn_click(self) -> None:
        self.__mp_anim_settings_window_init()

    def xm1_entry_key_release(self, text: str) -> None: 
        self.__set_main_window_x_entry_text(text)
    
    def ym1_entry_key_release(self, text: str) -> None: 
        self.__set_main_window_y_entry_text(text)

    def xm2_entry_key_release(self, text: str) -> None:
        self.__set_anim_settings_window_entry_x2_text(text)
    
    def ym2_entry_key_release(self, text: str) -> None:
        self.__set_anim_settings_window_entry_y2_text(text)

    def anim_start_btn_click(self, mode: str, entries: Dict[str, str]) -> None: 
        if mode is None:
            raise AnimationCalcException("Не установлен режим перемещения")

        if AdditionalFuncs.is_entry_valid(self.get_app_state()["a_entry_text"]) is not True:
            raise NotNumberEntryException("В одном или нескольких полях введены не числа")

        AdditionalFuncs.primal_entries_validation(entries)

        if AdditionalFuncs.is_entry_valid(
            self.get_app_state()["a_entry_text"]
        ) is not True:
            raise NotNumberEntryException("В поле ввода длины плеча введено не число")
        
        self.__set_a_value(float(self.get_app_state()["a_entry_text"]))

        xm1 = float(entries["xm1"])
        xm2 = float(entries["xm2"])
        ym1 = float(entries["ym1"])
        ym2 = float(entries["ym2"])
     
        if self.get_app_state()["plot_figure_calced"] is not True:
            raise AnimationCalcException("Сначала нужно рассчитать график")

        frames = MathFuncsForVisual.generate_animation_frames(
            xm1 = xm1,
            xm2 = xm2,
            ym1 = ym1,
            ym2 = ym2,
            mode = mode
        )

        AdditionalFuncs.check_animation_frames(
            frames,
            self.get_app_state()["a"]
        )

        self.__set_xy_values(x = xm1, y = ym1)
        self.__set_x2y2_values(x = xm2, y = ym2)

        self.__set_entries_state("disabled")
        self.__set_radio_btns_state("disabled")
        self.__set_start_btns_state("disabled")
        self.__set_show_prev_path_btn_state("disabled")
        self.__set_mp_widgets_state("disabled")

        self.__set_prev_path_coords(frames)
        self.__start_animation(frames)

    def destroy(self) -> None: 
        self.__anim_settings_window_dismiss()

    def set_values_after_animaion(self, xm2: float, ym2: float) -> None:
            outputs = AdditionalFuncs.calc_outputs({
                "x": xm2,
                "y": ym2,
                "a": self.get_app_state()["a"]
            })
            
            self.__set_anim_settings_window_M1_entries_text(str(xm2), str(ym2))
            self.__set_main_window_x_entry_text(str(xm2))
            self.__set_main_window_y_entry_text(str(ym2))
            self.__set_mp_x_list_entry_text(str(xm2))
            self.__set_mp_y_list_entry_text(str(ym2))
            self.__set_outputs(outputs)
    
    def unblock_widgets(self) -> None:    
        self.__set_entries_state("normal")
        self.__set_radio_btns_state("normal")
        self.__set_start_btns_state("normal")
        self.__set_show_prev_path_btn_state("normal")
        self.__set_mp_widgets_state("normal")