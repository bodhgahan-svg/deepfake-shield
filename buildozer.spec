[app]

# (str) Title of your application
title = Deep-Fake Shield

# (str) Package name
package.name = deepfakeshield

# (str) Package domain (needed for android packaging)
package.domain = org.decentralized

# (list) Source files to include (let it include python files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Source directory where the application files are located
source.dir = .

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy,requests

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible
android.api = 31

# (int) Minimum API your APK will support
android.minAPI = 21

# (int) Android SDK version to use
android.sdk = 31

# (str) Android NDK version to use
android.ndk = 25b

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Accept android SDK licenses automatically (1 = yes)
android.accept_sdk_license = True
# (str) Specific Android build tools version
android.build_tools_version = 31.0.2
