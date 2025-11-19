CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    streamer_name VARCHAR(255) UNIQUE NOT NULL,
    twitch_id VARCHAR(255),
    youtube_id VARCHAR(255),
    plan VARCHAR(50)
);

CREATE TABLE twitch_followers (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    from_id VARCHAR(255),
    to_id VARCHAR(255),
    followed_at TIMESTAMP,
    fetched_at TIMESTAMP
);

CREATE TABLE streams (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    platform VARCHAR(50),
    title VARCHAR(255),
    started_at TIMESTAMP,
    ended_at TIMESTAMP
);
