# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from main_startup.config_var import Config
from main_startup.core.decorators import friday_on_cmd, listen
from main_startup.helper_func.basic_helpers import edit_or_reply, get_text
from os import environ, execle, path, remove
from git import Repo
from datetime import datetime
import heroku3
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from main_startup.helper_func.logger_s import LogIt
from main_startup.core.startup_helpers import run_cmd

REPO_ = Config.UPSTREAM_REPO
BRANCH_ = Config.U_BRANCH


@friday_on_cmd(["update"],
  cmd_help={
    "help": "Update Your UserBot!",
    "example": "{ch}update"
    })
async def update_it(client, message):
    msg_ = await edit_or_reply(message, "`Updating Please Wait!`")
    try:
        repo = Repo()
    except InvalidGitRepositoryError:
        repo = Repo.init()
    if "upstream" in repo.remotes:
        origin = repo.remote("upstream")
    else:
        origin = repo.create_remote("upstream", REPO_)
    origin.fetch()
    repo.create_head(Config.U_BRANCH, origin.refs.master)
    repo.heads.master.set_tracking_branch(origin.refs.master)
    repo.heads.master.checkout(True)
    if repo.active_branch.name != Config.U_BRANCH:
        await msg_.edit(f"`Seems Like You Are Using Custom Branch - {repo.active_branch.name}! Please Switch To {Config.U_BRANCH} To Make This Updater Function!`")
        return
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(Config.U_BRANCH)
    if not Config.HEROKU_URL:
        try:
            ups_rem.pull(Config.U_BRANCH)
        except GitCommandError:
            repo.git.reset('--hard', 'FETCH_HEAD')
        await run_cmd('pip3 install --no-cache-dir -r requirements.txt')
        await msg_.edit("`Updated Sucessfully! Give Me A min To Restart!`")
        args = [sys.executable, "-m", "main_startup"]
        execle(sys.executable, *args, environ)
        return
    else:
        await msg_.edit("`Heroku Detected! Pushing, Please Halt!`")
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(Config.HEROKU_URL)
        else:
            remote = repo.create_remote("heroku", Config.HEROKU_URL)
        try:
            remote.push(refspec="HEAD:refs/heads/master", force=True)
        except BaseException as error:
            return await msg_.edit(f"**Updater Error** \nTraceBack : `{error}`")
        await msg_.edit("`Build Started! Please Wait For 10-15 Minutes!`")
