FROM python:3.10
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN pip install poetry && poetry install --no-root
COPY . /app
CMD ["poetry", "run", "uvicorn", "src.manufac_test.main:app", "--host", "0.0.0.0", "--port", "8000"]