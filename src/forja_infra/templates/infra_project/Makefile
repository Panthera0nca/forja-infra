.PHONY: install provision provision-kafka provision-lakehouse deploy ping

install:
	pip install ansible
	ansible-galaxy collection install -r requirements.yml

ping:
	ansible all -m ping

provision:
	ansible-playbook playbooks/provision.yml

provision-kafka:
	ansible-playbook playbooks/provision_kafka.yml

provision-lakehouse:
	ansible-playbook playbooks/provision_lakehouse.yml

deploy:
	ansible-playbook playbooks/deploy.yml
