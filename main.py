import yaml
import sys

docker_compose='''version: '3'

services:'''

service_template='''
  shadowsocks-{name}:
    image: shadowsocks/shadowsocks-libev:v3.3.5
    ports:
      - "{port}:8388/tcp"
      - "{port}:8388/udp"
    environment:
      METHOD: {method}
      PASSWORD: {password}
      DNS_ADDRS: {dns_addrs}
    restart: always'''

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

if len({i['name'] for i in config})<len(config):
    print('Error: name is not unique')
    sys.exit(1)

if len({i['port'] for i in config})<len(config):
    print('Error: port is not unique')
    sys.exit(1)

for i in config:
    docker_compose+=service_template.format_map(i)

text_file = open("docker-compose.yml", "w")
text_file.write(docker_compose)
text_file.close()

print('''Done.

To start the shadowsocks, use the command:
docker-compose up -d''')