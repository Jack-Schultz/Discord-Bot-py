import discord
from discord.ext import commands
import os
import json

# Get the absolute path to the config.json
base_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # One level up
config_path = os.path.join(base_directory, 'config.json')
# Load the configuration from config.json
with open(config_path) as config_file:
    config = json.load(config_file)


class UtilCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def ping(self, ctx: commands.Context):
        """Responds with 'pong' to check bot responsiveness."""
        await ctx.send('pong')

    @discord.app_commands.command(
        name="support",
        description="Get a link to the support server",
    )
    async def support(self, interaction: discord.Interaction):
        """Command to supply the support server link"""
        embed = discord.Embed(
            title="Thanks for reaching out!",
        )
        view = discord.ui.View()
        view.add_item(
            discord.ui.Button(
                label="Support Server",
                url=f"{config['support_server']}",
            )
        )
        await interaction.response.send_message(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(UtilCog(bot))
