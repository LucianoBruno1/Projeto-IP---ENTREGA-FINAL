from tkinter import * ##biblioteca para abrir a interace
import pycep_correios
import modulotelaprincipal
from tkinter import messagebox


listaemail = []
listasenha = []
listanome = []


janela = Tk()
janela.title('Login / cadastro')
janela.geometry('700x500')
janela.configure(bg='black')
janela.minsize(width=700, height=500)
janela.state('zoomed')


def janelacadastro():
    telacadastro = Toplevel()
    telacadastro.title('EFETUAR CADASTRO')
    telacadastro.configure(bg='black')
    telacadastro.state('zoomed')
    telacadastro.minsize(width = 700, height = 500)

    botaoprosseguir = Button(telacadastro,text='Prosseguir para Login',command=telacadastro.destroy)
    botaoprosseguir.place(x= 100, y= 300)



     ######## LABELS CADASTRO ##########
    titulo = Label(telacadastro, text='CADASTRO PHOENIX SUSHI',font=('Arial',15,'bold'),bg='red')
    titulo.pack()

    nomecadastro = Label(telacadastro, text='NOME:',font=('Arial',12,'bold'),bg='orange')
    nomecadastro.place(x=100,y=50)

    emailcadastro = Label(telacadastro, text='EMAIL:',font=('Arial',12,'bold'),bg='orange')
    emailcadastro.place(x=100, y=150)

    senhacadastro = Label(telacadastro, text='SENHA:',font=('Arial',12,'bold'),bg='orange')
    senhacadastro.place(x=100, y=250)

    cepcadastro = Label(telacadastro, text='CEP',font=('Arial',12,'bold'),bg='orange')
    cepcadastro.place(x=700, y=45)

    cidadecadastro = Label(telacadastro,text='CIDADE',font=('Arial',12,'bold'),bg='orange')
    cidadecadastro.place(x=700, y=145)

    bairrocadastro = Label(telacadastro,text='BAIRRO',font=('Arial',12,'bold'),bg='orange')
    bairrocadastro.place(x=700, y=245)

    ruacadastro = Label(telacadastro,text='RUA',font=('Arial',12,'bold'),bg='orange')
    ruacadastro.place(x=1150,y=142)

    numerocadastro = Label(telacadastro,text='N°',font=('Arial',12,'bold'),bg='orange')
    numerocadastro.place(x=1150, y=242)

    framecad1 = Frame(telacadastro, width=3,height=410,bg='orange')
    framecad1.place(x=600,y=0)

    framecad2 = Frame(telacadastro,width=1800,height=4,bg='orange')
    framecad2.place(x=0,y=410)



    ############## CAIXAS DE TEXTO CADASTRO ################

    textonome = Entry(telacadastro, bd=3, width = 32, font=('Arial',13,),justify=LEFT)
    textonome.place(x=180,y=48)

    textoemail = Entry(telacadastro, bd=3, width= 32, font=('Arial',13),justify=LEFT)
    textoemail.place(x=180, y=148)

    textosenha = Entry(telacadastro, bd=3, width=32, font=('Arial',13),justify=LEFT)
    textosenha.place(x=180,y=248)

    textocep = Entry(telacadastro, bd=3, width = 32, font=('Arial',13),justify=LEFT)
    textocep.place(x=765, y=43)

    textocidade = Entry(telacadastro,bd=3,width=32,font=('Arial',13),justify=LEFT)
    textocidade.place(x=783,y=142)

    textobairro = Entry(telacadastro, bd=3,width=32,font=('Arial',13),justify=LEFT)
    textobairro.place(x=783, y=242)

    textorua = Entry(telacadastro,bd=3,width=32,font=('Arial',13),justify=LEFT)
    textorua.place(x=1200, y=142)

    textonumero = Entry(telacadastro,bd=3,width=32,font=('Arial',13),justify=LEFT)
    textonumero.place(x=1190, y=242)

    def pegarcep():
        try:
            pegandocep = textocep.get()
            endereco = pycep_correios.get_address_from_cep(pegandocep)

            textocidade.insert(END,endereco['cidade'])
            textobairro.insert(END, endereco['bairro'])
            textorua.insert(END,endereco['logradouro'])

            textocidade ['state'] = DISABLED
            textobairro ['state'] = DISABLED
            textorua ['state'] = DISABLED

        except:
            messagebox.showinfo('CEP Inválido','Digite um CEP válido.')



################   FUNÇÃO PARA SALVAR NOME, EMAIL E SENHA NUM "BANCO DE DADOS"   ###############

    def salvar():

        inseriremail = textoemail.get()
        inserirsenha = textosenha.get()
        inserirnome = textonome.get()
        inserircep = textocep.get()

        if inseriremail == "":
            erro = Label(telacadastro, text='Nenhum campo deve ficar em branco',font=('Arial',12,'bold'),bg='red')
            erro.place(x=100, y=350)


        elif inserirsenha == "":
            erro = Label(telacadastro, text='Nenhum campo deve ficar em branco',font=('Arial',12,'bold'),bg='red')
            erro.place(x=100, y=350)


        elif inserirnome == "":
            erro = Label(telacadastro, text='Nenhum campo deve ficar em branco',font=('Arial',12,'bold'),bg='red')
            erro.place(x=100, y=350)


        elif inserircep == "":
            erro = Label(telacadastro, text='Nenhum campo deve ficar em branco', font=('Arial', 12, 'bold'), bg='red')
            erro.place(x=100, y=350)


        else:
            sucesso = Label(telacadastro,
                            text='Conta registrada com sucesso! Prossiga para o login clicando no botão acima.',
                            font=('Arial', 11, 'bold'), bg='lightgreen')
            sucesso.place(x=10, y=350)
            registrar['state'] = DISABLED


            listaemail.append(inseriremail)
            listasenha.append(inserirsenha)
            listanome.append(inserirnome)



    ####################################################

    registrar = Button(telacadastro,text='REGISTRAR',command=salvar)
    registrar.place(x = 300, y=300)

    botaocep = Button(telacadastro,text='Salvar endereço',command=pegarcep)
    botaocep.place(x=700,y=300)

########### DESIGNS #################

fundo = PhotoImage(file='fundo2.png')
labeltela = Label(janela, image=fundo)
labeltela.pack()

botaoentrar = PhotoImage(file='botaoentrar.png')
botaocadastrar = PhotoImage(file='botaocadastrar.png')


############ caixas de entrada de texto para login ###########

email = Entry(janela, bd=3, width=32, font=('Arial',13),justify=LEFT)
email.place(x=970, y=198)

senha = Entry(janela, show='*', bd=3, width=32, font=('Arial',13),justify=LEFT)
senha.place(x=970, y=366)


def entrar():
    emailget = email.get()
    senhaget = senha.get()


    if emailget in listaemail and senhaget in listasenha:
        logado = Label(text='BEM-VINDO!! Redirecionando para o cardápio.',font=('Arial',14,'bold'),bg='lightgreen')
        logado.place(x=900,y=440)
        janela.destroy()
        modulotelaprincipal.abrirrestaurante()


    else:
        negado = Label(text='Dados inválidos',font=('Arial',14),bg='red')
        negado.place(x=1000,y=440)


##################### DEFININDO AS IMAGENS DOS BOTÕES ####################


buttomentrar = Button(janela, image=botaoentrar,command=entrar)
buttomentrar.place(x=992,y=497)

buttomcadastrar = Button(janela, image=botaocadastrar,command=janelacadastro)
buttomcadastrar.place(x=992, y= 630)


janela.mainloop()