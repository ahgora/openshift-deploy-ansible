
Exemplo no centos7:

https://www.youtube.com/watch?v=-OOnGK-XeVY

https://docs.openshift.org/latest/install_config/install/host_preparation.html

yum install -y epel-release
yum install -y docker wget git ansible
yum install -y python-cryptography pyOpenSSL.x86_64

yum install -y NetworkManager
systemctl start NetworkManager

git clone https://github.com/openshift/openshift-ansible.git
git clone https://github.com/gshipley/installcentos.git

# Bug ansible:
wget http://cbs.centos.org/kojifiles/packages/ansible/2.2.0/0.50.prerelease.el7/noarch/ansible-2.2.0-0.50.prerelease.el7.noarch.rpm
yum localinstall ansible-2.2.0-0.50.prerelease.el7.noarch.rpm

# Gerar chave de ssh e colocar no host alvo para o ansible poder fazer o deploy

ansible-playbook -i inventory.erb openshift-ansible/playbooks/byo/config.yml


# Custom Cert:
https://docs.openshift.org/latest/install_config/certificate_customization.html

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
