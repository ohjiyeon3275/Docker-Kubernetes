
- what is kubernetes ?

- ecs
-> using a specific cloud service locks us into that service

-> k8s is like docker-compose for multiple machines.

- worker node
- proxy, config
- pod

---
### your work / kubernetes's work

- what k8s will do 
  - create your object and manage them
  - monitor pods and re-create them, scale pod etc.
  - k8s utilizes the provided resources to apply youre configuration / goals
  

- what you need to do / setup
  - create the cluster and the node instances
  - setup api erver, kubelet and ohter k8s services/ software on nodes
  - create other provider resources that might be needed (load-balancer, filesystems)

---

- worker node
  - worker node : think of it as ont computer / machines/ virtual instance
  - worker node is managed by the master node.
  - pod : hosts one or more appliation containers and thier resources
  - pods are created and managed by kubernetes.

--- 

- master node
  - api server : api for the kublets to communicate
  - scheduler : watches for new pods, seletes worker nodes to run them on
  - kube-controller-manager : watches and controls worker nodes, correct number of pods & more
  - cloud-controller-manager : like kube-controller-manager but for a specific cloud provider, knows how to interact with cloud provicer resources.
  

