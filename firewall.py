import mechanicalsoup


def https_check(domain):
	return domain.startswith("https:")


def privacy_policy(url):
	browser = mechanicalsoup.StatefulBrowser()
	try:
		browser.open(url, timeout=1)
	except Exception as e:
		print(f">> privacy policy checking failed (url opening). {e}")
		return False
	try:
		page = browser.get_current_page() 
		if page.title.startswith("40"):
			raise Exception(":: Error in domain.")
	except Exception as e:
		print(f">> privacy policy checking failed (scanning). {e}")
		return False
	links = page.findAll('a')
	inner_links = [a.text.lower() for a in links]
	return "privacy policy" in inner_links


def active(url):
	https_result = https_check(url)
	pp_result = privacy_policy(url)
	return https_result or pp_result


def checkin(url_list):
	return [ url for url in url_list if active(url)]
