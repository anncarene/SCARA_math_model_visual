from tkinter                                            import *
from tkinter                                            import ttk
from zope.interface                                     import implementer, provider

from interfaces.components.MP_AnimationSettingsWindow   import *

from actions.MP_AnimationSettingsWindow                 import *

from config                                             import INTERFACE_EXCEPTIONS_MODE

from backend.InterfaceVerificator                       import *

@InterfaceVerificator.except_if_not_provides(
    INTERFACE_EXCEPTIONS_MODE,
    IMP_AnimationSettingsWindowFactory
)
@InterfaceVerificator.except_if_not_implements(
    INTERFACE_EXCEPTIONS_MODE,
    IMP_AnimationSettingsWindow
)
@provider(IMP_AnimationSettingsWindowFactory)
@implementer(IMP_AnimationSettingsWindow)
class MP_AnimationSettingsWindow(Tk):
    """
        Класс, экземпляром которого является окно с настройками анимации
        для перемещения по нескольким точкам
    """

    def __init__(
        self, 
        actions: MP_AnimationSettingsWindowActions
    ):
        super().__init__()
        
        #конфигурация окна
        self.title("Настройки анимации по нескольким точкам")
        self.geometry("250x450")
        self.protocol("WM_DELETE_WINDOW", lambda: actions.destroy())
        
        #конфигурация сетки
        for i in range(2): self.columnconfigure(index=i, weight=1)
        for i in range(11): self.rowconfigure(index=i, weight=1)

        #обработчик событий
        self.actions = actions

        #элементы
        self.x_label = ttk.Label(self, text="x = ")
        self.x_list_entry = ttk.Entry(self)

        self.y_label = ttk.Label(self, text="y = ")
        self.y_list_entry = ttk.Entry(self)

        self.desc_codes_label = ttk.Label(self, text="Коды режимов перемещения")
        self.radial_code_label = ttk.Label(self, text="Радиальный - 1")
        self.linear_code_label = ttk.Label(self, text="Линейный - 2")
        self.integral_code_label = ttk.Label(self, text="Интегральный - 3")

        self.moving_mode_list_label = ttk.Label(self, text="Режимы перемещения: ")
        self.moving_mode_list_entry = ttk.Entry(self)

        self.clear_btn = ttk.Button(
            self,
            text="Очистить поля",
            command=self.__on_mp_clear_btn_click
        )
        self.start_btn = ttk.Button(
            self,
            text="Начать анимацию",
            command=self.__on_mp_start_btn_click
        )

        #начальное состояние элементов
        self.x_list_entry["state"]              = [actions.get_app_state()["mp_entries_state"]]
        self.y_list_entry["state"]              = [actions.get_app_state()["mp_entries_state"]]
        self.moving_mode_list_entry["state"]    = [actions.get_app_state()["mp_entries_state"]]
        self.start_btn["state"]                 = [actions.get_app_state()["mp_btns_state"]]
        self.clear_btn["state"]                 = [actions.get_app_state()["mp_btns_state"]]

        self.__insert_initial_values()

        #начальная привязка событий
        self.x_list_entry.bind("<FocusIn>", self.__on_mp_x_list_entry_focus_in)
        self.x_list_entry.bind("<FocusOut>", self.__on_mp_x_list_entry_focus_out)

        self.y_list_entry.bind("<FocusIn>", self.__on_mp_y_list_entry_focus_in)
        self.y_list_entry.bind("<FocusOut>", self.__on_mp_y_list_entry_focus_out)

        self.moving_mode_list_entry.bind(
            "<FocusIn>", 
            self.__on_mp_moving_mode_list_focus_in
        )
        self.moving_mode_list_entry.bind(
            "<FocusOut>",
            self.__on_mp_moving_mode_list_focus_out
        )

        #позиционирование
        elements_list = [
            [self.x_label, self.x_list_entry],
            [self.y_label, self.y_list_entry]
        ]

        for i in range(len(elements_list)):
            for j in range(2):
                elements_list[i][j].grid(row=i, column=j)

        elements_list = [
            self.desc_codes_label,
            self.radial_code_label,
            self.linear_code_label,
            self.integral_code_label,
            self.moving_mode_list_label,
            self.moving_mode_list_entry,
            self.clear_btn,
            self.start_btn
        ]

        for i in range(2, 10): elements_list[i - 2].grid(
            row=i,
            column=0,
            rowspan=1,
            columnspan=2
        )

    def __insert_initial_values(self) -> None:
        if (
            self.actions.get_app_state()["mp_x_list_entry_text"] is None or
            self.actions.get_app_state()["mp_x_list_entry_text"] == ""
        ):
            self.x_list_entry.insert(0, self.actions.get_app_state()["xm1_entry_text"])
        else:
            self.x_list_entry.insert(0, self.actions.get_app_state()["mp_x_list_entry_text"])
        
        if (
            self.actions.get_app_state()["mp_y_list_entry_text"] is None or
            self.actions.get_app_state()["mp_y_list_entry_text"] == ""
        ):
            self.y_list_entry.insert(0, self.actions.get_app_state()["ym1_entry_text"])
        else:
            self.y_list_entry.insert(0, self.actions.get_app_state()["mp_y_list_entry_text"])
        
        if (
            self.actions.get_app_state()["mp_moving_mode_list_entry_text"] is not None and
            self.actions.get_app_state()["mp_moving_mode_list_entry_text"] != ""
        ):
            self.moving_mode_list_entry.insert(0, self.actions.get_app_state()["mp_x_list_entry_text"])

    def __on_mp_x_list_entry_focus_in(self, event: Event) -> None: 
        self.x_list_entry.bind("<KeyRelease>", self.__on_mp_x_list_entry_key_release)
    
    def __on_mp_x_list_entry_focus_out(self, event: Event) -> None:
        self.x_list_entry.unbind("<KeyRelease>")
    
    def __on_mp_y_list_entry_focus_in(self, event: Event) -> None:
        self.y_list_entry.bind("<KeyRelease>", self.__on_mp_y_list_entry_key_release)

    def __on_mp_y_list_entry_focus_out(self, event: Event) -> None:
        self.y_list_entry.unbind("<KeyRelease>")
    
    def __on_mp_moving_mode_list_focus_in(self, event: Event) -> None:
        self.moving_mode_list_entry.bind("<KeyRelease>", self.__on_mp_moving_mode_list_entry_key_release)

    def __on_mp_moving_mode_list_focus_out(self, event: Event) -> None:
        self.moving_mode_list_entry.unbind("<KeaRelease>")

    def __on_mp_x_list_entry_key_release(self, event: Event) -> None:
        self.actions.mp_x_list_entry_key_release(
            text = self.x_list_entry.get()
        )

    def __on_mp_y_list_entry_key_release(self, event: Event) -> None:
        self.actions.mp_y_list_entry_key_release(
            text = self.y_list_entry.get()
        )
    
    def __on_mp_moving_mode_list_entry_key_release(self, event: Event) -> None:
        self.actions.mp_moving_mode_list_entry_key_release(
            text = self.moving_mode_list_entry.get()
        )
    
    def __on_mp_clear_btn_click(self) -> None:
        self.actions.mp_clear_btn_click()

    def __on_mp_start_btn_click(self) -> None: 
        try:
            self.actions.mp_start_btn_click(
                entries = {
                    "x_list": self.x_list_entry.get(),
                    "y_list": self.y_list_entry.get(),
                    "moving_mode_list": self.moving_mode_list_entry.get()
                }
            )
            
            sub_animations_num = len(self.actions.get_app_state()["mp_moving_mode_list"])
            
            self.after(
                5000 * sub_animations_num,
                self.actions.unblock_widgets
            )
            self.after(
                5050 * sub_animations_num,
                self.actions.set_values_after_animation
            )
        except (
            NotNumberEntryException,
            ConvertingException,
            AnimationCalcException
        ) as err:
            self.actions.err_window_init(err)
