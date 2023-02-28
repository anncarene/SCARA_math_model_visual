from abc                                import ABCMeta
from re                                 import match
from zope.interface                     import provider
from typing                             import Dict

from interfaces.backend.AdditionalFuncs import *

from config                             import INTERFACE_EXCEPTIONS_MODE

from backend.Converting                 import *
from backend.Exceptions                 import NotNumberEntryException, AnimationCalcException
from backend.InterfaceVerificator       import *

@InterfaceVerificator.except_if_not_provides(
    INTERFACE_EXCEPTIONS_MODE, 
    IAdditionalFuncsFactory
)
@provider(IAdditionalFuncsFactory)
class AdditionalFuncs():
    """
        AdditionalFuncsForWindows - абстрактный класс, содержащий в себе
        дополнительные функции, используемые окнами
    """

    __metaclass__: ABCMeta

    @staticmethod
    def calc_outputs(entries: Dict[str, str]) -> Dict[str, float]:
        """
            Рассчитывает и возвращает r, teta, phi, psi
            
            Аргументы:
            
            entries - словарь вида {"a": str, "x": str, "y": str} со входными данными
        """
        
        outputs: Dict[str, float] = {
            "r": 0.,
            "teta": 0.,
            "phi": 0.,
            "psi": 0.
        }
            
        outputs["phi"], outputs["r"]    = Converting.cartesianToPolar(
            float(entries["x"]),
            float(entries["y"])
        )
        outputs["teta"]                 = Converting.teta(outputs["r"], float(entries["a"]))
        outputs["psi"]                  = Converting.psi(outputs["teta"])
                
        return outputs
    
    @staticmethod
    def is_entry_valid(entry_value: str) -> bool:
        """
            С помощью регулярного выражения возвращает соответствие введенного в поле значения
            регулярному выражению, отвечающему float-числу с разделителем "."
        """
        
        return match("[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?" , entry_value) is not None
    
    @staticmethod
    def primal_entries_validation(entries: Dict[str, float]) -> None:
        """Первичная валидация введенных значений"""

        for key in entries:
                if AdditionalFuncs.is_entry_valid(entries[key]) is not True:
                    raise NotNumberEntryException("В одном или нескольких полях введены не числа")
    @staticmethod            
    def check_animation_frames(frames: List[Tuple[float, float]], a: float) -> None:
        for i in range(len(frames)):
            try:
                phi, r = Converting.cartesianToPolar(frames[i][0], frames[i][1])
                Converting.checkEntriedData(r, a)
            except:
                raise AnimationCalcException("Недопустимое перемещение")