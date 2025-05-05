"""
Common data for the assignment

*******************  DO NOT MODIFY!!!!  *********************
*******************  DO NOT MODIFY!!!!  *********************
*******************  DO NOT MODIFY!!!!  *********************
*******************  DO NOT MODIFY!!!!  *********************
*******************  DO NOT MODIFY!!!!  *********************
*******************  DO NOT MODIFY!!!!  *********************
*******************  DO NOT MODIFY!!!!  *********************

"""

import time
import requests

from cse351 import *

TOP_API_URL = 'http://127.0.0.1:8790'


# ----------------------------------------------------------------------------
def get_data_from_server(url):
    retries = 50
    delay = 0.01 # seconds
    for i in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            if response.status_code == 200:
                return response.json()
            break

        except requests.exceptions.ConnectionError as e:
            if i < retries - 1:
                time.sleep(delay)
            else:
                print("Max retries reached. Failing.")
                
        except requests.exceptions.Timeout:
            ...
            
        except requests.exceptions.RequestException as e:
            break

    return None