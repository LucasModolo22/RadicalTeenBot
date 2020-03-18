import discord
from discord.utils import get


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

bot = discord.Client()


@bot.event
async def on_ready():
    print('bot online')

@bot.event
async def on_member_join(user):
    await user.add_roles(678463459385540618)

@bot.event
async def on_message(message):
    if message.content.lower().startswith("?r"):
        
        global EkklesiaRole
        EkklesiaID = 678462920862072852
        EkklesiaRole = get(message.guild.roles, id=EkklesiaID)

        global JudahRole
        JudahID = 678463157374550017
        JudahRole = get(message.guild.roles, id=JudahID)

        global MaanaimRole
        MaanaimID = 678463077003427841
        MaanaimRole = get(message.guild.roles, id=MaanaimID)

        global AhavaRole
        AhavaID = 678463327793446913
        AhavaRole = get(message.guild.roles, id=AhavaID)

        global EliteRole
        EliteID = 678463392255705109
        EliteRole = get(message.guild.roles, id=EliteID)

        global TeknongramosRole
        TeknongramosID = 678463256460787732
        TeknongramosRole = get(message.guild.roles, id=TeknongramosID)

        global HovhanessRole
        HovhanessID = 678467646269685761
        HovhanessRole = get(message.guild.roles, id=HovhanessID)

        '''global NullRole
        NullID = 686764850416058378
        NullRole = get(message.guild.roles, id=NullID)'''


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
        '''escolhercelula.add_field(name = "Null", value = ":seven:", inline = True)'''
        global msg_bot
        msg_bot = await message.channel.send(embed = escolhercelula)

        await msg_bot.add_reaction("0️⃣")
        await msg_bot.add_reaction("1️⃣")
        await msg_bot.add_reaction("2️⃣")
        await msg_bot.add_reaction("3️⃣")
        await msg_bot.add_reaction("4️⃣")
        await msg_bot.add_reaction("5️⃣")
        await msg_bot.add_reaction("6️⃣")
        #await msg_bot.add_reaction("7️⃣")


        #Log
        global channel
        global msg_log
        channel = bot.get_channel(686371893007089694)
        msg_log = channel.send

@bot.event
async def on_reaction_add(reaction, user):
    celulas = [EkklesiaRole.id, JudahRole.id, MaanaimRole.id, AhavaRole.id, EliteRole.id, TeknongramosRole.id, HovhanessRole.id] #, NullRole.id]
    if msg_bot.id == reaction.message.id and user.name != msg_bot.author.name:
        verif = True
        for i in range(len(user.roles)):
            if user.roles[i].id in celulas:
                verif = False

        if verif:
            if reaction.emoji == "0️⃣":
                await user.add_roles(EkklesiaRole)
                await msg_log(embed = logentrou(user.name, EkklesiaRole.name))
            elif reaction.emoji == "1️⃣":
                await user.add_roles(HovhanessRole)
                await msg_log(embed = logentrou(user.name, HovhanessRole.name))
            elif reaction.emoji == "2️⃣":
                await user.add_roles(TeknongramosRole)
                await msg_log(embed = logentrou(user.name, TeknongramosRole.name))
            elif reaction.emoji == "3️⃣":
                await user.add_roles(JudahRole)
                await msg_log(embed = logentrou(user.name, JudahRole.name))
            elif reaction.emoji == "4️⃣":
                await user.add_roles(MaanaimRole)
                await msg_log(embed = logentrou(user.name, MaanaimRole.name))
            elif reaction.emoji == "5️⃣":
                await user.add_roles(EliteRole)
                await msg_log(embed = logentrou(user.name, EliteRole.name))
            elif reaction.emoji == "6️⃣":
                await user.add_roles(AhavaRole)
                await msg_log(embed = logentrou(user.name, AhavaRole.name))
            '''elif reaction.emoji == "7️⃣":
                await user.add_roles(NullRole)
                await msg_log(embed = logentrou(user.name, NullRole.name))'''

@bot.event
async def on_reaction_remove(reaction, user):
    if msg_bot.id == reaction.message.id:

        if reaction.emoji == "0️⃣":
            verif = True
            for i in range(len(user.roles)):
                if user.roles[i].id == EkklesiaRole.id:
                    verif = False
            if not verif:
                await user.remove_roles(EkklesiaRole)  
                await msg_log(embed = logsaiu(user.name, EkklesiaRole.name))     
        
        elif reaction.emoji == "1️⃣":
            verif = True
            for i in range(len(user.roles)):
                if user.roles[i].id == HovhanessRole.id:
                    verif = False
            if not verif:
                await user.remove_roles(HovhanessRole)
                await msg_log(embed = logsaiu(user.name, HovhanessRole.name))

        elif reaction.emoji == "2️⃣":
            verif = True
            for i in range(len(user.roles)):
                if user.roles[i].id == TeknongramosRole.id:
                    verif = False
            if not verif:
                await user.remove_roles(TeknongramosRole)
                await msg_log(embed = logsaiu(user.name, TeknongramosRole.name))
        
        elif reaction.emoji == "3️⃣":
            verif = True
            for i in range(len(user.roles)):
                if user.roles[i].id == JudahRole.id:
                    verif = False
            if not verif:
                await user.remove_roles(JudahRole) 
                await msg_log(embed = logsaiu(user.name, JudahRole.name))
        
        elif reaction.emoji == "4️⃣":
            verif = True
            for i in range(len(user.roles)):
                if user.roles[i].id == MaanaimRole.id:
                    verif = False
            if not verif:
                await user.remove_roles(MaanaimRole)
                await msg_log(embed = logsaiu(user.name, MaanaimRole.name))
        
        elif reaction.emoji == "5️⃣":
            verif = True
            for i in range(len(user.roles)):
                if user.roles[i].id == EliteRole.id:
                    verif = False
            if not verif:
                await user.remove_roles(EliteRole)
                await msg_log(embed = logsaiu(user.name, EliteRole.name))
        
        elif reaction.emoji == "6️⃣":
            verif = True
            for i in range(len(user.roles)):
                if user.roles[i].id == AhavaRole.id:
                    verif = False
            if not verif:
                await user.remove_roles(AhavaRole)
                await msg_log(embed = logsaiu(user.name, AhavaRole.name))
        
        '''elif reaction.emoji == "7️⃣":
            verif = True
            for i in range(len(user.roles)):
                if user.roles[i].id == NullRole.id:
                    verif = False
            if not verif:
                await user.remove_roles(NullRole)
                await msg_log(embed = logsaiu(, NullRole.name))'''
    

#bot teste
#bot.run('Njg4MjQzNTcxODY1NjgyMDEw.Xmxgqw.XhjuH_MD00rNAJf9ZTjKuqSlzcs')

#bot normal
bot.run('Njg2NzU0NTU5NTMxNDE3NjEx.XmcVXQ.JlCDQUiBkgFVw8-hqmMELI4IoRw')