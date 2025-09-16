.PHONY: venv run nginx check-http check-tls hosts-setup tls-cert dns-demo clean

venv:
	python3 -m venv venv
	. venv/bin/activate && pip install flask

run:
	PORT=8080 MESSAGE="Hola CC3S2" RELEASE="v1" python3 app.py

nginx:
	sudo systemctl restart nginx
	sudo systemctl status nginx

check-http:
	curl -v http://127.0.0.1:8080/

check-tls:
	openssl s_client -connect miapp.local:443 -servername miapp.local -brief
	curl -k https://miapp.local/

hosts-setup:
	echo "127.0.0.1 miapp.local" | sudo tee -a /etc/hosts

tls-cert:
	openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout miapp.key -out miapp.crt -subj "/CN=miapp.local"

dns-demo:
	dig +short miapp.local
	getent hosts miapp.local

clean:
	rm -rf venv *.pyc __pycache__