from tkinter                            import *
from tkinter                            import ttk
from tkinter                            import Event
from matplotlib.backends.backend_tkagg  import FigureCanvasTkAgg
from zope.interface                     import implementer

from interfaces.components.MainWindow   import *

from actions.MainWindow                 import *

from backend.MathFuncsForVisual         import *
from backend.Converting                 import *
from backend.AdditionalFuncs            import *

from components.PlotPicture             import *

@implementer(IMainWindow)            
class MainWindow(Tk):   
    """
        MainWindow - класс, реализующий графическую составляющую приложения.
        В обязательном порядке должен иметь только один экземпляр
    """
    
    def __init__(self, actions: MainWindowActions, plot_picture: PlotPicture):
        super().__init__()

        #конфигурация окна        
        self.title("Визуализация")
        self.geometry("750x550")
        self.protocol("WM_DELETE_WINDOW", lambda: actions.destroy())

        #конфигурация сетки
        for i in range(6): self.columnconfigure(index=i, weight=1)
        for i in range(10): self.rowconfigure(index=i, weight=1)
        
        #обработчик событий
        self.actions            = actions

        #элементы  
        self.plot_picture       = plot_picture

        self.a_label            = ttk.Label(self, text="a = ")
        self.a_entry            = ttk.Entry(self)

        self.x_label            = ttk.Label(self, text="x = ")
        self.x_entry            = ttk.Entry(self)
        
        self.y_label            = ttk.Label(self, text="y = ")
        self.y_entry            = ttk.Entry(self)
        
        self.r_label            = ttk.Label(self, text="r = ")
        self.r_value_label      = ttk.Label(self, text="")
        
        self.phi_label          = ttk.Label(self, text="phi = ")
        self.phi_value_label    = ttk.Label(self, text="")
        
        self.teta_label         = ttk.Label(self, text="teta = ")
        self.teta_value_label   = ttk.Label(self, text="")
        
        self.psi_label          = ttk.Label(self, text="psi = ")
        self.psi_value_label    = ttk.Label(self, text="")
        
        self.show_prev_path_btn = ttk.Button(
            self, 
            text="Показать предыдущий маршрут",
            command=self.__on_show_prev_path_btn_click
        )
        self.calcbtn = ttk.Button(
            self, 
            text = "Рассчитать", 
            command = self.__on_calc_btn_click
        )
        self.anim_settings_btn = ttk.Button(
            self, 
            text = "Настройки анимации",
            command = self.__on_anim_settings_btn_click
        )
        self.canvas = Canvas(bg="white", width=500, height=500)

        #Начальная привязка событий

        self.a_entry.bind("<FocusIn>", self.__on_a_entry_focus_in)
        self.a_entry.bind("<FocusOut>", self.__on_a_entry_focus_out)

        self.x_entry.bind("<FocusIn>", self.__on_x_entry_focus_in)
        self.x_entry.bind("<FocusOut>", self.__on_x_entry_focus_out)
        
        self.y_entry.bind("<FocusIn>", self.__on_y_entry_focus_in)
        self.y_entry.bind("<FocusOut>", self.__on_y_entry_focus_out)

        #позиционирование
        elements_list = [
            [self.a_label,      self.a_entry],
            [self.x_label,      self.x_entry],
            [self.y_label,      self.y_entry],
            [self.r_label,      self.r_value_label],
            [self.phi_label,    self.phi_value_label],
            [self.teta_label,   self.teta_value_label],
            [self.psi_label,    self.psi_value_label]
        ]
        
        for i in range(len(elements_list)):
            for j in range(2):
                elements_list[i][j].grid(row=i, column=j)
        
        self.show_prev_path_btn.grid(
            row=7,
            column=0,
            rowspan=1,
            columnspan=2
        )
        self.calcbtn.grid(
            row=8,
            column=0,
            rowspan=1,
            columnspan=2
        )
        self.anim_settings_btn.grid(
            row=9,
            column=0,
            rowspan=1,
            columnspan=2
        )
        self.canvas.grid(
            row=0,
            column=2,
            rowspan=10,
            columnspan=4
        )

    def draw_canvas(self) -> None:
        """Отрисовывает объект Canvas с fig внутри, задает его позиционирование"""

        self.canvas = FigureCanvasTkAgg(self.plot_picture.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(
            row=0,
            column=2,
            rowspan=10,
            columnspan=4
        )

    def __on_show_prev_path_btn_click(self) -> None:
        self.actions.show_prev_path_btn_click()

    def __on_a_entry_key_release(self, event: Event) -> None:
        self.actions.a_entry_key_release(self.a_entry.get())

    def __on_x_entry_key_release(self, event: Event) -> None:
        self.actions.x_entry_key_release(self.x_entry.get())

    def __on_y_entry_key_release(self, event: Event) -> None:
        self.actions.y_entry_key_release(self.y_entry.get())

    def __on_a_entry_focus_in(self, event: Event) -> None:
        self.a_entry.bind("<KeyRelease>", self.__on_a_entry_key_release)
    
    def __on_a_entry_focus_out(self, event: Event) -> None:
        self.a_entry.unbind("<KeyRelease>")
        self.actions.a_entry_key_release(self.a_entry.get())

    def __on_x_entry_focus_in(self, event: Event) -> None:
        self.x_entry.bind("<KeyRelease>", self.__on_x_entry_key_release)
    
    def __on_x_entry_focus_out(self, event: Event) -> None:
        self.x_entry.unbind("<KeyRelease>")

    def __on_y_entry_focus_in(self, event: Event) -> None:
        self.y_entry.bind("<KeyRelease>", self.__on_y_entry_key_release)
    
    def __on_y_entry_focus_out(self, event: Event) -> None:
        self.a_entry.unbind("<KeyRelease>")

    def __on_calc_btn_click(self) -> None: 
        self.actions.calc_btn_click(
            {
                "x": self.x_entry.get(),
                "y": self.y_entry.get(),
                "a": self.a_entry.get()
            }
        )
    
    def __on_anim_settings_btn_click(self) -> None: 
        self.actions.anim_settings_btn_click()
        