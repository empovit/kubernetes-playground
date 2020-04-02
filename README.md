# Demo Kubernetes Primitives and Commands

## Basic Commands

Manage objects defined in a declarative way:

* `kubectl apply -f <file>`
* `kubectl create -f <file>`
* `kubectl delete -f <file>`

List all objects

* `kubectl get all`

List objects of a particular type

* `kubectl get <type>`
* `kubectl get pod`
* `kubectl get service`

Watch objects of a particular type

* `kubectl get <type> -w`
* `kubectl get pod -w`

Print a particular object

* `kubectl get <type> <name>`
* `kubectl get pod web-server`

## Pods

The examples can be found under the *pod* directory.

1. Start a simple Web server that serves a default *index.html*.
2. Start the Web server and make it serve the *index.html* from this repository by cloning the repository to a shared volume.
3. Start the Web server, make it serve this repository, and periodically check for updates. Test by making changes to *index.html*, then committing and pushing them. Observe the page changing on the Web server.

**WARNING**: The files are hard-coded to point to this GitHub repository.
Since you do not have push permissions to it, you will need to modify the value of 
REPO_URL in the *.yaml* files inside the *pod* directory. 

Kubernetes networking is an advanced topic for now, so create a container to access the pod's IP address: 

* `kubectl run curl --generator=run-pod/v1 --image=radial/busyboxplus:curl -i --tty`

or attach to an already running pod to execute commands

* `kubectl attach curl -c curl -i -t`

Find out the IP address:

* `kubectl get pod web-server -o yaml | grep podIP`

Connect to the Web server from the *curl* container:

* `curl http://<ipaddress>:80/`

The pod can be deleted using:

* `kubectl delete pod web-server`


