server {
    listen [::]:443 ssl ipv6only=on; # managed by Certbot
    listen 443 ssl; # managed by Certbot
    server_name blacktyg3r.com www.blacktyg3r.com;

    location / {
        proxy_pass http://127.0.0.1:8666/;
    }

    location /static/ {
        root /home/blacktyger/blacktyg3r.com/dashboard/apps/;
    }

}

server {
    if ($host = www.blacktyg3r.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    if ($host = blacktyg3r.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot

    listen 80;
    listen [::]:80;

    server_name blacktyg3r.com www.blacktyg3r.com;
    return 404; # managed by Certbot

}
