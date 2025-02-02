# HNG12 Stage 0 Backend API

This is a simple Flask-based API for the HNG Internship Stage 0 task. The API returns the user's email, the current datetime in UTC, and a GitHub repository URL.

## Features
- Returns JSON response with:
  - `email`: Your email address
  - `current_datetime`: Current UTC time in ISO 8601 format
  - `github_url`: Link to your GitHub repository

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yvonnegichovi/HNG-Internship-c12.git
cd HNG-Internship-c12
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```

### 4. Test the API
Open your browser or use curl/Postman:
```bash
curl http://127.0.0.1:5000/
```
Expected response:
```json
{
  "email": "yvonnegichovi@gmail.com",
  "current_datetime": "2025-01-31T12:34:56Z",
  "github_url": "https://github.com/yvonnegichovi/HNG-Internship-c12"
}
```

## Deployment (Koyeb)
### 1. Visit Koyeb.com and Login
```bash
koyeb login
```

### 2. Create a Koyeb App
```bash
koyeb create your-app-name
```

### 3. Deploy the Application
```bash
git add .
git commit -m "Deploying to Koyeb"
git push
```

### 4. Test the Live API
```bash
curl https://striking-susanne-suivi-2e3e7030.koyeb.app/

```

## License
This project is open-source and available under the MIT License.

## Author
**Yvonne Ng'endo**

For any questions, feel free to reach out or open an issue in the repository!
