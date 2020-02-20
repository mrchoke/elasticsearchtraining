ARG ELK_VERSION=7.6.0

FROM docker.elastic.co/elasticsearch/elasticsearch:${ELK_VERSION}

ARG DUID=1000

ENV DUID=${DUID}

RUN usermod -u $DUID elasticsearch
RUN chown -R elasticsearch /usr/share/elasticsearch
RUN sed -i -e 's/--userspec=1000/--userspec=$DUID/g' \
           -e 's/UID 1000/UID $DUID/' \
           -e 's/chown -R 1000/chown -R $DUID/' /usr/local/bin/docker-entrypoint.sh
RUN chown elasticsearch /usr/local/bin/docker-entrypoint.sh
