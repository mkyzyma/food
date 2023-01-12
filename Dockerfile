FROM python:3.10
WORKDIR /app
COPY . /app/

RUN pip3 install poetry && poetry install
CMD ["poetry", "run", "uvicorn", "api.app:app", "--host=0.0.0.0", "--reload"]