from fastapi import FastAPI, HTTPException
from app.schemas import Post

app = FastAPI()

text_posts = {
    1: {"title": "Launching the Tiny AI Helper", "content": "Today I deployed a lightweight assistant designed to answer quick coding questions"},
    2: {"title": "Gardening Journal: Planta Care for Spring", "content": "This week I pruned rose bushes, checked soil pH, and planned a mulching schedule"},
    3: {"title": "Cloud Cost Optimization Experiment", "content": "I compared reserved instances vs. on-demand and set auto-scaling thresholds"},
    4: {"title": "Photo Walk: Street Portraits in Golden Hour", "content": "Captured candid portraits emphasizing natural lighting and urban textures"},
    5: {"title": "DIY Desk Organizer Build Plan", "content": "I designed a modular wooden organizer with cable channels and a drawer"},
    6: {"title": "Meal Prep: 5-Ingredient Weeknight Dinners", "content": "I planned five quick, balanced meals for busy weeknights"},
    7: {"title": "City Bike Route Optimization", "content": "Mapped safer routes through neighborhoods with fewer hills"},
    8: {"title": "Indie Game Prototype Milestone", "content": "Implemented a basic player controller and a minimal level design"},
    9: {"title": "Morning Routine Study", "content": "Tracked wake times and hydration to improve focus"},
    10: {"title": "Book Club: Sci-Fi Short Stories", "content": "Selected a collection of crisp, thought-provoking tales for discussion"},
}


@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int) -> Post:

    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: Post) -> Post:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post

