def generate_growth_plan(data, engagement_rate):
    bio = data["bio"]
    followers = data["followers"]

    plan = f"""
    SOCIAL MEDIA AUDIT REPORT

    Followers: {followers}
    Engagement Rate: {engagement_rate}%

    Profile Bio Analysis:
    {bio}

    Growth Recommendations:
    - Improve hook in first 3 seconds of reels
    - Use stronger CTA in captions
    - Post minimum 4 reels per week
    - Optimize hashtags for niche relevance
    - Collaborate with micro influencers

    30-Day Plan:
    Week 1: Optimize bio + branding
    Week 2: Launch reel consistency
    Week 3: Start paid ads testing
    Week 4: Influencer collaboration
    """

    return plan
