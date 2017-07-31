
import os

IOS_LOCALIZATION_DIR_NAME_MASK = u"{0}.lproj"
IOS_LOCALIZATION_FILE_NAME = u"Localizable.strings"

IOS_LOCALIZATION_GROUP_COMMENT_FORMAT = u"/* {0} */\n"
IOS_LOCALIZATION_FORMAT = u"\"{0}\" = \"{1}\";\n"

IOS_CONSTANTS_HEADER_FILE_NAME = u"LocalizationConstants.h"
IOS_CONSTANTS_SOURCE_FILE_NAME = u"LocalizationConstants.m"

IOS_CONSTANTS_HEADER_HEADER = u"#import <Foundation/Foundation.h>\n\n"
IOS_CONSTANTS_HEADER_CONST_FORMAT = u"extern NSString * const {0};\n"
IOS_CONSTANTS_HEADER_DESC_START_FORMAT = u"\n/*!\n"
IOS_CONSTANTS_HEADER_DESC_END_FORMAT = u"*/\n"
IOS_CONSTANTS_HEADER_COMM_FORMAT = u"* {0}\n\n"
IOS_CONSTANTS_HEADER_LANG_FORMAT = u"* @b {0}@: {1}\n\n"

IOS_CONSTANTS_SOURCE_HEADER = u"#import \"LocalizationConstants.h\"\n\n"
IOS_CONSTANTS_SOURCE_FORMAT = u"NSString * const {0} = @\"{1}\";\n"

IOS_CONSTANTS_SWIFT_FILE_NAME = u"LocalizationConstants.swift"
IOS_CONSTANTS_SWIFT_ENUM_HEADER = u"import Foundation\n\nenum L10n {\n"
IOS_CONSTANTS_SWIFT_ENUM_ITEM_FORMAT = u"\tcase {0}\n"
IOS_CONSTANTS_SWIFT_ENUM_FOOTER = u"}\n\n"
IOS_CONSTANTS_SWIFT_EXT_HEADER = u"""
extension L10n: CustomStringConvertible {
\tvar description: String { return self.string }

\tvar string: String {
\t\tswitch self {
"""
IOS_CONSTANTS_SWIFT_EXT_ITEM_FORMAT = u"\t\t\tcase .{0}:\n\t\t\t\treturn L10n.tr(key: \"{1}\")\n"
IOS_CONSTANTS_SWIFT_EXT_FOOTER = u"""
\t\t}
\t}

\tprivate static func tr(key: String, _ args: CVarArg...) -> String {
\t\tlet format = NSLocalizedString(key, bundle: Bundle(for: BundleToken.self), comment: "")
\t\treturn String(format: format, locale: Locale.current, arguments: args)
\t}
}

func tr(_ key: L10n) -> String {
\treturn key.string
}

private final class BundleToken {}
"""

def iosConstants(translations, languages):
    header = IOS_CONSTANTS_HEADER_HEADER
    source = IOS_CONSTANTS_SOURCE_HEADER
    for tr in translations:
        # Ignore empty keys.
        if (tr.iosKey is None):
            continue
        # Constant description.
        header += IOS_CONSTANTS_HEADER_DESC_START_FORMAT
        # Comment.
        if (tr.comment):
            header += IOS_CONSTANTS_HEADER_COMM_FORMAT.format(tr.comment)
        for languageId in range(0, len(languages)):
            language = languages[languageId]
            header += IOS_CONSTANTS_HEADER_LANG_FORMAT.format(language, tr.translations[languageId])
        header += IOS_CONSTANTS_HEADER_DESC_END_FORMAT
        # Constant itself.
        constant = "tr" + tr.iosKey.replace(".", "")
        header += IOS_CONSTANTS_HEADER_CONST_FORMAT.format(constant)
        source += IOS_CONSTANTS_SOURCE_FORMAT.format(constant, tr.iosKey)
    return (header, source)

def iosConstantsSwift(translations, languages):
    enum = IOS_CONSTANTS_SWIFT_ENUM_HEADER
    ext = IOS_CONSTANTS_SWIFT_EXT_HEADER
    for tr in translations:
        # Ignore empty keys.
        if (tr.iosKey is None):
            continue
        # TODO: Constant description.
        # Constant itself.
        constant = tr.iosKey.replace(".", "")
        enum += IOS_CONSTANTS_SWIFT_ENUM_ITEM_FORMAT.format(constant)
        ext += IOS_CONSTANTS_SWIFT_EXT_ITEM_FORMAT.format(constant, tr.iosKey)
    enum += IOS_CONSTANTS_SWIFT_ENUM_FOOTER
    ext += IOS_CONSTANTS_SWIFT_EXT_FOOTER
    result = enum + ext
    return result

def iosGenerateConstantsFiles(translations, languages):
    (header, source) = iosConstants(translations, languages)
    headerFileName = IOS_CONSTANTS_HEADER_FILE_NAME
    print("Generating iOS constants file '{0}'".format(headerFileName))
    with open(headerFileName, "w") as f:
        f.write(header.encode("utf-8"))
    sourceFileName = IOS_CONSTANTS_SOURCE_FILE_NAME
    print("Generating iOS constants file '{0}'".format(sourceFileName))
    with open(sourceFileName, "w") as f:
        f.write(source)

def iosGenerateLocalizationFiles(translations, languages):
    for languageId in range(0, len(languages)):
        language = languages[languageId]
        dirName = IOS_LOCALIZATION_DIR_NAME_MASK.format(language)
        # Create localization directory if it does not exist.
        if (not os.path.exists(dirName)):
            print("Creating directory '{0}'".format(dirName))
            os.makedirs(dirName)
        filePath = dirName + "/" + IOS_LOCALIZATION_FILE_NAME
        print("Generating iOS localization file '{0}'".format(filePath))
        with open(filePath, "w") as f:
            f.write(iosLocalization(translations, languageId))

def iosGenerateSwiftConstantsFile(translations, languages):
    source = iosConstantsSwift(translations, languages)
    sourceFileName = IOS_CONSTANTS_SWIFT_FILE_NAME
    print("Generating iOS constants file '{0}'".format(sourceFileName))
    with open(sourceFileName, "w") as f:
        f.write(source)

def iosLocalization(translations, languageId):
    contents = ""
    for tr in translations:
        # Ignore empty keys.
        if (tr.iosKey is None):
            continue
        if (tr.groupComment):
            contents += IOS_LOCALIZATION_GROUP_COMMENT_FORMAT.format(tr.groupComment)
        contents += IOS_LOCALIZATION_FORMAT.format(tr.iosKey, tr.translations[languageId])
    return contents.encode("utf-8")
