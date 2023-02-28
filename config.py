'''Конфигурация'''

from typing import Literal

'''
    Режим выкидывания исключений для интерфейсов. При разработке рекомендуется
    установить значение на 'logging'
'''
INTERFACE_EXCEPTIONS_MODE: Literal['logging', 'strict'] = 'logging' 