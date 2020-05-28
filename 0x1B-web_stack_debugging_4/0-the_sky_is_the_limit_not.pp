# Manifiest to change the maximum of requests given to server
exec { 'max-requests':
  command  => 'sed -i "s/15/3000" /etc/default/nginx',
  provider => 'shell',
  before   => Exec['restart-nginx'].
}

exec { 'restart-nginx':
  command  => 'sudo service nginx restart',
  provider => 'shell',
}
