import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__


def upload(file_name, file):
    with open('keys.txt', 'r') as f:        
        Lines = f.readlines()
        connect_str = Lines[0]

    # Create a local directory to hold blob data
    container_name = 'image'


    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create a file in the local data directory to upload and download
    local_file_name = file_name
    # upload_file_path = os.path.join(local_path, local_file_name)

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container='image', blob=local_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
    # with open(upload_file_path, "rb") as data:
    blob_client.upload_blob(file, overwrite=True)