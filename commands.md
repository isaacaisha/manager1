# manager1 commands eg.:

sudo systemctl daemon-reload
sudo systemctl restart manager1.service
sudo systemctl status manager1.service

sudo nginx -t
sudo systemctl restart nginx
sudo systemctl status nginx

sudo journalctl -u manager1.service -f

# CONNECT POSTGRES
sudo -i -u postgres
sudo nano /var/lib/pgsql/data/postgresql.conf

# systemd
sudo nano /etc/systemd/system/manager1.service

# nginx
sudo nano /etc/nginx/sites-available/manager1.conf

# CREATE SSL CERTIFICATE
sudo dnf install certbot python3-certbot-nginx
sudo certbot --nginx

# link the configuration to enable it
sudo ln -s /etc/nginx/sites-available/manager1 /etc/nginx/sites-enabled/

sudo certbot certificates
sudo certbot --nginx -d real-copromanager.siisi.online -d www.real-copromanager.siisi.online

sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048

sudo systemctl enable certbot.timer
sudo certbot renew --dry-run

# kill all port runing
sudo lsof -t -iTCP:8003 -sTCP:LISTEN | xargs sudo kill

# Testing
/home/siisi/manager1/venv/bin/gunicorn -b 0.0.0.0:8003 main:app

# Dockers
<!-- Docker -->
docker --version
docker-compose --version

sudo systemctl restart docker
sudo systemctl status docker

<!-- Start Odoo -->
<!-- locally -->
docker ps
docker-compose -f docker-compose-dev.yml down --volumes --remove-orphans
docker-compose -f system prune -a --volumes
docker-compose -f docker-compose-dev.yml down
docker-compose -f docker-compose-dev.yml up -d --build

docker-compose -f docker-compose-dev.yml down
docker-compose -f docker-compose-dev.yml up -d
docker-compose -f docker-compose-dev.yml logs -f
<!-- production -->
docker-compose -f docker-compose-prod.yml down
docker-compose -f docker-compose-prod.yml up -d
docker-compose -f docker-compose-prod.yml logs -f

# Find Your Computer's Local IP Address
ifconfig | grep inet
