# OS自体をアップグレードするorインスタンス自体を入れ替える

```
[NODES]
kubectl drain <nodename> --ignore-daemonsets

# shutdown my Instance
# -> wait until k8s recognize as 'NotReady' using `kubectl get node`

kubectl delete node <nodename>


sudo kubeadm token list

# TTLが切れている場合は新しくtokenを生成して joinできるようにする
TOKEN=$(sudo kubeadm token generate)
sudo kubeadm token create $TOKEN --ttl 3h --print-join-command

kubeadm join 172.31.20.86:6443 --token xxx

```

### TODO

- Masterを更新するときはどうするんだ？