#!/usr/bin/python3
"""
This module contains a script that generates .tgz archive from
the contents of th web_static folder of my AirBnB Clone repo
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """
    This fabric generates the .tgz archive from the web_static
    """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    r = local("sudo tar -cvzf {} web_static".format(filename))
    if r.succeeded:
        return filename
    else:
        return None
