import concurrent.futures
import requests
import time

def download_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.status_code, len(response.content)
    except requests.exceptions.RequestException as e:
        return None, str(e)

urls = [
    "https://www.github.com",
    "https://code.visualstudio.com",
    "https://www.lds.com",
    "https://www.python.org",
    "https://docs.python.org",
    "https://pypi.org",
    "https://www.wikipedia.org",
    "https://en.wikipedia.org/wiki/Main_Page",
    "https://creativecommons.org",
    "https://www.gnu.org",
    "https://www.eff.org",
    "https://www.w3.org",
    "https://www.ietf.org",
    "https://example.com",
    "https://example.net",
    "https://example.org",
    "https://www.rfc-editor.org",
    "https://www.iana.org",
    "https://www.internet.org",
    "https://www.sqlite.org/index.html",
    "https://pandas.pydata.org",
    "https://numpy.org",
    "https://scipy.org",
]

start_time = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:

    # map all the urls to the download_page function
    # This will use all 10 threads in the pool. This means that 10 URLS
    # will be downloaded concurrently.
    results = executor.map(download_page, urls)

    for url, result in zip(urls, results):
        status_code, content_length = result
        if status_code:
            print(f"Downloaded {url}: Status {status_code}, Length: {content_length}")
        else:
            print(f"Error downloading {url}: {content_length}")

end_time = time.time()

# --- Sequential Version (for comparison) ---
print()
start_time_sequential = time.time()
for url in urls:
    status, length = download_page(url)
    if status:
        print(f"Downloaded {url}: Status {status}, Length: {length}")
    else:
        print(f"Error downloading {url}: {length}")

end_time_sequential = time.time()

print()
print(f"Total time taken (with thread pool): {end_time - start_time:.2f} seconds")
print(f"Total time taken (sequential): {end_time_sequential - start_time_sequential:.2f} seconds")
