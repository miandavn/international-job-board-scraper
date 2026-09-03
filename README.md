# International Job Board Scraper

![Run Job Filter](https://github.com/miandavn/international-job-board-scraper/actions/workflows/run-job-filter.yml/badge.svg)

A working recruitment automation prototype that filters structured vacancy data according to defined role, location, language and working-model criteria.

## Project status

✅ Working prototype

The current version uses fictional sample data and does not scrape live job boards. It demonstrates the filtering, duplicate-detection, reporting and automation logic that could form part of a broader job-market monitoring workflow.

## The problem

Searching multiple job platforms manually is repetitive and time-consuming. Relevant vacancies can be difficult to identify when job titles, working models and terminology vary between employers.

This project explores how a structured workflow can:

- Apply consistent job-search criteria
- Identify relevant English-language vacancies
- Filter opportunities by location and working model
- Focus on selected HR and recruitment categories
- Remove duplicate results
- Explain why each vacancy matched
- Produce a structured CSV report
- Run automatically through GitHub Actions

## How it works

1. Fictional vacancy data is stored in `data/sample_jobs.csv`.
2. `job_filter.py` reads and evaluates each vacancy.
3. The script applies predefined recruitment criteria.
4. Duplicate vacancies are removed.
5. Matching jobs receive a plain-language match reason.
6. Results are saved to `output/matching_jobs.csv`.
7. GitHub Actions runs the workflow automatically when the script or sample data changes.

## Current search criteria

The demonstration currently looks for:

- English-language opportunities
- Roles based in Germany
- Remote roles anywhere in Germany
- Hybrid roles in Düsseldorf or Cologne
- Opportunities in:
  - Talent Acquisition
  - Recruiting Operations
  - HR Technology
  - HR Operations

The criteria are intentionally defined in the Python script so they can be reviewed and changed easily.

## Repository structure

```text
international-job-board-scraper/
├── .github/
│   └── workflows/
│       └── run-job-filter.yml
├── data/
│   └── sample_jobs.csv
├── output/
│   └── matching_jobs.csv
├── job_filter.py
└── README.md
