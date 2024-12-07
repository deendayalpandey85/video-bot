from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from server_uploader import get_upload_url, upload_video, create_post

class VideoHandler(FileSystemEventHandler):
    def __init__(self, flic_token):
        self.flic_token = flic_token

    def on_created(self, event):
        if event.src_path.endswith(".mp4"):
            print(f"New video detected: {event.src_path}")
            upload_data = get_upload_url(self.flic_token)
            if upload_data:
                upload_url, file_hash = upload_data
                upload_video(upload_url, event.src_path)
                create_post(self.flic_token, "Uploaded Video", file_hash, category_id=1)  # Example category_id

def start_monitoring(directory, flic_token):
    event_handler = VideoHandler(flic_token)
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=False)
    observer.start()
    print(f"Monitoring directory: {directory}")
    try:
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
        print("Stopped monitoring.")
