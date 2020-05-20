#Puppet manifest to replace a syntax error into wp-settings.php file.
exec { 'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}