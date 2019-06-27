#!/bin/bash
source /Users/kutch/.local/share/virtualenvs/env_django-ZXcG8Was/bin/activate
echo "committing updated resume information"
cd '/Users/kutch/resume'
git add -A
git commit -m "resume update"
git push
echo "building formatted resume"
python CreateResumeFromTemplate.py
echo "saving formatted resume as PDF"
python ShareResume.py
git add -A
git commit -m "resume update"
git push
echo "saved resume to AWS, committed to GitHub"