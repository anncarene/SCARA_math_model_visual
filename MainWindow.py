from tkinter                            import *
from tkinter                            import ttk
from typing                             import Dict
from matplotlib.figure                  import Figure
from matplotlib.backends.backend_tkagg  import FigureCanvasTkAgg
from re                                 import match
from zope.interface                     import implementer, provider

from MainWindowInterfaces   import *
from MathFuncsForVisual     import *
from Converting             import *
from ErrWindow              import *

class NotNumberEntryException(Exception):
    """Класс исключений для некорректных вводов (если не число вдруг введут)"""
    
    def __init__(self, *args):
        self.message = None
        
        if args:
            self.message = args[0]
            
    def __str__(self):
        return self.message

@provider(IMainWindowFactory)
@implementer(IMainWindow)            
class MainWindow(Tk):   
    """
        MainWindow - класс, реализующий графическую составляющую приложения.
        В обязательнои порядке должен иметь только один экземпляр
    """
    
    def __init__(self):
        super().__init__()

        #конфигурация окна        
        self.title("Визуализация")
        self.geometry("750x500")

        #конфигурация сетки
        for i in range(6): self.columnconfigure(index=i, weight=1)
        for i in range(8): self.rowconfigure(index=i, weight=1)
        
        #элементы  
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
        
        self.teta_label         = ttk.Label(self, text ="teta = ")
        self.teta_value_label   = ttk.Label(self, text="")
        
        self.psi_label          = ttk.Label(self, text ="psi = ")
        self.psi_value_label    = ttk.Label(self, text="")
        
        self.calcbtn            = ttk.Button(self, text="Рассчитать", command=self.onClick)
        self.canvas             = Canvas(bg="white", width=500, height=500)
            
        #позиционирование
        values_list = [
            [self.a_label,      self.a_entry],
            [self.x_label,      self.x_entry],
            [self.y_label,      self.y_entry],
            [self.r_label,      self.r_value_label],
            [self.phi_label,    self.phi_value_label],
            [self.teta_label,   self.teta_value_label],
            [self.psi_label,    self.psi_value_label]
        ]
        
        for i in range(len(values_list)):
            for j in range(2):
                values_list[i][j].grid(row=i, column=j)
        
        self.calcbtn.grid(
            row=7,
            column=0,
            rowspan=1,
            columnspan=2
        )
        self.canvas.grid(
            row=0,
            column=2,
            rowspan=8,
            columnspan=4
        )

    def drawCanvas(
        self, 
        fig: Figure
    ) -> None:
        """
            Отрисовывает объект Canvas с fig внутри, задает его позиционирование
            
            Аргументы:
            
            fig - отрисовываемый объект графика matplotlib 
        """

        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(
            row=0,
            column=2,
            rowspan=8,
            columnspan=4
        )
    
    @staticmethod
    def calc_plot_figure(
        a:      float, 
        psi:    float, 
        phi:    float
    ) -> Figure:
        """
            Создает и возвращает объект графика matplotlib с отрисованными функциямми y{I-IV}
            
            Аргументы:
            
            a - плечо привода
            
            psi - угол между плечом привода и осью OXr
            
            phi - угол поворота в полярной системе координат
        """
        
        fig = Figure(figsize=(5,5))
        
        x_spaces, y_spaces = MathFuncsForVisual.generate_spaces(a, psi, phi)     
        xI1, xI2, yI1, yI2 = MathFuncsForVisual.limits(psi, phi, a, 1)
        xIV1, xIV2, yIV1, yIV2 = MathFuncsForVisual.limits(psi, phi, a, 4)
        

        subplt = fig.add_subplot()
        subplt.set_xlim(left=-2.0*a, right=2.0*a)
        subplt.set_ylim(bottom=-2.0*a, top=2.0*a)
        for i in range(4):
            subplt.plot(
                x_spaces[i],
                y_spaces[i],
                linewidth=3.0,
                color='darkcyan'
            )
        subplt.scatter([xI1, xI2], [yI1, yI2], color="darkslateblue")
        subplt.scatter([xIV1, xIV2], [yIV1, yIV2], color="darkslateblue")
        subplt.grid(True)

        return fig
    
    def set_outputs(
        self,
        outputs: Dict[str, float]
    ) -> None:
        """
            Отображает в окне приложения пересчитанные r, teta, phi, psi
            
            Аргументы:
            
            outputs - словарь вида {"r": float, "teta": float, "phi": float, "psi": float}
        """
        
        self.r_value_label["text"]      = str(outputs["r"])
        self.teta_value_label["text"]   = str(Converting.radToDeg(outputs["teta"])) + " deg"
        self.phi_value_label["text"]    = str(Converting.radToDeg(outputs["phi"])) + " deg"
        self.psi_value_label["text"]    = str(Converting.radToDeg(outputs["psi"])) + " deg"
         
    @staticmethod
    def calc_outputs(entries: Dict[str, float]) -> Dict[str, float]:
        """
            Рассчитывает и возвращает r, teta, phi, psi
            
            Аргументы:
            
            entries - словарь вида {"a": float, "x": float, "y": float} со входными данными
        """
        
        outputs: Dict[str, float] = {
            "r": 0.,
            "teta": 0.,
            "phi": 0.,
            "psi": 0.
        }
            
        outputs["phi"], outputs["r"]    = Converting.cartesianToPolar(
            entries["x"],
            entries["y"]
        )
        outputs["teta"]                 = Converting.teta(outputs["r"], entries["a"])
        outputs["psi"]                  = Converting.psi(outputs["teta"])
                
        return outputs
    
    @staticmethod
    def is_entry_valid(entry_value: str) -> bool:
        """
            С помощью регулярного выражения возвращает соответствие введенного в поле значения
            регулярному выражению, отвечающему float-числу с разделителем "."
        """
        
        return match("[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?" , entry_value) is not None
        
    def onClick(self) -> None:
        """
            Функция, вызываемая на нажатие кнопки "Рассчитать". Обрабатывает введенные значения,
            с помощью is_entry_valid проверяет корректность ввода. В случае некорректного ввода
            выдает окно с ошибкой. Применяет calc_outputs, set_outputs и draw_canvas на основании введенных
            данных
        """
        
        try:
            entries: Dict = {
                "x": self.x_entry.get(),
                "y": self.y_entry.get(),
                "a": self.a_entry.get()
            }
            
            for key in entries:
                if MainWindow.is_entry_valid(entries[key]): 
                    entries[key] = float(entries[key])
                else: 
                    raise NotNumberEntryException("В одном или нескольких полях введены не числа")
            
            outputs = MainWindow.calc_outputs(entries)
            self.set_outputs(outputs)
            
            self.drawCanvas(
                MainWindow.calc_plot_figure(
                    entries["a"],
                    outputs["psi"],
                    outputs["phi"]
                )
            )
        except (NotNumberEntryException, ConvertingException) as err:
            err_window = ErrWindow(str(err))