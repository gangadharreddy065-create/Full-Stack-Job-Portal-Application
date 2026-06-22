import { useEffect, useState } from "react";
import { api } from "../api/client";

export default function MyApplicationsPage({
  onSelectJob,
}: {
  onSelectJob: (jobId: number) => void;
}) {
  const [apps, setApps] = useState<Array<{ id: number; job_id: number; cover_letter: string; created_at: string }>>(
    []
  );
  const [error, setError] = useState<string | null>(null);

  async function load() {
    setError(null);
    try {
      const data = await api.applications.mine();
      setApps(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to load applications");
    }
  }

  useEffect(() => {
    (async () => {
      await load();
    })();

  }, []);



  return (
    <div className="page">
      <h2>My Applications</h2>
      {error && <div className="error">{error}</div>}

      <div className="cards">
        {apps.map((a) => (
          <button key={a.id} className="card" onClick={() => onSelectJob(a.job_id)}>
            <div className="card-title">Job #{a.job_id}</div>
            <div className="card-meta">Applied: {new Date(a.created_at).toLocaleString()}</div>
          </button>
        ))}
      </div>

      {!error && apps.length === 0 && <div className="muted">No applications yet.</div>}
    </div>
  );
}

