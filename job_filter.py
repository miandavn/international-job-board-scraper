import csv
from pathlib import Path


INPUT_FILE = Path("data/sample_jobs.csv")
OUTPUT_FILE = Path("output/matching_jobs.csv")

TARGET_LANGUAGE = "English"
TARGET_COUNTRY = "Germany"
TARGET_CATEGORIES = {
    "Talent Acquisition",
    "Recruiting Operations",
    "HR Technology",
    "HR Operations",
}
HYBRID_LOCATIONS = {"Düsseldorf", "Cologne"}


def is_match(job):
    """Return True when a job meets the defined search criteria."""

    language_match = job["language"].strip() == TARGET_LANGUAGE
    country_match = job["country"].strip() == TARGET_COUNTRY
    category_match = job["category"].strip() in TARGET_CATEGORIES

    work_model = job["work_model"].strip()
    location = job["location"].strip()

    location_match = (
        work_model == "Remote"
        or (work_model == "Hybrid" and location in HYBRID_LOCATIONS)
    )

    return (
        language_match
        and country_match
        and category_match
        and location_match
    )


def create_match_reason(job):
    """Explain why a vacancy matched the search criteria."""

    if job["work_model"].strip() == "Remote":
        location_reason = "remote role in Germany"
    else:
        location_reason = f"hybrid role in {job['location'].strip()}"

    return (
        f"English-language {job['category'].strip()} opportunity; "
        f"{location_reason}"
    )


def remove_duplicates(jobs):
    """Remove duplicate vacancies using title, company and location."""

    unique_jobs = []
    seen = set()

    for job in jobs:
        identifier = (
            job["job_title"].strip().lower(),
            job["company"].strip().lower(),
            job["location"].strip().lower(),
        )

        if identifier not in seen:
            seen.add(identifier)
            unique_jobs.append(job)

    return unique_jobs


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    with INPUT_FILE.open("r", encoding="utf-8", newline="") as file:
        jobs = list(csv.DictReader(file))

    matching_jobs = [job for job in jobs if is_match(job)]
    matching_jobs = remove_duplicates(matching_jobs)

    for job in matching_jobs:
        job["match_reason"] = create_match_reason(job)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "job_title",
        "company",
        "location",
        "country",
        "language",
        "work_model",
        "category",
        "url",
        "match_reason",
    ]

    with OUTPUT_FILE.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(matching_jobs)

    print(f"Reviewed {len(jobs)} sample vacancies.")
    print(f"Found {len(matching_jobs)} matching vacancies.")
    print(f"Results saved to {OUTPUT_FILE}.")


if __name__ == "__main__":
    main()
