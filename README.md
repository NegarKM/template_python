# template_python
Template project for Python Flask application with following features:

- Unit tests
- API documentation using `Swagger`


# Run:
```
docker build -t template_python .
docker run -p 5001:5000 --env-file .env template_python
```
go to http://localhost:5001/api/swagger/ for swagger UI