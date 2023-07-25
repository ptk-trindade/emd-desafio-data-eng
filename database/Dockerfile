FROM postgres:latest
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_USER=username
ENV POSTGRES_DB=brt_db
COPY initdb.sql /docker-entrypoint-initdb.d/initdb.sql