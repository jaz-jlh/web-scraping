#Python Comment Web Scraping

This script uses python and the selenium module to pull comments on the Federal Automated Vehicles Policy from the [NHTSA Website](https://www.regulations.gov/document?D=NHTSA-2016-0090-0001).

Output from comment_aggregator.py can be piped to an output text document or viewed in the terminal.

all_comments.txt contains results of web scraping, although there are some formatting issues and comments that were not retrieved properly. Also, a vast majority of comments were from an online form, so to save space, those comments were replaced with the comment number that contains the first posting of the full comment.