# coding: utf-8
from yattag import Doc
from yattag import indent

version = ("1.0.0")

doc, tag, text = Doc().tagtext()


nom = input("Entrez le nom de ce QCM\n")
nom=str(nom)

UE = input("Veuillez saisir l'UE (uniquement la valeur numérique sans le point)\nExemple:\n      \"1.1 Psychologie, sociologie, anthropologie\" ==> 11:\n")

nbQ = input("\nCombien de questions souhaitez-vous mettre dans ce QCM ?\n")

doc.asis('<!DOCTYPE html>')
with tag('html', 'lang=\'fr\''):
    with tag('head'):
        doc.asis('<meta charset=\"utf-8\">')
        doc.asis('<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">')
        doc.asis('<title>QCM Stell - QCM</title>')
        doc.asis('<link rel="icon" href="">') #Modifier ici pour le favicon
        doc.asis('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.4/css/bulma.min.css">')
        doc.asis('<script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>')
        doc.asis('<link rel="stylesheet" href="Uyolo.css">')
        with tag('script', language='JavaScript'):
            doc.asis("\nfunction test(nom,n) {\n  var rep=true;\n  for (i=0; i<n; i++) {\n   if (nom[i].value==1 && nom[i].checked==false) rep=false;\n   if (nom[i].value==0 && nom[i].checked==true) rep=false;\n  }\n  return rep;\n }\n")
        with tag('script'):
            doc.asis("function openCity(cityName, elmnt, color) {\nvar i, tabcontent, tablinks;\ntabcontent = document.getElementsByClassName(\"tabcontent\");\nfor (i = 0; i < tabcontent.length; i++) {\n   tabcontent[i].style.display = \"none\";\n}\ntablinks = document.getElementsByClassName(\"tablink\");\nfor (i = 0; i < tablinks.length; i++) {\n     tablinks[i].style.backgroundColor = \"\";\n}\ndocument.getElementById(cityName).style.display = \"block\";\nelmnt.style.backgroundColor = color;\n}\ndocument.getElementById(\"defaultOpen\").click();")


    with tag('body'):
        with tag('div', id='container', style='margin:1%'):
            doc.stag('img',style='width:30%', src='https://media.discordapp.net/attachments/363315461087166466/551534610417319956/NUQxRjh6UDF2SEo0cFIwTEM1L3ZJdz09LS1sc09ZNXRaOWZLL0F3THk2aDRFM3lRPT0_--1dcac6de567f8b6d316709faf1516f.png')

        with tag('div', id='navbarMenuHeroA', klass="navbar-menu", style="background-color: #80C18E;"):
            with tag('div', klass="navbar-end", style="background-color: #80C18E;"):
                with tag('a', style="margin-right:10%; margin-left:10%", klass="navbar-item is-active", href="index.html"):
                    doc.stag('img', src="home.svg")

# Fil d'Arianne
        with tag('section', klass='container', style='margin-top:1%'):
            with tag('nav', klass='breadcrumb'):
                with tag('ul'):
                    with tag('li'):
                        with tag('a', href="../index.html"):
                            text('Home')
                    with tag('li'):
                        with tag('a', href="UE.html"):
                            text(UE)
                        with tag('li', klass="is-active"):
                            with tag('a', href="#"):
                                text(nom)

# Titre
        with tag('section', klass='content is-large'):
            with tag('h1', style="text-align:center"):
                text(nom)

# Questionnaire
        with tag('section', id='question', klass="container"):
            doc.stag('hr')
            nbQ=int(nbQ)
            for j in range (0,nbQ):
                with tag('form', name=nom):
                    question = input("\n\n\nDonnez la question:\n")
                    with tag('div', klass='content is-medium'):
                        with tag('p'):
                            with tag('b'):
                                text("Question :")
                        with tag('p'):
                            text(question)
                    nbR = input("Combien de réponses possibles ?\n")
                    nbR=int(nbR)
                    for i in range (0,nbR):
                        reponse=input("\nProposez la réponse:\n")
                        v=input("est-elle une bonne réponse ? 1 -> oui | 0 -> non\n")
                        doc.stag('br')
                        with tag('input', type='checkbox', name='choix', value=v):
                            text(reponse)
                    nbRc=str(nbR)
                    jQ=str(j+1)
                    doc.stag('br')
                    doc.stag('br')
                    a=("if (test(choix,"+nbRc+")) {\nalert('Bonne réponse.')\nopenCity('"+jQ+"', this, '#606c76')}\nelse {alert('Reponse fausse.')}")
                    with tag('input', type="button", name="bouton", value="check", onclick=a):
                        text("")
                    with tag('div', id=jQ, klass="tabcontent"):
                        with tag('h1'):
                            text('Correction')
                        corr=input("Entrez la correction de la question:\n")
                        with tag('p'):
                            text(corr)

        with tag('section', klass='footer'):
            with tag('div', id="footer", style="text-align:center"):
                with tag('p'):
                    text("Tout droit reservé | Framework : bulma.io | Généré par QCMaker")
                with tag('a', href="https://github.com/gnouf1/QCM-Maker"):
                    text(version)

result = indent(doc.getvalue())
Q="QCM/"
nom = Q + UE + nom + ".html"
fichier = open(nom, "w", encoding = "utf-8") #Ne jamais enlever ça
fichier.write(result)
fichier.close()
input('Appuyez sur ENTREE pour quitter')
