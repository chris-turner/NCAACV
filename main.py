from utils import read_video, save_video
from trackers import Tracker

def main():
    video_frames = read_video('videos\AmariLatimer.mp4')

    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frames)

    #save_video(video_frames, 'videos\output_video.mp4')

if __name__ == "__main__":
    main()