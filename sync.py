#!/usr/bin/python3

# @author: aghontpi
# File is run by github-action everyday and -
#  - syncs content with api

from pathlib import Path
import json
import requests
import datetime


class Utils(object):
    def __init__(self):
        self.offline_directory = Path(__file__).parent
        self.download_directory = "api"
        self.log_directory = "logs"
        self.state_filename = "syncState.json"
        self._log(
            f"\n{'*'*20} {datetime.datetime.now().strftime('%Y-%m-%d')} {'*'*20}")

    def _saveState(self, json_content):
        self._log("updating syncState", json_content)
        filepath = self.offline_directory.joinpath(self.state_filename)
        with open(filepath, 'w') as writefile:
            json.dump(json_content, writefile)
        writefile.close()

    def _log(self, log, _arg=''):
        filepath = self.offline_directory.joinpath(self.log_directory)
        log_string = f"{log} {str(_arg)}"
        if not Path.is_dir(filepath):
            Path(filepath).mkdir()
            log_string = f"creating logs path\n" + log_string
        filepath = filepath.joinpath('log.txt')
        with open(filepath, 'a+') as logFile:
            logFile.write(
                f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {log_string} \n")
        logFile.close()
        print(log_string)

    def _saveContent(self, json_content):
        id = json_content['num']
        img_url = json_content['img']
        img_name = img_url.split('/')[-1]
        # handle no image for a specific json
        if img_name == "":
            self._log("no image for :", id)
            return True
        download_directory = self.offline_directory.joinpath(
            self.download_directory)
        if not Path.is_dir(download_directory):
            try:
                Path(download_directory).mkdir()
            except:
                self._log("can not create api directory")
                return False
            self._log("saving in new directory :",
                      download_directory.as_posix())
        download_directory = download_directory.joinpath(str(id))
        if not Path.is_dir(download_directory):
            try:
                Path(download_directory).mkdir()
            except:
                self._log("can not create offline directory")
                return False
            self._log("saving in new directory : ",
                      download_directory.as_posix())

        # save assests
        img = requests.get(img_url)
        if img.status_code != 200:
            self._log("error downloading image :", img_url)
            return False
        file_path = download_directory.joinpath(img_name)
        with open(file_path, 'wb') as save_file:
            save_file.write(img.content)
        save_file.close()

        # saving the info.json
        file_path = download_directory.joinpath('info.0.json')
        json_content[
            'mirror_img'] = f'https://raw.githubusercontent.com/aghontpi/mirror-xkcd-api/main/api/{id}/{img_name}'
        with open(file_path, 'w') as save_file:
            json.dump(json_content, save_file)
        save_file.close()
        return True


class Sync(Utils):

    def __init__(self):
        self.urllink = 'https://xkcd.com/info.0.json'
        self.local_content = None
        self.remote_content = None
        super(Sync, self).__init__()

    def sync(self):
        if self._parseLocalstate()._parseRemoteState()._compareLocalAndRemote():
            self._log('no new content to sync')
            exit()
        self.downloadNewContent()

    def _parseLocalstate(self):
        filepath = self.offline_directory.joinpath(self.state_filename)
        if not Path.is_file(filepath):
            # not present, creating file
            self._log('creating local state file ')
            with open(filepath, 'w') as create_file:
                create_file.write('{"last_update_content": {"id": "1"}}')
            create_file.close()

        with open(filepath, encoding='utf-8') as json_file:
            data = json.loads(json_file.read())
        json_file.close()
        self.local_content = data
        return self

    def _parseRemoteState(self):
        try:
            remoteContent = requests.get(self.urllink).content
            remoteContent = (json.loads(remoteContent))
        except:
            pass
        self.remote_content = remoteContent
        return self

    def _compareLocalAndRemote(self):
        l_content_id = int(self.local_content['last_update_content']['id'])
        r_content_id = int(self.remote_content['num'])
        return not l_content_id < r_content_id

    def downloadNewContent(self):
        l_content = self.local_content
        r_content = self.remote_content
        # check local content id vs remote content id
        self._log("processing", l_content['last_update_content']['id'])
        l_content_id = int(l_content['last_update_content']['id'])
        r_content_id = int(r_content['num'])
        while l_content_id < r_content_id:
            try:
                json_content = json.loads(requests.get(
                    "https://xkcd.com/"+str(l_content_id)+"/info.0.json").content)
            except:
                self._log('can not contact remote for :', l_content_id)
                self._log('skipping ', l_content_id)
                l_content_id += 1
                continue
            if self._saveContent(json_content):
                l_content_id += 1
                l_content['last_update_content']['id'] = str(l_content_id)
                self._log('downloaded content :', l_content_id)
                self._saveState(self.local_content)
            else:
                self._log('error saving content... skipping')
                break


if __name__ == "__main__":
    sync = Sync()
    sync.sync()
