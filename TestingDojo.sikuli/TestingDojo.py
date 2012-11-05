def acessaGmailFF():
    openApp("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    wait("aboubhome-3.png", 10)
    click("aboubhome-3.png")
    type("l", KeyModifier.CTRL)
    paste("www.gmail.com.br")
    type(Key.ENTER)
    wait("Gmail-2.png", 15)
    assert exists ("Gmail-2.png"), "Deveria gmail estar habilitado!"

def testLoginInvalido():
    paste("Nomedeusuric.png", "cwi.teste1@gmail.com")
    type("Senha.png", "invalido")
    click("1348843243449.png")
    assert exists ("Oncmedeusuri.png"), "Deveria ter exibido a mensagem de erro!"

def testLoginValido():
    type("Senha.png", "cwi.teste1")
    click("1348843243449.png")
    wait ("Entradacwite.png",10)
    assert exists("Entradacwite.png"),"Deveria ter acessado o email!"

def testEnviaEmailSemDest():
    click(Pattern("botaoEscrever.png").similar(0.81).targetOffset(-24,0))
    wait("1348844371745.png",15)
    click("1348844371745.png")
    assert exists ("ErroEspecifi.png"), "Deveria ter aparecido a mensagem de erro!"


if __name__ == "__main__":
    acessaGmailFF()
    testLoginInvalido()
    testLoginValido()
    testEnviaEmailSemDest()
    
