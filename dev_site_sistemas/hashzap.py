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

# # =======ETAPA 1 ========       
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


# # =======ETAPA 2 ========       
# def main (pagina):
#         # tudo o que ela vai fazer
#         # criar alguma coisa
#         #criar o titulo
#         titulo=ft.Text("Hashzap")
#         #4 vamos configurar essa janela
#             # o que eu quero dentro da janela?
#                 # Titulo : bem vindo ao hashzap
#                 # campo de texto: escreva seu nome no chat
#                 # botao: entrar no chat

#         titulo_janela= ft.Text("Bem vindo ao Hashzap")
#         campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")

#         # ======= Etapa3=======
#             # tirar o titulo da pagina
#                 # tirar o botao_iniciar
#                 # fechar a janela
#                 #criar o chat
#                 # criar o campo de texto de env msg
#                 # criar o botao env msg
#         # 7 criar minha funcao clicar/entrar no site
#             # 8 criar o chat >> quero add msg + botao um do lado do outro
#             # texto_mensagem = ft.TextField(label="Digite sua mensagem")
#             # botao_enviar=ft.ElevatedButton("Enviar")

        
#         texto_mensagem = ft.TextField(label="Digite sua mensagem")


#         # 14 queremos enviar msg entao criamos a funcao enviar msg
#         def enviar_mensagem (evento):
#             #enviar msg no chat
#                 #usuario: msg
#             # limpar o campo de msg
#             # texto = texto_mensagem.value # mas o que quero que apareça? Lira: coe, glr                
#             texto = f"{campo_nome_usuario.value}:{texto_mensagem.value }"# mas o que quero que apareça? Lira: coe, glr
#             chat.controls.append(ft.Text(texto)) 
#             texto_mensagem.value = ""
#             pagina.update()

#         botao_enviar= ft.ElevatedButton("Enviar", on_click= enviar_mensagem)
#         # 10 vamos criar nosso chat
#         chat = ft.Column()

#         linha_mensagem = ft.Row([texto_mensagem, botao_enviar])






#         def entrar_chat(evento):
#             pagina.remove(titulo)
#             pagina.remove(botao_iniciar)
#             janela.open= False
#             # texto_mensagem = ft.TextField(label="Digite sua mensagem")
#             # pagina.add(texto_mensagem)
#             # # botao_enviar=ft.ElevatedButton("Enviar") elemento que criei >> entao coloco fora da funcao
#             # pagina.add(botao_enviar)
#             # 9  ao inves de dd separados usamos a linha de msg
#             pagina.add(linha_mensagem)

#             pagina.add(chat)
            
#             # 11 depois de criar um chat com as msg> quero escrever: usuario entrou no chat
#             #13 nome de forma dinamica
#             texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat"
#             # 12 add esse texto no nosso chat            
#             chat.controls.append(ft.Text(texto_entrou_chat))  # chat.controls.append(texto_entrou_chat)
            
#             pagina.update()
                

#         botao_entrar = ft.ElevatedButton("Entrar no chat", on_click= entrar_chat)

#         janela = ft.AlertDialog(title=  titulo_janela , content= campo_nome_usuario , actions= [botao_entrar] )   




#         def abrir_popup(evento):
#         # 5 como exibir essa janela na pagina? 
#                 pagina.dialog = janela
#                 janela.open =True
#         # 6 toda vez que  fazer uma alteracao visual na pagina atualizar a pagina
#                 pagina.update()
#         #1 botao precisa fazer algo...abrir janela antes do botao iniciar vamos criar funcao
#         #2 toda vez que clicar no botao vai usar essa funcao
#         #3 agora vamos criar essa fçao
#         botao_iniciar = ft. ElevatedButton("Iniciar Chat", on_click= abrir_popup) 

#         # colocar essa coisa na pagina
#         #adicionar o titulo na pag
#         pagina.add(titulo)
#         pagina.add(botao_iniciar)
        

# # executar o seu sistema
#  # ft.app(main)->PADRAO ABRE NORMAL 
# ft.app(main, view =ft.WEB_BROWSER) # SE COLOCO VIEW DESSE JEITO VEJO COMO SITE
        

# =======ETAPA 4 ========  TUNEL DE COMUNICAÇÃO 


       
def main (pagina):
        
        titulo=ft.Text("Hashzap")



        # 15 utilidade enviar msg no chat
        #17 tudo o que quero que apareca para todos user >> faça no tunel
        def enviar_mensagem_tunel (mensagem):
            chat.controls.append(ft.Text(mensagem)) # agora nao é o texto mas a msg
            pagina.update()
        #16 só cria o tunel
        pagina.pubsub.subscribe(enviar_mensagem_tunel)
        # se eu quero enviar para todos
        # pagina.pubsub.send_all()
        


        titulo_janela= ft.Text("Bem vindo ao Hashzap")
        campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")   
        

        def enviar_mensagem (evento):               
            texto = f"{campo_nome_usuario.value}:{texto_mensagem.value }"
            
            # chat.controls.append(ft.Text(texto)) quero que aparece pra tdos
            pagina.pubsub.send_all(texto) # envia uma msg no tunel >>> CHAMA O TUNEL
            texto_mensagem.value = ""
            pagina.update()

            #troco de lugar texto mensagem
        texto_mensagem = ft.TextField(label="Digite sua mensagem", on_submit= enviar_mensagem)
        botao_enviar= ft.ElevatedButton("Enviar", on_click= enviar_mensagem)
        chat = ft.Column()
        linha_mensagem = ft.Row([texto_mensagem, botao_enviar])

        def entrar_chat(evento):
            pagina.remove(titulo)
            pagina.remove(botao_iniciar)
            janela.open= False
            pagina.add(chat)
            pagina.add(linha_mensagem)
            texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat"          
            # chat.controls.append(ft.Text(texto_entrou_chat)) user entrou no chat ao inves de usar isso e mandar pro txto  mandamos pro tunel
            pagina.pubsub.send_all(texto_entrou_chat)
            pagina.update()
                
        botao_entrar = ft.ElevatedButton("Entrar no chat", on_click= entrar_chat)
        janela = ft.AlertDialog(title=  titulo_janela , content= campo_nome_usuario , actions= [botao_entrar] )   

        def abrir_popup(evento):
                pagina.dialog = janela
                janela.open =True
                pagina.update()
        botao_iniciar = ft. ElevatedButton("Iniciar Chat", on_click= abrir_popup) 
        pagina.add(titulo)
        pagina.add(botao_iniciar)
        
 
ft.app(main, view =ft.WEB_BROWSER) 