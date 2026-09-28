# Final Local Test Checklist

Run these commands after extracting the project:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py test
python manage.py runserver
```

Expected automated test result: all tests pass with `OK`.

Manual browser check:
1. Register a new account — placeholders and validation errors should be visible.
2. Log in and create a text post.
3. Create another post by choosing a JPG/PNG/WebP/GIF from the computer.
4. Open Search and search your own username — it should appear.
5. Create/login to a second account.
6. Follow the first account from Suggestions or Profile.
7. Like and comment on the first account's post.
8. Open Profile and verify post/follower/following counts.
9. Open Explore and verify posts appear in the grid.
10. Edit profile and confirm bio/name/location changes persist.
