#!/usr/bin/env python3

import requests
import os

# JFrog Artifactory details
ARTIFACTORY_URL = "http://192.168.13.130:8082/artifactory/example-repo-local/"
JAR_FILE_PATH = "/var/lib/jenkins/workspace/BATCH4/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"  # Update the path if necessary
ARTIFACT_NAME = "kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"
USERNAME = "admin"
PASSWORD = "Password@123"

# Upload JAR file to JFrog Artifactory
def upload_to_jfrog():
    if not os.path.exists(JAR_FILE_PATH):
        print("JAR file not found. Please build it first.")
        return

    url = ARTIFACTORY_URL + ARTIFACT_NAME
    with open(JAR_FILE_PATH, 'rb') as jar_file:
        response = requests.put(url, auth=(USERNAME, PASSWORD), data=jar_file)
    
    if response.status_code in [200, 201]:
        print("JAR file uploaded successfully!")
    else:
        print(f"Failed to upload JAR. Status Code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    upload_to_jfrog()
