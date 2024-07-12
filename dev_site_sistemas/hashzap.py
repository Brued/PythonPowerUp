#ETAPA 1
# Titulo: hashzap
# botao: iniciar chat
    # ETAPA  2 
        #popup / modal / alerta
        # Titulo : bem vindo ao hashzap
        # campo de texto: escreva seu nome no chat
        # botao: entrar no chat

            # ETAPA 3
            # sumir com o titulo e o botao inicial
             # fechar o Popup 
            # criar o chat (com a msg de nome do usuario entrou ..)

        # embaixo do chat:
            #  campo de texto: digite sua msg
            # botao enviar
                # vai aparecer a msg no chat com o nome do User 
                # lira: coe glr

# Flet -> aplicativo/site/prorama de computador
# pip install flet

# importar o flet

import flet as ft

# criar a função principal do seu sistema
            # tenho que ter o parametro obrigatoriamente ex (pagina)

# =======ETAPA 1 ========       
# def main (pagina):
#         # tudo o que ela vai fazer
#         # criar alguma coisa
#         #criar o titulo
#         titulo=ft.Text("Hashzap")

#         janela = ft.AlertDialog() # CONFIGURAR

#         botao_iniciar = ft. ElevatedButton("Iniciar Chat")

#         # colocar essa coisa na pagina
#         #adicionar o titulo na pag
#         pagina.add(titulo)
#         pagina.add(botao_iniciar)
        

# # executar o seu sistema
#  # ft.app(main)->PADRAO ABRE NORMAL 
# ft.app(main, view =ft.WEB_BROWSER) # SE COLOCO VIEW DESSE JEITO VEJO COMO SITE


# # construir site no python
# # flask google
# # django intagram


# # fast api
# # tornado
# # flet qual a vantagem? com o mesmo codigo conseguimos com mesmo codigo aplicativo/site/programa de computador

# ==================================================================


# etapa2
#popup / modal / alerta
# Titulo : bem vindo ao hashzap
        # campo de texto: escreva seu nome no chat
        # botao: entrar no chat





def main (pagina):
        # criar alguma coisa
        #criar o titulo
        titulo=ft.Text("Hashzap")
        
        titulo_janela = ft.Text("Bem Vindo ao hashzap")
        #3 o que quero por dentro da janela
        campo_nome_usuario = ft. TextField(label="Escreva seu nome no chat") # campo_nome_usuario = ft. TextField() sem rotulo
        texto_mensagem = ft.TextField(label="Digite sua mensagem")
        botao_enviar = ft.ElevatedButton("Enviar")

       # etapa3 Funcionalidades do chat
        #8 def funcao entrar no chat

        linha_mensagem = ft.Row([texto_mensagem, botao_enviar])   # fomando linha 2 ou mais um do lado do outro
        # 11
        chat = ft.Column ()
        def entrar_chat(evento):
        #     # 9 tirar o botao_iniciar
        #     # 10 fechar popup
        #     # 11 criar o chat
        #     # 12 criar o campo de texto  de enviar msg
        #     # 13 criar o botao enviar msg
            pagina.remove(titulo)
            pagina.remove(botao_iniciar)
            janela.open = False
                # texto_mensagem = ft.TextField(label="Digite sua mensagem") poderia ter coocado aqui
            # pagina.add(texto_mensagem)
            #     # botao_enviar = ft.ElevatedButton("Enviar")
            # pagina.add(botao_enviar)
            pagina.add (linha_mensagem)
            pagina.add(chat)

            # 12 escrevr a msg: usuario entrou no site >>> texto_entrou_chat = ft.Text("Lira entrou no chat")
            texto_entrou_chat = ft.Text("Lira entrou no chat") #a
            chat.controls.append(texto_entrou_chat) #b
            #a e b crie e adicionei o texto
           
            

            pagina.update()




        botao_entrar = ft.ElevatedButton("Entrar no chat", on_click= entrar_chat)

        #2 quando ele clicar no botao quero abrir o popup
        janela = ft.AlertDialog(  title= titulo_janela, content = campo_nome_usuario,  actions=[botao_entrar]) #4 adicionar na janela # se quiser posso add mais botao 
        

        def abrir_popup(evento):   #1 toda funcao usadda dentro de um botao tem que receber um evento como um parametro
                #5 coloca a janela na pagina
            pagina.dialog = janela
                #6 esse comando vai abri nossa janela
            janela.open = True
                #7 fizemos uma alteracao visual na pag >> atualizar
            pagina.update()

        botao_iniciar = ft. ElevatedButton("Iniciar Chat", on_click= abrir_popup)

        # colocar essa coisa na pagina
        # adicionar o titulo na pag
        pagina.add(titulo)
        pagina.add(botao_iniciar)
        

# executar o seu sistema
 # ft.app(main)-> abre em forma padrao
ft.app(main, view =ft.WEB_BROWSER) # SE COLOCO VIEW DESSE JEITO VEJO COMO SITE




        


 