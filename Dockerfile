FROM ubuntu

WORKDIR /app


ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3 python3-pip python3-opencv && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./src ./src

COPY ./Saved ./Saved


COPY ./files ./files



CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
