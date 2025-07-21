# Lighthouse reports

All Chrome Lighthouse reports are from the deployed version at Heroku.com, using Incognito mode.

## Index page (home / index.html)

![lighthouse_home.png](/static/readme/images/lighthouse_home.png)

## Blog list (blog / blog_list.html)

![lighthouse_blog.png](/static/readme/images/lighthouse_blog.png)

## Blog post (blog / blog_post.html)

![lighthouse_blog_post.png](/static/readme/images/lighthouse_blog_post.png)

## Events view (events / event_list.html)

![lighthouse_events.png](/static/readme/images/lighthouse_events.png)

## Event detail (events / event_detail.html)

![lighthouse_event_detail.png](/static/readme/images/lighthouse_event_detail.png)

## Event registration (events / event_registration.html)

![lighthouse_event_registration.png](/static/readme/images/lighthouse_event_registration.png)

## User profile (user_profile / user_profile.html)
![user_profile.png](/static/readme/images/lighthouse_user_profile.png)

## About & contact (about / about.html)
![](/static/readme/images/lighthouse_about.png)

## Test score evaluation

**Test score evaluation**
- The drop in SEO when showing blog posts and events is due to the standard "Read more" buttons, and not using more specific descriptions. Using other descriptions would however cause a more distracting appearance unless care would be taken to show all buttons still a uniform size.
- The drop in Assesibility in event_registration is due to a aria-hidden setting in a bootstrap modal. The decision was to leave this alone rather than risk unwanted behaviour in a third party component.
- Not surprisingly, event_registration has the lowest performance. This is due to the STRIPE payment implemented on this page but the performance is still within acceptable limits.
- Assesibility was first somewhat low on the blog_list view. This was due to insufficient contrast between the comment symbol and counter. This was adjusted to reach full assesibility score.