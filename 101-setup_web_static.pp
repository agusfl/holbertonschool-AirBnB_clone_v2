# Redo the task #0 but by using Puppet:

exec { 'update':
  command  => 'sudo apt-get -y update',
  provider => shell,
  before   => Exec['install_Nginx'],
}

exec {'install_Nginx':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
  before   => Exec['start_Nginx'],
}

exec {'start_Nginx':
  command  => 'sudo service nginx start',
  provider => shell,
  before   => Exec['create_directory'],
}

exec {'create_directory':
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  provider => shell,
  before   => Exec['create_other_directory'],
}

exec {'create_other_directory':
  command  => 'sudo mkdir -p /data/web_static/shared/',
  provider => shell,
  before   => Exec['content_for_html'],
}

exec {'content_for_html':
  command  => 'echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
',
  provider => shell,
  before   => Exec['create_symbolic_link'],
}

exec {'create_symbolic_link':
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => shell,
  before   => Exec['put_fabric'],
}

exec {'put_fabric':
  command  => 'sed -i "56i location /hbnb_static/ {\nalias /data/web_static/current/;\n}\n" /etc/nginx/sites-enabled/default',
  provider => shell,
  before   => Exec['restart_Nginx'],
}

exec {'restart_Nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
  before   => File['/data/']
}

file {'/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}
