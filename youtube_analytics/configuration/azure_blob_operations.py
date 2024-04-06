from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os
from youtube_analytics.logger import logging

load_dotenv()



def upload_to_blob_storage(file_path,file_name):
    blob_service_client = BlobServiceClient.from_connection_string(os.environ.get("CONNECTION_STRING"))
    blob_client = blob_service_client.get_blob_client(container=os.environ.get("CONTAINER_NAME"),blob=file_name)

    with open(file_path,"rb") as data:
        blob_client.upload_blob(data)

    logging.info(f"{file_name} has been uploaded!!")
    
