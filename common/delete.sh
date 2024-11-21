#!/bin/bash


kubectl delete pods --field-selector status.phase!=Running --namespace openfaas-fn
kubectl delete pods --field-selector status.phase!=Running --namespace knative-serverless

fission function delete --name fibonacci-single
fission route delete --function fibonacci-single
fission function delete --name fibonacci
fission route delete --function fibonacci

fission function delete --name quicksort-single
fission route delete --function quicksort-single
fission function delete --name quicksort
fission route delete --function quicksort

fission function delete --name users-single
fission route delete --function users-single
fission function delete --name users
fission route delete --function users

fission function delete --name thumbnail-single
fission route delete --function thumbnail-single
fission function delete --name thumbnail
fission route delete --function thumbnail

------

cd ~/serverless-frameworks/knative/functions/
kubectl delete --filename fibonacci/service.yaml
kubectl delete --filename fibonacci/service-single.yaml