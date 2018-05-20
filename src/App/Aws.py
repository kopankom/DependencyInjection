import boto3

class Aws():
    s3 = None
    def __init__(self, access_key, secret_key, session_token):
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
            aws_session_token=SESSION_TOKEN,
        )

        # Call S3 to list current buckets
        response = self.s3.list_buckets()

        # Get a list of all bucket names from the response
        buckets = [bucket['Name'] for bucket in response['Buckets']]

        # Print out the bucket list
        print("Bucket List: %s" % buckets)

    def setPassword(self, password):
        print(password)

    def setMongo(self, mongo):
        print(mongo.getSomething())

    def container_execution(self):
        print('container_execution')
