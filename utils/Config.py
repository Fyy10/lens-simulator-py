class Config:
    # Lens
    # 50mm f1.8
    focal_length = float(50.0)  # f
    focal_ratio = float(1.8)  # r, f-number, e.g., f/1.8
    sensor_dist = float(100.0)  # v
    sensor_xlim = float(100.0)

    aperture_sample_size = int(100)

    # render
    max_reflection_depth = int(1)
