# vdd
video-duplicate-detector. Can detect duplicate videos even with different resolutions or lengths

> [!NOTE]
> This Project is still under development

# Procedure

- foreach video
  - foreach frame
    - grayscale each frame
    - rescale all frames to common smaller size (eg. 240p)
    - create hash/identifier for each frame
    - add identifier to database!?
- search for common frames
- compare frames around common frames to search for similarities
- report
