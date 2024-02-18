import boto3

def create_snapshots_for_tagged_volumes(tag_key, tag_value):
    # Create a Boto3 EC2 client
    ec2_client = boto3.client('ec2',region_name='us-east-2')

    # Describe volumes with the specified tag
    response = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': f'tag:{tag_key}',
                'Values': [tag_value]
            }
        ]
    )

    # Create snapshots for each volume
    for volume in response['Volumes']:
        volume_id = volume['VolumeId']

        # Create snapshot
        snapshot_response = ec2_client.create_snapshot(
            VolumeId=volume_id,
            Description=f'Snapshot for volume {volume_id}'
        )

        snapshot_id = snapshot_response['SnapshotId']
        print(f'Snapshot {snapshot_id} created for volume {volume_id}')

if __name__ == "__main__":
    # Specify the tag key and value
    tag_key = 'mg'
    tag_value = 'mg'

    # Call the function to create snapshots
    create_snapshots_for_tagged_volumes(tag_key, tag_value)
