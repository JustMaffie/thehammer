"""
    The Hammer
    Copyright (C) 2018 JustMaffie

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from discord.ext import commands
import discord
import asyncio
from thehammer.decorators import is_owner
from thehammer.module import Module

class Admin(Module):
    @is_owner()
    @commands.command()
    async def reload(self, ctx, module):
        try:
            result = self.bot.unload_extension(module)
            if result == False:
                return await ctx.send("Module {module} does not exist!".format(module=module))
            self.bot.load_extension(module)
        except Exception as e:
            await ctx.send("An error occurred while reloading {module}\n``{e}``".format(module=module,e=e))
        else:
            await ctx.send("Module {module} reloaded successfully".format(module=module))

    @is_owner()
    @commands.command()
    async def shutdown(self, ctx):
        try:
            await ctx.send("Shutting down...")
        except:
            pass
        await self.bot.logout()

    @is_owner()
    @commands.command()
    async def load(self, ctx, module):
        try:
            result = self.bot.load_extension(module)
            if result == False:
                return await ctx.send("Module {module} does not exist!".format(module=module))
        except Exception as e:
            return await ctx.send("An error occurred while loading {module}\n{e}".format(module=module,e=e))
        return await ctx.send("Module {module} loaded successfully".format(module=module))

    @is_owner()
    @commands.command()
    async def unload(self, ctx, module):
        try:
            result = self.bot.unload_extension(module)
            if result == False:
                return await ctx.send("Module {module} does not exist!".format(module=module))
        except Exception as e:
            return await ctx.send("An error occurred while loading {module}\n{e}".format(module=module,e=e))
        return await ctx.send("Module {module} loaded successfully".format(module=module))

    # Thanks red
    @staticmethod
    def cleanup_code(content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    @staticmethod
    def sanitize_output(ctx: commands.Context, input_: str) -> str:
        """Hides the bot's token from a string."""
        token = ctx.bot.http.token
        r = "[EXPUNGED]"
        result = input_.replace(token, r)
        result = result.replace(token.lower(), r)
        result = result.replace(token.upper(), r)
        return result

    @staticmethod
    def get_syntax_error(e):
        """Format a syntax error to send to the user.
        Returns a string representation of the error formatted as a codeblock.
        """
        if e.text is None:
            return '```py\n{0.__class__.__name__}: {0}```'.format(e)
        return "```py\n{0.text}{1:>{0.offset}}\n{2}: {0}".format(e, '^', type(e).__name__)

    @commands.command(name='eval')
    @is_owner()
    async def _eval(self, ctx, *, body: str):
        env = {
            'bot': ctx.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            'discord': discord,
            'commands': commands
        }

        code = self.cleanup_code(body)

        try:
            result = eval(code, env)
        except SyntaxError as e:
            await ctx.send(self.get_syntax_error(e))
            return
        except Exception as e:
            await ctx.send('```py\n{}: {!s}```'.format(type(e).__name__, e))
            return

        if asyncio.iscoroutine(result):
            result = await result

        result = self.sanitize_output(ctx, str(result))

        await ctx.channel.send("```py\n{}```".format(result))

def setup(bot):
    bot.load_module(Admin)
