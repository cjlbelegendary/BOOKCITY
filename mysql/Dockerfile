FROM mysql:5.7
ENV MYSQL_ROOT_PASSWORD=Cjl202200202127==
ENV MYSQL_DATABASE=bookstore
COPY bookstore.sql /docker-entrypoint-initdb.d/
EXPOSE 3306
CMD ["mysqld"]