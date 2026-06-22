import { useEffect, useState } from "react";
import type { FormEvent } from "react";
import { api } from "../api/client";

export default function JobDetailPage({
  jobId,
  onApplied,
  onBack,
}: {
  jobId: number;
  onApplied: () => void;
  onBack: () => void;
}) {
  const [job, setJob] = useState<null | Awaited<ReturnType<typeof api.jobs.detail>>>(null);
  const [coverLetter, setCoverLetter] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [applying, setApplying] = useState(false);

  async function load() {
    if (!jobId) return;
    setLoading(true);
    setError(null);
    try {
      const data = await api.jobs.detail(jobId);
      setJob(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to load job");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    (async () => {
      await load();
    })();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [jobId]);



  async function handleApply(e: FormEvent) {
    e.preventDefault();
    if (!job) return;
    setApplying(true);
    setError(null);
    try {
      await api.applications.apply({ job_id: job.id, cover_letter: coverLetter });
      setCoverLetter("");
      onApplied();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Apply failed");
    } finally {
      setApplying(false);
    }
  }

  return (
    <div className="page">
      <button className="linkbtn" onClick={onBack}>
        ← Back
      </button>

      {loading && <div>Loading...</div>}
      {error && <div className="error">{error}</div>}

      {job && (
        <>
          <h2>{job.title}</h2>
          <div className="sub">
            {job.company} • {job.location} • {job.job_type}
          </div>
          <p className="desc">{job.description}</p>

          <form onSubmit={handleApply} className="form">
            <label>
              Cover letter
              <textarea
                value={coverLetter}
                onChange={(e) => setCoverLetter(e.target.value)}
                required
                rows={6}
              />
            </label>
            <button disabled={applying}>{applying ? "Applying..." : "Apply"}</button>
          </form>
        </>
      )}
    </div>
  );
}

