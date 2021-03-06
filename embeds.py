import discord
from discord.utils import get



#Funções LOG
def logentrou(nome, celula):
    log = discord.Embed(
        title = f"{nome} entrou em {celula}",
        color = 0x008000
    )
    return log

def logsaiu(nome, celula):
    log = discord.Embed(
        title = f"{nome} saiu de {celula}",
        color = 0xFF0000
    )
    return log



#Função Escolher Celula
def escolhercelula():
    escolhercelula = discord.Embed(
        title = "Seleciona a sua Célula:",
        color = 0xFFFAFA
    )
    escolhercelula.add_field(name = "🦁 Ekklesia", value = ":zero:", inline = True)
    escolhercelula.add_field(name = "🦅 Hovhaness", value = ":one:", inline = True)
    escolhercelula.add_field(name = "🌲 Teknongramos", value = ":two:", inline = True)
    escolhercelula.add_field(name = "🦁 Judah", value = ":three:", inline = True)
    escolhercelula.add_field(name = "🐺 Maanaim", value = ":four:", inline = True)
    escolhercelula.add_field(name = "🦅 Elite", value = ":five:", inline = True)
    escolhercelula.add_field(name = "🧡 Ahava", value = ":six:", inline = True)
    '''escolhercelula.add_field(name = "Makarias", value = ":seven:", inline = True)'''

    escolhercelula.set_footer(text = 'Qualquer dúvida digite .help "mensagem"')
    return escolhercelula

#Comandos
def comandoshelp():
    comandoshelp = discord.Embed(
        title = f"Comandos",
        color = 0xFFFAFA
    )

    comandoshelp.add_field(name = '.r', value = 'Aparece um novo bloco de escolher celula.\nEx: .r', inline = False)
    comandoshelp.add_field(name = '.anuncio', value = 'Faz anúncios com o bot.\nEx: .anuncio (posição do canal (.canaisdetexto)) "Titulo" "Mensagem" Url', inline = False)
    comandoshelp.add_field(name = '.clear', value = 'Apaga a quantidade de mensagens que você deseja.\nEx: .clear (numero ou all)', inline = False)
    comandoshelp.add_field(name = '.disc', value = 'Mostra o link do discord.\nEx: .disc', inline = False)
    comandoshelp.add_field(name = '.canal', value = 'Mostra a posição do canal de voz atual.\nEx: .canal', inline = False)
    comandoshelp.add_field(name = '.canais', value = 'Mostra a posição dos canais de voz e de texto.\nEx: .canais', inline = False)
    comandoshelp.add_field(name = '.canaisdevoz', value = 'Mostra a posição dos canais de voz.\nEx: .canaisdevoz', inline = False)
    comandoshelp.add_field(name = '.canaisdetexto', value = 'Mostra a posição dos canais de texto.\nEx: .canaisdetexto', inline = False)
    comandoshelp.add_field(name = '.mute', value = 'Silencia ou "diselencia" o canal de voz inteiro em que você está.\nEx: .mute (posição(.canaisdevoz)) on/off', inline = False)
    comandoshelp.add_field(name = '.move', value = 'Move usuários de um canal de voz para outro.\nEx: .move "de canal(posição(.canaisdevoz))" "para canal(posição(.canaisdevoz))"', inline = False)
        
    return comandoshelp

def anuncioembed(titulo, mensagem, url):
    anuncio = discord.Embed(
        title = f"{titulo}",
        color = 0xFF0000,
        description = f"{mensagem}",
    url=url).set_image(url=url)
    return anuncio

def muteon(channel):
    embed = discord.Embed(
        title=f"Todos os usuários do canal |{channel}| foram MUTADOS",
        color = 0xFFFAFA
    )
    return embed

def muteoff(channel):
    embed = discord.Embed(
        title=f"Todos os usuários do canal |{channel}| foram DESMUTADOS",
        color = 0xFFFAFA
    )
    return embed

def canalvoz(ctx):
    msg_final = ''
    for channel in ctx.guild.voice_channels:
        msg_final += f'\n{channel.position}° | {channel.name}'
    embed = discord.Embed(
        title = f'\tCanais de Voz',
        description = f'{msg_final}',
        color = 0xFFFAFA
    )
    return embed

def canaltexto(ctx):
    msg_final = ''
    for channel in ctx.guild.text_channels:
        msg_final += f'\n{channel.position}° | {channel.name}'
    embed = discord.Embed(
        title = f'\tCanais de Texto',
        description = f'{msg_final}',
        color = 0xFFFAFA
    )
    return embed

def canalatual(ctx):
    msg_final = ''
    for channel in ctx.guild.voice_channels:
        if ctx.author.voice.channel == channel:
            msg_final += f'\n{channel.position}° | {channel.name}'
    embed = discord.Embed(
        title = f'\tCanal de Voz Atual',
        description = f'{msg_final}',
        color = 0xFFFAFA
    )
    return embed

def msgclear(n):
    if n == 0:
        embed = discord.Embed(
            title = f"🧹 Nenhuma mensagem foi apagada",
            color = 0xFFFAFA
        )
    elif n == 1:
        embed = discord.Embed(
            title = f"🧹 Uma mensagem foi apagada.",
            color = 0xFFFAFA
        )
    else:
        embed = discord.Embed(
            title = f"🧹 {n} mensagens foram apagadas.",
            color = 0xFFFAFA
        )
    return embed

def helpembed(ctx, msg):
    embed = discord.Embed(
        title = f'{ctx.author} abriu um pedido de ajuda com a seguinte mensagem:',
        description = f'{msg}.',
        color = 0xFFFAFA
    )
    embed.add_field(name = 'Atenção', value = 'Se você conseguir resolver, clique no emoji ✅. Se não clique no ❌.', inline = False)
    return embed

def loghelp(ctx):
    embed = discord.Embed(
        title = f"{ctx.author} abriu um pedido de ajuda.",
        color = 0xFF0000
    )

    return embed

def msghelp(ctx):
    embed = discord.Embed(
        title = f"{ctx.author.name}, seu pedido de ajuda foi registrado. Em breve seu problema será resolvido. Você será avisado.",
        color = 0xFF0000
    )

    return embed

def resolvidomsg(ctx):
    embed = discord.Embed(
        title = f"{ctx.author.name}, seu problema foi resolvido.",
        color = 0x008000
    )

    return embed

def nresolvidomsg(ctx):
    embed = discord.Embed(
        title = f"O pedido de ajuda de {ctx.author.name} não foi resolvido.",
        color = 0xFF0000
    )

    return embed

def resolvido(ctx, msg):
    embed = discord.Embed(
        title = f'Pedido de {ctx.author} foi resolvido!',
        description = f'{msg}.',
        color = 0x008000
    )
    embed.set_image(url = 'https://www.easyvest.com.br/wp-content/uploads/2013/08/dwcheckyes.png')
    return embed

def nresolvido(ctx, msg):
    embed = discord.Embed(
        title = f'Pedido de {ctx.author} não resolvido! Caso enviado para Módolo',
        description = f'{msg}.',
        color = 0x008000
    )
    embed.set_image(url = 'https://pngimage.net/wp-content/uploads/2018/06/x-png-4.png')
    return embed



#Mensagens e erros
def possuicelula(nome):
    possuicelula = discord.Embed(
            title = f"{nome}, você já está em outra célula. Só é possível estar em uma de cada vez.",
            color = 0xFFFAFA
    )
    
    return possuicelula

def mesmacelula(nome):
    mesmacelula = discord.Embed(
            title = f"{nome}, você já está nessa célula. Para sair dela, clique novamente.",
            color = 0xFFFAFA
    )

    return mesmacelula

def bemvindo(user):
    bemvindo = discord.Embed(
        title = f"{user.name}, Bem-Vindo(a) ao discord do Radical Teen! Selecione a sua célula",
        color = 0xFFFAFA
    )
    return bemvindo

def sempermissao():
    embed = discord.Embed(
        title = f"Você não tem permissão para usar esse comando.",
        color = 0xFF0000
    )
    return embed

# def zoom(user):
#     embed = discord.Embed(
#         title = f"Na Na Ni Na Não, {user}!\nEspalhe o discord para a galera:\nhttps://discord.gg/AR3mQbQ",
#         color = 0xFF0000
#     )
#     return embed

def usoincorreto():
    embed = discord.Embed(
        title=f"Comando usado de forma incorreta. Para mais informações tente .comandos",
        color = 0xFF0000
    )
    return embed

def botreiniciando():
    embed = discord.Embed(
        title=f"O bot está reiniciando, aguarde um momento.",
        color = 0xFFFF00
    )
    return embed

def discor():
    embed = discord.Embed(
        title = f"📢 Espalhe o discord para a galera! \nhttps://discord.gg/AR3mQbQ",
        color = 0xFFFAFA
    )
    return embed

def discor1():
    embed = discord.Embed(
        title = f"📢 Convide seus amigos para cá! \nhttps://discord.gg/AR3mQbQ",
        color = 0xFFFAFA
    )
    return embed

def errorcomando():
    embed = discord.Embed(
        title = f"Esse comando não existe.",
        color = 0xFF0000
    )

    embed.add_field(name = '.comandos', value = 'Para mais comandos', inline = False)
    return embed