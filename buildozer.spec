[app]

# (str) Title of your application
title = Deep-Fake Shield

# (str) Package name
package.name = deepfakeshield

# (str) Package domain (needed for android packaging)
package.domain = org.decentralized

# (list) Source files to include (let it include python files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# यहाँ हम Python की जरूरी लाइब्रेरीज़ लिखेंगे जो ऐप के अंदर चलेंगी (जैसे requests, pillow आदि)
requirements = python3,kivy,requests

# (str) Supported orientations
orientation = portrait

# (list) Permissions
# इंटरनेट एक्सेस और नेटवर्क स्टेट ताकि ऐप सीधे स्ट्राइक या रिपोर्ट भेज सके
android.permissions = INTERNET,ACCESS_NETWORK_STATE

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2
