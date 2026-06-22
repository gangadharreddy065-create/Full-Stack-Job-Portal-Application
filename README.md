# Full Stack Job Portal Application

Monorepo with:
- `backend/`: FastAPI + SQLite (dev) + JWT auth
- `frontend/`: React

## Quick start

### 1) Backend
```bash
cd "backend"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### 2) Frontend
In another terminal:
```bash
cd "frontend"
npm install
npm run dev
```

Open the URL printed by the frontend dev server.

## Deployment

Recommended simple setup:
- Backend: Render Web Service
- Frontend: Render Static Site, Vercel, or Netlify

This repo also includes `render.yaml`, so you can deploy both services together using a Render Blueprint.

### Render Blueprint
1. Push this project to GitHub.
2. In Render, choose **New +** -> **Blueprint**.
3. Connect the GitHub repo and select `render.yaml`.
4. When Render asks for environment variables:
   - `FRONTEND_ORIGINS`: set this to your frontend URL, for example `https://job-portal-frontend.onrender.com`
   - `VITE_API_BASE_URL`: set this to your backend URL, for example `https://job-portal-api.onrender.com`

If Render gives your services slightly different URLs, update those two values after the first deploy and redeploy.

### Backend settings
If deploying the `backend/` folder as a Render Web Service:

```bash
Build Command: pip install -r requirements.txt
Start Command: python migrate_add_phone_number.py && python seed_internships.py && uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Set environment variables:

```bash
JWT_SECRET_KEY=<use-a-long-random-secret>
FRONTEND_ORIGINS=https://your-frontend-domain.com
DATABASE_URL=sqlite:///./app.db
```

For a public app where users will register and apply, use Render PostgreSQL or attach a persistent disk and store SQLite under that disk path. Otherwise, local SQLite data can be lost when the service redeploys or restarts.

### Frontend settings
If deploying the `frontend/` folder as a static site:

```bash
Build Command: npm install && npm run build
Publish Directory: dist
```

Set this environment variable to your deployed backend URL:

```bash
VITE_API_BASE_URL=https://your-backend-domain.onrender.com
```

For local development, copy `frontend/.env.example` to `frontend/.env.local` if you want to customize the API URL.
