from tkinter import *
import logica_timer.timer

# CORES
cor1 = '#000000'  # preto
cor2 = '#C0C0C0'  # cinza
cor3 = '#0000FF'  # azul
cor4 = '#00FF7F'  # verde
cor5 = '#FF0000'  # vermelho
cor6 = '#FFD700'  # amarelo

# Variaveis globais
global win, botão_iniciar, botão_parar, botão_reiniciar, rotulo_timer, tempo


# Configurando apresentação da janela
def janela():
    global win, botão_iniciar, botão_parar, botão_reiniciar, rotulo_timer
    win = Tk()
    win.title('Cronometro em Python')
    win.geometry('300x180')
    win.configure(bg=cor2)
    win.resizable(width=False, height=False)

    # Chamada do rótulo do temporizador
    rotulo_timer = Label(win, text=logica_timer.timer.tempo, font='Times 50 bold', bg=cor2, fg=cor1)
    rotulo_timer.place(x=20, y=20)

    # Chamada dos botões: Botão iniciar
    botão_iniciar = Button(win, command=logica_timer.timer.start, text='INICIAR', width=10, height=2, bg=cor4, fg=cor1,
                           font='Arial 10 bold', relief='flat', overrelief='solid')
    botão_iniciar.place(x=10, y=120)

    # Botão Parar
    botão_parar = Button(win, command=logica_timer.timer.stop, state='disabled', text='PARAR', width=10, height=2,
                         bg=cor4, fg=cor1, font='Arial 10 bold', relief='flat', overrelief='solid')
    botão_parar.place(x=105, y=120)
    # Botão Reiniciar
    botão_reiniciar = Button(win, command=logica_timer.timer.restart, text='REINICIAR', width=10, height=2, bg=cor4,
                             fg=cor1, font='Arial 10 bold', relief='flat', overrelief='solid')
    botão_reiniciar.place(x=200, y=120)

    # exibir a janela
    win.mainloop()


# função para desativar botões
def troca_estado_botões():
    if botão_iniciar['state'] == 'normal':
        botão_parar['state'] = 'normal'
        botão_iniciar['state'] = 'disabled'
    else:
        botão_iniciar['state'] = 'normal'
        botão_parar['state'] = 'disabled'
