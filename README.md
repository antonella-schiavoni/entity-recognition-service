## About The Project

A rest api that exposes and endpoint that returns the entities found in a text.

### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
* [Spacy](https://spacy.io/)
* [Locust](https://locust.io/)

## Getting Started

In order to run this project successfully, please follow the next steps.

### Prerequisites

This project was developed using python version 3.8.8. Make sure you are using the same python version. Use this command
to check it:

   ```sh
   python3 --version
   ```

### Installation

1. Download this code and store it in a folder
2. Create a new virtual environment
    ```sh
    python3 -m venv app
    source ./app/bin/activate
    ```
3. Install requirements:
    ```sh
    pip install -r src/requirements.txt
    ```
4. Download the spacy model
    ```sh
   python -m spacy download en_core_web_lg
   ```

## Usage

1. Run the server
   ```sh
   python src/app.py
   ```

2. Use a curl to obtain the response from the server.
   ```sh
   curl http://192.168.0.101:5000/entities?event_title=pink
   ```

3. To run the project test, just excecute:
    ```sh 
    pytest
    ```

4. To execute load tests with locust:
    ```sh
   locust 
    ```
   You can access the web interface at
   ```
    http://0.0.0.0:8089
   ```
   If this url does not work, doublecheck in the server logs that the port is available or that the url is the same.

5. Once you are in the URL, you have to type the following parametes:
    - Number of users (peak concurrency)
    - Spawn rate (users started/second)
    - Host (e.g. http://www.example.com). In here make sure you use the Flask url address. You can access it from Flask
      server logs

Alternatively, you can run the server using a docker image.

1. Install Docker in your laptop.

2. Build the docker image from the root directory of the project folder
   ```sh
    docker build -t app:latest -f Dockerfile .
   ```
3. Make sure you have the 5000 port available. If it's not the case, you can stop the current process in the 5000 port
   by executing
   ```sh
   lsof -ti:5000 | xargs kill -9
   ```
4. Then run the
   ```sh
   docker run -p 5000:5000 app
   ```
5. Use a curl to obtain the response from the dockerized server
   ```sh
   curl http://0.0.0.0:5000/entities?event_title=pink
   ```

## Roadmap

- [] Implement RegexEntityRecognizer
- [] Improve SynonymEntityRecognizer
- [] Sample data and do manual annotation
- [] Fine tune spacy ner model using the tagged data
