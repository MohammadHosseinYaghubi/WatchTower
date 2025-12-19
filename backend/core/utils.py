import requests
import time

def check_service(url, timeout=5):
    """
    Check the status of a service by making a GET request to the provided URL.

    Args:
        url (str): The URL of the service to check.
        timeout (int): The timeout for the request in seconds.

    Returns:
        dict: A dictionary containing the status of the service.
              {
                  'is_up': bool,
                  'status_code': int or None,
                  'response_time': float or None
              }
    """
    start = time.time()
    try:
        response = requests.get(url, timeout=timeout)
        elapsed = time.time() - start

        return {
            # 'is_up': response.status_code == 200,
            'is_up': response.status_code < 500,
            'status_code': response.status_code,
            'response_time': round(elapsed, 3)
        }
    except requests.RequestException:
        return {
            'is_up': False,
            'status_code': None,
            'response_time': None,
        }