import instaloader

def get_instagram_data(username):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)

    followers = profile.followers
    following = profile.followees
    posts = profile.mediacount
    bio = profile.biography
    external_url = profile.external_url

    post_data = []
    for post in profile.get_posts():
        post_data.append({
            "likes": post.likes,
            "comments": post.comments,
            "caption": post.caption
        })
        if len(post_data) >= 12:
            break

    return {
        "followers": followers,
        "following": following,
        "posts": posts,
        "bio": bio,
        "external_url": external_url,
        "post_data": post_data
    }
