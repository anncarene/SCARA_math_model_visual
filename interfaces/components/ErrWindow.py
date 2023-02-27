from zope.interface import Interface, Attribute

class IErrWindow(Interface):
    """Интерфейс, реализуемый классом ErrWindow."""
    
    """Поля"""
    label           = Attribute("Текст сообщения об ошибке")
    
    """Методы"""
    def dismiss(): pass