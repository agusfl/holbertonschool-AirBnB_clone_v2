#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack:
- Prototype: def do_pack():
- All files in the folder web_static must be added to the final archive
- All archives must be stored in the folder versions (your function should
create this folder if it doesn’t exist)
- The name of the archive created must be web_static_
<year><month><day><hour><minute><second>.tgz
- The function do_pack must return the archive path if the archive has been
correctly generated. Otherwise, it should return None

Info strftime: https://www.tutorialspoint.com/python/time_strftime.htm#:~:
text=Pythom%20time%20method%20strftime(),format%20must%20be%20a%20string.
Info tar: https://en.wikipedia.org/wiki/Tar_%28computing%29
"tar": la flag -c es de "create", -f es de "file" y -v de "verbose"
"""
from time import strftime
from fabric.api import local


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
