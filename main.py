from indeed import extract_indeed_pages, extract_indded_jobs


last_indeed_page = extract_indeed_pages()
indeed_jobs = extract_indded_jobs(last_indeed_page)

print(indeed_jobs)