
def iosLocalization(translations, languageId):
    contents = ""
    for tr in translations:
        # Ignore empty keys.
        if (not len(tr.iosKey)):
            continue
        contents += "\"{0}\" = \"{1}\";\n".format(tr.iosKey, tr.translations[languageId])
    return contents
