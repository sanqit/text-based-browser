def heading(title, level=1):
    return f"{'#' * max(min(level, 6), 1)} {title}"
