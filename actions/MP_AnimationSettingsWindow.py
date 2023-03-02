from typing                                         import Callable, Dict, List, Tuple
from zope.interface                                 import implementer, provider

from interfaces.actions.MP_AnimationSettingsWindow  import *

from config                                         import INTERFACE_EXCEPTIONS_MODE

from backend.InterfaceVerificator                   import *
from backend.Exceptions                             import *
from backend.AdditionalFuncs                        import *
from backend.MathFuncsForVisual                     import *

@InterfaceVerificator.except_if_not_provides(
    INTERFACE_EXCEPTIONS_MODE,
    IMP_AnimationSettingsWindowActionsFactory
)
@InterfaceVerificator.except_if_not_implements(
    INTERFACE_EXCEPTIONS_MODE,
    IMP_AnimationSettingsWindowActions
)
@provider(IMP_AnimationSettingsWindowActionsFactory)
@implementer(IMP_AnimationSettingsWindowActions)
class MP_AnimationSettingsWindowActions():
    
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
                ConvertingException | NotNumberEntryException | AnimationCalcException
            ],
            None
        ],
        set_a_value:                                Callable[[float], None],
        set_outputs:                                Callable[[Dict[str, float]], None],
        set_xy_values:                              Callable[[float, float], None],
        set_x2y2_values:                            Callable[[float, float], None],
        set_prev_path_coords:                       Callable[[List[Tuple[float, float]]], None],
        set_show_prev_path_btn_state:               Callable[[str], None],
        set_anim_settings_window_M1_entries_text:   Callable[[str, str], None],
        mp_anim_settings_window_dismiss:            Callable[[], None],
        set_mp_x_list:                              Callable[[List[float]], None],
        set_mp_y_list:                              Callable[[List[float]], None],
        set_mp_moving_mode_list:                    Callable[[List[int]], None],        
        set_mp_x_list_entry_text:                   Callable[[str], None],
        set_mp_y_list_entry_text:                   Callable[[str], None],
        set_mp_moving_mode_list_entry_text:         Callable[[str], None],
        set_mp_widgets_state:                       Callable[[str], None]
    ):
        self.__set_entries_state                        = set_entries_state
        self.__set_start_btns_state                     = set_start_btns_state
        self.__set_radio_btns_state                     = set_radio_btns_state
        self.__set_main_window_x_entry_text             = set_main_window_x_entry_text
        self.__set_main_window_y_entry_text             = set_main_window_y_entry_text
        self.__start_animation                          = start_animation
        self.__set_a_value                              = set_a_value
        self.__set_outputs                              = set_outputs
        self.__set_xy_values                            = set_xy_values
        self.__set_x2y2_values                          = set_x2y2_values
        self.__set_prev_path_coords                     = set_prev_path_coords
        self.__set_show_prev_path_btn_state             = set_show_prev_path_btn_state
        self.__set_anim_settings_window_M1_entries_text = set_anim_settings_window_M1_entries_text
        self.__mp_anim_settings_window_dismiss          = mp_anim_settings_window_dismiss
        self.__set_mp_x_list                            = set_mp_x_list
        self.__set_mp_y_list                            = set_mp_y_list
        self.__set_mp_moving_mode_list                  = set_mp_moving_mode_list
        self.__set_mp_x_list_entry_text                 = set_mp_x_list_entry_text
        self.__set_mp_y_list_entry_text                 = set_mp_y_list_entry_text
        self.__set_mp_moving_mode_list_entry_text       = set_mp_moving_mode_list_entry_text
        self.__set_mp_widgets_state                     = set_mp_widgets_state

        self.get_app_state      = get_app_state
        self.err_window_init    = err_window_init

    def __split_entries_text(self, entries: Dict[str, str]) -> Dict[str, List[str]]:
        
        split_entries = {
            "x_list": [],
            "y_list": [],
            "moving_mode_list": []
        }
        for key in entries:
            split_entries[key] = entries[key].split(",")
            for i in range(len(split_entries[key])):
                split_entries[key][i] = split_entries[key][i].strip()
        
        return split_entries

    def __split_entries_validation(self, split_entries: Dict[str, List[str]]) -> None: 
        
        for key in split_entries:
            for i in range(len(split_entries[key])):
                if split_entries[key][i] == "":
                    raise NotNumberEntryException(
                        "Списки чисел введены в неправильном формате"
                    )
        
        for key in split_entries:
            for i in range(len(split_entries[key])):
                if AdditionalFuncs.is_entry_valid(split_entries[key][i]) is not True:
                    raise NotNumberEntryException(
                        "В одном или нескольких полях введены не числа"
                    )
                
        if (
            len(split_entries["x_list"]) != len(split_entries["y_list"]) or
            len(split_entries["x_list"]) - 1 != len(split_entries["moving_mode_list"])
        ):
            raise AnimationCalcException(
                "Не для всех точек введены все данные"
            )
        
        if (len(split_entries["x_list"]) == 1):
            raise AnimationCalcException(
                "Для построения анимации нужны по крайней мере 2 точки"
            )

    def __moving_mode_final_validation(self, moving_mode_list: List[int]) -> None:
        for i in range(len(moving_mode_list)):
            match moving_mode_list[i]:
                case 1: pass
                case 2: pass
                case 3: pass
                case _:
                    raise AnimationCalcException(
                        "Одно или больше недопустимых значений кода режима перемещений"
                    )

    def __moving_mode_str_list(self, moving_mode_list: List[int]) -> List[str]:
        moving_mode_str_list = []
        
        for i in range(len(moving_mode_list)):
            match moving_mode_list[i]:
                case 1: moving_mode_str_list.append("radial")
                case 2: moving_mode_str_list.append("linear")
                case 3: moving_mode_str_list.append("integral")
        
        return moving_mode_str_list

    def mp_x_list_entry_key_release(self, text: str) -> None:
        self.__set_mp_x_list_entry_text(text)

    def mp_y_list_entry_key_release(self, text: str) -> None:
        self.__set_mp_y_list_entry_text(text)

    def mp_moving_mode_list_entry_key_release(self, text: str) -> None:
        self.__set_mp_moving_mode_list_entry_text(text)

    def mp_start_btn_click(self, entries: Dict[str, str]) -> None:
        
        split_entries = self.__split_entries_text(entries)
        self.__split_entries_validation(split_entries)

        if AdditionalFuncs.is_entry_valid(
            self.get_app_state()["a_entry_text"]
        ) is not True:
            raise NotNumberEntryException("В поле ввода длины плеча введено не число")
        
        self.__set_a_value(float(self.get_app_state()["a_entry_text"]))

        x_list           = []
        y_list           = []
        moving_mode_list = []

        for i in range(len(split_entries["x_list"])):
            x_list.append(float(split_entries["x_list"][i]))
            y_list.append(float(split_entries["y_list"][i]))

        for i in range(len(split_entries["moving_mode_list"])):
            moving_mode_list.append(float(split_entries["moving_mode_list"][i]))

        self.__moving_mode_final_validation(moving_mode_list)

        if self.get_app_state()["plot_figure_calced"] is not True:
            raise AnimationCalcException("Сначала нужно рассчитать график")

        moving_mode_str_list = self.__moving_mode_str_list(moving_mode_list)

        frames = []

        for i in range(len(x_list) - 1):
            frames.extend(
                MathFuncsForVisual.generate_animation_frames(
                    xm1 = x_list[i],
                    xm2 = x_list[i + 1],
                    ym1 = y_list[i],
                    ym2 = y_list[i + 1],
                    mode = moving_mode_str_list[i]
                )
            )

        AdditionalFuncs.check_animation_frames(
            frames,
            self.get_app_state()["a"]
        )

        self.__set_xy_values(x = x_list[0], y = y_list[0])
        self.__set_x2y2_values(x = x_list[-1], y = y_list[-1])
        self.__set_mp_x_list(x_list)
        self.__set_mp_y_list(y_list)
        self.__set_mp_moving_mode_list(moving_mode_list)

        self.block_other_windows_widgets()
        self.__set_mp_widgets_state("disabled")

        self.__set_prev_path_coords(frames)
        self.__start_animation(frames)

    def set_values_after_animation(self) -> None:
        x = self.get_app_state()["mp_x_list"][-1]
        y = self.get_app_state()["mp_y_list"][-1]

        self.__set_main_window_x_entry_text(x)
        self.__set_main_window_y_entry_text(y)
        
        self.__set_outputs(
            AdditionalFuncs.calc_outputs(
                {
                    "x": str(x),
                    "y": str(y),
                    "a": self.get_app_state()["a_entry_text"]
                }
            )
        )

        self.__set_anim_settings_window_M1_entries_text(str(x), str(y))

    def mp_clear_btn_click(self) -> None: 
        self.__set_mp_x_list([])
        self.__set_mp_y_list([])
        self.__set_mp_moving_mode_list([])
        self.__set_mp_x_list_entry_text("")
        self.__set_mp_y_list_entry_text("")
        self.__set_mp_moving_mode_list_entry_text("")

    def block_other_windows_widgets(self) -> None:
        self.__set_entries_state("disabled")
        self.__set_radio_btns_state("disabled")
        self.__set_start_btns_state("disabled")
        self.__set_show_prev_path_btn_state("disabled")

    def unblock_other_windows_widgets(self) -> None:
        self.__set_entries_state("normal")
        self.__set_radio_btns_state("normal")
        self.__set_start_btns_state("normal")
        self.__set_show_prev_path_btn_state("normal")        

    def unblock_widgets(self) -> None: 
        self.unblock_other_windows_widgets()
        self.__set_mp_widgets_state("normal")

    def unblock_mp_widgets(self) -> None:
        self.__set_mp_widgets_state("normal")

    def destroy(self) -> None: 
        self.__mp_anim_settings_window_dismiss()