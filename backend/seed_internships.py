from app.db.init_db import init_db
from app.db.models import Job
from app.db.session import SessionLocal


INTERNSHIPS = [
    {
        "company": "Kaizenat",
        "title": "Node.js Intern",
        "location": "Remote",
        "job_type": "Internship",
        "description": "Internship opportunity for candidates interested in Node.js backend development.",
    },
    {
        "company": "Kaizenat",
        "title": "React.js Intern",
        "location": "Remote",
        "job_type": "Internship",
        "description": "Internship opportunity for candidates interested in React.js frontend development.",
    },
    {
        "company": "Kaizenat",
        "title": "Python Intern",
        "location": "Remote",
        "job_type": "Internship",
        "description": "Internship opportunity for candidates interested in Python development.",
    },
    {
        "company": "Kasplo",
        "title": "Frontend Intern",
        "location": "Bangalore",
        "job_type": "Internship",
        "description": "Frontend internship focused on building user interfaces and web application features.",
    },
    {
        "company": "Techdew",
        "title": "PHP Developer Intern",
        "location": "Chennai",
        "job_type": "Internship",
        "description": "PHP developer internship for candidates interested in server-side web development.",
    },
    {
        "company": "Impactiva",
        "title": "Data Analyst Intern",
        "location": "Chennai",
        "job_type": "Internship",
        "description": "Data analyst internship focused on working with business data, reports, and insights.",
    },
    {
        "company": "Ventra Health",
        "title": "Data Analyst",
        "location": "Remote",
        "job_type": "Full-time",
        "description": "Remote data analyst role focused on analyzing data and supporting reporting workflows.",
    },
    {
        "company": "Zoho",
        "title": "Training & Internship",
        "location": "Chennai",
        "job_type": "Internship",
        "description": "Training and internship opportunity for candidates looking to build practical software skills.",
    },
    {
        "company": "Infinity Crest Group",
        "title": "Junior UI Designer",
        "location": "Chennai",
        "job_type": "Full-time",
        "description": "Junior UI designer role focused on creating clean and usable digital interfaces.",
    },
    {
        "company": "Winngoo UK Pvt Ltd",
        "title": "UI/UX Designer",
        "location": "Chennai",
        "job_type": "Full-time",
        "description": "UI/UX designer role focused on user experience, visual design, and product interfaces.",
    },
    {
        "company": "Skills Nurture",
        "title": "Data Science Intern",
        "location": "Remote",
        "job_type": "Internship",
        "description": "Data science internship focused on data analysis, modeling, and practical machine learning tasks.",
    },
    {
        "company": "Ascendas Technology",
        "title": "Junior Data Analyst",
        "location": "Chennai",
        "job_type": "Full-time",
        "description": "Junior data analyst role focused on preparing reports and finding insights from data.",
    },
    {
        "company": "Neolysi Technologies",
        "title": "Junior Software Developer",
        "location": "Chennai",
        "job_type": "Full-time",
        "description": "Junior software developer role for candidates starting their career in application development.",
    },
    {
        "company": "Neysa",
        "title": "Full Stack Developer Intern",
        "location": "Chennai",
        "job_type": "Internship",
        "description": "Full stack developer internship focused on frontend, backend, and web application development.",
    },
    {
        "company": "SCRY AI",
        "title": "Frontend Intern",
        "location": "Hyderabad",
        "job_type": "Internship",
        "description": "Frontend internship focused on building responsive web interfaces and frontend features.",
    },
    {
        "company": "Koders",
        "title": "Frontend Intern",
        "location": "Remote",
        "job_type": "Internship",
        "description": "Remote frontend internship for candidates interested in modern web UI development.",
    },
    {
        "company": "Krevok",
        "title": "UI/UX Designer",
        "location": "Chennai",
        "job_type": "Full-time",
        "description": "UI/UX designer role focused on interface design, user flows, and product experience.",
    },
    {
        "company": "Talview",
        "title": "Software Developer Intern",
        "location": "Bangalore",
        "job_type": "Internship",
        "description": "Software developer internship for candidates looking to gain hands-on coding experience.",
    },
    {
        "company": "Giva",
        "title": "Frontend Developer",
        "location": "Bangalore",
        "job_type": "Full-time",
        "description": "Frontend developer role focused on building and improving web application interfaces.",
    },
    {
        "company": "Adcanopus Digital Media",
        "title": "Frontend Developer",
        "location": "Bangalore",
        "job_type": "Full-time",
        "description": "Frontend developer role focused on creating responsive and engaging web experiences.",
    },
    {
        "company": "Syntellite",
        "title": "MERN Stack Intern",
        "location": "Bangalore",
        "job_type": "Internship",
        "description": "MERN stack internship focused on MongoDB, Express, React, and Node.js application development.",
    },
    {
        "company": "Care.fi",
        "title": "Data Analyst",
        "location": "Bangalore",
        "job_type": "Full-time",
        "description": "Data analyst role focused on analyzing business data and supporting decision-making.",
    },
]


def seed_jobs() -> None:
    init_db()
    db = SessionLocal()
    try:
        added = 0
        skipped = 0

        for item in INTERNSHIPS:
            exists = (
                db.query(Job)
                .filter(
                    Job.company == item["company"],
                    Job.title == item["title"],
                    Job.location == item["location"],
                )
                .first()
            )
            if exists:
                skipped += 1
                continue

            db.add(Job(**item))
            added += 1

        db.commit()
        print(f"Added {added} jobs. Skipped {skipped} existing jobs.")
    finally:
        db.close()


if __name__ == "__main__":
    seed_jobs()
