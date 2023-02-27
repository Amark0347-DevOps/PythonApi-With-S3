FROM python:latest
WORKDIR /app
COPY . ./
RUN pip install --upgrade pip
RUN pip install -r requirments.txt
CMD ["python","main.py"] 
#CMD ["uvicorn","main:app","--host", "0.0.0.0", "--port", "5800"]