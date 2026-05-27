from django.shortcuts import render

def home(request):
    contexto = {
        "home": {
            "botao_texto": "Conheça a turma do mistério"
        }
    }
    return render(request, "home.html", contexto)

def inicio(request):
    contexto = {
        "inicio": {
            "origem": "O desenho Scooby-Doo estreou em 13 de setembro de 1969 na CBS, criado por Joe Ruby e Ken Spears e produzido originalmente pela Hanna-Barbera. A motivação da emissora era oferecer uma animação divertida, mas que fosse considerada adequada por grupos de pais preocupados com a violência nos desenhos da época. O nome “Scooby-Doo” surgiu inspirado em um trecho da música Strangers in the Night, de Frank Sinatra, onde ele canta “Dooby Dooby Doo”. Escute agora:",
            "series": [
                "Scooby-Doo, Cadê Você? (1969–1970)",
                "Os Novos Filmes de Scooby-Doo (1972–1974)",
                "Scooby-Doo e Scooby-Loo (1979–1980)",
                "Os 13 Fantasmas de Scooby-Doo (1985)",
                "O Que Há de Novo, Scooby-Doo? (2002–2006)",
                "Scooby-Doo! Mistério S/A (2010–2013)",
                "A Pup Named Scooby-Doo (1988–1991) – versão infantil, mostrando a turma criança",
                "What's New, Scooby-Doo? Filmes especiais (2003–2009) – longa-metragens derivados da série moderna",
                "Be Cool, Scooby-Doo! (2015–2018) – estilo mais cartunesco e humor leve"
            ],
            "filmes": "Os filmes e expansões da franquia marcaram uma nova fase para Scooby-Doo: títulos como Scooby-Doo on Zombie Island (1998), Scooby-Doo and the Witch’s Ghost (1999), além das adaptações em live-action Scooby-Doo (2002) e Scooby-Doo 2 (2004) ajudaram a renovar o interesse do público. A partir de 2001, a produção passou para a Warner Bros., que consolidou a marca e ampliou seu alcance. Hoje, a franquia soma mais de 550 episódios e dezenas de filmes, exibidos em diversos países, incluindo o Brasil, e continua sendo lembrada por bordões clássicos como: “Eu teria conseguido se não fossem essas crianças xeretas e esse cachorro idiota!”."
        }
    }
    return render(request, "inicio.html", contexto)

def elenco(request):
    elenco = [
        {"nome": "Scooby-Doo", "descricao": "O grande danado que ama biscoitos Scooby e sempre se mete em confusão junto com Salsicha.", "img": "img/scooby-doo.png", "foto": "img/foto-scooby.jpg", "audio": "musica/scooby.mp3", "dublador": "Orlando Drummond"},
        {"nome": "Salsicha Rogers", "descricao": "Melhor amigo de Scooby, comilão e medroso, mas sempre fiel ao grupo.", "img": "img/salsicha.png", "foto": "img/foto-salsicha.jpg", "audio": "musica/salsicha.mp3", "dublador": "Mário Monjardim"},
        {"nome": "Daphne Blake", "descricao": "Amante da moda, corajosa e muitas vezes chamada de arruma-encrenca.", "img": "img/daphne.png", "foto": "img/foto-daphne.jpg", "audio": "musica/daphne.mp3", "dublador": "Miriam Ficher"},
        {"nome": "Velma Dinkley", "descricao": "A mente brilhante da equipe, sempre com soluções lógicas e rápidas.", "img": "img/velma.png", "foto": "img/foto-velma.jpg", "audio": "musica/velma.mp3", "dublador": "Maria Helena Pader"},
        {"nome": "Fred Jones", "descricao": "Líder nato, especialista em armadilhas e sempre pronto para investigar.", "img": "img/fred.png", "foto": "img/foto-fred.jpg", "audio": "musica/fred.mp3", "dublador": "Garcia Júnior"},
        # aqui você pode adicionar os outros até completar 11
    ]
    return render(request, "elenco.html", {"elenco": elenco})

def sobre(request):
    contexto = {
        "site": {
            "descricao": "Este site foi desenvolvido com muito mistério, e uma noite sem dormir. Criado por Hemerson Daniel. O objetivo é celebrar o universo de Scooby-Doo, trazendo curiosidades, elenco e homenagens aos dubladores que marcaram gerações. Feito com HTML, CSS, JavaScript e Django, porque até o Scooby precisa de um framework para resolver mistérios. Agradecemos a todos (eu mesmo) que contribuíram e principalmente ao café, que manteve o desenvolvedor acordado. ☕",
            "autor": "Hemerson Daniel",
            "github": "https://github.com/ohemesx",
            "objetivo": "Celebrar o universo de Scooby-Doo, trazendo curiosidades, elenco e homenagens aos dubladores que marcaram gerações.",
            "tecnologias": "HTML, CSS, JavaScript e Django",
            "agradecimento": "ao café ☕",
            "cores": ["rgb(57,1,88)", "#ff9100", "yellow", "#f4f46c"],
            "fontes": "Creepster, Open Sans, Arial",
            "fontes_consultadas": [
                {"nome": "Scooby-Doo Fandom Wiki", "url": "https://scoobydoo.fandom.com/wiki/Scooby-Doo_Wiki"},
                {"nome": "Warner Bros - Scooby-Doo", "url": "https://www.warnerbros.com/tv/scooby-doo"},
                {"nome": "Wikipedia - Scooby-Doo", "url": "https://pt.wikipedia.org/wiki/Scooby-Doo"},
            ]
        }
    }
    return render(request, "sobre.html", contexto)
