# Manifest that configures a custom HTTP header
exec { 'cmd_0':
  path    => '/usr/bin:/bin',
  command => 'sudo apt-get -y update',
  returns => [0,1]
}

exec { 'cmd_1':
  require => Exec['cmd_0'],
  path    => '/usr/bin:/bin',
  command => 'sudo apt-get -y install nginx',
  returns => [0,1]
}

exec { 'cmd_2':
  require => Exec['cmd_1'],
  path    => '/usr/bin:/bin',
  command => 'sudo sed -i "29i \ \tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf'
  returns => [0,1]
}

exec { 'cmd_3':
  require => Exec['cmd_2'],
  path    => '/usr/bin:/bin',
  command => 'sudo service nginx start',
  returns => [0,1]
}