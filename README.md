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

Show the details of a particular object

* `kubectl describe <type> <name>`

## Examples

 The following subdirectories contain simple examples with explanations. 
 The examples are organized mostly by object types.

* [Pods](pod/)
* [Jobs](job/)