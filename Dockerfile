# Use an official OpenJDK runtime as base image
FROM openjdk:21-jdk-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Maven wrapper and pom.xml first (for better caching)
COPY mvnw .
COPY .mvn .mvn
COPY pom.xml .

# Download dependencies (this layer is cached unless pom.xml changes)
RUN ./mvnw dependency:go-offline -B

# Copy the source code
COPY src src

# Build the application
RUN ./mvnw package -DskipTests

# Expose the port your app runs on (default 8080, but you changed to 8082)
EXPOSE 8082

# Run the jar
CMD ["java", "-jar", "target/*.jar"]