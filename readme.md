# camtest

Camera calibration and pose estimation with a ChArUco board (OpenCV).

## Setup

```
pip install -r requirements.txt
```

## Workflow

0. **Make the board.** Set the board parameters in `constants.py` (`SQUARE_LENGTH` and `MARKER_LENGTH` are in meters and must match the printed board). Run `python charuco.py` to generate `ChArUco_Marker1.png`, then print it and measure it.

1. **Capture images.** Run `python image.py`. Press `s` to save a frame and `Esc` to quit. Images are saved to a new timestamped folder, `calibration_images/<YYYY-MM-DD_HH-MM-SS>/`. The camera index is hardcoded in `image.py` (`cv2.VideoCapture(4)`), so change it if needed.

2. **Calibrate.** Run `python calibration.py` and enter the image folder name (just the name, relative to `calibration_images/`) when prompted. Frames with fewer than 12 ChArUco corners are skipped, and the RMS reprojection error is printed. The intrinsics (`mtx`, `dist`) are saved to `calibration_images/<folder>/<folder>_calibration_constants.json`.

3. **Verify with pose estimation.** In `pose.py`, set `json_file_path` to the JSON from step 2 and set the camera index (`cv2.VideoCapture(0)`) to match the camera you calibrated. Run `python pose.py`, enter the board's distance from the camera when prompted, then press `f` to start recording. It stops after 1000 samples or when you press `Esc`. Results are saved to `plot_data/<timestamp>_raw_(<dist>cm).json`. Pose is estimated for each marker separately (`estimatePoseSingleMarkers`).

4. **Plot.** Set `file_name` in `plot_data.py` to a file in `plot_data/` and run `python plot_data.py`. It prints the mean, median and standard deviation and shows x/y/z/roll/pitch/yaw scatter plots. `plot_dataCSV.py` does the same for a CSV file.
