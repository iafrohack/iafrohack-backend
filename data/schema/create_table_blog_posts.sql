CREATE TABLE blog_posts (

  id SERIAL PRIMARY KEY,
  status_id INTEGER DEFAULT 1,
  category_id INTEGER,
  content json not null,
  created_at timestamp default null,
  last_updated_at timestamp DEFAULT CURRENT_TIMESTAMP,

  FOREIGN KEY (status_id) REFERENCES post_statuses (id) ON UPDATE CASCADE,
  FOREIGN KEY (category_id) REFERENCES post_categories (id) ON UPDATE CASCADE

);

CREATE INDEX created_at_idx ON blog_posts USING btree (created_at);
CREATE INDEX last_updated_at_idx ON blog_posts USING btree (last_updated_at);


INSERT INTO blog_posts (category_id, content, created_at)
values (
1,
'{ "title": "Welcome to iAfrohack! An exciting journey begins...", "background_image": "https://r-fa.bstatic.com/images/hotel/max1024x768/788/78823412.jpg", "summary": "First blog post on iAfrohack. So much talk about, so many adventures to explore", "content": "<p>This has been quite a journey. With so many things going around me,I had been procrastinating on getting this blog out in the wild...", "category": "software-engineering" }',
NOW());
