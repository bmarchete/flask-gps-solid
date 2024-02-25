import pytest
from unittest.mock import Mock

from domain.model.travel_distance import TravelDistance
from domain.service.travel_distance_service import TravelDistanceService, TravelDistanceServiceException

@pytest.fixture
def mock_cache_storage():
    return Mock()

@pytest.fixture
def mock_travel_distance():
    return Mock()

@pytest.fixture
def mock_repository():
    return Mock()

@pytest.fixture
def travel_distance_service(mock_cache_storage, mock_travel_distance, mock_repository):
    return TravelDistanceService(travel_distance=mock_travel_distance, cache_storage=mock_cache_storage, repository=mock_repository)

origin = "CityA"
destination = "CityB"
distance = 100

def test_get_distance_from_cache(travel_distance_service, mock_cache_storage):

    mock_cache_storage.get.return_value = distance


    result = travel_distance_service.get_distance(origin, destination)

    assert result.distance == distance
    mock_cache_storage.get.assert_called_once_with(f"{origin}__{destination}")

def test_get_distance_when_not_in_cache(travel_distance_service, mock_cache_storage, mock_travel_distance, mock_repository):

    travel_distance_obj = TravelDistance(origin=origin, destination=destination, distance=distance)
    mock_cache_storage.get.return_value = None
    mock_travel_distance.get_distance.return_value = travel_distance_obj


    result = travel_distance_service.get_distance(origin, destination)

    assert result.distance == distance
    mock_cache_storage.set.assert_called_once_with(f"{origin}__{destination}", distance, 60)
    mock_repository.create_travel_distance.assert_called_once_with(travel_distance_obj)

def test_get_distance_when_travel_distance_service_throws_travel_distance_service_exception(travel_distance_service, mock_cache_storage, mock_travel_distance, mock_repository):

    mock_cache_storage.get.return_value = None
    mock_travel_distance.get_distance.side_effect = TravelDistanceServiceException

    with pytest.raises(TravelDistanceServiceException):
        travel_distance_service.get_distance(origin, destination)

    mock_cache_storage.set.assert_not_called()
    mock_repository.create_travel_distance.assert_not_called()

