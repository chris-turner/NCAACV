from utils import read_video, save_video

def main():
    video_frames = read_video('videos\AmariLatimer.mp4')

    save_video(video_frames, 'videos\output_video.mp4')

if __name__ == "__main__":
    main()