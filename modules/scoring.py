def calculate_engagement_rate(followers, post_data):
    if followers == 0:
        return 0

    total_engagement = 0
    for post in post_data:
        total_engagement += post["likes"] + post["comments"]

    avg_engagement = total_engagement / len(post_data)
    engagement_rate = (avg_engagement / followers) * 100

    return round(engagement_rate, 2)


def overall_score(engagement_rate, posts):
    score = 0

    if engagement_rate > 6:
        score += 30
    elif engagement_rate > 3:
        score += 20
    else:
        score += 10

    if posts > 50:
        score += 20
    else:
        score += 10

    return score
