import unittest
from unittest.mock import patch, MagicMock
import boto3

class TestEC2Launch(unittest.TestCase):

    @patch("boto3.client")
    def test_ec2_launch(self, mock_boto_client):
        mock_ec2 = MagicMock()
        mock_boto_client.return_value = mock_ec2

        # Simulate instance launch
        mock_ec2.run_instances.return_value = {
            "Instances": [{"InstanceId": "i-1234567890abcdef0"}]
        }

        # Import and run EC2 launch code
        from my_script import ec2
        response = ec2.run_instances(
            ImageId="ami-0c55b159cbfafe1f0",
            InstanceType="t2.micro",
            KeyName="test-key",
            SecurityGroups=["default"],
            MinCount=1,
            MaxCount=1,
            UserData="#!/bin/bash"
        )

        self.assertEqual(response["Instances"][0]["InstanceId"], "i-1234567890abcdef0")

if __name__ == "__main__":
    unittest.main()
