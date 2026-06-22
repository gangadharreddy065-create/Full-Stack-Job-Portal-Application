import { useEffect, useState } from "react";
import { api } from "../api/client";

export type Job = Awaited<ReturnType<typeof api.jobs.list>> extends Array<infer J> ? J : never;

export default function JobsPage({
  onSelectJob,
}: {
  onSelectJob: (jobId: number) => void;
}) {
  const [q, setQ] = useState("");
  const [location, setLocation] = useState("");
  const [jobs, setJobs] = useState<Job[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function load() {
    setLoading(true);
    setError(null);
    try {
      const data = await api.jobs.list({ q: q || undefined, location: location || undefined });
      setJobs(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to load jobs");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    (async () => {
      await load();
    })();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);



  return (
    <div className="page">
      <h2>Jobs</h2>
      <div className="filters">
        <label>
          Search
          <input value={q} onChange={(e) => setQ(e.target.value)} placeholder="title" />
        </label>
        <label>
          Location
          <input value={location} onChange={(e) => setLocation(e.target.value)} placeholder="location" />
        </label>
        <button onClick={load} disabled={loading}>
          {loading ? "Searching..." : "Search"}
        </button>
      </div>

      {error && <div className="error">{error}</div>}

      <div className="cards">
        {jobs.map((j) => (
          <button key={j.id} className="card" onClick={() => onSelectJob(j.id)}>
            <div className="card-title">{j.title}</div>
            <div className="card-meta">
              {j.company} • {j.location}
            </div>
            <div className="card-type">{j.job_type}</div>
          </button>
        ))}
      </div>
    </div>
  );
}

