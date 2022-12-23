#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from
the contents of the web_static folder"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    local('mkdir -p versions')
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "web_static_{}.tgz".format(time)
    file_name = "versions/{}".format(name)
    location = local('tar -cvzf file_name web_static')
    if location:
        return (location)
    else:
        return None
