from tkinter        import Event
from zope.interface import Interface, Attribute

class IAnimationSettingsWindow(Interface):
    """Интерфейс, реализуемый классом AnimationSettingsWindow"""

    """Поля"""
    actions                 = Attribute("Обработчик событий")

    xm1_label               = Attribute("Метка xm1=")
    ym1_label               = Attribute("Метка ym1=")
    xm2_label               = Attribute("Метка xm2=")    
    ym2_label               = Attribute("Метка ym2=")

    xm1_entry               = Attribute("Поле ввода для xm1")
    ym1_entry               = Attribute("Поле ввода для ym1")
    xm2_entry               = Attribute("Поле ввода для xm2")
    ym2_entry               = Attribute("Поле ввода для ym2")

    radio_btns_label        = Attribute("Метка-заголовок перед радио-кнопками")
    radial_mode_btn         = Attribute("Переключатель на радиальный режим перемещения")
    linear_mode_btn         = Attribute("Переключатель на линейный режим перемещения")
    integral_mode_btn       = Attribute("Переключатель на интегральный режим пермещения")

    anim_start_btn          = Attribute("Кнопка старта анимации")

    mode                    = Attribute("Режим перемещения")

    """Методы"""
    def __set_linear_mode() -> None: pass
    def __set_radial_mode() -> None: pass
    def __set_integral_mode() -> None: pass
    def __on_anim_start_btn_click() -> None: pass
    def __on_xm1_entry_key_release(event: Event) -> None: pass
    def __on_ym1_entry_key_release(event: Event) -> None: pass
    def __on_xm2_entry_key_release(event: Event) -> None: pass
    def __on_ym2_entry_key_release(event: Event) -> None: pass
    def __on_xm1_entry_focus_in(event: Event) -> None: pass
    def __on_ym1_entry_focus_in(event: Event) -> None: pass
    def __on_xm2_entry_focus_in(event: Event) -> None: pass
    def __on_ym2_entry_focus_in(event: Event) -> None: pass
    def __on_xm1_entry_focus_out(event: Event) -> None: pass
    def __on_ym1_entry_focus_out(event: Event) -> None: pass
    def __on_xm2_entry_focus_out(event: Event) -> None: pass
    def __on_ym2_entry_focus_out(event: Event) -> None: pass