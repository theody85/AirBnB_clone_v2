#!/usr/bin/python3
    """ 
    Fabric script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo,
    using the function do_pack
    :"""
   from fabric.api import local
   from datetime import datetime
   from os.path import isdir


   def do_pack():
       """Generates tgz"""
           currentdate = datetime.now().strftime("%Y%m%d%H%M%S")
               try:
                       local("mkdir -p versions")
                               file_name = "versions/web_static_{}.tgz".format(currentdate)
                                       local("tar -cvzf {} web_static".format(file_name))
                                               return file_name
                                                   except Exception:
                                                           return None
