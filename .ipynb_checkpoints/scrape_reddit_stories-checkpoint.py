import praw

# === FILL THIS IN ===
reddit = praw.Reddit(
    client_id='ecJz6vxIeYOUCvTvbRd9uQ',
    client_secret='SM9lSGpNNevkdgOHe7IP8SSL2zBIzw',
    user_agent='script by u/First-Entertainer923'
)

# Settings
subreddit_name = 'TrueOffMyChest'
num_posts = 10

# Grab posts
subreddit = reddit.subreddit(subreddit_name)
posts = subreddit.top(limit=num_posts)

# Save to text file
with open("reddit_stories.txt", "w", encoding="utf-8") as f:
    for post in posts:
        if post.selftext.strip():  # Only posts with actual text
            f.write(f"Title: {post.title}\n")
            f.write(f"Author: u/{post.author}\n")
            f.write(f"Upvotes: {post.score}\n")
            f.write(f"Link: https://reddit.com{post.permalink}\n\n")
            f.write(post.selftext.strip() + "\n")
            f.write("\n" + "="*80 + "\n\n")

print("✅ Done! Stories saved to reddit_stories.txt")
