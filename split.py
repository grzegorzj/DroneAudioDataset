from pydub import AudioSegment
import os

def split_audio(input_file, segment_duration=300):  # duration in milliseconds
    # Load the audio file
    audio = AudioSegment.from_wav(input_file)
    
    # Get the filename without extension
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    
    # Calculate the number of segments
    segment_count = len(audio) // segment_duration
    
    # Create segments and export
    for i in range(segment_count):
        start_time = i * segment_duration
        end_time = start_time + segment_duration
        segment = audio[start_time:end_time]
        
        # Export segment
        output_filename = f"./Binary_Drone_Audio/yes_drone/new_{i}.wav"
        segment.export(output_filename, format="wav")
        print(f"Created: {output_filename}")

# Example usage
if __name__ == "__main__":
    # Replace with your input file path
    input_wav = "./Binary_Drone_Audio/yes_drone/drone.wav"
    
    # You can adjust the segment duration (in milliseconds)
    # 300ms = 0.3 seconds
    split_audio(input_wav, segment_duration=300)
