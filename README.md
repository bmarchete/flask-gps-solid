# Python Flask Travel Distance API

This project is a Python Flask API that calculates the travel distance between two locations. It uses Google Maps API for distance calculation, Redis for caching, and SQLAlchemy for data persistence. The project is structured following the SOLID principles to ensure maintainability, flexibility, and testability.

## SOLID Principles

### Single Responsibility Principle

Each class in this project has a single responsibility. For example, the `TravelDistanceService` class is responsible for managing the logic of retrieving travel distances, while the `SQLAlchemyTravelDistanceRepository` class is responsible for managing the persistence of travel distance data.

### Open-Closed Principle

The project is structured in a way that allows for easy extension without modification of existing code. For instance, if a new method of calculating travel distance is introduced, a new class implementing the `TravelDistanceInterface` can be created without modifying the existing `GoogleMapsTravelDistanceService` class.

### Liskov Substitution Principle

The project uses interfaces to ensure that any class that can be used in place of another can be substituted without affecting the correctness of the program.

### Interface Segregation Principle

The interfaces in this project are client-specific. For example, the `TravelDistanceInterface` has methods that are specific to the needs of the classes that use it.

### Dependency Inversion Principle

High-level modules in this project do not depend on low-level modules. Both depend on abstractions. For example, the `TravelDistanceService` class does not depend on the `GoogleMapsTravelDistanceService` class directly. Instead, it depends on the `TravelDistanceInterface`abstraction.

## Project Structure

The project is structured into several directories:

- `src/adapters`: Contains code that adapts the application to external services like Google Maps API, Redis, and SQLAlchemy.
- `src/configuration`: Contains code related to the configuration of the application.
- `src/domain`: Contains the core business logic of the application.
- `src/main.py`: The entry point of the application.

## Running the Project

Before you run the application, make sure to create `.env` file. There is a sample file called `.env.sample`.

To run the project, you need to have Docker installed. You can start the application by running the following command in the root directory of the project:

```sh
docker-compose up --build
```

This will start the Flask application, along with the necessary services like Redis and PostgreSQL.

## API Usage

The API has a single endpoint, `/distance`, which accepts a GET request with two query parameters, `origin` and `destination`. The endpoint returns the travel distance between the origin and destination.

Example request:

```sh
curl "http://localhost:1911/distance?origin=New+York&destination=Los+Angeles"
```

## Testing

The project includes unit tests. You can run the tests by executing the following command in the root directory of the project:

```sh
python -m unittest discover
```

## Contributing

Contributions are welcome. Please submit a pull request or create an issue to discuss the changes you want to make.