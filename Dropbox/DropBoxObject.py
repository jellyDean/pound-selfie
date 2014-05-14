__author__ = 'jdh'
import dropbox
import os
import sys
import webbrowser
import ConfigParser
import pprint

########################################################################
class DropBoxObject(object):
    """
    Dropbox object that can access your dropbox folder,
    as well as download and upload files to dropbox
    """

    #----------------------------------------------------------------------
    def __init__(self, filename=None, path='/'):
        """Constructor"""
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.filename = filename
        self.path = path
        self.client = None
        self.appKey = ''
        self.appSecret = ''
        self.dropBoxFileList = []

        self.config()
        self.connect()
        folder_metadata = self.list_folder('Camera Uploads')
        dropBoxFileList = folder_metadata['contents']

        for fileDict in dropBoxFileList:
         self.dropBoxFileList.append(os.path.basename(fileDict['path']))

        self.process_meta_data(folder_metadata)

    #----------------------------------------------------------------------
    def config(self):
        config = ConfigParser.ConfigParser()
        config_path = os.path.join(self.base_path, "config.ini")
        if os.path.exists(config_path):
            config.read(config_path)
            if config.has_option('Config', 'app_key'):
               self.appKey = config.get('Config', 'app_key')

            if config.has_option('Config', 'app_secret'):
               self.appSecret = config.get('Config', 'app_secret')

        else:
            print "ERROR: config.ini not found! Exiting!"
            sys.exit(1)
    #----------------------------------------------------------------------
    def connect(self):
        """
        Connect and authenticate with dropbox
        """
        app_key = self.appKey
        app_secret =  self.appSecret

        access_type = "dropbox"
        session = dropbox.session.DropboxSession(app_key,
                                                 app_secret,
                                                 access_type)

        request_token = session.obtain_request_token()

        url = session.build_authorize_url(request_token)
        msg = "Opening %s. Please make sure this application is allowed before continuing."
        print msg % url
        webbrowser.open(url)
        raw_input("Press enter to continue")
        access_token = session.obtain_access_token(request_token)

        self.client = dropbox.client.DropboxClient(session)

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
    def list_folder(self, folder):
        """
        Return a dictionary of information about a folder
        """
        if folder:
            folder_metadata = self.client.metadata(folder)
        else:
            folder_metadata = self.client.metadata("/")
        return folder_metadata

    #----------------------------------------------------------------------
    def upload_file(self,filename,folder):
        """
        Upload a file to dropbox, returns file info dict
        """
        try:
            with open(filename) as fh:
                path = os.path.join(folder,filename)
                res = self.client.put_file(path, fh)
                print "uploaded: ", res
        except Exception, e:
            print "ERROR: ", e

        return res

if __name__ == "__main__":
    drop = DropBoxObject("somefile.txt")