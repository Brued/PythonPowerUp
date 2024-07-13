
# =======ETAPA 2 ========       
def main (pagina):
        # tudo o que ela vai fazer
        # criar alguma coisa
        #criar o titulo
        titulo=ft.Text("Hashzap")
        #4 vamos configurar essa janela
            # o que eu quero dentro da janela?
                # Titulo : bem vindo ao hashzap
                # campo de texto: escreva seu nome no chat
                # botao: entrar no chat

        titulo_janela= ft.Text("Bem vindo ao Hashzap")
        campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")
        botao_entrar = ft.ElevatedButton("Entrar no chat")

        janela = ft.AlertDialog(title=  titulo_janela , content= campo_nome_usuario , actions= [botao_entrar] )   




        def abrir_popup(evento):
        # 5 como exibir essa janela na pagina? 
                pagina.dialog = janela
                janela.open =True
        # 6 toda vez que  fazer uma alteracao visual na pagina atualizar a pagina
                pagina.update()
                print("Clicou no botao")
        #1 botao precisa fazer algo...abrir janela antes do botao iniciar vamos criar funcao
        #2 toda vez que clicar no botao vai usar essa funcao
        #3 agora vamos criar essa fçao
        botao_iniciar = ft. ElevatedButton("Iniciar Chat", on_click= abrir_popup) 

        # colocar essa coisa na pagina
        #adicionar o titulo na pag
        pagina.add(titulo)
        pagina.add(botao_iniciar)
        

# executar o seu sistema
 # ft.app(main)->PADRAO ABRE NORMAL 
ft.app(main, view =ft.WEB_BROWSER) # SE COLOCO VIEW DESSE JEITO VEJO COMO SITE
        
#1h