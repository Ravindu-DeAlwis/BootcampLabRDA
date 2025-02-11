FROM python:3.9
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . /app/
RUN python manage.py collectstatic --noinput
EXPOSE 8000
ENV DJANGO_SETTINGS_MODULE=settings.dev
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]