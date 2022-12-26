#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from
the contents of the web_static folder"""
from fabric.api import *
from datetime import datetime
import os
env.hosts = ['100.25.31.96', "107.23.94.25"]


def do_clean(number=0):
    """generates a .tgz archive from the contents of the web_static"""
    files_ = os.listdir("versions")
    files_.sort(reverse=True)
    present = len(files_)

    # if number is greter or equal to present file, do nothing
    if number >= present:
        return

    # If number is 0 or 1, keep only the most recent version of your archive
    if number == 0:
        number = 1
    num_del = present - number
    point = -1
    for i in range(num_del):
        local("rm versions/{}".format(files_[point]))
        point -= 1
    """
    Delete all unnecessary archives (all archives
    minus the number to keep) in the /data/web_static/releases
    folder of both of your web servers
    """
    with cd("/tmt"):
        run("ls -t -r | head -n -{} | sudo xargs rm".format(number))
