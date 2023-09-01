#!/bin/bash
set -e

curl -d '{"rooms":2, "distance":20}' -H "Content-Type: application/json" \
  -X POST http://localhost:5000/api

kubectl run -it --rm --image=curlimages/curl --restart=Never curl-test -- \
  -d '{"rooms":2, "distance":20}' -H "Content-Type: application/json" \
  -X POST http://$(k get svc ml-house-pricing-web --output=jsonpath='{.spec.clusterIPs[0]}'):80/api
