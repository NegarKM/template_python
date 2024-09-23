ARG BUILD_IMAGE

FROM $BUILD_IMAGE AS test

COPY Pipfile* /app/
COPY tests /app/tests

# Install pipenv and compilation dependencies
RUN pip install --upgrade pip==24.2 \
    && pip install pipenv

WORKDIR /app

# Install the package using pipenv pipfile
RUN pipenv install

EXPOSE 5000

ENTRYPOINT ["pipenv", "run"]
CMD [ "pytest", "tests" ]
