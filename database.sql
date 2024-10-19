"""Database tables"""


DROP TABLE IF EXISTS sentences;


CREATE TABLE sentences (
    id SERIAL PRIMARY KEY,
    sentence TEXT NOT NULL,
    timestamp TIMESTAMPTZ DEFAULT NOW()
);
