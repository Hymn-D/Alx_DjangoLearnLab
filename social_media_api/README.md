# Social Media API — Posts & Comments

## Endpoints

### Posts
| Method | Endpoint | Description |
|---------|-----------|-------------|
| GET | /api/posts/ | List all posts |
| POST | /api/posts/ | Create new post |
| GET | /api/posts/{id}/ | Retrieve post |
| PUT/PATCH | /api/posts/{id}/ | Update post (owner only) |
| DELETE | /api/posts/{id}/ | Delete post (owner only) |

### Comments
| Method | Endpoint | Description |
|---------|-----------|-------------|
| GET | /api/comments/ | List all comments |
| POST | /api/comments/ | Create comment |
| GET | /api/comments/{id}/ | Retrieve comment |
| PUT/PATCH | /api/comments/{id}/ | Update comment (owner only) |
| DELETE | /api/comments/{id}/ | Delete comment (owner only) |

### Features
- Authentication required for creation/edit/delete
- Pagination (5 per page)
- Search posts by title/content
- Permissions enforce ownership
