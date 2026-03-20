import os
import logging

# Configure logging
logging.basicConfig(
    filename="file_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def copy_file():
    """ Copies the content of one file into another"""
    source = input("Enter source file name: ")
    destination = input("Enter destination file name: ")

    print("Starting file copy...")

    try:
        # Check if source exists
        if not os.path.exists(source):
            raise FileNotFoundError("Source file does not exist.")

        # Prevent overwrite
        if os.path.exists(destination):
            raise FileExistsError("Destination file already exists.")

        # Read and write file
        with open(source, 'r') as src_file:
            content = src_file.read()
            print("Source file read successfully.")

        with open(destination, 'w') as dest_file:
            dest_file.write(content)
            print("Content written to destination.")  

        print("File copied successfully!")

    except FileNotFoundError as e:
        logging.error(e)
        print(f"Error: {e}")

    except FileExistsError as e:
        logging.error(e)
        print(f"Error: {e}")

    except PermissionError:
        logging.error("Permission denied")
        print("Error: You don't have permission to access this file.")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("An unexpected error occurred.")

    finally:
        print("File operation completed.")  


if __name__ == "__main__":
    copy_file()
