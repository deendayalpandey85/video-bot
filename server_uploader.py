import requests
import os
def get_upload_url(flic_token):
    url = "https://api.socialverseapp.com/posts/generate-upload-url"
    headers = {
        "Flic-Token": flic_token,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        upload_url = response.json().get("upload_url")
        hash_value = response.json().get("hash")
        return upload_url, hash_value
    else:
        print(f"Error getting upload URL: {response.status_code}")
        return None, None

# Function to upload the video
def upload_video(upload_url, video_path):
    try:
        with open(video_path, 'rb') as video_file:
            response = requests.put(upload_url, files={'file': video_file})
        if response.status_code == 200:
            print("Video uploaded successfully!")
        else:
            print(f"Error uploading video: {response.status_code}")
    except Exception as e:
        print(f"Error uploading video: {e}")

# Function to create a post on the server
def create_post(flic_token, title, hash_value, category_id):
    url = "https://api.socialverseapp.com/posts"
    headers = {
        "Flic-Token": flic_token,
        "Content-Type": "application/json"
    }
    
    body = {
        "title": title,
        "hash": hash_value,
        "is_available_in_public_feed": False,
        "category_id": category_id  # Example category_id = 1
    }
    
    try:
        response = requests.post(url, json=body, headers=headers)
        if response.status_code == 200:
            print("Post created successfully!")
        else:
            print(f"Error creating post: {response.status_code}")
    except Exception as e:
        print(f"Error creating post: {e}")
