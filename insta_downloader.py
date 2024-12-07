import instaloader

def download_instagram_video(post_url, target_folder):
    try:
        L = instaloader.Instaloader()
        shortcode = post_url.split("/")[-2]
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        L.download_post(post, target=target_folder)
        print(f"Instagram video downloaded to {target_folder}")
    except Exception as e:
        print(f"Error downloading Instagram video: {e}")
