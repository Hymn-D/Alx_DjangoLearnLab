# Django Blog Authentication System

## Overview
This authentication system allows users to register, log in, log out, and manage their profiles.

## Features
- User registration (with email)
- Login and logout
- Profile view and update
- Secure password hashing
- CSRF protection on all forms

## URLs
- /register – User registration
- /login – User login
- /logout – Logout
- /profile – Profile management

## Testing
1. Register a user.
2. Log in and visit the profile page.
3. Update user info and confirm success message.
4. Log out and confirm redirection to login page.

# Blog Post Management Features

## Overview
Implements full CRUD functionality for blog posts.

## Features
- List all posts (`/posts/`)
- View details of a single post (`/posts/<id>/`)
- Create new post (authenticated users only)
- Edit/Delete posts (only the author can)

## Permissions
- **Create:** Login required
- **Update/Delete:** Only post author
- **List/Detail:** Public access

## Testing
1. Log in and create a post.
2. Edit and delete only your own posts.
3. Check unauthorized access is blocked.
4. Verify navigation between pages.

# Comment Feature Documentation

## Overview
Adds a comment system for blog posts. Each comment is linked to a specific post and user.

## Features
- Display all comments under each blog post
- Authenticated users can add new comments
- Only comment authors can edit or delete their comments

## URLs
- Add comment: `/post/<post_id>/comments/new/`
- Edit comment: `/comments/<id>/update/`
- Delete comment: `/comments/<id>/delete/`

## Permissions
- **Add:** Authenticated users only
- **Edit/Delete:** Only comment author

## Testing
1. Log in and add a comment to a post.
2. Edit and delete your own comment.
3. Confirm others can only view your comments, not modify them.

