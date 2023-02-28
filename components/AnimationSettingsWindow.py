from tkinter                                        import *
from tkinter                                        import ttk
from tkinter                                        import Event
from zope.interface                                 import implementer
from interfaces.components.AnimationSettingsWindow  import *

from actions.AnimationSettingsWindow                import *

from config                                         import INTERFACE_EXCEPTIONS_MODE

from backend.InterfaceVerificator                   import *

@InterfaceVerificator.except_if_not_implements(
    INTERFACE_EXCEPTIONS_MODE,
    IAnimationSettingsWindow
)
@implementer(IAnimationSettingsWindow)
class AnimationSettingsWindow(Tk):
    """
        AnimationSettingsWindow - класс окна с настройками анимации. Экземпляр
        класса в обязательном порядке единовременно может быть только один
    """

    def __init__(
        self,
        actions:        AnimationSettingsWindowActions,
    ):
        super().__init__()

        #конфигурация окна
        self.title("Настройки анимации")
        self.geometry("250x400")
        self.protocol("WM_DELETE_WINDOW", lambda: actions.destroy())

        #конфигурация сетки
        for i in range(2): self.columnconfigure(index=i, weight=1)
        for i in range(9): self.rowconfigure(index=i, weight=1)
        
        #обработчик событий
        self.actions            = actions

        #элементы
        self.xm1_label          = ttk.Label(self, text="x(M1) = ")
        self.xm1_entry          = ttk.Entry(self)

        self.ym1_label          = ttk.Label(self, text="y(M1) = ")
        self.ym1_entry          = ttk.Entry(self)

        self.xm2_label          = ttk.Label(self, text="x(M2) = ")
        self.xm2_entry          = ttk.Entry(self)

        self.ym2_label          = ttk.Label(self, text="y(M2) = ")
        self.ym2_entry          = ttk.Entry(self)

        self.radio_btns_label   = ttk.Label(self, text="Режим перемещений:")
        
        self.radial_mode_btn = ttk.Radiobutton(
            self,
            text = "Радиальный",
            command = self.__set_radial_mode
        )
        self.linear_mode_btn = ttk.Radiobutton(
            self,
            text = "Линейный",
            command = self.__set_linear_mode
        )
        self.integral_mode_btn = ttk.Radiobutton(
            self,
            text = "Интегральный",
            command = self.__set_integral_mode
        )
        self.anim_start_btn = ttk.Button(
            self, 
            text = "Начать анимацию", 
            command = self.__on_anim_start_btn_click
        )

        #начальное состояние элементов
        self.xm1_entry["state"] = [actions.get_app_state()["anim_settings_window_entries_state"]]
        self.ym1_entry["state"] = [actions.get_app_state()["anim_settings_window_entries_state"]]
        self.xm2_entry["state"] = [actions.get_app_state()["anim_settings_window_entries_state"]]
        self.ym2_entry["state"] = [actions.get_app_state()["anim_settings_window_entries_state"]]

        self.radial_mode_btn["state"]   = [actions.get_app_state()["anim_settings_window_radio_btns_state"]]
        self.linear_mode_btn["state"]   = [actions.get_app_state()["anim_settings_window_radio_btns_state"]]
        self.integral_mode_btn["state"]  = [actions.get_app_state()["anim_settings_window_radio_btns_state"]]

        self.anim_start_btn["state"] = [actions.get_app_state()["anim_settings_window_start_btn_state"]]

        self.xm1_entry.insert(0, actions.get_app_state()["xm1_entry_text"])
        self.ym1_entry.insert(0, actions.get_app_state()["ym1_entry_text"])
        self.xm2_entry.insert(0, actions.get_app_state()["xm2_entry_text"])
        self.ym2_entry.insert(0, actions.get_app_state()["ym2_entry_text"])

        #другие поля класса
        self.mode = actions.get_app_state()["moving_mode"]
        
        #начальная привязка событий             
        self.xm1_entry.bind("<FocusIn>", self.__on_xm1_entry_focus_in)
        self.xm1_entry.bind("<FocusOut>", self.__on_xm1_entry_focus_out)

        self.ym1_entry.bind("<FocusIn>", self.__on_ym1_entry_focus_in)
        self.ym1_entry.bind("<FocusOut>", self.__on_ym1_entry_focus_out)

        self.xm2_entry.bind("<FocusIn>", self.__on_xm2_entry_focus_in)
        self.xm2_entry.bind("<FocusOut>", self.__on_xm2_entry_focus_out)

        self.ym2_entry.bind("<FocusIn>", self.__on_ym2_entry_focus_in)
        self.ym2_entry.bind("<FocusOut>", self.__on_ym2_entry_focus_out)

        #позиционирование
        elements_list = [
            [self.xm1_label, self.xm1_entry],
            [self.ym1_label, self.ym1_entry],
            [self.xm2_label, self.xm2_entry],
            [self.ym2_label, self.ym2_entry]
        ]

        for i in range(len(elements_list)):
            for j in range(2):
                elements_list[i][j].grid(row=i, column=j)

        elements_list = [
            self.radio_btns_label,
            self.radial_mode_btn,
            self.linear_mode_btn,
            self.integral_mode_btn,
            self.anim_start_btn
        ]

        for i in range(4, 9): elements_list[i - 4].grid(
            row=i,
            column=0,
            rowspan=1,
            columnspan=2
        )

    def __set_linear_mode(self) -> None:
        self.mode = "linear"
        self.actions.set_moving_mode("linear")

    def __set_radial_mode(self) -> None:
        self.mode = "radial"
        self.actions.set_moving_mode("radial")

    def __set_integral_mode(self) -> None:
        self.mode = "integral"
        self.actions.set_moving_mode("integral")

    def __on_anim_start_btn_click(self) -> None:
        try:
            self.actions.anim_start_btn_click(
                mode = self.mode,
                entries = {
                    "xm1": self.xm1_entry.get(),
                    "ym1": self.ym1_entry.get(),
                    "xm2": self.xm2_entry.get(),
                    "ym2": self.ym2_entry.get()
                }
            )
            self.after(
                6050, 
                lambda: self.actions.set_values_after_animaion(
                    float(self.xm2_entry.get()), 
                    float(self.ym2_entry.get())
                )
            )
            self.after(6000, self.actions.unblock_widgets)
        
        except (
            NotNumberEntryException,
            ConvertingException,
            AnimationCalcException
        ) as err:
            self.actions.err_window_init(err)


    def __on_xm1_entry_key_release(self, event: Event) -> None:
        self.actions.xm1_entry_key_release(
            text = self.xm1_entry.get()
        )

    def __on_ym1_entry_key_release(self, event: Event) -> None:
        self.actions.ym1_entry_key_release(
            text = self.ym1_entry.get()
        )
    
    def __on_xm2_entry_key_release(self, event: Event) -> None:
        self.actions.xm2_entry_key_release(
            text = self.xm2_entry.get()
        )

    def __on_ym2_entry_key_release(self, event: Event) -> None:
        self.actions.ym2_entry_key_release(
            text = self.ym2_entry.get()
        )

    def __on_xm1_entry_focus_in(self, event: Event) -> None:
        self.xm1_entry.bind("<KeyRelease>", self.__on_xm1_entry_key_release)

    def __on_ym1_entry_focus_in(self, event: Event) -> None:
        self.ym1_entry.bind("<KeyRelease>", self.__on_ym1_entry_key_release)

    def __on_xm2_entry_focus_in(self, event: Event) -> None:
        self.xm2_entry.bind("<KeyRelease>", self.__on_xm2_entry_key_release)

    def __on_ym2_entry_focus_in(self, event: Event) -> None:
        self.ym2_entry.bind("<KeyRelease>", self.__on_ym2_entry_key_release)

    def __on_xm1_entry_focus_out(self, event: Event) -> None:
        self.xm1_entry.unbind("<KeyRelease>")    

    def __on_ym1_entry_focus_out(self, event: Event) -> None:
        self.ym1_entry.unbind("<KeyRelease>")
        
    def __on_xm2_entry_focus_out(self, event: Event) -> None:
        self.xm2_entry.unbind("<KeyRelease>")
    
    def __on_ym2_entry_focus_out(self, event: Event) -> None:
        self.ym2_entry.unbind("<KeyRelease>")