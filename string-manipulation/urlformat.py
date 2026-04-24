def parse_url(url):
    parts = url.split("/")
    base = parts[0] + "//" + parts[2]
    path = "/" + "/".join(parts[3:])
    
    return base, path

base, path = parse_url("https://example.com/products/item1")
print("Base URL:", base)
print("Path:", path)