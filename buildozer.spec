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
# Here we will write the required Python libraries for the app (like requests, pillow, etc.)
requirements = python3,kivy,requests

# (str) Supported orientations
orientation = portrait

# (list) Permissions
# Internet access and network state so the app can send strikes or reports directly
android.permissions = INTERNET,ACCESS_NETWORK_STATE

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2
# (int) Accept android SDK licenses automatically (1 = yes)
android.accept_sdk_license = True
