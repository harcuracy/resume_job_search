from apify_client import ApifyClient
import os
from dotenv import load_dotenv

load_dotenv()

apify_client = ApifyClient(os.getenv("APIFY_API_KEY"))


def fetch_linkedin_jobs(search_query: str, location: str, max_results: int = 10):
  run_input = {
    "title": search_query,
    "location": location,
    "rows": max_results,
    "proxy": {
        "useApifyProxy": True,
        "apifyProxyGroups": ["RESIDENTIAL"],
    },
}
  run = apify_client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)
  jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
  return jobs

def fetch_naukri_jobs(search_query,location: str, max_results = 50):

    run_input = {
        "keyword": search_query,
        "maxJobs": max_results,
        "freshness": "all",
        "sortBy": "relevance",
        "experience": "all",
    }

    # Run the Actor and wait for it to finish
    run = apify_client.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs

