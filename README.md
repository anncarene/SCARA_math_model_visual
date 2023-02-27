## Визуализация мат. модели расчета положений для SCARA 

ver 2.0

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

## Changelog
### 1.0: 
- Реализация базового функционала расчета положения ребер
### 2.0
- Оптимизация расчета списка точек для генерации графика
- Добавление анимирования нескольких режимов перемещения привода
- Глобальное изменение архитектуры приложения