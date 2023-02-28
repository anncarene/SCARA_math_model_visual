from typing                         import List
from zope.interface                 import implementer

from interfaces.State               import *

from config                         import INTERFACE_EXCEPTIONS_MODE

from backend.InterfaceVerificator   import *

@InterfaceVerificator.except_if_not_implements(
    INTERFACE_EXCEPTIONS_MODE,
    IState
)
@implementer(IState)
class State():
    """Класс, экземпляр которого хранит глобальные переменные состояния приложения."""

    def __init__(self):
        self.r:             float   = None
        self.a:             float   = None
        self.phi:           float   = None
        self.psi:           float   = None
        self.teta:          float   = None
        
        self.xm1:           float   = None
        self.ym1:           float   = None
        self.xm2:           float   = None
        self.ym2:           float   = None

        self.anim_settings_window_entries_state:    str = "normal"
        self.anim_settings_window_radio_btns_state: str = "normal"
        self.anim_settings_window_start_btn_state:  str = "normal"

        self.xm1_entry_text:    str = ""
        self.ym1_entry_text:    str = ""

        self.xm2_entry_text:    str = ""
        self.ym2_entry_text:    str = ""

        self.a_entry_text:      str = ""

        self.moving_mode:       str = None

        self.anim_settings_window_opened:   bool = False
        self.plot_figure_calced:            bool = False
        self.prev_path_showed:              bool = False

        self.prev_path_x_coords: List[float] = []
        self.prev_path_y_coords: List[float] = []