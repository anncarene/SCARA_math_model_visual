from zope.interface         import implementer
from tkinter                import *
from tkinter                import ttk

from ErrWindowInterfaces    import *

@implementer(IErrWindow)
class ErrWindow(Toplevel):
    """ErrWindow - класс, реализующий диалоговое окно, появляющееся при ошибочно введенных данных"""
    
    def __init__(self, *args):
        super().__init__()
        
        self.title("Ошибка")
        self.geometry("750x50")
        
        self.protocol("WM_DELETE_WINDOW", lambda: self.dismiss())
        
        self.label = ttk.Label(text=args[0], master=self, font=("Arial", 14))
        self.label.pack(anchor="center", expand=1)
        self.grab_set()
        
    def dismiss(self) -> None:
        """Расфокус окна с ошибкой и его уничтожение"""
        
        self.grab_release()
        self.destroy()