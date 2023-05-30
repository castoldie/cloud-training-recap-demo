import os
import numpy as np

##################  VARIABLES  ##################
DATA_SIZE = os.environ.get('DATA_SIZE')
CHUNK_SIZE = os.environ.get('CHUNK_SIZE')
GCP_PROJECT = os.environ.get('GCP_PROJECT')
GCP_PROJECT_WAGON = os.environ.get('GCP_PROJECT_WAGON')
BQ_DATASET = os.environ.get('BQ_DATASET')
BQ_REGION = os.environ.get('BQ_REGION')
MODEL_TARGET = os.environ.get('MODEL_TARGET')
BUCKET_NAME = os.environ.get('BUCKET_NAME')
##################  CONSTANTS  #####################
LOCAL_DATA_PATH = os.path.join(os.path.expanduser('~'), ".lewagon", "mlops", "data")
LOCAL_REGISTRY_PATH =  os.path.join(os.path.expanduser('~'), ".lewagon", "mlops", "training_outputs")

COLUMN_NAMES_RAW = ['fare_amount','pickup_datetime', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count']

DTYPES_RAW = {
    "fare_amount": "float32",
    "pickup_datetime": "datetime64[ns, UTC]",
    "pickup_longitude": "float32",
    "pickup_latitude": "float32",
    "dropoff_longitude": "float32",
    "dropoff_latitude": "float32",
    "passenger_count": "int16"
}

DTYPES_PROCESSED = np.float32
