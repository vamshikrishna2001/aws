import boto3

def list_volume_tags(volume_id):
    # Create an EC2 client
    ec2_client = boto3.client('ec2',region_name='us-east-2')

    try:
        # Describe volume to get its tags
        response = ec2_client.describe_volumes(VolumeIds=[volume_id])

        # Extract tags from the response
        if 'Volumes' in response and response['Volumes']:
            volume_tags = response['Volumes'][0].get('Tags', [])
            
            # Print the tags
            if volume_tags:
                print(f"Tags for Volume {volume_id}:")
                for tag in volume_tags:
                    key = tag['Key']
                    value = tag['Value']
                    print(f"{key}: {value}")
            else:
                print(f"No tags found for Volume {volume_id}")
        else:
            print(f"Volume {volume_id} not found.")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Specify the Volume ID
    volume_id = "vol-0c5c9b02577ebfbf8"

    # Call the function to list tags for the specified volume
    list_volume_tags(volume_id)
