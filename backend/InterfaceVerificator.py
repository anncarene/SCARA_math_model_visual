from abc                    import ABCMeta
from zope.interface         import Invalid
from zope.interface.verify  import verifyObject, verifyClass
from typing                 import Literal, Callable

class InterfaceVerificator():
    """
        Абстрактный класс, содержащий в себе приверку реализации / предоставления
        классом интерфейса
    """

    __metaclass__: ABCMeta

    @staticmethod
    def except_if_not_implements(
        mode: Literal['logging', 'strict'],
        interface: any
    ) -> Callable:
        pass
        def decorator(interface_implementer: Callable) -> Callable:
            match mode:
                case 'logging':
                    try:
                        verifyClass(interface, interface_implementer)
                    except Invalid as err:
                        print(str(err))
                case 'strict':
                    verifyClass(interface, interface_implementer)
            return interface_implementer
        return decorator
    
    @staticmethod
    def except_if_not_provides(
        mode: Literal['logging', 'strict'],
        interface: any
    ) -> Callable:
        pass
        def decorator(interface_implementer: Callable) -> Callable:
            match mode:
                case 'logging':
                    try:
                        verifyObject(interface, interface_implementer)
                    except Invalid as err:
                        print(str(err))
                case 'strict':
                    verifyObject(interface, interface_implementer)
            return interface_implementer
        return decorator
