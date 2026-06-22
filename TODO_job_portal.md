e # TODO - Full Stack Job Portal Application

## Plan overview
- Backend (FastAPI) already scaffolded with endpoints:
  - GET /api/jobs
  - GET /api/jobs/{id}
  - POST /api/jobs (admin only)
  - POST /api/auth/register
  - POST /api/auth/login
  - GET /api/auth/me
  - POST /api/applications
  - GET /api/applications/mine
- Next step is building frontend React app that consumes these endpoints.

## Steps
1. Update frontend to replace default Vite template with job portal UI + routing.
2. Implement API client (fetch wrapper) with JWT storage + Authorization header.
3. Implement pages:
   - Auth: Login + Register
   - Jobs: List + Job Details + Apply
   - My Applications: list applications + status/confirmation
4. Update App layout/nav + basic styling.
5. Run frontend and verify API calls against running backend.

