import discord
from discord import slash_command, option
from discord.ext import commands

from utilities.database import modifier


class Blacklist(discord.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @slash_command()
    @commands.is_owner()
    @option("server", discord.Guild, description="The server to blacklist")
    @option("reason", str, description="The reason for the blacklist")
    async def blacklist(self, ctx, server, reason):
        """ Blacklist a server from the bot """
        await modifier("INSERT IGNORE INTO blacklist (guild_id, reason) VALUES (%s, %s)", [server.id, reason])
        guild = self.bot.get_guild(server.id)
        await guild.leave()
        await ctx.respond(f'Successfully added guild {server} to the blacklist for:\n**{reason}**')


def setup(bot: discord.Bot):
    bot.add_cog(Blacklist(bot))
