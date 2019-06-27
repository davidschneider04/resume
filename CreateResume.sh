#!/bin/bash
echo "committing updated resume information"
cd '/Users/kutch/resume'
git fetch
source /Users/kutch/.local/share/virtualenvs/env_django-ZXcG8Was/bin/activate
git add -A
git commit -m "resume update"
git push
echo "building formatted resume"
ipython3 CreateResumeFromTemplate.py
echo "saving formatted resume as PDF"
ipython3 ShareResume.py
echo "saved resume to AWS, committed to GitHub"