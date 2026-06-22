import { useState } from "react";
import type { FormEvent } from "react";
import { api } from "../api/client";

export default function RegisterPage({ onAuthed }: { onAuthed: () => void }) {
  const [full_name, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [phone_number, setPhoneNumber] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setSuccess(null);
    try {
      await api.auth.register(full_name, email, phone_number, password);
      await api.auth.login(email, password);
      setSuccess("Account created. Opening jobs...");
      onAuthed();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Register failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="page">
      <h2>Register</h2>
      <form onSubmit={handleSubmit} className="form">
        <label>
          Full name
          <input value={full_name} onChange={(e) => setFullName(e.target.value)} required />
        </label>
        <label>
          Email
          <input value={email} onChange={(e) => setEmail(e.target.value)} required type="email" />
        </label>
        <label>
          Phone number
          <input
            value={phone_number}
            onChange={(e) => setPhoneNumber(e.target.value)}
            required
            type="tel"
            inputMode="tel"
            placeholder="9876543210"
          />
        </label>
        <label>
          Password
          <input value={password} onChange={(e) => setPassword(e.target.value)} required type="password" />
        </label>
        <button type="submit" disabled={loading}>
          {loading ? "Registering..." : "Register"}
        </button>
        {success && <div className="success">{success}</div>}
        {error && <div className="error">{error}</div>}
        <div className="muted">After registering, you will be logged in automatically.</div>
      </form>
    </div>
  );
}
