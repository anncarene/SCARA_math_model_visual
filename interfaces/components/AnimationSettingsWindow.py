from zope.interface                     import Interface, Attribute

from actions.AnimationSettingsWindow    import *

class IAnimationSettingsWindowFactory(Interface):
    """Интерфейс, предоставляемый классом AnimationSettingsWindow"""

    def __call__(actions: AnimationSettingsWindowActions): pass

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
    show_mp_settings_btn    = Attribute("Кнопка, открывающая окно с расширенными настройками анимации")

    mode                    = Attribute("Режим перемещения")