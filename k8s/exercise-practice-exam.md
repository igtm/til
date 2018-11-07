# Exercise: Practice Exam

The Certified Kubernetes Administrator Exam is a practical test of your knowledge of Kubernetes.  It contains no multiple-choice questions or any academic type questions of any kind.  The entire test is a series of tasks to perform in a Kubernetes cluster.  In the formal exam, you have three hours to complete everything.  See the video titled, "Registering for & Taking the Exam" for a full description of what taking the exam is like and what you can expect.

In order to prepare you for the real exam, this practice exam is not quiz questions since you will not be asked any of those types of questions on the real thing.  Instead, this exam is a series of tasks much like the tasks you will be asked to perform on the real exam.  Note that this practice exam is designed to challenge you in the same way as the real exam, but it is NOT the actual questions you will receive on the exam.  You should use this practice exam as a way for you to judge your readiness to sit for the real thing.  How you use this exercise is entirely up to you, but I suggest using it as a dry run to test your skills.

## To use the practice exam as a dry run:

1) Prepare a quiet place where you will be alone and undisturbed for about four hours.

2) Save any files or notes you've made on your Kubernetes Master node, and then tear-down and rebuild your lab cluster with one master and one worker node according to the instructions in the first exercise in this course.  Once your cluster is ready, log in to the master node.  You are now ready to begin your dry run.

3) In the real exam, you'll not be permitted to use any written notes.  You may visit any website you like, and having the kubernetes.io documentation pages is encouraged.  There's even a cheat sheet (at https://kubernetes.io/docs/reference/kubectl/cheatsheet/) that contains a lot of very useful information and is available to you during the exam.  You don't want to rely too heavily on this documentation, however, as time is against you.

4) Open up Notepad (or similar) to keep track of what you've done and what you still need to accomplish.  Just like on the real exam, you're responsible for knowing what you've done and what you haven't.

5) The solution contains methods to check your work.  If your answers differ from those in the solution, then you need to spend additional time working through problems of that nature prior to sitting for the exam.

6) Set a timer.  Because the test is "open book" (well, open documentation on the Internet) your biggest enemies are time and your own organizational skills.  Being able to complete the test in a timely fashion is critical to obtaining your certification.

Again, these are not actual questions from the exam, but are similar.  If you can complete these questions in three hours or less and find that you understand what you're doing, then you should be ready for the real thing.  

Good luck

## Test tasks begin here.
 

1.Create a job that calculates pi to 2000 decimal points using the container with the image named perl and the following entry point to the container:

```
 ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
Once the job has completed, save the result to your home directory in a file called pi.result.txt.
```


2.Create yaml for a pod that uses the nginx image and listens on port 80. The pod should have the name nginx-pod and be labeled with app: nginx. Save the yaml to your home directory as nginx-pod.yaml and start the pod.





3.Create yaml for a deployment of two replicas of nginx, listening on the container's port 80. They should bear the label of tier=frontend and app-nginx. The deployment should be named nginx-deployment. Leave a copy of the yaml in your home directory with the name nginx-deployment.yaml.





4.Create a pod called "with-files" with an nginx image listening on port 80. The pod should attach to emptyDir storage, mounted to /tmp in the container. Connect to the pod and create a file with zero bytes in the /tmp directory called "linuxacademy.txt." Do not delete this pod. If you create other artifacts in the course working on this, you may delete them from your home directory or create a directory called "extras" in your home directory and move the files there.





5.Label the worker node of your cluster with rack=qa.





6.Create a file called counter.yaml in your home directory and paste the following yaml into it:

```
apiVersion: v1
kind: Pod
metadata:
  name: counter
spec:
  containers:
  - name: count
    image: busybox
    args: [/bin/sh, -c, 'i=0; while true; do echo "$i: $(date)"; i=$((i+1)); sleep 1; done']
```

Start this pod. Once its logs exceed a count of 20 (no need to be precise, any time after it has reached 20 is fine) save the logs into a file in your home directory called count.result.txt. Delete the pod.




7.Create a deployment with two replicas of nginx:1.7.9. The container listens on port 80. It should be named "web-dep" and be labeled with tier=frontend with an annotation of AppVersion=3.4. The containers must be running with the UID of 1000.

 

8.Upgrade the image in use by the web-dep deployment to nginx:1.9





9.Roll the image in use by the web-dep deployment to the previous version. Do not set the version number of the image explicitly for this command.





10.Scale the number of replicas of the web-dep deployment up to 3.





11.Expose the web-dep deployment as a service using a NodePort.





12.Configure a DaemonSet to run the image k8s.gcr.io/pause:2.0 in the cluster.





13.Configure the cluster to use 8.8.8.8 and 8.8.4.4 as upstream DNS servers.





14.A legacy application (yaml below) requires that the IP address or host name of the web-dep endpoint be configured as an environment variable called "FROBOZZ" in the container. Alter the yaml accordingly, leave a copy in your home directory with the name zork.yaml, and start the pod.

```
apiVersion: apps/v1beta2
kind: Deployment
metadata:
  name: zork
  namespace: default
spec:
  selector:
    matchLabels:
      app: zork-app
  template:
    metadata:
      labels:
        app: zork-app
    spec:
      containers:
      - name: p114
        image: k8s.gcr.io/pause:2.0
```



15.Create a pod using the k8s.gcr.io/pause:20 container image that is allowed to run on the master node if necessary, but does not have to be scheduled there.





16.Copy all Kubernetes Scheduler logs into a logs directory in your home directory.





17.Run the pod below until the counter in its stdout exceeds 20 (no need to be precise) and then extract the legacy log file to the logs directory in your home directory. Delete the pod.

```
apiVersion: v1
kind: Pod
metadata:
  name: counter2
spec:
  containers:
  - name: count
    image: busybox
    args: [/bin/sh, -c, 'i=0; while true; do echo "$i: $(date)"; echo "$(date) - File - $i" >> /var/www/countlog; i=$((i+1)); sleep 3; done']
```



18.Build a default network policy that disallows all traffic to pods in the default namespace.





19.Remove the taint from the master node so it can now accept any work -- even from nodes with no tolerations of the master node.





20.Create a yaml file for a secret called my-secret and saved in a file in your home directory called my-secret.yaml. The secret should have two fields: a username and password. The username should be set to "admin" and the password should be set to "iHeartKittens"