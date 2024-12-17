FROM python:3.13.1
WORKDIR /app
COPY . /app
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV PYTHONPATH=/app
CMD ["python", "app.py"]
