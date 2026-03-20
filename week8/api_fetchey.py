import request
import logging

logging.basicConfig(
        filename="api_errors.logs",
        level=logging.ERROR,
        format="%(asctime)s-%(levelname)s - %(message)s"
        )

API_URL ="https://jsonplaceholder.typicode.com/posts/1"

def fetch_data():
    print("Starting API requerst...") 
    
    try:
        response= requests.get(API_URL, timeout=5)

        print(f"Status Code: {response.status_code}")
        response.raise_for_status()

        data = response.json()

        print("Data successfully fetched!")
        return data
    except requests.exceptions.Timeout:
        logging.error("Request timed out")
        print("Error: Unable to connect to the API. check your internet.")

    except requests.exceptions.ConnectionError:
        logging.error("Connection Error occurred")
        print("Error: Unable to connect to the API. Check your Internet.")

    except requests.exceptions.HTTPError:
        logging.error(f"HTTP error: {e}")
        print("Error: Server returned an error ({e}")

    except ValueError:
        logging.error("Invalid JSON response")
        print("Error: Received invalid data from Api.")

    except Exception as e:
        logging.error(f"Unexpected Error: {e}")
        print("An unexpected Error occured.")

    finally:
        print("Api attempt finished.")


    if __name__ == "__main__":
        result= fetch_data()
        if result:
            print("\nFetched Data:")
            print(result)

