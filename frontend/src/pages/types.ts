export type Route =
  | { name: "jobs" }
  | { name: "job"; jobId: number }
  | { name: "mine" }
  | { name: "login" }
  | { name: "register" };

