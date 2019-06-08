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


INSERT INTO blog_posts (id,category_id, content, created_at)
values (
1,
1,
'{
  "title": "Welcome to iAfrohack! An Exciting Journey Begins...",
  "background_image": "https://r-fa.bstatic.com/images/hotel/max1024x768/788/78823412.jpg",
  "summary": "Introducing you to a New Adventure: Welcome to iAfrohack...",
  "content": "<p style=margin-top: 30px;>What a journey this has been! <\/p><br \/>\r\n    <p ><\/p>\r\n    <p >I first wanted to build a blog of mine back when I was still in college.\r\n     The motivations were as crystal clear then than they are now: I wanted a space of my own where I could express my ideas, share knowledge I had gained, while learning how to do so many things along the way. <\/p>\r\n    <p ><\/p>\r\n    <p >Social media networks did not cut it for me due to several reasons: your main audience there are your friends ( and online &ldquo;friends&rdquo;) and family.\r\n    There are simply things they are not interested in, in what you have to say. <\/p>\r\n    <p ><\/p>\r\n    <p >In addition, there is way too much noise in social media, your thoughts will be just another piece of the noise, and disappear in the abyss that is social media feeds.<\/p>\r\n    <p ><\/p>\r\n    <p >With a space of your own, the audience is the entire World, your writings and ideas will stand the test of times as long as your site is up, and as you put the ideas together you are\r\n    primed to learn a great deal along the way.<\/p>\r\n    <p ><\/p>\r\n    <p >I don&rsquo;t want to just write blog posts: I want to build blog posts and so much more. <\/p>\r\n    <p >I want to experiment with new and existing tech stacks in projects and share what I learned from them.<\/p>\r\n    <p >I want to share the tips as I get them in my experience as a human being. <\/p>\r\n\r\n    <p > I want to build things together with my audience, learn together.<\/p>\r\n    <p ><\/p>\r\n    <p >It has been a long journey and I have finally made the first step happen.<\/p>\r\n    <p ><\/p>\r\n    <p >So, come Join me to this new adventure. <\/p>\r\n\r\n\r\n    <p ><\/p>\r\n    <p ><\/p>\r\n\r\n    <p>  Welcome to iAfrohack!<\/p>",
 "tags": [ "software engineering", "blog", "coding"],
  "category": "software-engineering"
}',
NOW());
