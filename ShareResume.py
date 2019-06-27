#!/usr/bin/env python
# coding: utf-8

# ## Note:
# None of this is intended to work if you are not me-- it relies on files based on my local machine so as to hide security credentials. I am providing this code as a template to those interested. If you are not interested in implementing your own customization, feel free to reach out to david@davidtschneider.com and we can discuss rates regarding a custom solution.

# In[1]:

def main():
	import shutil, os, time, pyautogui, subprocess, datetime, boto3
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys


	# In[2]:


	os.chdir('/Users/kutch/resume/')
	currentdate = datetime.datetime.today().strftime('%Y-%m-%d')


	# ### Convert previously saved Word file to PDF

	# In[3]:
	with open('word_commands.txt') as f:
		txt = f.read()
		instructions = txt.split(';')
		for instruction in instructions:
			exec(instruction)

	#word default save location is the downloads folder. could probably fix this if i want
	shutil.copyfile('/Users/kutch/Downloads/DavidSchneiderResume.pdf', 'DavidSchneiderResume.pdf')


	# ### Upload PDF file to CDNs

	# #### GitHub

	# In[7]:


	subprocess.run(f"git add -A; git commit -m 'updated on {currentdate}'; git push;", shell=True)


	# #### s3

	# In[8]:


	#credentials/client creation
	with open('/Users/kutch/Desktop/Projects/AWS/creds.txt') as creds:
	    txt = [line.strip() for line in creds.readlines()]
	    a_key, sa_key = txt[0], txt[1]
	s3 = boto3.resource('s3', aws_access_key_id = a_key, aws_secret_access_key = sa_key)
	client = boto3.client('s3', aws_access_key_id = a_key, aws_secret_access_key = sa_key)
	#upload
	client.upload_file('DavidSchneiderResume.pdf', 'davidschneiderprojects', 'DavidSchneiderResume.pdf', ExtraArgs={'ACL':'public-read', 'ContentType': 'application/pdf', 'ContentDisposition':'inline'})
	print('successfully uploaded PDF to AWS.')

if __name__ == "__main__":
    # execute only if run as a script
    main()
