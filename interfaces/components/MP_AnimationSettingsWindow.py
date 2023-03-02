from zope.interface                     import Interface, Attribute

from actions.MP_AnimationSettingsWindow import *

class IMP_AnimationSettingsWindowFactory(Interface):
    """Интерфейс, предоставляемый классом MP_AnimationSettingsWindow"""

    def __call__(actions: MP_AnimationSettingsWindowActions): pass

class IMP_AnimationSettingsWindow(Interface):
    """Интерфейс, реализуемый классом MP_AnimationSettingsWindow"""

    actions                 = Attribute("Обработчик событий")
    
    x_label                 = Attribute("Метка x = ")
    x_list_entry            = Attribute("Поле ввода для значений x")

    y_label                 = Attribute("Метка y = ")
    y_list_entry            = Attribute("Поле ввода для значений y")

    desc_codes_label        = Attribute("Метка-дескриптор")
    radial_code_label       = Attribute("Метка для кода режима перемещения")
    linear_code_label       = Attribute("Метка для кода режима перемещения")
    integral_code_label     = Attribute("Метка для кода режима перемещения")
    
    moving_mode_list_label  = Attribute("Метка для поля ввода кодов режимов перемещения")
    moving_mode_list_entry  = Attribute("Поле ввода для режимов перемещения")
    
    clear_btn               = Attribute("Кнопка очистки полей")
    start_btn               = Attribute("Кнопка запуска анимации")