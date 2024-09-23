ARG PYTHON_VERSION=3.11.4
FROM python:${PYTHON_VERSION}-slim AS serve

COPY Pipfile* /app/

# Install pipenv and compilation dependencies
RUN pip install --upgrade pip==24.2 \
    && pip install pipenv

WORKDIR /app
COPY src /app/src/

ENV PIPENV_VENV_IN_PROJECT=1
ENV PYTHONPATH=$PYTHONPATH:/app/src

# Install the package using pipenv pipfile
RUN pipenv install

# Install the package using setup.py setuptools
#COPY setup.py /app/
#RUN pipenv run pip install .

RUN apt-get update \
  && apt-get install -y curl

ENV APP_USER=app_user

RUN addgroup --system $APP_USER && \
    adduser --shell /bin/false --system --uid 1000 $APP_USER

RUN chown -R $APP_USER:$APP_USER /app

USER 1000

EXPOSE 5000

ENTRYPOINT ["pipenv", "run", "gunicorn"]

CMD [ "-c", "/app/src/api_service/app/gunicorn.conf.py", "src.api_service.app.__init__:application" ]
