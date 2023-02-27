from zope.interface import Interface, Attribute

class IState(Interface):
    """Интерфейс, реализуемый классом State"""

    """Поля"""
    
    r           = Attribute("Радуис текущей точки M в полярной системе координат")
    a           = Attribute("Текущее заданное значение длины ребра")
    phi         = Attribute("Текущий угол phi точки M в полярной системе координат")
    psi         = Attribute("Текущее значение psi")
    teta        = Attribute("Текущее значение teta")
    xm1         = Attribute("Текущее значение xm1")
    xm2         = Attribute("Текущее значение xm2")
    ym1         = Attribute("Текущее значение ym1")
    ym2         = Attribute("Текущее значение ym2")
    
    anim_settings_window_opened = Attribute("Открыто ли окно с настройками анмимации")
    plot_figure_calced          = Attribute("Рассчитан ли привод")
    prev_path_showed            = Attribute("Показан ли последний маршрут привода")

    xm1_entry_text  = Attribute("Текст в поле ввода xm1")
    ym1_entry_text  = Attribute("Текст в поле ввода ym1")

    xm2_entry_text  = Attribute("Текст в поле ввода xm2")
    ym2_entry_text  = Attribute("Текст в поле ввода ym2")

    a_entry_text    = Attribute("Текст в поле ввода a")
    
    moving_mode     = Attribute("Текущий режим перемещения")

    anim_settings_window_entries_state      = Attribute("State полей ввода окна настроек анимации")
    anim_settings_window_radio_btns_state   = Attribute("State радиокнопок окна ввода настроек анимации")
    anim_settings_window_start_btn_state    = Attribute("State кнопки старта анимации")

    prev_path_x_coords = Attribute("Список значний x последнего маршрута")
    prev_path_y_coords = Attribute("Список значний y последнего маршрута")