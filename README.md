
## Pré-Requisitos

O.S : CentOS7
Softwares: docker


## Passos para Instalação:

### Servidores de openshift


$yum install -y NetworkManager
$systemctl start NetworkManager

- Instale o docker

sed -i '/OPTIONS=.*/c\OPTIONS="--selinux-enabled --insecure-registry 172.30.0.0/16"' /etc/sysconfig/docker

ou

cp /lib/systemd/system/docker.service  /etc/systemd/system/

e adicione ExecStart=/usr/bin/dockerd  --insecure-registry 172.30.0.0/16

### Configurações gerais - Ubuntu/CentOS
$git clone https://github.com/openshift/openshift-ansible.git
$git clone https://github.com/gshipley/installcentos.git

- Criar o arquivo users.htpasswd e atualizar o path do arquivo users.htpasswd na variavel "openshift_master_htpasswd_file" do invetory.erb
- Gerar chave de ssh e colocar no host alvo para o ansible poder fazer o deploy:

$cd openshift-ansible/
$git branch
$git checkout <versão-do-openshift>

### No centOS:

$yum install -y epel-release
$yum install -y wget git ansible
$yum install -y python-cryptography pyOpenSSL.x86_64

$ansible-playbook -i inventory.erb openshift-ansible/playbooks/byo/config.yml -v

### No Ubuntu

$sudo apt-get install ansible
$sudo pip install pyopenssl

$ansible-playbook -i inventory.erb openshift-ansible/playbooks/byo/config.yml -v


## Bugs

### ansible:

wget http://cbs.centos.org/kojifiles/packages/ansible/2.2.0/0.50.prerelease.el7/noarch/ansible-2.2.0-0.50.prerelease.el7.noarch.rpm
yum localinstall ansible-2.2.0-0.50.prerelease.el7.noarch.rpm

# Examples:

https://github.com/openshift/openshift-ansible/blob/master/inventory/byo/hosts.origin.example
https://github.com/raffaelespazzoli/openshift-enablement-exam/blob/master/hosts
https://blog.openshift.com/use-of-selectors-to-get-pods-on-desired-nodes/
oadm policy reconcile-cluster-roles --additive-only=true --confirm

Problema DNS:
dig @10.10.10.155 +short kubernetes.default.svc
dig @10.10.10.29 +short kubernetes.default.svc
dig @127.0.0.1 +short kubernetes.default.svc

oadm policy add-cluster-role-to-user cluster-admin admin --config=/etc/origin/master/admin.kubeconfig

curl https://172.30.0.1:443/healthz
curl https://kubernetes.default.svc.cluster.local/healthz

## Troubleshooting

Problema com certificados durante a instalação:

https://github.com/openshift/openshift-ansible/issues/1431


## Documentação:

https://www.youtube.com/watch?v=-OOnGK-XeVY

https://docs.openshift.org/latest/install_config/install/host_preparation.html

# Custom Cert:
https://docs.openshift.org/latest/install_config/certificate_customization.html
