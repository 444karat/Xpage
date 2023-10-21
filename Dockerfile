FROM python:3.10.4
WORKDIR .
COPY . .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["uvicorn", "app.main:app", "--reload",  "--host", "0.0.0.0", "--port", "8000"]