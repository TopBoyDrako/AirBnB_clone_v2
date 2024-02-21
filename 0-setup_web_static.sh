#!/usr/bin/env bash
#This script sets up a web server for the deployment of web_static

sudo apt update
sudo apt install nginx -y

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo '<html>
  <head>
  </head>
  <body>
    This is for web_static
  </body>
</html>' > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

sed -i '51 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

service nginx restart
