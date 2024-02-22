#!/usr/bin/python3
"""
This is a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the
function do_deploy
"""
from fabric.api import *
from datetime import datetime
from os.path 


env.hosts = ['54.296.35.48', '34.299.66.60']


def do_deploy(archive_path):
    """
    This distributes an archive to a web server
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if exists(archive_path) is False:
        return False
    filename = archive_path.split('/')[-1]

    no_tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])

    tmp = "/tmp/" + filename

    try:
        put(archive_path, "/tmp/")

        run("mkdir -p {}/".format(no_tgz))

        run("tar -xzf {} -C {}/".format(tmp, no_tgz))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
        run("rm -rf {}/web_static".format(no_tgz))
        run("rm -rf /data/web_static/current")

        run("ln -s {}/ /data/web_static/current".format(no_tgz))

        return True
    except:
        return False
