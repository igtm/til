# kubeadmが入ってる場合

```
sudo kubeadm init --pod-network-cidr=10.244.0.0/16

mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config
  
sudo kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/v0.9.1/Documentation/kube-flannel.yml


kubeadm join 172.31.20.86:6443 --token xxx
```


============================

# 生Ubuntu 16でインストール

```
#sudo dpkg --configure -a
#apt-get -f install

apt install -y docker.io

CentOS 7 の systemd によるリソース管理と Docker の相性が悪く、このようなエラーが発生する場合があるようです。
cat > /etc/docker/daemon.json
{
 "exec-opts": ["native.cgroupdriver=systemd"]
}

curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
cat > /etc/apt/sources.list.d/kubernetes.list
deb http://apt.kubernetes.io/ kubernetes-xenial main
apt update

apt install -y kubelet kubeadm kubectl

kubeadm init --pod-network-cidr=10.244.0.0/16


kubeadm join 172.31.124.78:6443 --token xxx

```

==============================

# 生CentOSからインストール

```

swapoff -a
vi /etc/fstab (コメントアウトする)

yum -y update
yum -y install docker

systemctl enable docker
systemctl start docker

cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOF

setenforce 0 (SELinuxを切る)
vi /etc/selinux/config (permissiveにする)

yum  install -y kubelet kubeadm kubectl

systemctl enable kubelet
systemctl start kubelet

cat <<EOF >  /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF

kubeadm init --pod-network-cidr=10.244.0.0/16

mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/v0.9.1/Documentation/kube-flannel.yml

(なぜか作られないので自分で以下を作る)
mkdir -p /etc/cni/net.d
cat > /etc/cni/net.d/10-flannel.conf
{
	"name": "cbr0",
	"type": "flannel",
	"delegate": {
		"isDefaultGateway": true
	}
}

kubeadm join 172.31.20.42:6443 --token xxx

```