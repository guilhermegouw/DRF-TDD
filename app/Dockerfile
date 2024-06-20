FROM python:3.11.2-slim-buster
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# Install dependencies
RUN pip install --upgrade pip
# Copy requirements files
COPY ./requirements.txt ./requirements-dev.txt ./
# Install requirements
RUN pip install -r requirements.txt \
  && pip install -r requirements-dev.txt

# Copy entrypoint
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Add app
COPY . .

# Run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
