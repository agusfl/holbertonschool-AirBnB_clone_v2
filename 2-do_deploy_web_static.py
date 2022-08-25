#!/usr/bin/python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy:
- Prototype: def do_deploy(archive_path):
- Returns False if the file at the path archive_path doesn’t exist
- The script should take the following steps:
* Upload the archive to the /tmp/ directory of the web server
* Uncompress the archive to the folder /data/web_static/releases/<archive
filename without extension> on the web server
* Delete the archive from the web server
* Delete the symbolic link /data/web_static/current from the web server
* Create a new the symbolic link /data/web_static/current on the web server,
linked to the new version of your code (/data/web_static/releases/<archive
filename without extension>)
- All remote commands must be executed on your both web servers (using
env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
- Returns True if all operations have been done correctly, otherwise returns
False
- You must use this script to deploy it on your servers: xx-web-01 and
xx-web-02
"""
from fabric.api import run, put, env
from os.path import exists  # To check if a file exists
# Seteo environmental variables para los servidores 4390-web-01 and 4390-web-02
env.hosts = ['54.160.237.107', '54.242.209.114']
# Define user as a environmental variable
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    Extract files from archive and deploy on the web server.
    """
    if exists(archive_path) is False:
        return False
    try:
        # upload the archive to /tmp
        put(archive_path, "/tmp/")
        # Nombre del archivo CON la extension (.tgz)
        filename = archive_path.split("/")[1]
        # Nombre del archivo SIN la extension
        filename_no_ext = filename.split(".")[0]
        # Ruta completa hacia el archivo SIN extension
        path = "/data/web_static/releases/" + filename_no_ext + "/"
        # Create directory if not exits already
        run("mkdir -p " + path)
        # Uncompress archive that was upload with the previous "put" command
        run("tar -xzf /tmp/" + filename + " -C " + path)
        # Remove archive from server
        run("rm /tmp/{}".format(filename))
        run("mv " + path + "web_static/* " + path)
        # Delete archive from the server
        run("rm -rf " + path + "web_static")
        # Delete symbolic link from the server
        run("rm -rf /data/web_static/current")
        # Se crea un symbolic link en el servidor con la nueva ruta (sin ext)
        run("ln -s " + path + " /data/web_static/current")
        print("New version deployed!")
        return True

    except Exception:
        return False
