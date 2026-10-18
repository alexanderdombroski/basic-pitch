from pathlib import Path
from basic_pitch import ICASSP_2022_MODEL_PATH
from basic_pitch.inference import predict_and_save

# Modify this filename
FILE = "YOUR_FILE.m4a"


def main():
    if not FILE:
        print("Please set the FILE constant to your input audio file path.")
        return

    audio_path = Path(FILE)
    if not audio_path.exists():
        print(f"File not found: {audio_path}")
        return

    # Prepare out/ directory
    out_dir = Path("out")
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Processing: {audio_path}...")
    predict_and_save(
        audio_path_list=[str(audio_path)],
        output_directory=str(out_dir),
        save_midi=True,
        sonify_midi=False,
        save_model_outputs=False,
        save_notes=False,
        model_or_model_path=ICASSP_2022_MODEL_PATH,
    )

    # basic-pitch saves by default as `<stem>_basic_pitch.mid`
    generated_midi = out_dir / f"{audio_path.stem}_basic_pitch.mid"
    target_midi = out_dir / f"{audio_path.stem}.mid"

    if generated_midi.exists():
        generated_midi.replace(target_midi)
        print(f"Complete! MIDI saved to: {target_midi}")
    else:
        print(f"Complete! Output saved in: {out_dir}")


if __name__ == "__main__":
    main()
