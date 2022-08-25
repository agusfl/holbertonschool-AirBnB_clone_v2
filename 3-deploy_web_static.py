#!/usr/bin/python3
"""
Write a Fabric script that creates and distributes an archive to your web
servers, using the function deploy:
- Prototype: def deploy():
- The script should take the following steps:
* Call the do_pack() function and store the path of the created archive
* Return False if no archive has been created
* Call the do_deploy(archive_path) function, using the new path of the new
archive
* Return the return value of do_deploy
- All remote commands must be executed on both of web your servers (using
env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
- You must use this script to deploy it on your servers: xx-web-01 and
xx-web-02
"""
from fabric.api import run, put, env
from os.path import exists  # To check if a file exists
# Seteo environmental variables para los servidores 4390-web-01 and 4390-web-02
env.hosts = ['54.160.237.107', '54.242.209.114']
# Define user as a environmental variable
env.user = "ubuntu"
# import do_pack() function from task 1
do_pack = __import__('1-pack_web_static').do_pack
# import function from task 2
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """
    Creates and distributes an archive to your web servers.
    """
    # Call the do_pack() function made in task 1 to create path of archive
    path = do_pack()

    # Return False if no archive has been created
    if exists(path) is False:
        return False

    # Call the do_deploay function (made in task 2) with the new path
    deploy = do_deploy(path)
    return deploy
