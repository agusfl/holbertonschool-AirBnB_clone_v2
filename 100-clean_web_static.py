#!/usr/bin/python3
"""
Write a Fabric script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives, using the function do_clean:
- Prototype: def do_clean(number=0):
- number is the number of the archives, including the most recent, to keep.
* If number is 0 or 1, keep only the most recent version of your archive.
* if number is 2, keep the most recent, and second most recent versions of your
archive.
* etc.
- Your script should:
* Delete all unnecessary archives (all archives minus the number to keep) in
the versions folder
* Delete all unnecessary archives (all archives minus the number to keep) in
the /data/web_static/releases folder of both of your web servers
- All remote commands must be executed on both of your web servers (using
the env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
"""
from fabric.api import run, env, local
# Seteo environmental variables para los servidores 4390-web-01 and 4390-web-02
env.hosts = ['54.160.237.107', '54.242.209.114']
# Define user as a environmental variable
env.user = "ubuntu"


def do_clean(number=0):
    """
    Function that deletes out-of-date archives, depending of the argument
    passed. By default number is set to 0.
    """
    # Se pasa number a tipo int para poder compararlo en if siguiente con
    # numeros (integers)
    num = int(number)

    if num == 0 or num == 1:
        # Move locally into "versions" folder to be able to remove archives y
        # se encadena comando para eliminar todos los archivos viejos salvo el
        # ultimo,se encadena con ; porque sino tomaba los comandos por separado
        local("cd versions ; rm `ls -t | awk 'NR>1'`")

        # Move to path indicated in command in servers and remove all files
        # except the newest archive
        run("cd /data/web_static/releases ; rm `ls -t | awk 'NR>1'`")

    if number == 2:
        # Move locally into "versions" folder to be able to remove archives y
        # se encadena comando para eliminar todos los archivos viejos salvo los
        # ultimos dos
        local("cd versions ; rm `ls -t | awk 'NR>2'`")

        # Move to path indicated in command in servers and remove all files
        # except the 2 newest archives
        run("cd /data/web_static/releases ; rm `ls -t | awk 'NR>2'`")
