# template_python
Template project for Python Flask application with following features:

- Unit tests
- API documentation using `Swagger`


# Run:
```
docker build -t template_python .
docker run --name template_python_src -p 5001:5000 --env-file .env template_python
```
or run:
```
./scripts/start.sh
```

go to http://localhost:5001/api/swagger/ for swagger UI

# Test:
```
docker rm --force template_python_test 
docker build -t template_python_build .
docker build --build-arg BUILD_IMAGE=template_python_build --no-cache -t template_python_test --file tests/Dockerfile .
docker run --name template_python_test --env-file .env --interactive --tty template_python_test
```
or run:
```
./scripts/test.sh
```
