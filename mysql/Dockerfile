FROM mysql:5.7
ENV MYSQL_ROOT_PASSWORD=Cjl202200202127==
ENV MYSQL_DATABASE=bookstore
EXPOSE 3306
COPY bookstore.sql /docker-entrypoint-initdb.d/
COPY my.cnf /etc/mysql/my.cnf
CMD ["mysqld"]