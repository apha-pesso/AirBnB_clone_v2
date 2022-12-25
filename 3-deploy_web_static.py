#!/usr/bin/python3
"""Fabric script for full deployment"""
from fabric.api import *
from datetime import datetime
# Import the do_pack and do_deploy function
packer = __import__('1-pack_web_static').do_pack
deployer = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ['100.25.31.96', "107.23.94.25"]
# env.hosts = ['100.25.31.96']


def deploy():
    """Fabric script that creates and distributes an archive
    to your web servers"""
    # call the do_pack function
    path = packer()
    if not path:
        return False
    ret = deployer(path)
    return (ret)
