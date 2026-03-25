# Use a lightweight Java runtime
FROM eclipse-temurin:21-jre-alpine

# Set the working directory
WORKDIR /app

# Copy the JAR file that was built by the GitHub Action
# Note: GitHub Actions puts the build result in the target/ folder
COPY target/*.jar app.jar

# Expose the port your app runs on
EXPOSE 8082

# Run the application
ENTRYPOINT ["java", "-jar", "app.jar"]
