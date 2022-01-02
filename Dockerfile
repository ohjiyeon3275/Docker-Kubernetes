FROM openjdk

WORKDIR /app

COPY . .

RUN ./mvnw dependency:go-offline

CMD ["./mvnw", "spring-boot:run"]

EXPOSE 8899