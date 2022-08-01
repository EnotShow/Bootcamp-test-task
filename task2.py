import random
import string
from moviepy.editor import VideoFileClip
from pathlib import Path
import requests

__author__ = 'EnotShow'
__author_link__ = 'https://github.com/EnotShow'


class TikTokConverter:
    """ Download and convert video to gif """

    def __init__(self):
        self.videos_path = 'results/videos/'
        self.gif_path = 'results/gif/'

    @staticmethod
    def _generate_file_name():
        """ Generate file name """
        file_name = ''
        for i in range(10):
            file_name = file_name + random.choice(string.ascii_letters)
        return file_name

    def video_download(self, video_url: str,):
        """ Download viedeos from """
        try:
            response = requests.get(url=video_url)

            file_link = self.videos_path + self._generate_file_name() + '.mp4'
            with open(file_link, 'wb') as file:
                file.write(response.content)
            return file_link

        except Exception as _ex:
            print(_ex)
            print('\nOpps... you got error. ')

    def video_to_gif(self, file_link: str):
        """ Convert video to gif """
        videoClip = VideoFileClip(file_link)
        file_name = file_link.replace(self.videos_path, '').replace('.mp4', '') + '.gif'
        videoClip.write_gif(self.gif_path + file_name)
        return self.gif_path + file_name


if __name__ == '__main__':
    print(f'Your welcome!\nWriten by {__author__} {__author_link__}')
    url = str(input('Insert your TikTok video url:\n'))
    TTConv = TikTokConverter()
    gif_path = TTConv.video_to_gif(TTConv.video_download(url))
    print(f'Successful! You can find you gif at:\n{Path(__file__)}/{gif_path}')
