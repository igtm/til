# Kuberentesをアップグレードする

```
[MASTER]
sudo apt upgrade kubeadm

sudo kubeadm upgrade plan

sudo kubeadm upgarde apply v1.xx.x


[MASTER & NODES]
kubectl drain <nodename> --ignore-daemonsets
# エラーが出たときは、evictできないものがあるので、手動で殺すなりなんなりする

sudo apt upgarde
sudo apt upgrade kubelet

kubectl uncordon <nodename>

```