import gui.gui

# variaveis globais
global tempo, inicio
tempo = '00:00:00'
inicio = False
contador = 0
limitador = 60


# Funçãp da lógica do cronometro e atualização do rótulo do temporizador
def timer():
    global tempo, inicio, contador, limitador
    if inicio:
        crono = str(tempo)
        h, m, s = map(int, crono.split(':'))
        s = int(contador)
        if s >= limitador:
            contador = 0
            m += 1
            if m >= limitador:
                m = 0
                h += 1
                if h >= limitador:
                    h = 0
        s = str(0) + str(s)
        m = str(0) + str(m)
        h = str(0) + str(h)
        crono = str(h[-2:]) + ':' + str(m[-2:]) + ':' + str(s[-2:])
        gui.gui.rotulo_timer['text'] = crono
        tempo = crono
        gui.gui.Tk.after(gui.gui.rotulo_timer, 1000, timer)
        contador += 1


# Função para iniciar o temporizador
def start():
    global inicio
    inicio = True
    gui.gui.troca_estado_botões()
    timer()


# Função para parar o temporizador
def stop():
    global inicio
    inicio = False
    gui.gui.troca_estado_botões()


# Função para reiniciar o temporizador
def restart():
    global contador, tempo
    contador = 0
    tempo = '00:00:00'
    gui.gui.rotulo_timer['text'] = tempo
