# NFS を追加 (Ubuntu 16使用)

```
[NFSサーバー側]
apt install nfs-kernel-server
mkdir -p /var/nfs/general
chown nobody:nogroup /var/nfs/general

vi /etc/exports
# 以下を追記
# /var/nfs/general <IPアドレス>(rw,sync,no_subtree_check) <IPアドレス>(..同じ) 

systemctl restart nfs-kernel-server


[NFSクライアント側]
apt install nfs-common

```