__author__ = 'jdh'
import dropbox
import os
import sys
import webbrowser
import ConfigParser

import time

#----------------------------------------------------------------------
def config():
  config = ConfigParser.ConfigParser()
  config_path = os.path.join(os.getcwd(), '..', 'Dropbox', "config.ini")
  if os.path.exists(config_path):
      config.read(config_path)
      if config.has_option('Config', 'app_key'):
         appKey = config.get('Config', 'app_key')

      if config.has_option('Config', 'app_secret'):
         appSecret = config.get('Config', 'app_secret')

      return appKey,appSecret

  else:
      print "ERROR: config.ini not found! Exiting!"
      sys.exit(1)
#----------------------------------------------------------------------
def connect(app_key,app_secret):
  """
  Connect and authenticate with dropbox
  """

  access_type = "dropbox"
  session = dropbox.session.DropboxSession(app_key,
                                           app_secret,
                                           access_type)

  request_token = session.obtain_request_token()

  url = session.build_authorize_url(request_token)
  msg = "Opening %s. Please make sure this application is allowed before continuing."
  print msg % url
  webbrowser.open(url)

  print("You have ten seconds to authorize dropbox. Get on it cowboy!")
  time.sleep(10)
  access_token = session.obtain_access_token(request_token)

  client = dropbox.client.DropboxClient(session)
  return client

#----------------------------------------------------------------------
def download_file(self, filename=None, outDir=None):
  """
  Download either the file passed to the class or the file passed
  to the method
  """

  if filename:
      fname = filename
      f, metadata = self.client.get_file_and_metadata("/" + fname)
  else:
      fname = self.filename
      f, metadata = self.client.get_file_and_metadata("/" + fname)

  if outDir:
      dst = os.path.join(outDir, fname)
  else:
      dst = fname

  with open(fname, "w") as fh:
      fh.write(f.read())

  return dst, metadata

#----------------------------------------------------------------------
def get_account_info(self):
  """
  Returns the account information, such as user's display name,
  quota, email address, etc
  """
  return self.client.account_info()

#----------------------------------------------------------------------
def list_folder(client,folder):
  """
  Return a dictionary of information about a folder
  """
  dropBoxFileList = []
  if folder:
      folder_metadata = client.metadata(folder)
  else:
      folder_metadata = client.metadata("/")
  dropBoxDictionaryList = folder_metadata['contents']

  for fileDict in dropBoxDictionaryList:
     dropBoxFileList.append(os.path.basename(fileDict['path']))

  return dropBoxFileList

#----------------------------------------------------------------------
def upload_file(client,filename,folder):
  """
  Upload a file to dropbox, returns file info dict
  """
  f = open(filename, 'rb')
  response = client.put_file('Camera Uploads/' + filename, f)
  print "uploaded:", response


