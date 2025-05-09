import logging
import time
from typing import TYPE_CHECKING

from discord.ext import commands
from tortoise import Tortoise
from discord import app_commands, Interaction
from .chanceme import get_chanceme_response, create_groq_client

log = logging.getLogger("ballsdex.core.commands")

if TYPE_CHECKING:
    from .bot import BallsDexBot

class Core(commands.Cog):
    """
    Core commands of BallsDex bot
    """

    def __init__(self, bot: "BallsDexBot"):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """
        Ping!
        """
        await ctx.send("Pong")

    @commands.command()
    @commands.is_owner()
    async def reloadtree(self, ctx: commands.Context):
        """
        Sync the application commands with Discord
        """
        await self.bot.tree.sync()
        await ctx.send("Application commands tree reloaded.")

    async def reload_package(self, package: str, *, with_prefix=False):
        try:
            try:
                await self.bot.reload_extension(package)
            except commands.ExtensionNotLoaded:
                await self.bot.load_extension(package)
        except commands.ExtensionNotFound:
            if not with_prefix:
                return await self.reload_package("ballsdex.packages." + package, with_prefix=True)
            raise

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, package: str):
        """
        Reload an extension
        """
        try:
            await self.reload_package(package)
        except commands.ExtensionNotFound:
            await ctx.send("Extension not found.")
        except Exception:
            await ctx.send("Failed to reload extension.")
            log.error(f"Failed to reload extension {package}", exc_info=True)
        else:
            await ctx.send("Extension reloaded.")

    @commands.command()
    @commands.is_owner()
    async def reloadcache(self, ctx: commands.Context):
        """
        Reload the cache of database models.

        This is needed each time the database is updated, otherwise changes won't reflect until
        next start.
        """
        await self.bot.load_cache()
        await ctx.message.add_reaction("✅")

    @commands.is_owner()
    @app_commands.checks.cooldown(1, 30.0)
    @app_commands.command(name="chanceme", description="Get your definitely accurate chanceme here")
    async def chanceme(self, interaction: Interaction, user_input: str):
        # response_message = f"{interaction.user.mention} Your input was: {user_input}. whts up lil bro lock in goofy ahh ecs i swear"
        client = create_groq_client()
        response_message = get_chanceme_response(client, user_input)
        if response_message is None:
            response_message = "Sorry, I couldn't generate a response. Please reduce the size of your chanceme and try again."
        response = f"{interaction.user.mention}, here's your roast: \n {response_message}"
        await interaction.response.send_message(response_message, ephemeral=False)
        # time.sleep(60)

    @commands.command()
    @commands.is_owner()
    async def analyzedb(self, ctx: commands.Context):
        """
        Analyze the database. This refreshes the counts displayed by the `/about` command.
        """
        connection = Tortoise.get_connection("default")
        t1 = time.time()
        await connection.execute_query("ANALYZE")
        t2 = time.time()
        await ctx.send(f"Analyzed database in {round((t2 - t1) * 1000)}ms.")