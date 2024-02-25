import time
import pytest
from unittest.mock import patch
from domain.utils.retry_with_backoff import RetryLimitExceededException, retry_with_backoff

def counter_func(limit):
    count = [0] 

    def inner_func():
        count[0] += 1
        if count[0] < limit:
            raise ValueError("Simulated Failure")
        return "Success"

    return inner_func

def test_success_on_first_try():
    @retry_with_backoff(retries=3, backoff_in_seconds=1)
    def success_func():
        return "Success"

    assert success_func() == "Success"

def test_success_after_retries():
    limited_func = counter_func(2)

    @retry_with_backoff(retries=3, backoff_in_seconds=1)
    def wrapped_func():
        return limited_func()

    assert wrapped_func() == "Success"

def test_failure_after_exceeding_retry_limit():
    limited_func = counter_func(5)

    @retry_with_backoff(retries=3, backoff_in_seconds=1)
    def wrapped_func():
        return limited_func()

    with pytest.raises(RetryLimitExceededException):
        wrapped_func()


def test_backoff_timing():
    attempts = []

    @retry_with_backoff(retries=3, backoff_in_seconds=1)
    def fail_func():
        attempts.append(time.time())
        raise Exception("Simulated Failure")

    with patch('time.sleep') as mock_sleep:
        with pytest.raises(RetryLimitExceededException):
            fail_func()

       
        assert mock_sleep.call_count == 2  

     
        mock_sleep.assert_any_call(1) 
        mock_sleep.assert_any_call(2) 