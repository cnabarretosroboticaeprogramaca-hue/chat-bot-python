import ProjetoChatbot as pc
import tkinter as tk

main_window = tk.Tk()

main_window.title('Chat com a Maria')
main_window.geometry('420x520')
main_window.resizable(False, False)

frame_entrada = tk.Frame(main_window)
frame_entrada.grid(row=0, column=0, padx=10, pady=10)

label_entrada = tk.Label(frame_entrada, text='Digite sua mensagem:')
label_entrada.grid(row=0, column=0)

entrada_mensagem = tk.Entry(frame_entrada, width=40)
entrada_mensagem.grid(row=1, column=0)

frame_conversa = tk.Frame(main_window)
frame_conversa.grid(row=1, column=0, padx=10, pady=10)

historico = tk.StringVar()
historico.set('')

label_historico = tk.Label(frame_conversa, textvariable=historico,
justify='left', wraplength=380)
label_historico.grid(row=0, column=0)

nome_maquina = 'Maria'
entrada_sugestao = False
entrada_nome_usuario = True
nome_usuario = ''

historico.set(f'{nome_maquina}: Qual é o seu nome?')

def roda_Chatbot():
    global entrada_nome_usuario, nome_usuario, entrada_sugestao
    texto = entrada_mensagem.get()
    if entrada_nome_usuario:
        nome_usuario = texto
        saudacao = pc.saudacao_GUI(nome_usuario, nome_maquina)
        historico.set(historico.get() + f'\n{nome_usuario}:{nome_usuario}\n{nome_maquina}: {saudacao}')
        entrada_nome_usuario = False
        
    elif entrada_sugestao:
        pc.salva_sugestao(texto)
        historico.set(historico.get() + f'\n{nome_usuario}:{texto}\n{nome_maquina}: Entendido, muito obrigada!')
        entrada_sugestao = False
    else:
        historico.set(historico.get() + f'\n{nome_usuario}: {texto}')
        resposta = pc.buscaResposta_GUI(texto)
        if resposta == 'Hum...':
            entrada_sugestao = True
            resposta_formatada = 'Hum... não sei responder isso. O que eu deveria dizer da próxima vez?'
        elif resposta == 'fim':
            resposta_formatada = 'Até mais! Foi ótimo conversar com você!'
        else:
            resposta_formatada = pc.exibeResposta_GUI(resposta, nome_maquina)
        historico.set(historico.get() + f'\n{nome_maquina}:{resposta_formatada}')
    entrada_mensagem.delete(0, 'end')
    
botao_enviar = tk.Button(frame_entrada, text='Enviar', command=roda_Chatbot)
botao_enviar.grid(row=2, column=0)

main_window.mainloop()