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

        pyperclip.copy(self.login)
        self.pg.hotkey('ctrl', 'v')
        self.pg.press('tab')
        pyperclip.copy(self.senha)

        self.pg.hotkey('ctrl', 'v')
        self.pg.press('enter')

        sleep(time)
    #sleep(30)

    def in_game(self):
        self.pg.click(x=433, y=194)
        sleep(2)
        self.pg.click(x=362, y=706)
        sleep(2)
        self.pg.click(x=848, y=838)
        sleep(2)
        self.pg.click(x=928, y=598)
        sleep(2)

    def top_lane(self):
        if self.first_lane is False:
            self.pg.click(x=976, y=846)
            sleep(2)
            self.pg.click(x=834, y=785)
            self.first_lane = True
            return self.first_lane

        self.pg.click(x=1014, y=843)
        sleep(2)
        self.pg.click(x=878, y=792)
        return

    def jungle_lane(self):
        if self.first_lane is False:
            self.pg.click(x=976, y=846)
            sleep(2)
            self.pg.click(x=881, y=787)
            self.first_lane = True
            return self.first_lane

        self.pg.click(x=1014, y=843)
        sleep(2)
        self.pg.click(x=924, y=775)
        return

    def mid_lane(self):
        if self.first_lane is False:
            self.pg.click(x=976, y=846)
            sleep(2)
            self.pg.click(x=943, y=778)
            self.first_lane = True
            return self.first_lane

        self.pg.click(x=1014, y=843)
        sleep(2)
        self.pg.click(x=978, y=779)
        return

    def adc_lane(self):
        if self.first_lane is False:
            self.pg.click(x=976, y=846)
            sleep(2)
            self.pg.click(x=986, y=780)
            self.first_lane = True
            return self.first_lane

        self.pg.click(x=1014, y=843)
        sleep(2)
        self.pg.click(x=1039, y=780)
        return

    def sup_lane(self):
        if self.first_lane is False:
            self.pg.click(x=976, y=846)
            sleep(2)
            self.pg.click(x=1065, y=778)
            self.first_lane = True
            return self.first_lane

        self.pg.click(x=1014, y=843)
        sleep(2)
        self.pg.click(x=1097, y=780)
        return

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
    abrir_jogo.open_app(10)
    abrir_jogo.login_game(30)
    abrir_jogo.in_game()
    abrir_jogo.jungle_lane()
    abrir_jogo.top_lane()
    sleep(2)
    abrir_jogo.position()





