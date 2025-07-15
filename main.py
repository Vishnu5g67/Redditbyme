import praw

reddit = praw.Reddit(
    client_id="ltT3GwgUf9XsxDakhOro7A", # Replace with your actual client ID
    client_secret="aZVwBFAbHj2_H8a3TQyj3FI5kfwcWA", # Replace with your actual client secret
    user_agent="vishnuvardhan" # Replace with your actual user agent
)

def extract_username(url):
    if url.endswith("/"):
        url = url[:-1]
    return url.split("/")[-1]

def fetch_user_data(username):
    user = reddit.redditor(username)
    posts = []
    comments = []

    for post in user.submissions.new(limit=30):
        posts.append(f"[Post in r/{post.subreddit}]: {post.title}\n{post.selftext}\n")

    for comment in user.comments.new(limit=30):
        comments.append(f"[Comment in r/{comment.subreddit}]: {comment.body}\n")

    return posts, comments

def save_raw_data(username, posts, comments):
    with open(f"{username}_rawdata.txt", "w", encoding="utf-8") as f:
        f.write(f"Reddit Username: {username}\n\n")
        f.write("=== POSTS ===\n")
        f.write("\n".join(posts))
        f.write("\n\n=== COMMENTS ===\n")
        f.write("\n".join(comments))


if __name__ == "__main__":
    url = input("Enter Reddit profile URL (e.g., https://www.reddit.com/user/kojied/): ")
    username = extract_username(url)
    posts, comments = fetch_user_data(username)
    save_raw_data(username, posts, comments)
    print(f"\n✅ Data saved to {username}_rawdata.txt. Open it and paste it into ChatGPT to generate the user persona.")