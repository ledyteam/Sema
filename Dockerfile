FROM python:3.10.10-buster

#>>> http://bugs.python.org/issue19846
ENV LANG C.UTF-8
#>>> interaktiv xTermimiz yoxdur
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qq update -y && apt-get -qq upgrade -y
RUN apt-get -qq install -y \
    git \
    curl \
    wget \
    ffmpeg \
    opus-tools


#>>> Quraşdırma tələbləri
RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -U -r cod.txt

RUN chmod a+x start
CMD ["./start"]
