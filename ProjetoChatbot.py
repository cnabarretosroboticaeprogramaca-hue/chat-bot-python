import random
import datetime
from zoneinfo import ZoneInfo

def saudacoes(nome):
  hora = datetime.datetime.now(ZoneInfo("America/Sao_Paulo"))
  print(hora)

  if hora.hour < 12:
    periodo = 'Bom dia'
  elif hora.hour < 18:
    periodo = 'Boa tarde'
  else:
    periodo = 'Boa noite'
  frases = [
    f'{periodo}! Eu sou a {nome}, tudo bem?',
    f'{periodo}! Aqui é a {nome}. Como posso ajudar?',
    f'{periodo}! {nome} na área, vamos conversar?',
  ]
  print(random.choice(frases))

def recebeTexto():
  palavras_proibidas = ['idiota', 'burro', 'chato']
  texto = input('Você: ')
  for p in palavras_proibidas:
    if p in texto.lower():
      print('Vamos manter a conversa respeitosa, ok?')
      return recebeTexto()
  return texto

def buscaResposta(texto):
  despedidas = ['tchau', 'até mais', 'falou', 'flw']

  if texto.lower().strip() in despedidas:
    return 'fim'

  with open('base_conhecimento.txt', 'a+') as conhecimento:
    conhecimento.seek(0)

    while True:
        linha = conhecimento.readline()

        if linha == '':
          # chegamos ao fim do arquivo: o chatbot não sabe responder
          conhecimento.write(texto.strip() + '\n')
          nova_resposta = input('Hum, eu não sei responder isso! O que você esperava ouvir? ')
          conhecimento.write('Chatbot: ' + nova_resposta.strip() + '\n')
          return 'Hum...'

        if linha.strip() == texto.strip():
          proxima_linha = conhecimento.readline()
          if proxima_linha != '':
            return proxima_linha.strip()

def exibeResposta(resposta, nome):
  if resposta == 'fim':
    print(f'{nome}: Até mais! Foi ótimo conversar com você!')
    return 'fim'
  resposta_formatada = resposta.replace('Chatbot', nome)
  print(resposta_formatada)
  return 'continua'

def saudacao_GUI(nome_usuario, nome_maquina):
  return f'Olá, {nome_usuario}! Eu sou a {nome_maquina}, tudo bem?'
def exibeResposta_GUI(resposta, nome):
  return resposta.replace('Chatbot', nome)
def salva_sugestao(texto):
  with open('base_conhecimento.txt', 'a') as conhecimento:
    conhecimento.write('Chatbot: ' + texto.strip() + '\n')
def jaccard(texto1, texto2):
  palavras1 = set(texto1.split())
  palavras2 = set(texto2.split())
  intersecao = palavras1.intersection(palavras2)
  uniao = palavras1.union(palavras2)
  return len(intersecao) / len(uniao)
def limpa_frase(texto):
  texto = texto.lower()
  texto = texto.replace('\n', '')
  texto = texto.replace('cliente: ', '')
  for sinal in ['.', ',', '!', '?']:
    texto = texto.replace(sinal, '')
  return texto.strip()
def buscaResposta_GUI(texto):
  despedidas = ['tchau', 'até mais', 'falou', 'flw']
  texto_limpo = limpa_frase(texto)
  if texto_limpo in despedidas:
    return 'fim'
  with open('base_conhecimento.txt', 'a+') as conhecimento:
    conhecimento.seek(0)
    while True:
      linha = conhecimento.readline()
      if linha == '':
        return 'Hum...'
      linha_limpa = limpa_frase(linha)
      if jaccard(linha_limpa, texto_limpo) > 0.3:
        proxima_linha = conhecimento.readline()
        if proxima_linha != '':
          return proxima_linha.strip()




