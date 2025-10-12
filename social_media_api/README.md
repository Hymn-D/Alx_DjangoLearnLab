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

## ❤️ Likes API
| Method | Endpoint | Description |
|---------|-----------|-------------|
| POST | /api/posts/<pk>/like/ | Like a post |
| POST | /api/posts/<pk>/unlike/ | Unlike a post |

## 🔔 Notifications API
| Method | Endpoint | Description |
|---------|-----------|-------------|
| GET | /api/notifications/ | List all notifications for the logged-in user |

### Example Notification
```json
{
  "id": 1,
  "actor": "john",
  "verb": "liked your post",
  "target_object": "First Post",
  "timestamp": "2025-10-12T15:00:00Z"
}
