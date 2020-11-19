import mechanicalsoup


def https_check(domain):
	return domain.startswith("https:")


def privacy_policy(url):
	browser = mechanicalsoup.Browser()
	try:
		browser.open(url, timeout=5)
	except:
		print(">> privacy policy checking failed.")
		return False
	page_soup = browser.page.soup 
	links = page_soup.findAll('a')
	inner_links = [a.text.lower() for a in links]
	return "privacy policy" in inner_links


def active(url):
	print(">> {}".format(url.strip()))
	https_result = https_check(url)
	print(https_result)
	pp_result = privacy_policy(url)
	print(pp_result)
	print()
	return https_result or pp_result


def checkin(url_list):
	return [ url for url in url_list if active(url)]



def test_bench():
	with open("./docs/google.txt", 'r') as file:
		lines = file.readlines()
		urls = [line for line in lines]
		print("> File read:")
		print(urls)
		urls = checkin(urls)
		print("> Output:")
		print(urls)


if __name__ == "__main__":
	test_bench()