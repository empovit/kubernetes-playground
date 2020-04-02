# Pod Examples

1. Start a simple Web server that serves a default *index.html*.
2. Start the Web server and make it serve the *index.html* from this repository by cloning the repository to a shared volume.
3. Start the Web server, make it serve this repository, and periodically check for updates. Test by making changes to *index.html*, then committing and pushing them. Observe the page changing on the Web server.

**WARNING**: The files are hard-coded to point to this GitHub repository.
Since you do not have push permissions to it, you will need to modify the value of 
REPO_URL in the *.yaml* files inside this directory. 

Kubernetes networking is an advanced topic for now, so you will need a pod to access another pod's IP address (on the same internal network): 

* `kubectl run curl --generator=run-pod/v1 --image=radial/busyboxplus:curl -i --tty`

or attach to an already running pod to execute commands

* `kubectl attach curl -c curl -i -t`

Find out the IP address:

* `kubectl get pod web-server -o yaml | grep podIP`

Connect to the Web server from the *curl* container:

* `curl http://<ipaddress>:80/`

The pod can be deleted using:

* `kubectl delete pod web-server`