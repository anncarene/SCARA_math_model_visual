from typing import Dict
from zope.interface import Interface


class AdditionalFuncsFactory(Interface):
    """Интерфейс, предоставляемый классом AdditionalFuncsForWindows"""

    def is_entry_valid(entry_value: str) -> bool: pass
    
    def calc_outputs(entries: Dict[str, float]) -> Dict[str, float]: pass
    
    def primal_entries_validation(entries: Dict[str, float]) -> None: pass
    