- [ ] Ajax : Ajax is asynchronous javascript requests.
- [ ] Advantages of react:
  - [ ] A single js file can be downloaded and all rendering will happen without reloading page.
- [ ] Change content of activate file in virtualenv to:
```bash
source (find . -name activate.fish)
clear
```

- [ ] Trailing slash observations
  - [ ] Don't apply trailing slash in urls.py
  - [ ] When using XMLHttpResponse, apply trailing slash.
  - [ ] When creating POST form in html, apply trailing slash.
2:36

### HTTP Code
- [ ] 403 : Require Login
- [ ] 401 : Unauthorized
- [ ] 400 : Invalid request
- [ ] 201 : Created Successfully
- [ ] 200 : Action done Successfully
- [ ] 500 : Server me kuchh jhol hua !!!


### Javascript
- [ ] hljs : Code highlighting and copy functionality.

### Production
- [ ] To serve static files, use AWS-S3 and preferably cloud-front.
- [ ] To use react static files in django, copy the build->static folder to the django-root directory.
  - [ ] Also add in settings.py:
  ```py
  STATICFILES_DIRS =[ os.path.join(BASE_DIR, 'static')]
  STATIC_ROOT = os.path.join(BASE_DIR, 'static-root')
  ```