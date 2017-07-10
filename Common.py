
CFG_KEY_ID = 0
CFG_VALUE_ID = 1
CFG_KEY_VALUE_COLUMNS_NB = 2

def configurationFromPage(page):
    cfg = {}
    rawValues = page.get_all_values()
    for row in rawValues:
        key = row[CFG_KEY_ID]
        # Only take those rows that
        # * have key value pairs
        # * have keys
        if (len(key) and (len(row) >= CFG_KEY_VALUE_COLUMNS_NB)):
            value = row[CFG_VALUE_ID]
            cfg[key] = value
    return cfg

def parsePage(page, cfg):
    # Get raw page values.
    raw = page.get_all_values()

    translationsColumnId = int(cfg["TRANSLATION_COLUMN"]) - 1

    # Get list of languages.
    languagesRowId = int(cfg["LANGUAGES_ROW"]) - 1
    row = raw[languagesRowId]
    languagesNb = len(row)
    languages = []
    for columnId in range(translationsColumnId, languagesNb):
        languages.append(raw[languagesRowId][columnId])
    print("Found languages: '{0}'".format(languages))
    translations = []

    return translations


