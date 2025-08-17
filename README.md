# chingu-backend

Core Components

Backend API: .NET Core Web API (main business logic, login, user management).

AI Service: Python FastAPI (wraps Gemini API, handles AI-related requests).

Database: Firestore (NoSQL, easy to scale, fits MVP needs).

Authentication: Firebase Auth (Google-ready, simple for email/password, Google login, etc.).

Storage: Firebase Storage (for user uploads, documents, images).

Flow

User signs up/logs in → handled by Firebase Auth.

API requests → go to .NET Core backend.

Backend stores/retrieves data from Firestore.

For AI requests → .NET calls Python FastAPI (Gemini wrapper).

Responses returned to frontend.

