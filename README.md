# gctrl_python
Python version of gctrl for arduino simple cnc (python g-code sender)

gctrl написанный на processing не подошел, из-за проблем: 
- большая нагрузка на процессор (для слабых ПК) 
- нестабильность программы 
- иногда не запускается, оставляя в памяти свой экземпляр и т.д.

Так как проект образовательный, идея перенести код в python оказалась очень интересной и полезной. Теперь любой может используя прошивку от [сюда](  https://github.com/adidax/mini_cnc_plotter_firmware/blob/master/mini_cnc_plotter_firmware.ino), сделать свой ЧПУ плоттер управляемый через python.
