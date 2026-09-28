# Nexora — Social Media Platform

Nexora is a full-stack social media web application developed as **Task 2** for the **CodeAlpha Full Stack Development Internship**.

The project provides a modern social networking experience where users can create profiles, publish posts, interact through likes and comments, follow other users, search accounts, and explore community posts.

## Features

- User registration, login, and logout
- User profiles
- Edit profile
- Create posts with captions
- Upload images from the computer
- Optional image URL support
- Like and unlike posts
- Add comments
- Follow and unfollow users
- Followers and following counts
- Search users by username or name
- Suggested users
- Explore page
- Profile post grid
- Delete own posts
- Responsive desktop and mobile interface
- Django admin panel

## Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Django Templates

### Backend
- Python
- Django

### Database
- SQLite

### Authentication
- Django Authentication System

## CodeAlpha Task 2 Requirements

This project covers the required functionality for **Task 2 — Social Media Platform**:

- ✅ User profiles
- ✅ Posts
- ✅ Comments
- ✅ Like system
- ✅ Follow / unfollow system
- ✅ Frontend using HTML, CSS, and JavaScript
- ✅ Django backend
- ✅ Database for users, posts, comments, and follower relationships

## Project Structure

```text
CodeAlpha_SocialMediaPlatform/
│
├── social/                     # Main social media application
│   ├── migrations/             # Database migrations
│   ├── admin.py                # Django admin configuration
│   ├── forms.py                # Registration, profile and post forms
│   ├── models.py               # Profile, Post, Comment, Like and Follow models
│   ├── signals.py              # Automatic profile creation
│   ├── tests.py                # Automated application tests
│   ├── urls.py                 # Application routes
│   └── views.py                # Feed, profile and interaction logic
│
├── social_platform/            # Django project configuration
├── static/                     # CSS, JavaScript and favicon
├── templates/                  # Application templates
├── media/                      # User-uploaded images (created locally)
│
├── manage.py
├── requirements.txt
├── FINAL_TEST_CHECKLIST.md
├── LOCAL_TEST_CHECKLIST.md
├── PROJECT_REQUIREMENTS_CHECKLIST.md
└── README.md
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_SocialMediaPlatform.git
cd CodeAlpha_SocialMediaPlatform
```

### 2. Create a virtual environment

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
venv\Scripts\activate
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Apply database migrations

```powershell
python manage.py migrate
```

### 6. Run automated tests

```powershell
python manage.py test
```

The final test result should end with:

```text
OK
```

### 7. Create an admin account (optional)

```powershell
python manage.py createsuperuser
```

### 8. Start the development server

```powershell
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

## Application Flow

1. Create an account or log in.
2. View posts in the home feed.
3. Create a post with a caption and optional image.
4. Like or unlike posts.
5. Add comments.
6. Search for other users.
7. Visit user profiles.
8. Follow or unfollow users.
9. View followers, following counts, and profile posts.
10. Discover community posts from the Explore page.

## Automated Testing

The project contains tests for:

- Automatic profile creation
- User registration
- Post creation
- Like and unlike functionality
- Comment creation
- Follow and unfollow functionality
- User search
- Explore page
- Image upload

Run all tests with:

```powershell
python manage.py test
```

## Database and Media

- SQLite is used for local development.
- `db.sqlite3` is generated locally after migrations and is excluded from Git.
- Uploaded post images are stored inside `media/posts/`.
- Runtime media files are excluded from Git.

## Project Demo

▶ **[Watch the Nexora Project Demo on LinkedIn](https://www.linkedin.com/feed/update/urn:li:ugcPost:7510187402771189760/)**

## Internship

**CodeAlpha — Full Stack Development Internship**  
**Task 2 — Social Media Platform**

---

Developed by **Gopi Vemuri**.
