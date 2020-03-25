# Install Nginx web server with a puppet script
exec { 'nginx':
  provider => 'shell',
  command  => 'sudo apt-get update -y;sudo apt-get install nginx -y;echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html;sudo sed -i "s/server_name_;/server_name _;\n\trewrite ^\/redirect_me https:\/\/michaelauditore.github.io permanent;/" /etc/nginx/sites-available/default;sudo service nginx start',
}