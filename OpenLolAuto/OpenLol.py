import pyautogui
from time import sleep
import pyperclip


class OpenLol:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
        self.pg = pyautogui

        self.pg.PAUSE = 1.5

        self.app_is_open = False
        self.first_lane = False

    def open_app(self, time=0):
        self.pg.press('win')
        self.pg.write('League of Legends')
        self.pg.press('enter')

        self.app_is_open = True
        sleep(time)
        return self.app_is_open

    # sleep(15)

    def login_game(self, time=0):
        sleep(0.5)
        pyperclip.copy(self.login)
        self.pg.hotkey('ctrl', 'v')
        self.pg.press('tab')
        pyperclip.copy(self.senha)

        self.pg.hotkey('ctrl', 'v')
        self.pg.press('enter')

        sleep(time)

    # sleep(30)

    def in_game(self):
        while True:
            btn_jogar = self.pg.locateOnScreen("jogar.png", confidence=0.5)
            if btn_jogar:
                self.pg.click(btn_jogar)
                sleep(2)

                btn_alternativa = self.pg.locateOnScreen("alternativa.PNG", confidence=0.9)
                self.pg.click(btn_alternativa)
                sleep(2)

                btn_confirma_sala = self.pg.locateOnScreen("ConfirmarSala.PNG", confidence=0.5)
                self.pg.click(btn_confirma_sala)
                sleep(2)

                break
            else:
                pass

    def top_lane(self):
        while True:
            btn_escolher_lane = self.pg.locateOnScreen("escolher_lane.PNG", confidence=0.9)
            if btn_escolher_lane:
                self.pg.click(btn_escolher_lane)
                btn_top_lane = self.pg.locateOnScreen("top_lane.PNG", confidence=0.9)
                self.pg.click(btn_top_lane)
                break
            else:
                pass

        return

    def jungle_lane(self):
        while True:
            btn_escolher_lane = self.pg.locateOnScreen("escolher_lane.PNG", confidence=0.9)
            if btn_escolher_lane:
                self.pg.click(btn_escolher_lane)
                btn_jungle_lane = self.pg.locateOnScreen("jungle_lane.PNG", confidence=0.9)
                self.pg.click(btn_jungle_lane)
                break
            else:
                pass

        return

    def mid_lane(self):
        while True:
            btn_escolher_lane = self.pg.locateOnScreen("escolher_lane.PNG", confidence=0.9)
            if btn_escolher_lane:
                self.pg.click(btn_escolher_lane)
                btn_mid_lane = self.pg.locateOnScreen("mid_lane.PNG", confidence=0.9)
                self.pg.click(btn_mid_lane)
                break
            else:
                pass

        return

    def adc_lane(self):
        while True:
            btn_escolher_lane = self.pg.locateOnScreen("escolher_lane.PNG", confidence=0.9)
            if btn_escolher_lane:
                self.pg.click(btn_escolher_lane)
                btn_adc_lane = self.pg.locateOnScreen("adc_lane.PNG", confidence=0.9)
                self.pg.click(btn_adc_lane)
                break
            else:
                pass
     
        return

    def sup_lane(self):
        while True:
            btn_escolher_lane = self.pg.locateOnScreen("escolher_lane.PNG", confidence=0.9)
            if btn_escolher_lane:
                self.pg.click(btn_escolher_lane)
                btn_sup_lane = self.pg.locateOnScreen("sup_lane.PNG", confidence=0.9)
                self.pg.click(btn_sup_lane)
                break
            else:
                pass

        return

    def start_game(self):
        while True:
            btn_start = self.pg.locateOnScreen("encontrar_partida.PNG", confidence=0.9)
            if btn_start:
                self.pg.click(btn_start)
                break
            else:
                pass

    def position(self):

        print(self.pg.position())


class Save:
    def __init__(self, login=None, senha=None):
        self.login = login
        self.senha = senha

        self.login_registred = None
        self.pass_registred = None

    def save_file(self):
        with open("C:/Users/gabri/OneDrive/Área de Trabalho/video_aula/OpenLolAuto/save.txt", 'w') as save:
            save.write(f'{self.login},{self.senha}')
            save.close()

    def read_file(self):
        with open("save.txt", 'r') as file:
            for row in file:
                pass
            self.login_registred, self.pass_registred= row.split(',')

        return




if __name__ == '__main__':
    """salva_dados = Save('login', 'pass')
    salva_dados.save_file()
    
    Use para registrar seu login e senha uma unica vez
    """
    """
    dados = Save('login', 'pass')
    dados.read_file()
    
    Use para pegar os dados ja salvos
    """
    # use um tempo para cada interação para nao haver bugs, e ajuste do seu jeito e so por a quantidade de tempo
    dados = Save()
    dados.read_file()

    abrir_jogo = OpenLol(dados.login_registred, dados.pass_registred)
    # abrir_jogo.open_app(10)
    # abrir_jogo.login_game(30)
    abrir_jogo.in_game()
    abrir_jogo.top_lane()
    abrir_jogo.mid_lane()
    abrir_jogo.start_game()
    # abrir_jogo.adc_lane()
    # sleep(2)
    # abrir_jogo.position()










