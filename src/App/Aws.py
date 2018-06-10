import boto3

class Aws():
    s3 = None
    aws_bucket = "vidii-user-media-uploads"

    def __init__(self, access_key, secret_key):
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
        )

        # Call S3 to list current buckets
        # response = self.s3.list_buckets()
        #
        # # Get a list of all bucket names from the response
        # buckets = [bucket['Name'] for bucket in response['Buckets']]
        #
        # # Print out the bucket list
        # print("Bucket List: %s" % buckets)

    def upload_file(self, file_name, new_file_name):
        self.s3.upload_file(file_name, self.aws_bucket, new_file_name)

        return 'https://s3.amazonaws.com/vidii-user-media-uploads/{}'.format(new_file_name)
