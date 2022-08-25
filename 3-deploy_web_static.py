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
from fabric.api import run, put, env, local
from os.path import exists  # To check if a file exists
from time import strftime
# Seteo environmental variables para los servidores 4390-web-01 and 4390-web-02
env.hosts = ['54.160.237.107', '54.242.209.114']
# Define user as a environmental variable
env.user = "ubuntu"


# Function from task 1 --> do_pack()
def do_pack():
    """
    Script that generates a .tgz archive from the contents of the web_static
    folder
    """
    # Ya lo habiamos usado el strftime en otro proyecto de AirBnB
    time = strftime("%Y%M%d%H%M%S")

    # Hago el codigo en un try y un except por si el archivo no se genero'
    # correctamente
    try:
        # Create directory "versions" locally
        local("mkdir -p versions")
        # Creo el nombre de la forma que lo piden
        archive_name = "versions/web_static_{}.tgz".format(time)
        # Se crea el "archive_name" de los contenidos dentro de web_static
        local("tar -cvzf {} web_static/".format(archive_name))
        # Se retorna el archive_name
        return archive_name
    except Exception:
        return None


# Function from task 2 --> do_deploy
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
        # and save it in a new path that is created with -C option
        run("tar -xzf /tmp/" + filename + " -C " + path)

        # Le cambiamos el nombre al archivo que creamos recien con la
        # info descomprimida
        run("mv " + path + "web_static/*" + " " + path)

        # Remove archive from server
        run("rm /tmp/{}".format(filename))
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


def deploy():
    """
    Creates and distributes an archive to your web servers.
    """
    # Call the do_pack() function made in task 1 to create path of archive
    path = do_pack()

    # Return False if no archive has been created
    if path is None:
        return False

    # Call the do_deploay function (made in task 2) with the new path
    deploy = do_deploy(path)
    return deploy
