from playsound import playsound
def playSong(mood):
    if(mood in [3,4,6]):
        path={3 : "G:/Documents/Machine_Learning/Emotion-Recognition-song-recomendation-master/music/happy/1.mp3",4 : "G:/Documents/Machine_Learning/Emotion-Recognition-song-recomendation-master/music/sad/1.mp3",6 : "G:/Documents/Machine_Learning/Emotion-Recognition-song-recomendation-master/music/neutral/1.mp3"}
        playsound(path[mood])
