# Job Examples

The job counts words in a UTF-8 text file using a Python script.
The script and the text file are during the init step.

Useful commands:

* `kubectl get job -w`
* `kubectl get pod -l job-name=word-count -w`
* `kubectl describe job word-count`
* `kubectl get pod -l job-name=word-count`
* `kubectl logs $(kubectl get pod -l job-name=word-count -o name)`
* `kubectl delete job word-count`