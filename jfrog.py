#!/usr/bin/env python3

import requests
import subprocess

def jfrogUpload():
    # Define the URL, file path, and authentication credentials
    url = 'http://54.237.49.56:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    file_path = '/var/lib/jenkins/workspace/BATCH4/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    username = 'admin'
    password = 'Password@123'  # Replace 'your_password' with the actual password

    # Send the PUT request with authentication and file upload
    with open(file_path, 'rb') as file:
        response = requests.put(url, auth=(username, password), data=file)

    # Check the response status code
    if response.status_code == 201:
        print("\nPUT request was successful!")
    else:
        print(f"PUT request failed with status code {response.status_code}")
        print("Response content:")
        print(response.text)


def main():
    jfrogUpload()

##############################################################################################################
if __name__ == "__main__":
    main()
