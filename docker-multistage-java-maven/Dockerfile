FROM maven:3.9.16-eclipse-temurin-17 AS build
WORKDIR /test
COPY pom.xml .
COPY /src ./src
RUN mvn clean validate
RUN mvn package

RUN mvn install

FROM amazoncorretto:17-alpine-full 
WORKDIR /test
COPY --from=build /test/target/docker-multistage-1.0-SNAPSHOT.jar app.jar

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]