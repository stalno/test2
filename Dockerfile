#
FROM python:3.12
#
WORKDIR /code
#
COPY ./requirements.txt /code/requirements.txt
RUN apt update && apt -y upgrade
RUN apt install -y wget
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#
COPY ./ /code/
#
ENV PORT 80
VOLUME ["/app/data"]
EXPOSE $PORT
#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]