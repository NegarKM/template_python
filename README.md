# template_python
Template project for Python Flask application with following features:

- API documentation using `Swagger`
- Unit tests
- Database Connection (SQLAlchemy, Flyway)


# Run:
```
docker build -t sample-api-image .
docker run --name sample-api -p 5001:5000 --env-file .env sample-api-image
```
or run:
```
docker-compose build
docker-compose up
```
or run:
```
./scripts/start.sh
```

go to http://localhost:5001/api/swagger/ for swagger UI

# Test:
```
docker rm --force sample-api-test 
docker build -t sample-api-build .
docker build --build-arg BUILD_IMAGE=sample-api-build --no-cache -t sample-api-test --file tests/Dockerfile .
docker run --name sample-api-test --env-file .env --interactive --tty sample-api-test
```
or run:
```
./scripts/test.sh
```
