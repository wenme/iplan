apache2 + uwsgi

sudo apt-get install libapache2-mod-uwsgi
sudo a2enmod uwsgi

apache2 config:
<VirtualHost *:80>
        ServerName api.i-plan.com.cn
        ErrorLog ${APACHE_LOG_DIR}/error_api.log
        CustomLog ${APACHE_LOG_DIR}/access_api.log common
        ProxyPass / uwsgi://127.0.0.1:8002/
</VirtualHost>

uwsgi ini config:
[uwsgi]
touch-reload    = /tmp/iplan_prod.reload
chdir           = /root/iplan_prod/iplan/
module          = iplan.wsgi:application
master          = true
processes       = 1
socket          = 127.0.0.1:8002
chmod-socket    = 666
vacuum          = true
thunder-lock    = true
pidfile         = /tmp/iplan_prod.pid
env             = DJANGO_SETTINGS_MODULE=iplan.settings
