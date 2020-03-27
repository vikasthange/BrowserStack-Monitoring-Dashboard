FROM telegraf:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
		python \
		python-pip \
	&& pip install requests

CMD ["telegraf"]
