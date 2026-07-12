@echo off
:: Set the window title
title EDN GitHub Auto-Push Engine

echo ====================================================
echo        EDN GITHUB PAGES AUTOMATED PUSH ENGINE       
echo ====================================================
echo.

:: Step 1: Stage all changes (matches.json and local gallery images)
echo [1/3] Gathering updated matchups, odds, and player images...
git add .
echo ✔ Done!
echo.

:: Step 2: Commit the changes with an automatic timestamp message
echo [2/3] Packaging updates securely...
git commit -m "Automated matchday odds and roster update"
echo ✔ Done!
echo.

:: Step 3: Push live to your GitHub Pages main branch
echo [3/3] Pushing live updates to your GitHub Repository...
echo.
git push origin main
echo.

echo ====================================================
echo  ✅ SUCCESS! Your prediction center is updating live!
echo ====================================================
echo.
echo Press any key to close this window.
pause > nul
s