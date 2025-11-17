@echo off
echo Opening Icon Generator for Chrome Extension...
echo.
echo This will open the icon generator in your default browser.
echo Follow the instructions to generate and download the icons.
echo.
pause

start create_icons.html

echo.
echo Instructions:
echo 1. Click "Generate Icons" to preview the icons
echo 2. Click "Download All Icons" to download PNG files
echo 3. Save the files as icon16.png, icon48.png, and icon128.png
echo 4. Place them in the icons\ folder
echo.
echo After generating icons, you can install the extension:
echo 1. Open Chrome and go to chrome://extensions/
echo 2. Enable Developer mode
echo 3. Click "Load unpacked" and select this folder
echo.
pause
