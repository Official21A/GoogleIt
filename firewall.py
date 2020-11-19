import mechanicalsoup


def https_check(domain):
	return domain.startswith("https:")


def privacy_policy(url):
	browser = mechanicalsoup.Browser()
	try:
		page = browser.get(url)
	except:
		return False
	page_soup = page.soup 
	links = page_soup.findAll('a')
	inner_links = [a.text.lowwer() for a in links]
	return "privacy policy" in inner_links