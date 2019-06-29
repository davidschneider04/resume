#!/bin/bash
pdfseparate -l 1 DavidSchneiderResume.pdf DavidSchneiderResume1.pdf
rm DavidSchneiderResume.pdf
mv DavidSchneiderResume1.pdf DavidSchneiderResume.pdf
pdf2svg DavidSchneiderResume.pdf DavidSchneiderResume.svg