class S3Bucket:
    def __init__(self):
        self.buckets={}

    def create_bucket(self, name):
        self.buckets[name]={}
        print(f"Bucket {name} created.")

    def put_object(self, bucket, key, data):
        if bucket in self.buckets:
            self.buckets[bucket][key]=data
            print(f"Object {key} added to bucket {bucket}.")
        else:
            print(f"Bucket {bucket} not found.")

    def get_object(self, bucket, key):
        return self.buckets.get(bucket, {}).get(key, None)

class S3BucketWithPermissions(S3Bucket):
    def __init__(self):
        super().__init__()
        self.permissions={}

    def set_permission(self, bucket, key, permission):
        if bucket not in self.permissions:
            self.permissions[bucket]={}
        self.permissions[bucket][key]=permission
        print(f"Permission {permission} set for {key} in bucket {bucket}.")

    def check_permission(self, bucket, key, action):
        return self.permissions.get(bucket, {}).get(key) == action

class S3BucketWithVersioning(S3Bucket):
    def __init__(self):
        super().__init__()
        self.versions={}

    def put_object(self, bucket, key, data):
        if bucket not in self.versions:
            self.versions[bucket]={}
        if key not in self.versions[bucket]:
            self.versions[bucket][key]=[]
        self.versions[bucket][key].append(data)
        super().put_object(bucket, key, data)

    def get_object_versions(self, bucket, key):
        return self.versions.get(bucket, {}).get(key, [])

# Ejemplo de uso de S3
s3=S3BucketWithPermissions()
s3.create_bucket('mybucket')
s3.put_object('mybucket', 'file1.txt', 'Hello, S3 Bucket!')
print(s3.get_object('mybucket', 'file1.txt'))  
s3.set_permission('mybucket', 'file1.txt', 'read')
print(s3.check_permission('mybucket', 'file1.txt', 'read'))

s3v=S3BucketWithVersioning()
s3v.create_bucket('versioned-bucket')
s3v.put_object('versioned-bucket', 'file2.txt', 'Version 1')
s3v.put_object('versioned-bucket', 'file2.txt', 'Version 2')
print(s3v.get_object_versions('versioned-bucket', 'file2.txt'))


def configure_versioning(bucket):
    bucket.versioning_enabled=True
    print(f"Versioning enabled for bucket {bucket}")

def configure_replication(source_bucket, dest_bucket):
    source_bucket.replication=dest_bucket
    print(f"Replication from {source_bucket} to {dest_bucket} configured")

def host_static_website(bucket):
    bucket.website_enabled=True
    print(f"Static website hosting enabled for bucket {bucket}")

def configure_glacier_lifecycle(bucket):
    bucket.lifecycle_policy='glacier'
    print(f"Glacier lifecycle policy configured for bucket {bucket}")


class S3BucketWithFeatures(S3Bucket):
    def __init__(self):
        super().__init__()
        self.versioning_enabled=False
        self.replication=None
        self.website_enabled=False
        self.lifecycle_policy=None

s3f=S3BucketWithFeatures()
s3f.create_bucket('feature-bucket')
configure_versioning(s3f)
configure_replication(s3f, 'replica-bucket')
host_static_website(s3f)
configure_glacier_lifecycle(s3f)
