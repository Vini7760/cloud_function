tep 1: Set Up Google Cloud Storage (GCS)
Create a GCS Bucket:
Go to the Google Cloud Console.
Navigate to "Cloud Storage" and create a new bucket.
Step 2: Set Up a Cloud Function
Create a Cloud Function:

Navigate to "Cloud Functions" in the Google Cloud Console.
Click "Create Function".
Configure the basic settings such as name, region, and memory allocation.
Set the Trigger:

Choose "Cloud Storage" as the trigger.
Select the bucket you created.
Choose "Finalized" for the event type to trigger the function when a file is uploaded.

step: 3 is the code

Deploy the Cloud Function:
Click "Deploy" to deploy the function.
Step 3: Test the Function
Upload Files:
Upload different types of files (images, documents, audio) to the GCS bucket.
The Cloud Function should automatically organize these files into respective folders (images/, documents/, audio/, others/).
Final Steps
Verify File Organization:

Check the bucket to ensure files are moved to the correct folders.
Monitor and Logs:

Monitor the function's execution and view logs in the Google Cloud Console under "Cloud Functions" and "Logs".
This setup ensures that whenever a new file is uploaded to the GCS bucket, the Cloud Function is triggered, and the file is moved to the appropriate folder based on its type.
