import { useEffect, useMemo, useState } from "react";
import "./App.css";
import PageShell from "./pages/PageShell";
import JobsPage from "./pages/JobsPage";
import JobDetailPage from "./pages/JobDetailPage";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import MyApplicationsPage from "./pages/MyApplicationsPage";
import type { Route } from "./pages/types";
import { api } from "./api/client";

function parseRoute(): Route {
  const hash = window.location.hash.replace("#", "").replace(/^\//, "");
  if (!hash || hash === "/" || hash === "jobs") return { name: "jobs" };
  const [path, param] = hash.split("/");
  if (path === "job" && param) {
    const id = Number(param);
    if (!Number.isNaN(id)) return { name: "job", jobId: id };
  }
  if (path === "mine") return { name: "mine" };
  if (path === "login") return { name: "login" };
  if (path === "register") return { name: "register" };
  return { name: "jobs" };
}

function App() {
  const [route, setRoute] = useState<Route>(() => parseRoute());
  const [me, setMe] = useState<null | Awaited<ReturnType<typeof api.auth.me>>>(null);
  const [authError, setAuthError] = useState<string | null>(null);

  const authed = !!me;

  useEffect(() => {
    function onHashChange() {
      setRoute(parseRoute());
    }
    window.addEventListener("hashchange", onHashChange);
    return () => window.removeEventListener("hashchange", onHashChange);
  }, []);

  useEffect(() => {
    async function loadMe() {
      const token = localStorage.getItem("token");
      if (!token) {
        setMe(null);
        return;
      }
      try {
        const data = await api.auth.me();
        setMe(data);
      } catch {
        localStorage.removeItem("token");
        setMe(null);
      }
    }
    loadMe();
  }, []);

  const navRight = useMemo(() => {
    if (!authed) {
      return (
        <div className="nav-right">
          <a className="nav-link" href="#/login">
            Login
          </a>
          <a className="nav-link" href="#/register">
            Register
          </a>
        </div>
      );
    }

    return (
      <div className="nav-right">
        <span className="nav-user">{me?.full_name}</span>
        <a
          className="nav-link"
          href="#/mine"
          aria-disabled={route.name === "mine"}
        >
          My Applications
        </a>
        <button
          className="nav-btn"
          onClick={() => {
            localStorage.removeItem("token");
            setMe(null);
            setAuthError(null);
            window.location.hash = "#/jobs";
          }}
        >
          Logout
        </button>
      </div>
    );
  }, [authed, me?.full_name, route.name]);

  return (
    <PageShell
      right={
        <div className="nav">
          {navRight}
          {authError ? <div className="error">{authError}</div> : null}
        </div>
      }
    >
      {route.name === "jobs" && (
        <JobsPage
          onSelectJob={(jobId) => {
            window.location.hash = `#/job/${jobId}`;
          }}
        />
      )}

      {route.name === "job" && (
        <JobDetailPage
          jobId={route.jobId}
          onApplied={() => {
            window.location.hash = "#/mine";
          }}
          onBack={() => {
            window.location.hash = "#/jobs";
          }}
        />
      )}

      {route.name === "mine" &&
        (authed ? (
          <MyApplicationsPage
            onSelectJob={(jobId) => {
              window.location.hash = `#/job/${jobId}`;
            }}
          />
        ) : (
          <LoginPage
            onAuthed={() => {
              window.location.hash = "#/mine";
            }}
          />
        ))}

      {route.name === "login" && (
        <LoginPage
          onAuthed={() => {
            api.auth
              .me()
              .then((data) => setMe(data))
              .catch(() => setMe(null));
            window.location.hash = "#/jobs";
          }}
        />
      )}

      {route.name === "register" && (
        <RegisterPage
          onAuthed={() => {
            setAuthError(null);
            api.auth
              .me()
              .then((data) => setMe(data))
              .catch(() => setMe(null));
            window.location.hash = "#/jobs";
          }}
        />
      )}
    </PageShell>
  );
}

export default App;
