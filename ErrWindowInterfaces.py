from zope.interface import Interface, Attribute

class IErrWindow(Interface):
    """Интерфейс, реализуемый классом ErrWindow."""
    
    """Поля"""
    title           = Attribute("Заголовок окна")
    geometry        = Attribute("Геометрия")
    label           = Attribute("Текст сообщения об ошибке")
    
    def dismiss(self):
        """"""