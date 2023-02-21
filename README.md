## Визуализация мат. модели расчета положений для SCARA 

1-я тестировочная версия

### Установка зависимостей

В папке с проектом в терминале введите:

```
$ python3 -m venv mmv_env
$ source mmv_env/bin/activate
$ pip install --no-cache-dir -r requirements.txt
```

### Запуск

В папке с проектом в терминале введите:

```
$ python3 main.py
```

*Примечание: python должен быть версии 3.10 и отконфигурирован для использования tkinter.*

Если Ваш python не поддерживает tkinter, произведите следующие действия:

Arch-based distros

```
$ sudo pacman -S tk
```

Debian-based distros
```
$ sudo apt-get install -y python3-tk
```

RHEL-based distros
```
$ sudo dnf install -y python3.10-tkinter.x86-64
```