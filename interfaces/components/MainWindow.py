from tkinter                import Event
from zope.interface         import Interface, Attribute

class IMainWindow(Interface):
    """Интерфейс, реализуемый классом MainWindow"""
    
    """Поля"""
    actions                     = Attribute("Обработчик событий")
    
    plot_picture                = Attribute("Объект графика")

    a_label                     = Attribute("Метка a=")
    x_label                     = Attribute("Метка x=")
    y_label                     = Attribute("Метка y=")
    
    a_entry                     = Attribute("Поле ввода для a")
    x_entry                     = Attribute("Поле ввода для x")
    y_entry                     = Attribute("Поле ввода для y")

    r_label                     = Attribute("Метка r=")
    phi_label                   = Attribute("Метка phi=")
    psi_label                   = Attribute("Метка psi=")
    
    r_value_label               = Attribute("Метка с рассчитанным значением r")
    phi_value_label             = Attribute("Метка с рассчитанным значением phi")
    psi_value_label             = Attribute("Метка с рассчитанным значением psi")

    show_prev_path_btn          = Attribute("Показать/скрыть последний маршрут привода")
    calcbtn                     = Attribute("Кнопка расчета графика")
    anim_settings_btn           = Attribute("Кнопка настроек анимации")

    canvas                      = Attribute("Объект Canvas с визуализацией. Либо просто пустой")

    """Методы"""
    def draw_canvas() -> None: pass