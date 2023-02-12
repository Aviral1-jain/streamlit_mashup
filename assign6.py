from pytube import YouTube,Search
import moviepy.editor as mp
from pydub import AudioSegment
from youtubesearchpython import VideosSearch
import os
import sys
import shutil
import time
import librosa
import numpy as np
import soundfile as sf
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders




def Download(singer_name , N):
    results=[]
    s=Search(singer_name)
    s.results
    s.get_next_results()
    s.get_next_results()
    for i in range(N):
        results.append(s.results[i])

    
    for str in results:
        y=str
        vids = y.streams.first()
        vids.download('Videos/')


def convertToAudio(video_folder,audio_folder):
    #directory = 'Videos'
    #path = os.path.join(os.getcwd(), audio_folder)
   
    for filename in os.listdir(video_folder):
    
        clip = mp.VideoFileClip(os.path.join(video_folder,filename))
        audio = clip.audio
        audio.write_audiofile(os.path.join(audio_folder, filename.split(".")[0]+".mp3"))



# numVideos=nvids
def cut_audio(audio_folder , dn,output_file):
    audios = []
    for Audio in os.listdir(audio_folder):
        audios.append(Audio)
    
    filename = os.path.join(audio_folder,audios[0])
    y, sr = librosa.load(filename)
    y_cut = y[:(dn * sr)]
    for j in range(1,len(audios)):
        filename  =os.path.join(audio_folder,audios[j])
        y, sr = librosa.load(filename)
        y_cut=np.append(y_cut , y[:(dn * sr)])
    sf.write(output_file,y_cut,sr)




def send_email(subject, body, sender, recipients, password):
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipients
    html_part = MIMEText(body)
    message.attach(html_part)
    
    filename = subject
    attachment = open(filename, "rb")
  
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
    
    # To change the payload into encoded form
    p.set_payload((attachment).read())
    
    # encode into base64
    encoders.encode_base64(p)
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    
    # attach the instance 'p' to instance 'msg'
    message.attach(p)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender, password)
    server.sendmail(sender, recipients, message.as_string())
    server.quit()
    print("Email Sent!")



def removeDirectories(video_folder,audio_folder):
    shutil.rmtree(video_folder)
    shutil.rmtree(audio_folder)
     




if __name__=='__main__':
    singer_name = sys.argv[1]
    N=int(sys.argv[2])
    y=int(sys.argv[3])
    output_file = sys.argv[4]
    emailid=sys.argv[5]
    
    if not os.path.exists('Videos'):
        os.mkdir('Videos')
    if not os.path.exists('Audios'):
        os.mkdir('Audios')

    Download(singer_name,N)
    convertToAudio('Videos','Audios')
    cut_audio('Audios',y,output_file)
    removeDirectories('Videos','Audios')
    gmail = "jainaviral0619@gmail.com"
    gmailpwd = "lgybuusjxdskxbus"
    email = emailid
    send_email(output_file, output_file, gmail, email, gmailpwd)




    
