import yamlParser

site = yamlParser.yamlParse()

print site["site_name"]
print site["theme"]
