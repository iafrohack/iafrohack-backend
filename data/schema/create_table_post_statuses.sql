CREATE TABLE post_statuses (
  id SERIAL PRIMARY KEY,
  name VARCHAR (20),
  created_at timestamp default null,
  last_updated_at timestamp DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO post_statuses (id, name, created_at)
values

(1, 'Draft', NOW()),

(2, 'Published', NOW()),

(3, 'Archived', NOW());
