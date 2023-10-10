import machine
import ssd1306

# Configuración de la pantalla OLED
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))  # Configura el bus I2C
oled = ssd1306.SSD1306_I2C(128, 64, i2c)  # Crea una instancia de la pantalla

# Limpia la pantalla
oled.fill(0)
oled.show()

# Muestra el texto "Hola Mundo"
oled.text("Hola Mundo", 0, 0)
oled.show()