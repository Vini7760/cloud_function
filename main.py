import os
from google.cloud import storage

def organize_files(data, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This function organizes files into folders based on their type.
    """
    file_name = data['name']
    bucket_name = data['bucket']

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    # Determine the folder based on file type
    _, file_extension = os.path.splitext(file_name)
    if file_extension in ['.jpg', '.jpeg', '.png']:
        folder = 'images/'
    elif file_extension in ['.txt', '.pdf', '.docx']:
        folder = 'documents/'
    elif file_extension in ['.mp3', '.wav']:
        folder = 'audio/'
    else:
        folder = 'others/'

    # Construct the new file path
    new_file_name = folder + os.path.basename(file_name)
    new_blob = bucket.blob(new_file_name)

    # Copy the file to the new location
    new_blob.rewrite(blob)

    # Delete the old file
    blob.delete()

    print(f"File {file_name} moved to {new_file_name}.")
