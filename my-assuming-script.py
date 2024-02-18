import boto3

def create_snapshot_in_cross_account(volume_id, target_account_role_arn, region_name='your_region_here'):
    # Create an STS client
    sts_client = boto3.client('sts', region_name=region_name)

    # Assume role in the target account
    assumed_role = sts_client.assume_role(
        RoleArn=target_account_role_arn,
        RoleSessionName='AssumeRoleSession'
    )

    # Create an EC2 client using the assumed role credentials
    ec2_client = boto3.client(
        'ec2',
        aws_access_key_id=assumed_role['Credentials']['AccessKeyId'],
        aws_secret_access_key=assumed_role['Credentials']['SecretAccessKey'],
        aws_session_token=assumed_role['Credentials']['SessionToken'],
        region_name=region_name
    )

    try:
        # Create snapshot
        snapshot_response = ec2_client.create_snapshot(
            VolumeId=volume_id,
            Description=f'Snapshot for volume {volume_id}'
        )

        snapshot_id = snapshot_response['SnapshotId']
        print(f'Snapshot {snapshot_id} created for volume {volume_id}')

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Specify the Volume ID
    volume_id = "vol-0b2b3667ce70b4a35"

    # Specify the target AWS account role ARN
    target_account_role_arn = "arn:aws:iam::206582773499:role/my-remote-role"

    # Specify the AWS region
    region_name = "us-east-2"

    # Call the function to create a snapshot in the target account
    create_snapshot_in_cross_account(volume_id, target_account_role_arn, region_name)
