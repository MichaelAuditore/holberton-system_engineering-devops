# Manifest that configures NGINX
exec { 'cmd_0':
  path    => '/usr/bin:/bin',
  command => 'sudo sudo apt-get update -y',
  returns => [0,1]
}

exec { 'cmd_1':
  require => Exec['cmd_0'],
  path    => '/usr/bin:/bin',
  command => 'sudo apt-get install nginx -y',
  returns => [0,1]
}

exec { 'cmd_2':
  require => Exec['cmd_1'],
  path    => '/usr/bin:/bin',
  command => 'echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html',
  returns => [0,1]
}

exec { 'cmd_3':
  require => Exec['cmd_2'],
  path    => '/usr/bin:/bin',
  command => 'sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me michaelauditore.github.io permanent;/" /etc/nginx/sites-enabled/default',
  returns => [0,1]
}

exec { 'cmd_4':
  require => Exec['cmd_3'],
  path    => '/usr/bin:/bin:/usr/sbin',
  command => 'sudo service nginx start',
  returns => [0,1]
}