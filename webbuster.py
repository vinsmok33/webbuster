#!/usr/bin/env python3
import requests
import argparse
import concurrent.futures

def dir_bruteforce(url, wordlist, threads=20, codes=[200,301,302,403]):
    if not url.startswith("http"):
        url = "http://" + url

    def check_path(path):
        full_url = f"{url.rstrip('/')}/{path.strip()}"
        try:
            r = requests.get(full_url, timeout=5)
            if r.status_code in codes:
                return f"[{r.status_code}] {full_url}"
        except requests.RequestException:
            return None

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(check_path, word) for word in wordlist]
        for f in concurrent.futures.as_completed(futures):
            res = f.result()
            if res:
                results.append(res)

    return results

def main():
    parser = argparse.ArgumentParser(description="WebBuster - simple web directory brute forcer")
    parser.add_argument("url", help="Target URL (e.g. http://example.com)")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist")
    parser.add_argument("-t", "--threads", type=int, default=20, help="Number of threads (default: 20)")
    args = parser.parse_args()

    with open(args.wordlist, "r") as f:
        words = f.readlines()

    found = dir_bruteforce(args.url, words, threads=args.threads)
    print("\n--- Results ---")
    for item in found:
        print(item)

if __name__ == "__main__":
    main()
