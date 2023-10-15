# ml-model-house-pricing
Example how to build and run a Machine Learning (ML) models using [Scikit-Learn](https://scikit-learn.org/stable/) and [Flask](http://flask.pocoo.org/).

##

![predict](https://miro.medium.com/v2/resize:fit:1150/format:webp/1*R6MR34xT4Ve6fI744EVN0A.png)


## Docker deployment

- ML image:
```
$ docker run -it --rm -v $(PWD)/data/prices.csv:/data/prices.csv \
    ghcr.io/atrakic/ml-house-pricing-model:latest /data/prices.csv
```

- Web
```
$ docker run -it --rm -e MODEL_FILE=/date/model.pkl \
    -v $(PWD)/model/model.pkl:/data/model.pkl \
    -p 8080:8080 \
    ghcr.io/atrakic/ml-house-pricing-web:latest
```

### Docker-compose

```
$ docker-compose up --build --no-deps --remove-orphans -d

# Test
$ curl -d '{"rooms":2, "distance":20}' -H "Content-Type: application/json" \
    -X POST http://localhost:5000/api
```

### Kubernetes deployment

```
$ kubectl apply -f ./k8s/web.yml

# Test
$ kubectl describe -f k8s-manifests/web.yml
$ kubectl run -it --rm --image=curlimages/curl --restart=Never curl-test -- \
    -d '{"rooms":2, "distance":20}' -H "Content-Type: application/json" \
    -X POST http://$(kubectl get svc ml-house-pricing-web --output=jsonpath='{.spec.clusterIPs[0]}'):80/api
```

## LICENSE
See [LICENSE](LICENSE) for details.
